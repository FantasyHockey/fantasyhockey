from abc import ABC, abstractmethod
from fantasyhockey.data_fetching.models import *


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

    def reverse_map(self, obj: object) -> dict:
        """
        Reverse maps the attributes of the given object to a dictionary.

        Args:
            obj (object): The object whose attributes will be reverse mapped.

        Returns:
            dict: A dictionary containing the reverse mapped attributes of the object.
        """
        result = {}
        for json_key, attr_name in self.field_map.items():
            result[json_key] = getattr(obj, attr_name)
        return result


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
            "id": "year",
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
            season.year,
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
    
class GoalieAdvancedStatsDaysRestApiMapper(ApiMapper):
    """
    Maps the data from the API response to the `GoalieAdvancedStatsDaysRest` object.

    Args:
        data_parser (DataParser): The data parser object used to parse the API response.
        util (Util): The utility object used to retrieve team IDs from abbreviations.

    Attributes:
        data_parser (DataParser): The data parser object used to parse the API response.
        util (Util): The utility object used to retrieve team IDs from abbreviations.
        field_map (dict): A dictionary mapping the API response keys to the corresponding attribute names in `GoalieAdvancedStatsDaysRest`.

    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "gamesPlayed": "games_played",
            "gamesPlayedDaysRest0": "games_played_days_rest_0",
            "gamesPlayedDaysRest1": "games_played_days_rest_1",
            "gamesPlayedDaysRest2": "games_played_days_rest_2",
            "gamesPlayedDaysRest3": "games_played_days_rest_3",
            "gamesPlayedDaysRest4": "games_played_days_rest_4",
            "gamesPlayedDaysRest4Plus": "games_played_days_rest_4_plus",
            "gamesStarted": "games_started",
            "losses": "losses",
            "otLosses": "ot_losses",
            "savePct": "save_percent",
            "savePctDaysRest0": "save_percent_days_rest_0",
            "savePctDaysRest1": "save_percent_days_rest_1",
            "savePctDaysRest2": "save_percent_days_rest_2",
            "savePctDaysRest3": "save_percent_days_rest_3",
            "savePctDaysRest4": "save_percent_days_rest_4",
            "savePctDaysRest4Plus": "save_percent_days_rest_4_plus"
        }

    def map(self, source: dict) -> object:
        """
        Maps the data from the API response to a `GoalieAdvancedStatsDaysRest` object.

        Args:
            source (dict): The API response data.

        Returns:
            GoalieAdvancedStatsDaysRest: The mapped `GoalieAdvancedStatsDaysRest` object.

        """
        goalie_stats = GoalieAdvancedStatsDaysRest()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
            setattr(goalie_stats, attr_name, value)
        return goalie_stats

class GoalieAdvancedStatsDaysRestDatabaseMapper:
    """
    Maps `GoalieAdvancedStatsDaysRest` objects to database rows and vice versa.
    
    """

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        """
        Maps a `GoalieAdvancedStatsDaysRest` object to a tuple of parameters for database operations.

        Args:
            season (Season): The `GoalieAdvancedStatsDaysRest` object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.

        """
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.games_played,
            season.games_played_days_rest_0,
            season.games_played_days_rest_1,
            season.games_played_days_rest_2,
            season.games_played_days_rest_3,
            season.games_played_days_rest_4,
            season.games_played_days_rest_4_plus,
            season.games_started,
            season.losses,
            season.ot_losses,
            season.save_percent,
            season.save_percent_days_rest_0,
            season.save_percent_days_rest_1,
            season.save_percent_days_rest_2,
            season.save_percent_days_rest_3,
            season.save_percent_days_rest_4,
            season.save_percent_days_rest_4_plus
        )
    
    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the goalie_advanced_stats_days_rest table.

        Returns:
            str: The insert query string.

        """
        return """
            INSERT INTO goalie_advanced_stats_days_rest (id, year, team_id, games_played, games_played_days_rest_0, games_played_days_rest_1,\
            games_played_days_rest_2, games_played_days_rest_3, games_played_days_rest_4, games_played_days_rest_4_plus, games_started, losses,\
            ot_losses, save_percent, save_percent_days_rest_0, save_percent_days_rest_1, save_percent_days_rest_2, save_percent_days_rest_3,\
            save_percent_days_rest_4, save_percent_days_rest_4_plus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the goalie_advanced_stats_days_rest table.

        Returns:
            str: The update query string.

        """
        return """
            UPDATE goalie_advanced_stats_days_rest SET
            year = %s,
            team_id = %s,
            games_played = %s,
            games_played_days_rest_0 = %s,
            games_played_days_rest_1 = %s,
            games_played_days_rest_2 = %s,
            games_played_days_rest_3 = %s,
            games_played_days_rest_4 = %s,
            games_played_days_rest_4_plus = %s,
            games_started = %s,
            losses = %s,
            ot_losses = %s,
            save_percent = %s,
            save_percent_days_rest_0 = %s,
            save_percent_days_rest_1 = %s,
            save_percent_days_rest_2 = %s,
            save_percent_days_rest_3 = %s,
            save_percent_days_rest_4 = %s,
            save_percent_days_rest_4_plus = %s
            WHERE id = %s AND year = %s
            """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a goalie advanced stats days rest record exists in the goalie_advanced_stats_days_rest table.

        Returns:
            str: The existence check query string.

        """
        return "SELECT 1 FROM goalie_advanced_stats_days_rest WHERE id = %s AND year = %s"

class GoalieAdvancedStatsPenaltyShotsApiMapper(ApiMapper):

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "penaltyShotSavePct": "penalty_shot_save_percent",
            "penaltyShotsAgainst": "penalty_shots_against",
            "penaltyShotsGoalsAgainst": "penalty_shots_goals_against",
            "penaltyShotsSaves": "penalty_shots_saves"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieAdvancedStatsPenaltyShots()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsPenaltyShotsDatabaseMapper:

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.penalty_shot_save_percent,
            season.penalty_shots_against,
            season.penalty_shots_goals_against,
            season.penalty_shots_saves
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO goalie_advanced_stats_penalty_shots (id, year, team_id, penalty_shot_save_percent, penalty_shot_against,\
            penalty_shot_goals_against, penalty_shot_saves) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_advanced_stats_penalty_shots SET
            year = %s,
            team_id = %s,
            penalty_shot_save_percent = %s,
            penalty_shot_against = %s,
            penalty_shot_goals_against = %s,
            penalty_shot_saves = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_advanced_stats_penalty_shots WHERE id = %s AND year = %s"
    
class GoalieAdvancedStatsSavesByStrength(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "evGoalsAgainst": "ev_goals_against",
            "evSavePct": "ev_save_percent",
            "evSaves": "ev_saves",
            "evShotsAgainst": "ev_shots_against",
            "ppGoalsAgainst": "pp_goals_against",
            "ppSavePct": "pp_save_percent",
            "ppSaves": "pp_saves",
            "ppShotsAgainst": "pp_shots_against",
            "shGoalsAgainst": "pk_goals_against",
            "shSavePct": "pk_save_percent",
            "shSaves": "pk_saves",
            "shShotsAgainst": "pk_shots_against"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieAdvancedStatsSavesByStrength()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsSavesByStrengthDatabaseMapper:
    
        @staticmethod
        def to_database_params(season: Season) -> tuple:
            return (
                season.player_id,
                season.year,
                season.team_id,
                season.ev_goals_against,
                season.ev_save_percent,
                season.ev_saves,
                season.ev_shots_against,
                season.pp_goals_against,
                season.pp_save_percent,
                season.pp_saves,
                season.pp_shots_against,
                season.pk_goals_against,
                season.pk_save_percent,
                season.pk_saves,
                season.pk_shots_against
            )
        
        @staticmethod
        def create_insert_query() -> str:
            return """
                INSERT INTO goalie_advanced_stats_saves_by_strength (id, year, team_id, ev_goals_against, ev_save_percent,\
                ev_saves, ev_shots_against, pp_goals_against, pp_save_percent, pp_saves, pp_shots_against, pk_goals_against,\
                pk_save_percent, pk_saves, pk_shots_against) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        
        @staticmethod
        def create_update_query() -> str:
            return """
                UPDATE goalie_advanced_stats_saves_by_strength SET
                year = %s,
                team_id = %s,
                ev_goals_against = %s,
                ev_save_percent = %s,
                ev_saves = %s,
                ev_shots_against = %s,
                pp_goals_against = %s,
                pp_save_percent = %s,
                pp_saves = %s,
                pp_shots_against = %s,
                pk_goals_against = %s,
                pk_save_percent = %s,
                pk_saves = %s,
                pk_shots_against = %s
                WHERE id = %s AND year = %s
                """
        
        @staticmethod
        def create_check_existence_query() -> str:
            return "SELECT 1 FROM goalie_advanced_stats_saves_by_strength WHERE id = %s AND year = %s"
        
class GoalieAdvancedStatsStartRelievedApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "gamesPlayed": "games_played",
            "gamesRelieved": "games_relieved",
            "gamesRelievedGoalsAgainst": "games_relieved_goals_against",
            "gamesRelievedLosses": "games_relieved_losses",
            "gamesRelievedOtLosses": "games_relieved_ot_losses",
            "gamesRelievedSavePct": "games_relieved_save_percent",
            "gamesRelievedSaves": "games_relieved_saves",
            "gamesRelievedShotsAgainst": "games_relieved_shots_against",
            "gamesRelievedTies": "games_relieved_ties",
            "gamesRelievedWins": "games_relieved_wins",
            "gamesStarted": "games_started",
            "gamesStartedGoalsAgainst": "games_started_goals_against",
            "gamesStartedLosses": "games_started_losses",
            "gamesStartedOtLosses": "games_started_ot_losses",
            "gamesStartedSavePct": "games_started_save_percent",
            "gamesStartedSaves": "games_started_saves",
            "gamesStartedShotsAgainst": "games_started_shots_against",
            "gamesStartedTies": "games_started_ties",
            "gamesStartedWins": "games_started_wins"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieAdvancedStatsStartRelieved()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
            setattr(goalie_stats, attr_name, value)
        return goalie_stats

