from abc import ABC, abstractmethod
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.fetch import FetchSeasons, FetchDraftRankings
from fantasyhockey.data_fetching.maps import SeasonDatabaseMapper, DraftRankingDatabaseMapper


class AbstractUpdater(ABC):
    """
    Abstract base class for updating entities in the database.
    """

    def __init__(self, database_operator):
        """
        Initializes the AbstractUpdater instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.
        """
        self.database_operator = database_operator

    def update_in_db(self):
        """
        Fetches the data and updates the corresponding table in the database.
        """
        entities = self.fetch_entities()
        for entity in entities:
            if self.entity_exists(entity):
                query = self.create_update_query()
                params = self.to_database_params(entity)
                self.database_operator.write(query, params[1:] + (params[0],))
            else:
                query = self.create_insert_query()
                params = self.to_database_params(entity)
                self.database_operator.write(query, params)

    @abstractmethod
    def fetch_entities(self):
        """
        Fetches the entities to be updated.
        
        Returns:
            list: A list of entities to be updated.
        """
        pass

    @abstractmethod
    def entity_exists(self, entity):
        """
        Checks if an entity exists in the database.
        
        Parameters
        ----------
        entity : object
            The entity to check.
        
        Returns:
            bool: True if the entity exists, False otherwise.
        """
        pass

    @abstractmethod
    def create_insert_query(self) -> str:
        """
        Creates an insert query for the entities table.
        
        Returns:
            str: The insert query string.
        """
        pass

    @abstractmethod
    def create_update_query(self) -> str:
        """
        Creates an update query for the entities table.
        
        Returns:
            str: The update query string.
        """
        pass

    @abstractmethod
    def to_database_params(self, entity) -> tuple:
        """
        Maps an entity object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        entity : object
            The entity to be mapped.
        
        Returns:
            tuple: The tuple of parameters for database operations.
        """
        pass

class CentralUpdater:
    """
    A class to manage and execute updates for various entities in the database.
    """

    def __init__(self, updaters):
        """
        Initializes the CentralUpdater instance.
        
        Parameters
        ----------
        updaters : list
            A list of AbstractUpdater instances to be executed.
        """
        self.updaters = updaters

    def update_all(self):
        """
        Executes the update_in_db method for each updater in the list.
        """
        for updater in self.updaters:
            updater.update_in_db()
           
class UpdateSeasons(AbstractUpdater):
    """
    A class to update the seasons table in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_seasons: FetchSeasons):
        """
        Initializes the UpdateSeasons instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.
            
        fetch_seasons : FetchSeasons
            An instance of the FetchSeasons class to fetch the seasons data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_seasons = fetch_seasons

    def fetch_entities(self):
        """
        Fetches the seasons to be updated.
        
        Returns:
            list: A list of Season objects to be updated.
        """
        return self.fetch_seasons.get_data()

    def entity_exists(self, season) -> bool:
        """
        Checks if a season exists in the seasons table.
        
        Parameters
        ----------
        season : Season
            The Season object to check.
        
        Returns:
            bool: True if the season exists, False otherwise.
        """
        query = SeasonDatabaseMapper.create_check_existence_query()
        result = self.database_operator.read(query, (season.year,))
        return bool(result)

    def create_insert_query(self) -> str:
        """
        Creates an insert query for the seasons table.
        
        Returns:
            str: The insert query string.
        """
        return SeasonDatabaseMapper.create_insert_query()

    def create_update_query(self) -> str:
        """
        Creates an update query for the seasons table.
        
        Returns:
            str: The update query string.
        """
        return SeasonDatabaseMapper.create_update_query()

    def to_database_params(self, season) -> tuple:
        """
        Maps a Season object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        season : Season
            The Season object to be mapped.
        
        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return SeasonDatabaseMapper.to_database_params(season)
    
class UpdateDraftRankings(AbstractUpdater):
    """
    A class to update the draft_rankings table in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_draft_rankings: FetchDraftRankings):
        """
        Initializes the UpdateDraftRankings instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.

        fetch_draft_rankings : FetchDraftRankings
            An instance of the FetchDraftRankings class to fetch the draft rankings data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_draft_rankings = fetch_draft_rankings

    def fetch_entities(self):
        """
        Fetches the draft rankings to be updated.
        
        Returns:
            list: A list of DraftRanking objects to be updated.
        """
        return self.fetch_draft_rankings.get_data()
    
    def entity_exists(self, draft_ranking) -> bool:
        """
        Checks if a draft ranking exists in the draft_rankings table.
        
        Parameters
        ----------
        draft_ranking : DraftRanking
            The DraftRanking object to check.
        
        Returns:
            bool: True if the draft ranking exists, False otherwise.
        """
        query = DraftRankingDatabaseMapper.create_check_existence_query()
        result = self.database_operator.read(query, (draft_ranking.year, draft_ranking.first_name, draft_ranking.last_name, draft_ranking.position_code))
        return bool(result)

    def create_insert_query(self) -> str:
        """
        Creates an insert query for the draft_rankings table.
        
        Returns:
            str: The insert query string.
        """
        return DraftRankingDatabaseMapper.create_insert_query()
    
    def create_update_query(self) -> str:
        """
        Creates an update query for the draft_rankings table.
        
        Returns:
            str: The update query string.
        """
        return DraftRankingDatabaseMapper.create_update_query()
    
    def to_database_params(self, draft_ranking) -> tuple:
        """
        Maps a DraftRanking object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        draft_ranking : DraftRanking
            The DraftRanking object to be mapped.
        
        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return DraftRankingDatabaseMapper.to_database_params(draft_ranking)
    
  