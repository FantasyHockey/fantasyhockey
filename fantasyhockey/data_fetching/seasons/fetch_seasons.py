from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.seasons.models.season import Season
from fantasyhockey.util.data_parser import DataParser

class FetchSeasons:
    """
    A class to fetch the seasons data from the NHL API.

    Methods
    -------
    get_seasons()
        Fetches the seasons data from the NHL API and returns a list of Season objects.
    """

    def __init__(self):
        self.api_connector = APIConnector()
        self.data_parser = DataParser()
        self.seasons = []


    def get_seasons(self):
        """
        Fetches the seasons data from the NHL API and returns a list of Season objects.
        """
        if not self.seasons:
            self.__fetch()
        return self.seasons

    def __fetch(self):
        data = self.api_connector.get_json("https://api-web.nhle.com/v1/standings-season/")
        for season_data in data["seasons"]:
            try:
                season = Season(season_data["id"])
                season.set_conference_in_use(self.data_parser.parse(season_data, "conferencesInUsess", "none"))
                season.set_division_in_use(self.data_parser.parse(season_data, "divisionsInUse", "none"))
                season.set_point_for_ot_loss_in_use(self.data_parser.parse(season_data, "pointForOTlossInUse", "none"))
                season.set_regulation_wins_in_use(self.data_parser.parse(season_data, "regulationWinsInUse", "none"))
                season.set_row_in_use(self.data_parser.parse(season_data, "rowInUse", "none"))
                season.set_standings_end(self.data_parser.parse(season_data, "standingsEnd", "none"))
                season.set_standings_start(self.data_parser.parse(season_data, "standingsStart", "none"))
                season.set_ties_in_use(self.data_parser.parse(season_data, "tiesInUse", "none"))
                season.set_wild_card_in_use(self.data_parser.parse(season_data, "wildcardInUse", "none"))
                self.seasons.append(season)
            except ValueError as e:
                print(f"Error occurred while fetching season data (id: {season_data['id']}): {e}")