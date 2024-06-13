from abc import ABC, abstractmethod
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.serializers import SerializerFactory
from fantasyhockey.data_fetching.models import *

class DataFetcher(ABC):
    """
    Abstract base class for fetching data.

    Attributes:
        _data (list): A list to store the fetched data.
        _items (list): A list to store the items to fetch data for.
        _database_operator (DatabaseOperator): An instance of the DatabaseOperator class.
        _api_connector (APIConnector): An instance of the APIConnector class.
        _data_parser (DataParser): An instance of the DataParser class.
        _util (Util): An instance of the Util class.
        _serializer (Serializer): An instance of the Serializer class.

    Methods:
        get_data(): Returns the fetched data.
        _fetch(): Fetches the data by calling _get_items() and _get_data_by_item() methods.
        _get_items(): Abstract method to be implemented by subclasses to get the items to fetch data for.
        _get_data_by_item(): Abstract method to be implemented by subclasses to fetch data for each item.
        _process_data(data): Abstract method to be implemented by subclasses to process the fetched data.
    """

    def __init__(self):
        self._data = []
        self._items = []
        self._data_parser = DataParser()
        self._database_operator = DatabaseOperator()
        self._api_connector = APIConnector()
        self._serializer = SerializerFactory.get_serializer("json")

    def get_data(self):
        """
        Returns the fetched data.

        Returns:
            list: The fetched data.
        """
        if not self._data:
            self._fetch()
        return self._data

    def _fetch(self):
        """
        Fetches the data by calling _get_items() and _get_data_by_item() methods.
        """
        self._get_items()
        self._get_data_by_item()

    def _fetch_paginated_data(self, url, start=0, accumulated_data=None):
        """
        Recursively fetches paginated data from the given URL.

        Args:
            url (str): The URL to fetch data from.
            start (int): The starting point for fetching data.
            accumulated_data (list): The accumulated data from previous pages.

        Returns:
            list: The accumulated data from all pages.
        """
        if accumulated_data is None:
            accumulated_data = []

        paginated_url = f"{url}&start={start}"
        data = self._api_connector.get_json(paginated_url)

        total_count = data["total"]
        accumulated_data.extend(data["data"])

        if start + len(data["data"]) < total_count:
            return self._fetch_paginated_data(url, start + len(data["data"]), accumulated_data)
        else:
            return accumulated_data

    @abstractmethod
    def _get_items(self):
        """
        Abstract method to be implemented by subclasses to get the items to fetch data for.
        """
        pass

    @abstractmethod
    def _get_data_by_item(self):
        """
        Abstract method to be implemented by subclasses to fetch data for each item.
        """
        pass

    @abstractmethod
    def _process_data(self, data):
        """
        Abstract method to be implemented by subclasses to process the fetched data.

        Args:
            data (list): The fetched data.
        """
        pass

class FetchSeasons(DataFetcher):
    def __init__(self):
        super().__init__()

    def _get_items(self):
        self._items = self._api_connector.get_json("https://api-web.nhle.com/v1/standings-season/")["seasons"]

    def _get_data_by_item(self):
        for season in self._items:
            try:
                season_obj = self._serializer.deserialize(season, Season)
                self._data.append(season_obj)
            except ValueError as e:
                print(f"Error occurred while fetching season data (id: {season['id']}): {e}")
            
            
    def _process_data(self, data):
        pass

class FetchDraftRankings(DataFetcher):
    """
    A class to fetch the draft ranking data from the NHL API.

    Methods
    -------
    get_draft_ranking()
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
    """

    def __init__(self):
        super().__init__()

    def _get_items(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
        """
        data = self._api_connector.get_json("https://api-web.nhle.com/v1/draft/rankings/now")
        self.items = data["rankings"]
        for item in self.items:
            item["year"] = data["draftYear"]

    def _get_data_by_item(self):
        for item in self.items:
            try:
                draft_ranking = self._serializer.deserialize(item, DraftRanking)
                self._data.append(draft_ranking)
            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {item['firstName']}): {e}")

    def _process_data(self, data):
        pass

class FetchTeams(DataFetcher):
    """
    A class to fetch the team data from the NHL API.

    Methods
    -------
    get_teams()
        Fetches the team data from the NHL API and returns a list of team objects

    Notes
    -------
    The NHL API does not provide a direct endpoint to fetch team data. The team data is fetched from the standings data.
    But I will add all of the stat data into one team data for each team.
    """

    def __init__(self):
        super().__init__()
        self.__TEAM_ID_URL = "https://api.nhle.com/stats/rest/en/team"
        self.__ROSTER_SEASON_URL = "https://api-web.nhle.com/v1/roster-season/mtl"
        self.__TEAM_URL = "https://api-web.nhle.com/v1/standings/"
        self.team_id_lookup = None   

    def _get_items(self):
        """
        Fetches the team data from the NHL API and returns a list of team objects
        """
        self._get_team_id_lookup()
        years = self._api_connector.get_json(self.__ROSTER_SEASON_URL)
        for year in years:
            self._process_data(year)
        

    def _get_data_by_item(self):
        for team in self._items:
            try:
                draft_ranking = self._serializer.deserialize(item, DraftRanking)
                self._data.append(draft_ranking)
            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {item['firstName']}): {e}")


    def _process_data(self, year):
        data = self._api_connector.get_json(self.__TEAM_URL + str(year)[4:] + "-04-18")
        for team_json in data["standings"]:
            self._items.append(team_json)

    def _get_team_id_lookup(self):
        """
        Fetches and stores the team ID lookup data.
        """
        data = self._api_connector.get_json(self.__TEAM_ID_URL)
        self.team_id_lookup = data["data"]