class GoalieAdvancedStatsStartRelievedDatabaseMapper:

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.games_played,
            season.games_relieved,
            season.games_relieved_goals_against,
            season.games_relieved_losses,
            season.games_relieved_ot_losses,
            season.games_relieved_save_percent,
            season.games_relieved_saves,
            season.games_relieved_shots_against,
            season.games_relieved_ties,
            season.games_relieved_wins,
            season.games_started,
            season.games_started_goals_against,
            season.games_started_losses,
            season.games_started_ot_losses,
            season.games_started_save_percent,
            season.games_started_saves,
            season.games_started_shots_against,
            season.games_started_ties,
            season.games_started_wins
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO goalie_advanced_stats_start_relieved (id, year, team_id, games_played, games_relieved, games_relieved_goals_against,\
                games_relieved_losses, games_relieved_ot_losses, games_relieved_save_percent,\
                games_relieved_saves, games_relieved_shots_against, games_relieved_ties, games_relieved_wins, games_started, games_started_goals_against,\
                games_started_losses, games_started_ot_losses, games_started_save_percent, games_started_saves, games_started_shots_against,\
                games_started_ties, games_started_wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_advanced_stats_start_relieved SET
            year = %s,
            team_id = %s,
            games_played = %s,
            games_relieved = %s,
            games_relieved_goals_against = %s,
            games_relieved_losses = %s,
            games_relieved_ot_losses = %s,
            games_relieved_save_percent = %s,
            games_relieved_saves = %s,
            games_relieved_shots_against = %s,
            games_relieved_ties = %s,
            games_relieved_wins = %s,
            games_started = %s,
            games_started_goals_against = %s,
            games_started_losses = %s,
            games_started_ot_losses = %s,
            games_started_save_percent = %s,
            games_started_saves = %s,
            games_started_shots_against = %s,
            games_started_ties = %s,
            games_started_wins = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_advanced_stats_start_relieved WHERE id = %s AND year = %s"
    
class GoalieAdvancedStatsShootoutApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "careerShootoutGamesPlayed": "career_shootout_games_played",
            "careerShootoutGoalsAllowed": "career_shootout_goals_allowed",
            "careerShootoutLosses": "career_shootout_losses",
            "careerShootoutSavePct": "career_shootout_save_percent",
            "careerShootoutSaves": "career_shootout_saves",
            "careerShootoutShotsAgainst": "career_shootout_shots_against",
            "shootoutGoalsAgainst": "shootout_goals_against",
            "shootoutLosses": "shootout_losses",
            "shootoutSavePct": "shootout_save_percent",
            "shootoutSaves": "shootout_saves",
            "shootoutShotsAgainst": "shootout_shots_against",
            "shootoutWins": "shootout_wins"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieAdvancedStatsShootout()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsShootoutDatabaseMapper:

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.career_shootout_games_played,
            season.career_shootout_goals_allowed,
            season.career_shootout_losses,
            season.career_shootout_save_percent,
            season.career_shootout_saves,
            season.career_shootout_shots_against,
            season.shootout_goals_against,
            season.shootout_losses,
            season.shootout_save_percent,
            season.shootout_saves,
            season.shootout_shots_against,
            season.shootout_wins
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO goalie_advanced_stats_shootout (id, year, team_id, career_shootout_games_played, career_shootout_goals_allowed,\
                career_shootout_losses, career_shootout_save_percent, career_shootout_saves, career_shootout_shots_against, career_shootout_wins,\
                shootout_goals_against, shootout_losses, shootout_save_percent, shootout_saves, shootout_shots_against, shootout_wins)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_advanced_stats_shootout SET
            year = %s,
            team_id = %s,
            career_shootout_games_played = %s,
            career_shootout_goals_allowed = %s,
            career_shootout_losses = %s,
            career_shootout_save_percent = %s,
            career_shootout_saves = %s,
            career_shootout_shots_against = %s,
            career_shootout_wins = %s,
            shootout_goals_against = %s,
            shootout_losses = %s,
            shootout_save_percent = %s,
            shootout_saves = %s,
            shootout_shots_against = %s,
            shootout_wins = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_advanced_stats_shootout WHERE id = %s AND year = %s"
    
class GoalieAdvancedStatsApiMapper(ApiMapper):

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "completeGamePctg": "complete_game_percent",
            "completeGames": "complete_games",
            "gamesStarted": "games_started",
            "goals_against": "goals_against",
            "goalsAgainstAverage": "goals_against_average",
            "goalsFor": "goals_for",
            "goalsForAverage": "goals_for_average",
            "incompleteGames": "incomplete_games",
            "qualityStart": "quality_starts",
            "qualityStartsPct": "quality_starts_percent",
            "regulationLosses": "regulation_losses",
            "regulationWins": "regulation_wins",
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieAdvancedStats()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsDatabaseMapper:

    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.complete_game_percent,
            season.complete_games,
            season.games_started,
            season.goals_against,
            season.goals_against_average,
            season.goals_for,
            season.goals_for_average,
            season.incomplete_games,
            season.quality_starts,
            season.quality_starts_percent,
            season.regulation_losses,
            season.regulation_wins
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO goalie_advanced_stats (id, year, team_id, complete_game_percent, complete_games, games_played,\
                games_started, goals_against, goals_against_average, goals_for, goals_for_average, incomplete_games, quality_start,\
                quality_starts_percent, regulation_losses, regulation_wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_advanced_stats SET
            year = %s,
            team_id = %s,
            complete_game_percent = %s,
            complete_games = %s,
            games_played = %s,
            games_started = %s,
            goals_against = %s,
            goals_against_average = %s,
            goals_for = %s,
            goals_for_average = %s,
            incomplete_games = %s,
            quality_start = %s,
            quality_starts_percent = %s,
            regulation_losses = %s,
            regulation_wins = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_advanced_stats WHERE id = %s AND year = %s"
    
class GoalieYouthStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "season": "year",
            "teamName": "team_name",
            "leagueAbbrev": "league_abbrev",
            "gameTypeId": "game_type_id",
            "sequence": "sequence",
            "gamesPlayed": "games_played",
            "savePctg": "save_percent",
            "goalsAgainstAvg": "goals_against_average",
            "goalsAgainst": "goals_against",
            "wins": "wins",
            "losses": "losses",
            "toi": "time_on_ice",
            "ties": "ties"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieYouthStats()
        for json_key, attr_name in self.field_map.items():
            if json_key == "teamName":
                value = self.data_parser.double_parse(source, "teamName", "default", "none")
            else:
                value = self.data_parser.parse(source, json_key, "none")
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieYouthStatsDatabaseMapper:
    
        @staticmethod
        def to_database_params(season: Season) -> tuple:
            return (
                season.player_id,
                season.year,
                season.team_name,
                season.league_abbrev,
                season.game_type_id,
                season.sequence,
                season.games_played,
                season.save_percent,
                season.goals_against_average,
                season.goals_against,
                season.wins,
                season.losses,
                season.time_on_ice,
                season.ties
            )
        
        @staticmethod
        def create_insert_query() -> str:
            return """
                    INSERT INTO goalie_youth_stats (id, year, team_name, league_name, game_type_id, sequence, games_played, save_percent,\
                    goals_against_average, goals_against, wins, losses, time_on_ice, ties) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        
        @staticmethod
        def create_update_query() -> str:
            return """
                UPDATE goalie_youth_stats SET
                year = %s,
                team_name = %s,
                league_name = %s,
                game_type_id = %s,
                sequence = %s,
                games_played = %s,
                save_percent = %s,
                goals_against_average = %s,
                goals_against = %s,
                wins = %s,
                losses = %s,
                time_on_ice = %s,
                ties = %s
                WHERE id = %s AND year = %s AND team_name = %s AND league_name = %s AND game_type_id = %s AND sequence = %s
                """
        
        @staticmethod
        def create_check_existence_query() -> str:
            return "SELECT 1 FROM goalie_youth_stats WHERE id = %s AND year = %s AND team_name = %s AND league_name = %s AND game_type_id = %s AND sequence = %s"

class GoalieStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "season": "year",
            "teamName": "team_id",
            "gameTypeId": "game_type_id",
            "sequence": "sequence",
            "gamesPlayed": "games_played",
            "goals": "goals",
            "assists": "assists",
            "gamesStarted": "games_started",
            "wins": "wins",
            "losses": "losses",
            "otLosses": "ot_losses",
            "shotsAgainst": "shots_against",
            "goalsAgainst": "goals_against",
            "savePctg": "save_percent",
            "shutouts": "shutouts",
            "timeOnIce": "time_on_ice",
            "penaltyMinutes": "penalty_minutes",
            "goalsAgainstAvg": "goals_against_average"
        }

    def map(self, source: dict) -> object:
        goalie_stats = GoalieStats()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_name(self.data_parser.double_parse(source, "teamName", "default", "none"))
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieStatsDatabaseMapper:
        
    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.game_type_id,
            season.sequence,
            season.games_played,
            season.goals,
            season.assists,
            season.games_started,
            season.wins,
            season.losses,
            season.ot_losses,
            season.shots_against,
            season.goals_against,
            season.save_percent,
            season.shutouts,
            season.time_on_ice,
            season.penalty_minutes,
            season.goals_against_average
        )
            
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO goalie_stats (id, team_id, year, game_type_id, sequence, games_played, goals, assists, games_started,\
                wins, losses, ot_losses, shots_against, goals_against, save_percent, shutouts, time_on_ice, goals_against_average,\
                penalty_minutes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_stats SET
            team_id = %s,
            year = %s,
            game_type_id = %s,
            sequence = %s,
            games_played = %s,
            goals = %s,
            assists = %s,
            games_started = %s,
            wins = %s,
            losses = %s,
            ot_losses = %s,
            shots_against = %s,
            goals_against = %s,
            save_percent = %s,
            shutouts = %s,
            time_on_ice = %s,
            goals_against_average = %s,
            penalty_minutes = %s
            WHERE id = %s AND team_id = %s AND year = %s AND game_type_id = %s AND sequence = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_stats WHERE id = %s AND team_id = %s AND year = %s AND game_type_id = %s AND sequence = %s"
            
class SkaterStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "season": "year",
            "teamName": "team_id",
            "gamesPlayed": "games_played",
            "goals": "goals",
            "assists": "assists",
            "points": "points",
            "plusMinus": "plus_minus",
            "pim": "penalty_minutes",
            "gameWinningGoals": "game_winning_goals",
            "otGoals": "ot_goals",
            "powerPlayGoals": "power_play_goals",
            "powerPlayPoints": "power_play_points",
            "shootingPctg": "shooting_percent",
            "shorthandedGoals": "shorthanded_goals",
            "shorthandedPoints": "shorthanded_points",
            "shots": "shots",
            "avgToi": "average_time_on_ice",
            "gameTypeId": "game_type_id",
            "sequence": "sequence",
            "faceoffWinningPctg": "faceoff_winning_percent"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterStats()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_name(self.data_parser.double_parse(source, "teamName", "default", "none"))
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterStatsDatabaseMapper:
        
        @staticmethod
        def to_database_params(season: Season) -> tuple:
            return (
                season.player_id,
                season.year,
                season.team_id,
                season.games_played,
                season.goals,
                season.assists,
                season.points,
                season.plus_minus,
                season.penalty_minutes,
                season.game_winning_goals,
                season.ot_goals,
                season.power_play_goals,
                season.power_play_points,
                season.shooting_percent,
                season.shorthanded_goals,
                season.shorthanded_points,
                season.shots,
                season.average_time_on_ice,
                season.game_type_id,
                season.sequence,
                season.faceoff_winning_percent
            )
        
        @staticmethod
        def create_insert_query() -> str:
            return """
                    INSERT INTO skater_stats (id, team_id, games_played, goals, assists, points, plus_minus, penalty_minutes,\
                    game_winning_goals, ot_goals, power_play_goals, power_play_points, shooting_percent, shorthanded_goals, shorthanded_points,\
                    shots, time_on_ice, game_type_id, year, sequence, faceoff_percent) VALUES (%s, %s, %s,\
                    %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s, %s, %s, %s, %s, %s, %s)
                """
        
        @staticmethod
        def create_update_query() -> str:
            return """
                UPDATE skater_stats SET
                team_id = %s,
                games_played = %s,
                goals = %s,
                assists = %s,
                points = %s,
                plus_minus = %s,
                penalty_minutes = %s,
                game_winning_goals = %s,
                ot_goals = %s,
                power_play_goals = %s,
                power_play_points = %s,
                shooting_percent = %s,
                shorthanded_goals = %s,
                shorthanded_points = %s,
                shots = %s,
                time_on_ice = %s,
                game_type_id = %s,
                year = %s,
                sequence = %s,
                faceoff_percent = %s
                WHERE id = %s AND team_id = %s AND year = %s AND game_type_id = %s AND sequence = %s
                """
        
        @staticmethod
        def create_check_existence_query() -> str:
            return "SELECT 1 FROM skater_stats WHERE id = %s AND team_id = %s AND year = %s AND game_type_id = %s AND sequence = %s"
        
class SkaterAdvancedStatsCorsiFenwickApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "gamesPlayed": "games_played",
            "satAgainst": "corsi_against",
            "satAhead": "corsi_ahead",
            "satBehind": "corsi_behind",
            "satClose": "corsi_close",
            "satFor": "corsi_for",
            "satTied": "corsi_tied",
            "satTotal": "corsi_total",
            "satRelative": "corsi_relative",
            "usatAgainst": "fenwick_against",
            "usatAhead": "fenwick_ahead",
            "usatBehind": "fenwick_behind",
            "usatClose": "fenwick_close",
            "usatFor": "fenwick_for",
            "usatTied": "fenwick_tied",
            "usatTied": "fenwick_tied",
            "usatTotal": "fenwick_total",
            "usatRelative": "fenwick_relative",
            "timeOnIcePerGame5v5": "time_on_ice_per_game_5v5",
            "satPercentage": "corsi_percentage",
            "satPercentageAhead": "corsi_percentage_ahead",
            "satPercentageBehind": "corsi_percentage_behind",
            "satPercentageClose": "corsi_percentage_close",
            "satPercentageTied": "corsi_percentage_tied",
            "shootingPct5v5": "shooting_percent_5v5",
            "skaterSavePct5v5": "skater_save_percent_5v5",
            "skaterShootingPlusSavePct5v5": "skater_shooting_plus_save_percent_5v5",
            "usatPercentage": "fenwick_percentage",
            "usatPercentageAhead": "fenwick_percentage_ahead",
            "usatPercentageBehind": "fenwick_percentage_behind",
            "usatPrecentageClose": "fenwick_percentage_close",
            "usatPercentageTied": "fenwick_percentage_tied",
            "zoneStartPct5v5": "zone_start_percent_5v5"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsCorsiFenwick()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsCorsiFenwickDatabaseMapper:
        
    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.games_played,
            season.corsi_against,
            season.corsi_ahead,
            season.corsi_behind,
            season.corsi_close,
            season.corsi_for,
            season.corsi_tied,
            season.corsi_total,
            season.corsi_relative,
            season.fenwick_against,
            season.fenwick_ahead,
            season.fenwick_behind,
            season.fenwick_close,
            season.fenwick_for,
            season.fenwick_tied,
            season.fenwick_total,
            season.fenwick_relative,
            season.time_on_ice_per_game_5v5,
            season.corsi_percentage,
            season.corsi_percentage_ahead,
            season.corsi_percentage_behind,
            season.corsi_percentage_close,
            season.corsi_percentage_tied,
            season.shooting_percent_5v5,
            season.skater_save_percent_5v5,
            season.skater_shooting_plus_save_percent_5v5,
            season.fenwick_percentage,
            season.fenwick_percentage_ahead,
            season.fenwick_percentage_behind,
            season.fenwick_percentage_close,
            season.fenwick_percentage_tied,
            season.zone_start_percent_5v5
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO skater_advanced_stats_corsi_fenwick (id, year, team_id, games_played, corsi_against, corsi_ahead, corsi_behind, corsi_close,\
                corsi_for, corsi_tied, corsi_total, fenwick_against, fenwick_ahead, fenwick_behind, fenwick_close, fenwick_for, fenwick_relative, fenwick_tied,\
                fenwick_total, corsi_percent, corsi_ahead_percent, corsi_behind_percent, corsi_close_percent, corsi_tied_percent, corsi_relative, shooting_percent_5on5,\
                skater_save_percent_5on5, skater_shooting_plus_save_percent_5on5, time_on_ice_5on5_per_game, fenwick_percent, fenwick_ahead_percent, fenwick_behind_percent,\
                fenwick_close_percent, fenwick_tied_percent, zone_start_5on5_percent) VALUES (%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,\
                %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE skater_advanced_stats_corsi_fenwick SET
            year = %s,
            team_id = %s,
            games_played = %s,
            corsi_against = %s,
            corsi_ahead = %s,
            corsi_behind = %s,
            corsi_close = %s,
            corsi_for = %s,
            corsi_tied = %s,
            corsi_total = %s,
            fenwick_against = %s,
            fenwick_ahead = %s,
            fenwick_behind = %s,
            fenwick_close = %s,
            fenwick_for = %s,
            fenwick_relative = %s,
            fenwick_tied = %s,
            fenwick_total = %s,
            corsi_percent = %s,
            corsi_ahead_percent = %s,
            corsi_behind_percent = %s,
            corsi_close_percent = %s,
            corsi_tied_percent = %s,
            corsi_relative = %s,
            shooting_percent_5on5 = %s,
            skater_save_percent_5on5 = %s,
            skater_shooting_plus_save_percent_5on5 = %s,
            time_on_ice_5on5_per_game = %s,
            fenwick_percent = %s,
            fenwick_ahead_percent = %s,
            fenwick_behind_percent = %s,
            fenwick_close_percent = %s,
            fenwick_tied_percent = %s,
            zone_start_5on5_percent = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM skater_advanced_stats_corsi_fenwick WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsFaceoffsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "defensiveZoneFaceoffs": "defensive_zone_faceoffs",
            "defensiveZoneFaceoffWins": "defensive_zone_faceoffs_won",
            "defensiveZoneFaceoffLosses": "defensive_zone_faceoffs_lost",
            "evFaceoffs": "ev_faceoffs",
            "evFaceoffsWon": "ev_faceoffs_won",
            "evFaceoffsLost": "ev_faceoffs_lost",
            "faceoffWinPct": "faceoff_percentage",
            "neutralZoneFaceoffs": "neutral_zone_faceoffs",
            "neutralZoneFaceoffWins": "neutral_zone_faceoffs_won",
            "neutralZoneFaceoffLosses": "neutral_zone_faceoffs_lost",
            "offensiveZoneFaceoffs": "offensive_zone_faceoffs",
            "offensiveZoneFaceoffWins": "offensive_zone_faceoffs_won",
            "offensiveZoneFaceoffLosses": "offensive_zone_faceoffs_lost",
            "ppFaceoffs": "pp_faceoffs",
            "ppFaceoffsWon": "pp_faceoffs_won",
            "ppFaceoffsLost": "pp_faceoffs_lost",
            "shFaceoffs": "pk_faceoffs",
            "shFaceoffsWon": "pk_faceoffs_won",
            "shFaceoffsLost": "pk_faceoffs_lost",
            "totalFaceoffs": "total_faceoffs",
            "totalFaceoffWins": "total_faceoffs_won",
            "totalFaceoffLosses": "total_faceoffs_lost"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsFaceoffs()
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsFaceoffsDatabaseMapper:
            
    @staticmethod
    def to_database_params(season: Season) -> tuple:
        return (
            season.player_id,
            season.year,
            season.defensive_zone_faceoffs,
            season.defensive_zone_faceoffs_won,
            season.defensive_zone_faceoffs_lost,
            season.ev_faceoffs,
            season.ev_faceoffs_won,
            season.ev_faceoffs_lost,
            season.faceoff_percentage,
            season.neutral_zone_faceoffs,
            season.neutral_zone_faceoffs_won,
            season.neutral_zone_faceoffs_lost,
            season.offensive_zone_faceoffs,
            season.offensive_zone_faceoffs_won,
            season.offensive_zone_faceoffs_lost,
            season.pp_faceoffs,
            season.pp_faceoffs_won,
            season.pp_faceoffs_lost,
            season.pk_faceoffs,
            season.pk_faceoffs_won,
            season.pk_faceoffs_lost,
            season.total_faceoffs,
            season.total_faceoffs_won,
            season.total_faceoffs_lost
        )
    
    @staticmethod
    def create_insert_query() -> str:
        return """
                INSERT INTO skater_advanced_stats_faceoffs (id, year, team_id, defensive_zone_faceoffs, defensive_zone_faceoffs_won, defensive_zone_faceoffs_lost,\
                ev_faceoffs, ev_faceoffs_won, ev_faceoffs_lost, faceoff_percent, neutral_zone_faceoffs, neutral_zone_faceoffs_won, neutral_zone_faceoffs_lost,\
                offensive_zone_faceoffs, offensive_zone_faceoffs_won, offensive_zone_faceoffs_lost, pp_faceoffs, pp_faceoffs_won, pp_faceoffs_lost, pk_faceoffs,\
                pk_faceoffs_won, pk_faceoffs_lost, total_faceoffs, total_faceoffs_won, total_faceoffs_lost) VALUES (%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,\
                %s,%s, %s,%s, %s,%s,%s, %s,%s, %s)
                """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE skater_advanced_stats_faceoffs SET
            year = %s,
            team_id = %s,
            defensive_zone_faceoffs = %s,
            defensive_zone_faceoffs_won = %s,
            defensive_zone_faceoffs_lost = %s,
            ev_faceoffs = %s,
            ev_faceoffs_won = %s,
            ev_faceoffs_lost = %s,
            faceoff_percent = %s,
            neutral_zone_faceoffs = %s,
            neutral_zone_faceoffs_won = %s,
            neutral_zone_faceoffs_lost = %s,
            offensive_zone_faceoffs = %s,
            offensive_zone_faceoffs_won = %s,
            offensive_zone_faceoffs_lost = %s,
            pp_faceoffs = %s,
            pp_faceoffs_won = %s,
            pp_faceoffs_lost = %s,
            pk_faceoffs = %s,
            pk_faceoffs_won = %s,
            pk_faceoffs_lost = %s,
            total_faceoffs = %s,
            total_faceoffs_won = %s,
            total_faceoffs_lost = %s
            WHERE id = %s AND year = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM skater_advanced_stats_faceoffs WHERE id = %s AND year = %s"
    

class Team