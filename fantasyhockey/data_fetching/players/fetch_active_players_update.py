from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.players.models.player import Player
from fantasyhockey.data_fetching.players.models.player_draft import PlayerDraft
from fantasyhockey.data_fetching.players.models.player_awards import PlayerAwards
from fantasyhockey.data_fetching.players.models.player_details import PlayerDetails

class FetchActivePlayersUpdate:

    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.api_connector = APIConnector()
        self.__players = []
        self.__player_ids = []

    def get_players(self):
        self.player_ids = self.__fetch_active_players()
        for player_id in self.player_ids:
            player = Player(player_id)
            
            self.__get_player_data()

    def __get_player_data(self):
        for player_id in self.__player_ids:
            json = self.api_connector.get_json(f"https://api-web.nhle.com/v1/player/{player_id}/landing")
            player = Player(player_id)

            self.__get_player_draft(player, json)
            self.__get_player_awards(player, json)
            self.__get_player_details(player, json)
            self.__players.append(player)


    def __fetch_active_players(self):
        query = "SELECT player_id FROM players WHERE is_active = 1"
        res = self.database_operator.read(query)
        player_ids = []
        for row in res:
            player_ids.append(row[0])
        return player_ids

    def check_is_player_active(self, player_id):
        player_info = self.__fetch_landing_info(player_id)
        return player_info["isActive"] == True
    
    def fetch_new_team_id(self, player_id, team_id):
        player_info = self.__fetch_landing_info(player_id)
        new_team_id = player_info["currentTeamId"]

        if new_team_id != team_id:
            return new_team_id
        return None
    
    def __fetch_landing_info(self, player_id):
        url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
        return self.api_connector.get_json(url)
  
    def __parse_data_none(self, json, key):
        """Parse json data."""
        if json and key in json:
            return json[key]
        return None
    
    def __parse_data_empty_list(self, json, key):
        """Parse json data."""
        if key in json:
            return json[key]
        return []
    
    def __get_player_draft(self, player, json):
        player_id = player.get_player_id()
        player_draft = PlayerDraft(player_id)
        try:
            draft_details = self.__parse_data_none(json, "draftDetails")
            if draft_details:
                player_draft.set_year(self.__parse_data_none(draft_details, "year"))
                team_abbrev = self.__parse_data_none(draft_details, "teamAbbrev")
                team_id = self.__get_team_id_from_abbrev(team_abbrev)
                player_draft.set_team_id(team_id)
                player_draft.set_round(self.__parse_data_none(draft_details, "round"))
                player_draft.set_pick_in_round(self.__parse_data_none(draft_details, "pickInRound"))
                player_draft.set_overall_pick(self.__parse_data_none(draft_details, "overallPick"))
            else:
                player_draft.set_year(None)
                player_draft.set_team_id(None)
                player_draft.set_round(None)
                player_draft.set_pick_in_round(None)
                player_draft.set_overall_pick(None)
                print("Error parsing draft details from player id: ", player_id)
        except KeyError:
            print("Error parsing draft details from player id: ", player_id)
        except ValueError:
            print("Error parsing draft details from player id: ", player_id)
        
        player.set_player_draft(player_draft)

    def __get_player_awards(self, player: Player, json):
        player_id = player.get_player_id()
        try:
            awards = self.__parse_data_empty_list(json, "awards")
            if awards:
                for award in awards:
                    for seasons in award["seasons"]:
                        player_award = PlayerAwards(player_id)
                        player_award.set_year(seasons["seasonId"])
                        player_award.set_award(award["default"])
                        player.add_player_award(player_award)
        except KeyError:
            print("Error parsing player awards from player id (likely doesn't have any awards): ", player_id)

        except ValueError:
            print("Error parsing player awards from player id (likely doesn't have any awards): ", player_id)

    def __get_player_details(self, player: Player, json):
        player_id = player.get_player_id()
        player_details = PlayerDetails(player_id)
        try:
            first_name = self.__parse_data_none(json, "firstName")
            if first_name:
                player_details.set_first_name(self.__parse_data_none(first_name, "default"))
            else:
                player_details.set_first_name(None)
                print("Error parsing first name from player id: ", player_id)
            
            last_name = self.__parse_data_none(json, "lastName")
            if last_name:
                player_details.set_last_name(self.__parse_data_none(last_name, "default"))
            else:
                player_details.set_last_name(None)
                print("Error parsing last name from player id: ", player_id)

            player_details.set_jersey_number(self.__parse_data_none(json, "sweaterNumber"))
            player_details.set_position(self.__parse_data_none(json, "position"))
            player_details.set_headshot(self.__parse_data_none(json, "headshot"))
            player_details.set_hero_image(self.__parse_data_none(json, "heroImage"))
            player_details.set_height_inches(self.__parse_data_none(json, "heightInCentimeters"))
            player_details.set_weight_pounds(self.__parse_data_none(json, "weightInPounds"))
            player_details.set_birth_date(self.__parse_data_none(json, "birthDate"))

            birth_city = self.__parse_data_none(json, "birthCity")
            if birth_city:
                player_details.set_birth_city(self.__parse_data_none(birth_city, "default"))
            else:
                player_details.set_birth_city(None)
                print("Error parsing birth city from player id: ", player_id)

            birth_state_province = self.__parse_data_none(json, "birthStateProvince")
            if birth_state_province:
                player_details.set_birth_state_province(self.__parse_data_none(birth_state_province, "default"))
            else:
                player_details.set_birth_state_province(None)
                print("Error parsing birth state province from player id: ", player_id)

            player_details.set_birth_country(self.__parse_data_none(json, "birthCountry"))
            player_details.set_shoots_catches(self.__parse_data_none(json, "shootsCatches"))
            player_details.set_in_top_100_all_time(self.__parse_data_none(json, "inTop100AllTime"))
            player_details.set_in_hhof(self.__parse_data_none(json, "inHHOF"))
            player.set_player_details(player_details)
        except KeyError:
            print("Error parsing player details from player id: ", player_id)
        except ValueError:
            print("Error parsing player details from player id: ", player_id)


    def __get_team_id_from_abbrev(self, team_abbrev):
        query = "SELECT team_id FROM teams WHERE team_abbreviation = %s"
        params = (team_abbrev,)
        res = self.db_operator.read(query, params)
        return res[0][0] if res else None