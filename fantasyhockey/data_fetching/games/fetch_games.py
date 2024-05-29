from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.games.models.game import Game
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util

class FetchGames:
    def __init__(self):
        self.__games = []
        self.__game_ids = []
        self.__database_operator = DatabaseOperator()
        self.__api_connector = APIConnector()
        self.__data_parser = DataParser()
        self.__util = Util()

    def get_games(self):
        if not self.__games:
            self.__fetch()
        return self.__games

    def __fetch(self):
        self.__get_all_games()

        #self.__get_skater_data()


    def __get_skater_data(self):
        count = 0
        for skater_id in self.__skater_ids:
            count += 1
            print(f"Fetching skater {count} of {len(self.__skater_ids)}")
        

    def __get_skater_stats(self, skater_id):
        url = f"https://api-web.nhle.com/v1/player/{skater_id}/landing"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "seasonTotals", "empty_list")

        stat_seasons = []
        youth_seasons = []


    def __get_all_games(self):
        query = "SELECT team_abbreviation, year FROM teams;"
        res = self.__database_operator.read(query)
        all_game_ids = []
        for row in res:
            team_abbrev = row[0]
            year = row[1]
            ids = self.__lookup_season_schedule(team_abbrev, year)
            all_game_ids.extend(ids)

        self.__game_ids = list(set(all_game_ids))
        

    def __lookup_season_schedule(self, team_abbrev, year):
        url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_abbrev}/{year}"
        data = self.__api_connector.get_json(url)
        team_game_ids = []
        try:
            for game in data["games"]:
                team_game_ids.append(game["id"])
        except:
            print(f"Error fetching games for {team_abbrev} in {year}")

        return team_game_ids
