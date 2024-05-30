<<<<<<< HEAD
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.draft_rankings.models.draft_ranking import DraftRanking
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.data_fetching.serializers import SerializeDraftRanking

class FetchDraftRankings:
=======
from abc import ABC, abstractmethod
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.serializers import SerializerFactory
from fantasyhockey.data_fetching.models import Season, DraftRanking

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
        count = 0
        for season in self._items:
            try:
                season_obj = self._serializer.deserialize(season, Season)
                count += 1
                self._data.append(season_obj)
            except ValueError as e:
                print(f"Error occurred while fetching season data (id: {season['id']}): {e}")
            
            
    def _process_data(self, data):
        pass

class FetchDraftRankings(DataFetcher):
>>>>>>> a39f72b (Start of refactor)
    """
    A class to fetch the draft ranking data from the NHL API.

    Methods
    -------
    get_draft_ranking()
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
    """
<<<<<<< HEAD
    

    def __init__(self):
        self.api_connector = APIConnector()
        self.data_parser = DataParser()
        self.draft_rankings = []

    def get_draft_rankings(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
        """
        if not self.draft_rankings:
            self.__fetch()
        return self.draft_rankings

    def __fetch(self):
        data = self.api_connector.get_json("https://api-web.nhle.com/v1/draft/rankings/now")
        year = data["draftYear"]
        for player_data in data["rankings"]:
            try:
                final_rank = 0
                if "finalRank" in player_data:
                   final_rank = player_data["finalRank"]
                    
                ranking = SerializeDraftRanking(player_data).__serialize()
               
            

            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {player_data['firstName']}): {e}")

    
=======

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
>>>>>>> a39f72b (Start of refactor)
