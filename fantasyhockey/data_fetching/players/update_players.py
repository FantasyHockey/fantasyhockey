from fantasyhockey.data_fetching.players.fetch_players import FetchPlayers
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.models.player import Player

class UpdatePlayers:

    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_players = FetchPlayers()

    def update_in_db(self):
        players = self.fetch_players.get_players()
        for player in players:
            query, params = self.__create_query(player)
            self.database_operator.write(query, params)

    def __create_query(self, player: Player) -> tuple:
        query = "INSERT INTO players (id, team_id, is_active) VALUES (%s, %s, %s)"
        params = (player.get_player_id(), player.get_team_id(), player.get_is_active())
        return query, params