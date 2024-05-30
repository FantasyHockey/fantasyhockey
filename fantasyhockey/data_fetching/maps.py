from abc import ABC, abstractmethod
from fantasyhockey.data_fetching.models import Season, DraftRanking


class ApiMapper(ABC):
    """Abstract base class for mapping objects to dictionaries and vice versa."""

    @abstractmethod
    def map(self, source: dict) -> object:
        """Maps a dictionary to an object.

        Args:
            source (dict): The dictionary to be mapped.

        Returns:
            object: The mapped object.
        """
        pass

    @abstractmethod
    def reverse_map(self, obj: object) -> dict:
        """Maps an object to a dictionary.

        Args:
            obj (object): The object to be mapped.

        Returns:
            dict: The mapped dictionary.
        """
        pass


class ApiMapperFactory:
    """
    Factory class for creating mappers based on object type.
    """

    @staticmethod
    def get_mapper(obj_type: object) -> ApiMapper:
        """
        Returns a mapper based on the given object type.

        Parameters:
        - obj_type (str): The type of object for which to create a mapper.

        Returns:
        - Mapper: The mapper object.

        Raises:
        - ValueError: If the object type is unknown.
        """
        if obj_type == Season:
            return SeasonApiMapper()
        elif obj_type == DraftRanking:
            return DraftRankingApiMapper()
        else:
            raise ValueError(f"Unknown object type: {obj_type}")
        
class SeasonApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a Season object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the Season object.
    """

    def __init__(self):
        self.field_map = {
            "id": "season_id",
            "conferencesInUse": "conference_in_use",
            "divisionsInUse": "division_in_use",
            "pointForOTlossInUse": "point_for_ot_loss_in_use",
            "regulationWinsInUse": "regulation_wins_in_use",
            "rowInUse": "row_in_use",
            "standingsEnd": "standings_end",
            "standingsStart": "standings_start",
            "tiesInUse": "ties_in_use",
            "wildcardInUse": "wild_card_in_use"
        }

    def map(self, source: dict) -> object:
        """
        Maps data from a dictionary to a Season object.

        Args:
            source (dict): The dictionary containing the data to be mapped.

        Returns:
            object: The mapped Season object.
        """
        season = Season()
        for json_key, attr_name in self.field_map.items():
            setattr(season, attr_name, source.get(json_key))
        return season

    def reverse_map(self, obj: object) -> dict:
        """
        Maps data from a Season object to a dictionary.

        Args:
            obj (object): The Season object to be mapped.

        Returns:
            dict: The mapped dictionary.
        """
        result = {}
        for json_key, attr_name in self.field_map.items():
            result[json_key] = getattr(obj, attr_name)
        return result
    
class SeasonDatabaseMapper:
    """
    Maps Season objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        """
        Maps a Season object to a tuple of parameters for database operations.

        Args:
            season (Season): The Season object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            season.season_id,
            season.conference_in_use,
            season.division_in_use,
            season.point_for_ot_loss_in_use,
            season.regulation_wins_in_use,
            season.row_in_use,
            season.standings_start,
            season.standings_end,
            season.ties_in_use,
            season.wild_card_in_use
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the seasons table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO seasons (
                year, conferences_in_use, divisions_in_use, point_for_ot_loss, regulation_wins, `row`,
                standings_start_date, standings_end_date, ties_in_use, wild_card_in_use
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the seasons table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE seasons SET
                conferences_in_use = %s,
                divisions_in_use = %s,
                point_for_ot_loss = %s,
                regulation_wins = %s,
                `row` = %s,
                standings_start_date = %s,
                standings_end_date = %s,
                ties_in_use = %s,
                wild_card_in_use = %s
            WHERE year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a season exists in the seasons table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM seasons WHERE year = %s"
    
class DraftRankingApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a DraftRanking object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the DraftRanking object.
    """

    def __init__(self):
        self.field_map = {
            "year": "year",
            "firstName": "first_name",
            "lastName": "last_name",
            "positionCode": "position_code",
            "shootsCatches": "shoots_catches",
            "heightInInches": "height_inches",
            "weightInPounds": "weight_pounds",
            "lastAmateurClub": "last_amateur_club",
            "lastAmateurLeague": "last_amateur_league",
            "birthDate": "birth_date",
            "birthCity": "birth_city",
            "birthStateProvince": "birth_state_province",
            "birthCountry": "birth_country",
            "midtermRank": "midterm_rank",
            "finalRank": "final_rank"
        }

    def map(self, source: dict) -> object:
        """
        Maps data from a dictionary to a DraftRanking object.

        Args:
            source (dict): The dictionary containing the data to be mapped.

        Returns:
            object: The mapped DraftRanking object.
        """
        draft_ranking = DraftRanking()
        for json_key, attr_name in self.field_map.items():
            setattr(draft_ranking, attr_name, source.get(json_key))
        return draft_ranking

    def reverse_map(self, obj: object) -> dict:
        """
        Maps data from a DraftRanking object to a dictionary.

        Args:
            obj (object): The DraftRanking object to be mapped.

        Returns:
            dict: The mapped dictionary.
        """
        result = {}
        for json_key, attr_name in self.field_map.items():
            result[json_key] = getattr(obj, attr_name)
        return result
    
class DraftRankingDatabaseMapper:
    """
    Maps DraftRanking objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(draft_ranking: DraftRanking) -> tuple:
        """
        Maps a DraftRanking object to a tuple of parameters for database operations.

        Args:
            draft_ranking (DraftRanking): The DraftRanking object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            draft_ranking.year,
            draft_ranking.first_name,
            draft_ranking.last_name,
            draft_ranking.position_code,
            draft_ranking.shoots_catches,
            draft_ranking.height_inches,
            draft_ranking.weight_pounds,
            draft_ranking.last_amateur_club,
            draft_ranking.last_amateur_league,
            draft_ranking.birth_date,
            draft_ranking.birth_city,
            draft_ranking.birth_state_province,
            draft_ranking.birth_country,
            draft_ranking.midterm_rank,
            draft_ranking.final_rank
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the draft_rankings table.

        Returns:
            str: The insert query string.
        """
        return """
                INSERT INTO draft_rankings (year, first_name, last_name, position_code,\
                shoots_catches, height_inches, weight_pounds, last_amateur_club, last_amateur_league, birth_date, birth_city, birth_state_province, birth_country, midterm_rank, final_rank)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the draft_rankings table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE draft_rankings SET
                first_name = %s,
                last_name = %s,
                position_code = %s,
                shoots_catches = %s,
                height_inches = %s,
                weight_pounds = %s,
                last_amateur_club = %s,
                last_amateur_league = %s,
                birth_date = %s,
                birth_city = %s,
                birth_state_province = %s,
                birth_country = %s,
                midterm_rank = %s,
                final_rank = %s
            WHERE year = %s AND first_name = %s AND last_name = %s
        """
    
    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a draft ranking exists in the draft_rankings table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM draft_rankings WHERE year = %s AND first_name = %s AND last_name = %s AND position_code = %s"