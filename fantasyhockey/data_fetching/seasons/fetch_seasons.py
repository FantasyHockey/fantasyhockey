from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.seasons.models.season import Season

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
                season.set_conference_in_use(self.__parse_data(season_data, "conferencesInUsess"))
                season.set_division_in_use(self.__parse_data(season_data, "divisionsInUse"))
                season.set_point_for_ot_loss_in_use(self.__parse_data(season_data, "pointForOTlossInUse"))
                season.set_regulation_wins_in_use(self.__parse_data(season_data, "regulationWinsInUse"))
                season.set_row_in_use(self.__parse_data(season_data, "rowInUse"))
                season.set_standings_end(self.__parse_data(season_data, "standingsEnd"))
                season.set_standings_start(self.__parse_data(season_data, "standingsStart"))
                season.set_ties_in_use(self.__parse_data(season_data, "tiesInUse"))
                season.set_wild_card_in_use(self.__parse_data(season_data, "wildcardInUse"))
                self.seasons.append(season)
            except ValueError as e:
                print(f"Error occurred while fetching season data (id: {season_data['id']}): {e}")

    def __parse_data(self, json, key):
        if key in json:
            return json[key]
        raise ValueError(f"Key {key} not found in JSON data.")