from fantasyhockey.data_fetching.players.fetch_players_from_scratch import FetchPlayersFromScratch
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.models.player import Player
from fantasyhockey.data_fetching.players.fetch_active_players_update import FetchActivePlayersUpdate
from fantasyhockey.data_fetching.players.models.player_awards import PlayerAwards
from fantasyhockey.data_fetching.players.models.player_details import PlayerDetails
from fantasyhockey.data_fetching.players.models.player_draft import PlayerDraft

class UpdatePlayers:

    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_players = FetchPlayersFromScratch()
        self.fetch_active_players_update = FetchActivePlayersUpdate()

    def write_in_db_from_scratch(self):
        """
        Fetches all players from the NHL API and writes them to the database for the first time.
        """
        players = self.fetch_players.get_players()
        for player in players:
            #query, params = self.__create_players_query(player)
            #self.database_operator.write(query, params)

            """try:
                player_details = player.get_player_details()
                query, params = self.__create_player_details_query(player_details)
                self.database_operator.write(query, params)
            except Exception as e:
                print("Error writing player details to the database: ", e, "will try to update")
                query, params = self.__update_player_details_query(player_details)
                self.database_operator.write(query, params)
            """
            """
            try:
                player_draft = player.get_player_draft()
                query, params = self.__create_player_draft_query(player_draft)
                self.database_operator.write(query, params)
            except Exception as e:
                print("Error writing player draft to the database: ", e, "will try to update")
                query, params = self.__update_player_draft_query(player_draft)
                self.database_operator.write(query, params)
            """
            try:
                player_awards = player.get_player_awards()
                print("Updating player awards")
                print(player_awards)
                for award in player_awards:
                    query, params = self.__create_player_awards_query(award)
                    self.database_operator.write(query, params)
            except Exception as e:
                print("Error writing player awards to the database: ", e, "will try to update")
                for award in player_awards:
                    query, params = self.__update_player_awards_query(award)
                    self.database_operator.write(query, params)

    def write_in_db_update(self):
        """
        Updates the players table in the database.
        """
        players = self.fetch_active_players_update.get_players()
        for player in players:
            try:
                query, params = self.__update_players_query(player)
                self.database_operator.write(query, params)
            except Exception as e:
                print("Error updating player in the database: ", e, "will try to create a new player entry")
                query, params = self.__create_players_query(player)
                self.database_operator.write(query, params)
            
            player_details = player.get_player_details()
            try:
                query, params = self.__update_player_details_query(player_details)
                self.database_operator.write(query, params)
            except Exception as e:
                print("Error updating player details in the database: ", e, "will try to create a new player details entry")
                query, params = self.__create_player_details_query(player_details)
                self.database_operator.write(query, params)

            player_draft = player.get_player_draft()
            try:
                query, params = self.__update_player_draft_query(player_draft)
                self.database_operator.write(query, params)
            except Exception as e:
                print("Error updating player draft in the database: ", e, "will try to create a new player draft entry")
                query, params = self.__create_player_draft_query(player_draft)
                self.database_operator.write(query, params)

            player_awards = player.get_player_awards()
            try:
                for award in player_awards:
                    query, params = self.__update_player_awards_query(award)
                    self.database_operator.write(query, params)
            except Exception as e:
                print("Error updating player awards in the database: ", e, "will try to create a new player awards entry")
                for award in player_awards:
                    query, params = self.__create_player_awards_query(award)
                    self.database_operator.write(query, params)

    def __create_players_query(self, player: Player) -> tuple:
        query = "INSERT INTO players (id, team_id, is_active) VALUES (%s, %s, %s)"
        params = (player.get_player_id(), player.get_team_id(), player.get_is_active())
        return query, params
    
    def __create_player_awards_query(self, award: PlayerAwards) -> tuple:
        query = "INSERT INTO player_awards (id, award_name, year) VALUES (%s, %s, %s)"
        params = (award.get_player_id(), award.get_award(), award.get_year())
        return query, params

    def __create_player_details_query(self, player_details: PlayerDetails) -> tuple:
        query = "INSERT INTO player_details (id, first_name, last_name, birth_date, birth_city\
            , birth_state_province, birth_country, height_inches, weight_pounds, shoots_catches, position\
            , jersey_number, headshot, hero_image, in_top_100_all_time, in_hhof) VALUES (%s, %s, %s, %s, %s, %s, %s, %s\
            , %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (player_details.get_player_id(), player_details.get_first_name(), player_details.get_last_name(), player_details.get_birth_date(), player_details.get_birth_city()
            , player_details.get_birth_state_province(), player_details.get_birth_country(), player_details.get_height_inches(), player_details.get_weight_pounds(), player_details.get_shoots_catches(), player_details.get_position()
            , player_details.get_jersey_number(), player_details.get_headshot(), player_details.get_hero_image(), player_details.get_in_top_100_all_time(), player_details.get_in_hhof())
        return query, params

    def __create_player_draft_query(self, player_draft: PlayerDraft) -> tuple:
        query = "INSERT INTO player_draft (id, year, team_id, round, pick_in_round, overall_pick) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (player_draft.get_player_id(), player_draft.get_year(), player_draft.get_team_id(), player_draft.get_round(), player_draft.get_pick_in_round(), player_draft.get_overall_pick())
        return query, params
    
    def update_active_players(self):
        """
        Updates the is_active and team_id columns in the players table.
        """
        active_players = self.__query_active_players()
        for player in active_players:
            player_id = player.get_player_id()
            is_active = self.fetch_active_players_update.check_is_player_active(player_id)
            if not is_active:
                query = "UPDATE players SET is_active = 0 WHERE id = %s"
                params = (player_id,)
                self.database_operator.write(query, params)
            else:
                team_id = player.get_team_id()
                new_team_id = self.fetch_active_players_update.fetch_new_team_id(player_id, team_id)
                if new_team_id:
                    query = "UPDATE players SET team_id = %s WHERE id = %s"
                    params = (new_team_id, player_id)
                    self.database_operator.write(query, params)
    
    def __query_active_players(self) -> list:
        query = "SELECT id, team_id, is_active FROM players WHERE is_active = 1"
        res = self.database_operator.read(query)
        active_players = []
        for row in res:
            player = Player(row[0])
            player.set_team_id(row[1])
            player.set_is_active(row[2])
            active_players.append(player)
        return active_players

    def __update_team_id(self, player_id, team_id):
        url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
        player_info = self.api_connector.get_json(url)
        new_team_id = player_info["currentTeamId"]

        if new_team_id != team_id:
            return new_team_id
        return None
    
    def __update_players_query(self, player: Player) -> tuple:
        query = "UPDATE players SET team_id = %s, is_active = %s WHERE id = %s"
        params = (player.get_team_id(), player.get_is_active(), player.get_player_id())
        return query, params
    
    def __update_player_details_query(self, player_details: PlayerDetails) -> tuple:
        query = "UPDATE player_details SET first_name = %s, last_name = %s, birth_date = %s, birth_city = %s\
            , birth_state_province = %s, birth_country = %s, height_inches = %s, weight_pounds = %s, shoots_catches = %s, position = %s\
            , jersey_number = %s, headshot = %s, hero_image = %s, in_top_100_all_time = %s, in_hhof = %s WHERE id = %s"
        params = (player_details.get_first_name(), player_details.get_last_name(), player_details.get_birth_date(), player_details.get_birth_city()
            , player_details.get_birth_state_province(), player_details.get_birth_country(), player_details.get_height_inches(), player_details.get_weight_pounds(), player_details.get_shoots_catches(), player_details.get_position()
            , player_details.get_jersey_number(), player_details.get_headshot(), player_details.get_hero_image(), player_details.get_in_top_100_all_time(), player_details.get_in_hhof(), player_details.get_player_id())
        return query, params
    
    def __update_player_draft_query(self, player_draft: PlayerDraft) -> tuple:
        query = "UPDATE player_draft SET year = %s, team_id = %s, round = %s, pick_in_round = %s, overall_pick = %s WHERE id = %s"
        params = (player_draft.get_year(), player_draft.get_team_id(), player_draft.get_round(), player_draft.get_pick_in_round(), player_draft.get_overall_pick(), player_draft.get_player_id())
        return query, params
    
    def __update_player_awards_query(self, award: PlayerAwards) -> tuple:
        query = "UPDATE player_awards SET award_name = %s, year = %s WHERE id = %s"
        params = (award.get_award(), award.get_year(), award.get_player_id())
        return query, params
    