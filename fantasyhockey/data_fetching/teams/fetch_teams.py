from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.teams.team import Team

class FetchTeams:
    def __init__(self):
        self.api_connector = APIConnector()
        self.franchises = []
        self.__FRANCHISE_URL = "https://api.nhle.com/stats/rest/en/franchise"

    def __fetch_franchise_ids(self):
        data = self.api_connector.get_json(self.__FRANCHISE_URL)
        for franchise_data in data["data"]:
            self.franchises.append(Team(self.__parse_data(franchise_data, "id")))

    def __parse_data(self, json, key):
        if key in json:
            return json[key]
        raise ValueError(f"Key {key} not found in JSON data.")