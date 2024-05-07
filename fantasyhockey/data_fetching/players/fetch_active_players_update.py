from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.players.models.player import Player
from fantasyhockey.data_fetching.players.models.player_draft import PlayerDraft
from fantasyhockey.data_fetching.players.models.player_awards import PlayerAwards
from fantasyhockey.data_fetching.players.models.player_details import PlayerDetails
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util

class FetchActivePlayersUpdate:

    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.api_connector = APIConnector()
        self.util = Util()
        self.data_parser = DataParser()
        self.__players = []
        self.__player_ids = []

    def get_players(self):
        if not self.__players:
            self.__fetch_active_players()
        return self.__players
    
    def __fetch_active_players(self):
        query = "SELECT id FROM players WHERE is_active = 1;"
        res = self.database_operator.read(query)
        player_ids = []
        for row in res:
            player_ids.append(row[0])
        self.__player_ids = player_ids
        self.__get_player_data()

    def __get_player_data(self):
        count = 0
        for player_id in self.__player_ids:
            count += 1
            print("Fetching player data for player id: ", player_id, " (", count, "/", len(self.__player_ids), ")")
            json = self.api_connector.get_json(f"https://api-web.nhle.com/v1/player/{player_id}/landing")
            player = Player(player_id)
            
            try:
                if "currentTeamId" not in json:
                    team_id = None
                else:
                    team_id = self.data_parser.parse(json, "currentTeamId", "error")
                player.set_team_id(team_id)
            except KeyError:
                print("Error parsing team id from player id: ", player_id)
                continue
            try: 
                is_active = self.data_parser.parse(json, "isActive", "error")
                player.set_is_active(is_active)
            except KeyError:
                print("Error parsing is active from player id: ", player_id)
                continue


            self.__get_player_draft(player, json)
            self.__get_player_awards(player, json)
            self.__get_player_details(player, json)
            self.__players.append(player)

    def check_is_player_active(self, player_id, json):
        return json["isActive"] == True
    
    def fetch_new_team_id(self, player_id, team_id, json):
        new_team_id = json["currentTeamId"]

        if new_team_id != team_id:
            return new_team_id
        return None
    
    def __fetch_landing_info(self, player_id):
        url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
        return self.api_connector.get_json(url)
    
    def __get_player_draft(self, player: Player, json):
        player_id = player.get_player_id()
        player_draft = PlayerDraft(player_id)

        player_draft.set_year(self.data_parser.double_parse(json, "draftDetails", "year", "none"))
        team_abbrev = self.data_parser.double_parse(json, "draftDetails", "teamAbbrev", "none")
        team_id = self.util.get_team_id_from_abbrev(team_abbrev)
        player_draft.set_team_id(team_id)
        player_draft.set_round(self.data_parser.double_parse(json, "draftDetails", "round", "none"))
        player_draft.set_pick_in_round(self.data_parser.double_parse(json, "draftDetails", "pickInRound", "none"))
        player_draft.set_overall_pick(self.data_parser.double_parse(json, "draftDetails", "overallPick", "none"))
        
        player.set_player_draft(player_draft)

    def __get_player_awards(self, player: Player, json):
        player_id = player.get_player_id()
        try:
            awards = self.data_parser.parse(json, "awards", "empty_list")
            for award in awards:
                for seasons in award["seasons"]:
                    player_award = PlayerAwards(player_id)
                    player_award.set_year(self.data_parser.parse(seasons, "seasonId", "none"))
                    player_award.set_award(self.data_parser.double_parse(award, "trophy", "default", "none"))
                    player.add_player_award(player_award)
        except KeyError as e:
            print("Error parsing player awards from player id (likely doesn't have any awards): ", player_id)
            print(e)

        except ValueError as e:
            print("Error parsing player awards from player id (likely doesn't have any awards): ", player_id)
            print(e)

    def __get_player_details(self, player: Player, json):
        player_id = player.get_player_id()
        player_details = PlayerDetails(player_id)
        try:
            player_details.set_first_name(self.data_parser.double_parse(json, "firstName", "default", "none"))

            player_details.set_last_name(self.data_parser.double_parse(json, "lastName", "default", "none"))

            player_details.set_jersey_number(self.data_parser.parse(json, "sweaterNumber", "none"))
            player_details.set_position(self.data_parser.parse(json, "position", "none"))
            player_details.set_headshot(self.data_parser.parse(json, "headshot", "none"))
            player_details.set_hero_image(self.data_parser.parse(json, "heroImage", "none"))
            player_details.set_height_inches(self.data_parser.parse(json, "heightInCentimeters", "none"))
            player_details.set_weight_pounds(self.data_parser.parse(json, "weightInPounds", "none"))
            player_details.set_birth_date(self.data_parser.parse(json, "birthDate", "none"))

            player_details.set_birth_city(self.data_parser.double_parse(json, "birthCity", "default", "none"))

            player_details.set_birth_state_province(self.data_parser.double_parse(json, "birthStateProvince", "default", "none"))

            player_details.set_birth_country(self.data_parser.parse(json, "birthCountry", "none"))
            player_details.set_shoots_catches(self.data_parser.parse(json, "shootsCatches", "none"))
            player_details.set_in_top_100_all_time(self.data_parser.parse(json, "inTop100AllTime", "false"))
            player_details.set_in_hhof(self.data_parser.parse(json, "inHHOF", "false"))
            player.set_player_details(player_details)
        except KeyError as e:
            print("Error parsing player details from player id: ", player_id)
            print(e)
        except ValueError as e:
            print("Error parsing player details from player id: ", player_id)
            print(e)