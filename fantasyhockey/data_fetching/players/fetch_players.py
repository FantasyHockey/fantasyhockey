from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.players.models.player import Player

class FetchPlayers:
    def __init__(self):
        self.db_operator = DatabaseOperator()
        self.api_connector = APIConnector()
        self.__player_ids = []
        self.__players = []

    def get_players(self):
        if not self.__players:
            self.__fetch()
        return self.__players

    def __fetch(self):
        team_ids = self.__get_all_team_ids()
        for team in team_ids:
            self.__fetch_players_for_team(team[0], team[1])
        self.__remove_duplicates() # Remove duplicates

        self.__get_players()
    
    def __get_all_team_ids(self):
        """Get all team ids from the database."""
        query = "SELECT team_abbreviation, year FROM teams"
        res = self.db_operator.read(query)
        ids = []
        for row in res:
            ids.append([row[0], row[1]])

        # Eliminate duplicates
        for i in range(len(ids)):
            for j in range(i+1, len(ids)):
                if ids[i][0] == ids[j][0]:
                    ids.pop(j)
                    break
        return ids

    def __fetch_players_for_team(self, team_abbrev, year):
        """Fetch players for a given team."""
        players = self.api_connector.get_json(f"https://api-web.nhle.com/v1/roster/{team_abbrev}/{year}")

        try:
            forwards = self.__parse_data(players, "forwards")
            for player in forwards:
                try:
                    self.__player_ids.append(self.__parse_data(player, "id"))
                except KeyError:
                    print("Error parsing a player id from the forwards from team id: ", team_abbrev, " year: ", year)
                    continue
            defensemen = self.__parse_data(players, "defensemen")
            for player in defensemen:
                try:
                    self.__player_ids.append(self.__parse_data(player, "id"))
                except KeyError:
                    print("Error parsing a player id from the defensemen from team id: ", team_abbrev, " year: ", year)
                    continue

            goalies = self.__parse_data(players, "goalies")
            for player in goalies:
                try:
                    self.__player_ids.append(self.__parse_data(player, "id"))
                except KeyError:
                    print("Error parsing a player id from the goalies from team id: ", team_abbrev, " year: ", year)
                    continue
        except KeyError:
            print("Error parsing players from team id: ", team_abbrev, " year: ", year)
            return

    def __remove_duplicates(self):
        """Remove duplicate player ids."""
        self.__player_ids = list(set(self.__player_ids))

    def __parse_data(self, json, key):
        """Parse json data."""
        if key in json:
            return json[key]
        raise ValueError(f"Key {key} not found in json.")

    def __get_players(self):
        """Get players from the database."""
        for player_id in self.__player_ids:
            json = self.api_connector.get_json(f"https://api-web.nhle.com/v1/player/{player_id}/landing")
            player = Player(player_id)
            try:
                if "currentTeamId" not in json:
                    team_id = None
                else:
                    team_id = self.__parse_data(json, "currentTeamId")
                player.set_team_id(team_id)
            except KeyError:
                print("Error parsing team id from player id: ", player_id)
                continue
            try: 
                is_active = self.__parse_data(json, "isActive")
                player.set_is_active(is_active)
            except KeyError:
                print("Error parsing is active from player id: ", player_id)
                continue
            self.__players.append(player)
