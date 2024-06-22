from abc import ABC, abstractmethod
from fantasyhockey.data_fetching.models import *
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util


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
        data_parser = DataParser()
        util = Util()
        if obj_type == Season:
            return SeasonApiMapper()
        elif obj_type == DraftRanking:
            return DraftRankingApiMapper()

        elif obj_type == GoalieAdvancedStatsDaysRest:
            return GoalieAdvancedStatsDaysRestApiMapper(data_parser, util)
        elif obj_type == GoalieAdvancedStatsPenaltyShots:
            return GoalieAdvancedStatsPenaltyShotsApiMapper(data_parser, util)
        elif obj_type == GoalieAdvancedStatsSavesByStrength:
            return GoalieAdvancedStatsSavesByStrengthApiMapper(data_parser, util)
        elif obj_type == GoalieAdvancedStatsStartRelieved:
            return GoalieAdvancedStatsStartRelievedApiMapper(data_parser, util)
        elif obj_type == GoalieAdvancedStatsShootout:
            return GoalieAdvancedStatsShootoutApiMapper(data_parser, util)
        elif obj_type == GoalieAdvancedStats:
            return GoalieAdvancedStatsApiMapper(data_parser, util)
        elif obj_type == GoalieYouthStats:
            return GoalieYouthStatsApiMapper(data_parser, util)
        elif obj_type == GoalieStats:
            return GoalieStatsApiMapper(data_parser, util)
        elif obj_type == SkaterStats:
            return SkaterStatsApiMapper(data_parser, util)
        elif obj_type == YouthSkaterStats:
            return SkaterYouthStatsApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsCorsiFenwick:
            return SkaterAdvancedStatsCorsiFenwickApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsFaceoffs:
            return SkaterAdvancedStatsFaceoffsApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsGoals:
            return SkaterAdvancedStatsGoalsApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsMisc:
            return SkaterAdvancedStatsMiscApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsPenalties:
            return SkaterAdvancedStatsPenaltiesApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsPenaltyKill:
            return SkaterAdvancedStatsPenaltyKillApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsPowerplay:
            return SkaterAdvancedStatsPowerplayApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsScoring:
            return SkaterAdvancedStatsScoringApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsShootout:
            return SkaterAdvancedStatsShootoutApiMapper(data_parser, util)
        elif obj_type == SkaterAdvancedStatsTOI:
            return SkaterAdvancedStatsTOIApiMapper(data_parser, util)
        elif obj_type == PlayerAwards:
            return PlayerAwardsApiMapper(data_parser)
        elif obj_type == PlayerDetails:
            return PlayerDetailsApiMapper(data_parser)
        elif obj_type == PlayerDraft:
            return PlayerDraftApiMapper(data_parser, util)
        elif obj_type == TeamStats:
            return TeamStatsApiMapper(data_parser, util)
        elif obj_type == TeamData:
            return TeamDataApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsTeamGoalGames:
            return TeamAdvancedStatsTeamGoalGamesApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsShotType:
            return TeamAdvancedStatsShotTypeApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsScoringFirst:
            return TeamAdvancedStatsScoringFirstApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsPowerplayPenaltyKill:
            return TeamAdvancedStatsPowerplayPenaltyKillApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsPenalties:
            return TeamAdvancedStatsPenaltiesApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsOutshootOutshot:
            return TeamAdvancedStatsOutshootOutshotApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsMisc:
            return TeamAdvancedStatsMiscApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsLeadingTrailing:
            return TeamAdvancedStatsLeadingTrailingApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsGoalsByStrength:
            return TeamAdvancedStatsGoalsByStrengthApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsGoalsByPeriod:
            return TeamAdvancedStatsGoalsByPeriodApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsFaceoffPercent:
            return TeamAdvancedStatsFaceoffPercentApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsDaysRest:
            return TeamAdvancedStatsDaysRestApiMapper(data_parser, util)
        elif obj_type == TeamAdvancedStatsCorsiFenwick:
            return TeamAdvancedStatsCorsiFenwickApiMapper(data_parser, util)
        elif obj_type == Games:
            return GamesApiMapper(data_parser, util)
        elif obj_type == GameBoxscore:
            return GameBoxscoreApiMapper(data_parser, util)
        elif obj_type == GameGoalieStats:
            return GameGoalieStatsApiMapper(data_parser, util)
        elif obj_type == GameGoals:
            return GameGoalsApiMapper(data_parser, util)
        elif obj_type == GamePlays:
            return GamePlaysApiMapper(data_parser, util)
        elif obj_type == GameRoster:
            return GameRosterApiMapper(data_parser, util)
        elif obj_type == GameScoreboard:
            return GameScoreboardApiMapper(data_parser, util)
        elif obj_type == GameSkaterStats:
            return GameSkaterStatsApiMapper(data_parser, util)
        elif obj_type == GameThreeStars:
            return GameThreeStarsApiMapper(data_parser, util)
        elif obj_type == PlayoffBracket:
            return PlayoffBracketApiMapper(data_parser, util)
        elif obj_type == Referees:
            return RefereesApiMapper(data_parser, util)
        elif obj_type == ShiftData:
            return ShiftDataApiMapper(data_parser, util)
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
            "gamesPlayedDaysRest4Plus": "games_played_days_rest_4_plus",
            "gamesStarted": "games_started",
            "losses": "losses",
            "otLosses": "ot_losses",
            "savePct": "save_percent",
            "savePctDaysRest0": "save_percent_days_rest_0",
            "savePctDaysRest1": "save_percent_days_rest_1",
            "savePctDaysRest2": "save_percent_days_rest_2",
            "savePctDaysRest3": "save_percent_days_rest_3",
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStatsDaysRest(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats

class GoalieAdvancedStatsDaysRestDatabaseMapper:
    """
    Maps `GoalieAdvancedStatsDaysRest` objects to database rows and vice versa.
    
    """

    @staticmethod
    def to_database_params(season: GoalieAdvancedStatsDaysRest) -> tuple:
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
            season.games_played_days_rest_4_plus,
            season.games_started,
            season.losses,
            season.ot_losses,
            season.save_percent,
            season.save_percent_days_rest_0,
            season.save_percent_days_rest_1,
            season.save_percent_days_rest_2,
            season.save_percent_days_rest_3,
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
            games_played_days_rest_2, games_played_days_rest_3, games_played_days_rest_4_plus, games_started, losses,\
            ot_losses, save_percent, save_percent_days_rest_0, save_percent_days_rest_1, save_percent_days_rest_2, save_percent_days_rest_3,\
            save_percent_days_rest_4_plus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            games_played_days_rest_4_plus = %s,
            games_started = %s,
            losses = %s,
            ot_losses = %s,
            save_percent = %s,
            save_percent_days_rest_0 = %s,
            save_percent_days_rest_1 = %s,
            save_percent_days_rest_2 = %s,
            save_percent_days_rest_3 = %s,
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStatsPenaltyShots(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsPenaltyShotsDatabaseMapper:

    @staticmethod
    def to_database_params(season: GoalieAdvancedStatsPenaltyShots) -> tuple:
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
    
class GoalieAdvancedStatsSavesByStrengthApiMapper(ApiMapper):
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStatsSavesByStrength(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsSavesByStrengthDatabaseMapper:
    
        @staticmethod
        def to_database_params(season: GoalieAdvancedStatsSavesByStrength) -> tuple:
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStatsStartRelieved(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats

class GoalieAdvancedStatsStartRelievedDatabaseMapper:

    @staticmethod
    def to_database_params(season: GoalieAdvancedStatsStartRelieved) -> tuple:
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
            "careerShootoutWins": "career_shootout_wins",
            "shootoutGoalsAgainst": "shootout_goals_against",
            "shootoutLosses": "shootout_losses",
            "shootoutSavePct": "shootout_save_percent",
            "shootoutSaves": "shootout_saves",
            "shootoutShotsAgainst": "shootout_shots_against",
            "shootoutWins": "shootout_wins"
        }

    def map(self, source: dict) -> object:
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStatsShootout(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsShootoutDatabaseMapper:

    @staticmethod
    def to_database_params(season: GoalieAdvancedStatsShootout) -> tuple:
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
            season.career_shootout_wins,
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
            "teamAbbrevs": "team_id",
            "completeGamePct": "complete_game_percentage",
            "completeGames": "complete_games",
            "gamesStarted": "games_started",
            "goalsAgainst": "goals_against",
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieAdvancedStats(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieAdvancedStatsDatabaseMapper:

    @staticmethod
    def to_database_params(season: GoalieAdvancedStats) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
            season.complete_game_percentage,
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
                INSERT INTO goalie_advanced_stats (id, year, team_id, complete_game_percent, complete_games,\
                games_started, goals_against, goals_against_average, goals_for, goals_for_average, incomplete_games, quality_start,\
                quality_starts_percent, regulation_losses, regulation_wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_advanced_stats SET
            year = %s,
            team_id = %s,
            complete_game_percent = %s,
            complete_games = %s,
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
            "leagueAbbrev": "league_name",
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieYouthStats(player_id)
        for json_key, attr_name in self.field_map.items():
            if json_key == "teamName":
                value = self.data_parser.double_parse(source, "teamName", "default", "none")
            else:
                value = self.data_parser.parse(source, json_key, "none")
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieYouthStatsDatabaseMapper:
    
        @staticmethod
        def to_database_params(season: GoalieYouthStats) -> tuple:
            return (
                season.player_id,
                season.year,
                season.team_name,
                season.league_name,
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
        player_id = self.data_parser.parse(source, "playerId", "none")
        goalie_stats = GoalieStats(player_id)
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_name(self.data_parser.double_parse(source, "teamName", "default", "none"))
                if value == None:
                    value = 0
            setattr(goalie_stats, attr_name, value)
        return goalie_stats
    
class GoalieStatsDatabaseMapper:
        
    @staticmethod
    def to_database_params(season: GoalieStats) -> tuple:
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
                INSERT INTO goalie_stats (id, year, team_id, game_type_id, sequence, games_played, goals, assists, games_started,\
                wins, losses, ot_losses, shots_against, goals_against, save_percent, shutouts, time_on_ice, penalty_minutes,\
                goals_against_average) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    
    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE goalie_stats SET
            team_id = %s,
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
            WHERE id = %s AND year = %s AND team_id = %s AND game_type_id = %s AND sequence = %s
            """
    
    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM goalie_stats WHERE id = %s AND year = %s AND team_id = %s AND game_type_id = %s AND sequence = %s"
            
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
        skater_stats = SkaterStats(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_name(self.data_parser.double_parse(source, "teamName", "default", "none"))
                if value == None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterStatsDatabaseMapper:
        
        @staticmethod
        def to_database_params(season: SkaterStats) -> tuple:
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
                season.time_on_ice,
                season.game_type_id,
                season.sequence,
                season.faceoff_percent
            )
        
        @staticmethod
        def create_insert_query() -> str:
            return """
                    INSERT INTO skater_stats (id, year, team_id, games_played, goals, assists, points, plus_minus, penalty_minutes,\
                    game_winning_goals, ot_goals, power_play_goals, power_play_points, shooting_percent, shorthanded_goals, shorthanded_points,\
                    shots, time_on_ice, game_type_id, sequence, faceoff_percent) VALUES (%s, %s, %s,\
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
                sequence = %s,
                faceoff_percent = %s
                WHERE id = %s AND year = %s AND team_id = %s AND game_type_id = %s AND sequence = %s
                """
        
        @staticmethod
        def create_check_existence_query() -> str:
            return "SELECT 1 FROM skater_stats WHERE id = %s AND team_id = %s AND year = %s AND game_type_id = %s AND sequence = %s"

class SkaterYouthStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "season": "year",
            "teamName": "team_name",
            "leagueAbbrev": "league_name",
            "gameTypeId": "game_type_id",
            "sequence": "sequence",
            "gamesPlayed": "games_played",
            "goals": "goals",
            "assists": "assists",
            "points": "points",
            "pim": "pim",
        }

    def map(self, source: dict) -> object:
        skater_stats = YouthSkaterStats(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            if json_key == "teamName":
                value = self.data_parser.double_parse(source, "teamName", "default", "none")
            else:
                value = self.data_parser.parse(source, json_key, "none")
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterYouthStatsDatabaseMapper:
    
        @staticmethod
        def to_database_params(season: YouthSkaterStats) -> tuple:
            return (
                season.player_id,
                season.year,
                season.team_name,
                season.league_name,
                season.game_type_id,
                season.sequence,
                season.games_played,
                season.goals,
                season.assists,
                season.points,
                season.pim
            )
        
        @staticmethod
        def create_insert_query() -> str:
            return """
                    INSERT INTO skater_youth_stats (id, year, team_name, league_name, game_type_id, sequence, games_played, goals, assists, points, pim) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        
        @staticmethod
        def create_update_query() -> str:
            return """
                UPDATE skater_youth_stats SET
                year = %s,
                team_name = %s,
                league_name = %s,
                game_type_id = %s,
                sequence = %s,
                games_played = %s,
                goals = %s,
                assists = %s,
                points = %s,
                pim = %s
                WHERE id = %s AND year = %s AND team_name = %s AND league_name = %s AND game_type_id = %s AND sequence = %s
                """
        
        @staticmethod
        def create_check_existence_query() -> str:
            return "SELECT 1 FROM skater_youth_stats WHERE id = %s AND year = %s AND team_name = %s AND league_name = %s AND game_type_id = %s AND sequence = %s"

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
            "usatTotal": "fenwick_total",
            "usatRelative": "fenwick_relative",
            "timeOnIcePerGame5v5": "time_on_ice_per_game_5v5",
            "satPercentage": "corsi_percentage",
            "satPercentageAhead": "corsi_ahead_percentage",
            "satPercentageBehind": "corsi_behind_percentage",
            "satPercentageClose": "corsi_close_percentage",
            "satPercentageTied": "corsi_tied_percentage",
            "shootingPct5v5": "shooting_percent_5on5",
            "skaterSavePct5v5": "skater_save_percent_5on5",
            "skaterShootingPlusSavePct5v5": "skater_shooting_plus_save_percent_5on5",
            "usatPercentage": "fenwick_percentage",
            "usatPercentageAhead": "fenwick_ahead_percentage",
            "usatPercentageBehind": "fenwick_behind_percentage",
            "usatPrecentageClose": "fenwick_close_percentage",
            "usatPercentageTied": "fenwick_tied_percentage",
            "zoneStartPct5v5": "zone_start_5on5_percentage",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsCorsiFenwick(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                if type(value) == list:
                    value = self.util.get_team_id_from_abbrev(value[-1])
                else:
                    value = self.util.get_team_id_from_abbrev(value)

                if value is None:
                    value = 0

            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsCorsiFenwickDatabaseMapper:
        
    @staticmethod
    def to_database_params(season: SkaterAdvancedStatsCorsiFenwick) -> tuple:
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
            season.time_on_ice_5on5_per_game,
            season.corsi_percentage,
            season.corsi_ahead_percentage,
            season.corsi_behind_percentage,
            season.corsi_close_percentage,
            season.corsi_tied_percentage,
            season.shooting_percent_5on5,
            season.skater_save_percent_5on5,
            season.skater_shooting_plus_save_percent_5on5,
            season.fenwick_percentage,
            season.fenwick_ahead_percentage,
            season.fenwick_behind_percentage,
            season.fenwick_close_percentage,
            season.fenwick_tied_percentage,
            season.zone_start_5on5_percentage
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
            "totalFaceoffLosses": "total_faceoffs_lost",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsFaceoffs(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsFaceoffsDatabaseMapper:
            
    @staticmethod
    def to_database_params(season: SkaterAdvancedStatsFaceoffs) -> tuple:
        return (
            season.player_id,
            season.year,
            season.team_id,
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
                %s,%s, %s,%s, %s,%s,%s, %s, %s, %s)
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
    
class SkaterAdvancedStatsGoalsApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsGoals object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsGoals object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "evenStrengthGoalDifference": "even_strength_goal_difference",
            "evenStrengthGoalsAgainst": "even_strength_goals_against",
            "evenStrengthGoalsFor": "even_strength_goals_for",
            "evenStrengthTimeOnIcePerGame": "even_strength_time_on_ice_per_game",
            "gamesPlayed": "games_played",
            "powerPlayerGoalFor": "pp_goals_for",
            "powerPlayGoalsAgainst": "pp_goals_against",
            "shortHandedGoalsFor": "pk_goals_for",
            "shortHandedGoalsAgainst": "pk_goals_against",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsGoals(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsGoalsDatabaseMapper:
    """
    Maps SkaterAdvancedStatsGoals objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_goals: SkaterAdvancedStatsGoals) -> tuple:
        """
        Maps a SkaterAdvancedStatsGoals object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_goals (SkaterAdvancedStatsGoals): The SkaterAdvancedStatsGoals object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_goals.player_id,
            skater_advanced_stats_goals.year,
            skater_advanced_stats_goals.team_id,
            skater_advanced_stats_goals.even_strength_goal_difference,
            skater_advanced_stats_goals.even_strength_goals_against,
            skater_advanced_stats_goals.even_strength_goals_for,
            skater_advanced_stats_goals.even_strength_time_on_ice_per_game,
            skater_advanced_stats_goals.games_played,
            skater_advanced_stats_goals.pp_goals_for,
            skater_advanced_stats_goals.pp_goals_against,
            skater_advanced_stats_goals.pk_goals_for,
            skater_advanced_stats_goals.pk_goals_against
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_goals table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_goals (
                id, year, team_id, even_strength_goal_difference, even_strength_goals_against, 
                even_strength_goals_for, even_strength_time_on_ice_per_game, games_played, pp_goals_for, 
                pp_goals_against, pk_goals_for, pk_goals_against
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_goals table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_goals SET
                team_id = %s,
                even_strength_goal_difference = %s,
                even_strength_goals_against = %s,
                even_strength_goals_for = %s,
                even_strength_time_on_ice_per_game = %s,
                games_played = %s,
                pp_goals_for = %s,
                pp_goals_against = %s,
                pk_goals_for = %s,
                pk_goals_against = %s
            WHERE id = %s and year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_goals exists in the skater_advanced_stats_goals table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_goals WHERE id = %s AND year = %s"

class SkaterAdvancedStatsMiscApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsMisc object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsMisc object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "blockedShots": "blocked_shots",
            "emptyNetAssists": "empty_net_assists",
            "emptyNetGoals": "empty_net_goals",
            "emptyNetPoints": "empty_net_points",
            "firstGoals": "first_goals",
            "giveaways": "giveaways",
            "gamesPlayed": "games_played",
            "hits": "hits",
            "missedShotCrossbar": "missed_shot_crossbar",
            "missedShotGoalpost": "missed_shot_goalpost",
            "missedShotOver": "missed_shot_over",
            "missedShotWideOfNet": "missed_shot_wide",
            "missedShots": "missed_shots",
            "otGoals": "ot_goals",
            "takeaways": "takeaways",
            "timeOnIcePerGame": "time_on_ice_per_game",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsMisc(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsMiscDatabaseMapper:
    """
    Maps SkaterAdvancedStatsMisc objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_misc: SkaterAdvancedStatsMisc) -> tuple:
        """
        Maps a SkaterAdvancedStatsMisc object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_misc (SkaterAdvancedStatsMisc): The SkaterAdvancedStatsMisc object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_misc.player_id,
            skater_advanced_stats_misc.year,
            skater_advanced_stats_misc.team_id,
            skater_advanced_stats_misc.blocked_shots,
            skater_advanced_stats_misc.empty_net_assists,
            skater_advanced_stats_misc.empty_net_goals,
            skater_advanced_stats_misc.empty_net_points,
            skater_advanced_stats_misc.first_goals,
            skater_advanced_stats_misc.giveaways,
            skater_advanced_stats_misc.games_played,
            skater_advanced_stats_misc.hits,
            skater_advanced_stats_misc.missed_shot_crossbar,
            skater_advanced_stats_misc.missed_shot_goalpost,
            skater_advanced_stats_misc.missed_shot_over,
            skater_advanced_stats_misc.missed_shot_wide,
            skater_advanced_stats_misc.missed_shots,
            skater_advanced_stats_misc.ot_goals,
            skater_advanced_stats_misc.takeaways,
            skater_advanced_stats_misc.time_on_ice_per_game
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_misc table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_misc (
                id, year, team_id, blocked_shots, empty_net_assists, empty_net_goals,
                empty_net_points, first_goals, giveaways, games_played, hits, missed_shot_crossbar,
                missed_shot_goalpost, missed_shot_over, missed_shot_wide, missed_shots, ot_goals,
                takeaways, time_on_ice_per_game
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_misc table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_misc SET
                team_id = %s,
                blocked_shots = %s,
                empty_net_assists = %s,
                empty_net_goals = %s,
                empty_net_points = %s,
                first_goals = %s,
                giveaways = %s,
                games_played = %s,
                hits = %s,
                missed_shot_crossbar = %s,
                missed_shot_goalpost = %s,
                missed_shot_over = %s,
                missed_shot_wide = %s,
                missed_shots = %s,
                ot_goals = %s,
                takeaways = %s,
                time_on_ice_per_game = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_misc exists in the skater_advanced_stats_misc table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_misc WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsPenaltiesApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsPenalties object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsPenalties object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "gameMisconductPenalties": "game_misconduct_penalties",
            "gamesPlayed": "games_played",
            "majorPenalties": "major_penalties",
            "matchPenalties": "match_penalties",
            "minorPenalties": "minor_penalties",
            "misconductPenalties": "misconduct_penalties",
            "netPenalties": "net_penalties",
            "penalties": "penalties",
            "penaltiesDrawn": "penalties_drawn",
            "penaltyMinutes": "penalty_minutes",
            "timeOnIcePerGame": "time_on_ice_per_game",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsPenalties(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsPenaltiesDatabaseMapper:
    """
    Maps SkaterAdvancedStatsPenalties objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_penalties: SkaterAdvancedStatsPenalties) -> tuple:
        """
        Maps a SkaterAdvancedStatsPenalties object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_penalties (SkaterAdvancedStatsPenalties): The SkaterAdvancedStatsPenalties object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_penalties.player_id,
            skater_advanced_stats_penalties.year,
            skater_advanced_stats_penalties.team_id,
            skater_advanced_stats_penalties.game_misconduct_penalties,
            skater_advanced_stats_penalties.games_played,
            skater_advanced_stats_penalties.major_penalties,
            skater_advanced_stats_penalties.match_penalties,
            skater_advanced_stats_penalties.minor_penalties,
            skater_advanced_stats_penalties.misconduct_penalties,
            skater_advanced_stats_penalties.net_penalties,
            skater_advanced_stats_penalties.penalties,
            skater_advanced_stats_penalties.penalties_drawn,
            skater_advanced_stats_penalties.penalty_minutes,
            skater_advanced_stats_penalties.time_on_ice_per_game
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_penalties table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_penalties (
                id, year, team_id, game_misconduct_penalties, games_played, major_penalties,
                match_penalties, minor_penalties, misconduct_penalties, net_penalties, penalties,
                penalties_drawn, penalty_minutes, time_on_ice_per_game
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_penalties table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_penalties SET
                team_id = %s,
                game_misconduct_penalties = %s,
                games_played = %s,
                major_penalties = %s,
                match_penalties = %s,
                minor_penalties = %s,
                misconduct_penalties = %s,
                net_penalties = %s,
                penalties = %s,
                penalties_drawn = %s,
                penalty_minutes = %s,
                time_on_ice_per_game = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_penalties exists in the skater_advanced_stats_penalties table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_penalties WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsPenaltyKillApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsPenaltyKill object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsPenaltyKill object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "shAssists": "pk_assists",
            "shGoals": "pk_goals",
            "shIndividualSatFor": "pk_individual_corsi_for",
            "shPrimaryAssists": "pk_primary_assists",
            "shSecondaryAssists": "pk_secondary_assists",
            "shShootingPct": "pk_shooting_percentage",
            "shShots": "pk_shots",
            "shTimeOnIce": "pk_time_on_ice",
            "shTimeOnIcePerGame": "pk_time_on_ice_per_game",
            "shTimeOnIcePctPerGame": "pk_time_on_ice_percentage",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsPenaltyKill(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsPenaltyKillDatabaseMapper:
    """
    Maps SkaterAdvancedStatsPenaltyKill objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_penalty_kill: SkaterAdvancedStatsPenaltyKill) -> tuple:
        """
        Maps a SkaterAdvancedStatsPenaltyKill object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_penalty_kill (SkaterAdvancedStatsPenaltyKill): The SkaterAdvancedStatsPenaltyKill object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_penalty_kill.player_id,
            skater_advanced_stats_penalty_kill.year,
            skater_advanced_stats_penalty_kill.team_id,
            skater_advanced_stats_penalty_kill.pk_assists,
            skater_advanced_stats_penalty_kill.pk_goals,
            skater_advanced_stats_penalty_kill.pk_individual_corsi_for,
            skater_advanced_stats_penalty_kill.pk_primary_assists,
            skater_advanced_stats_penalty_kill.pk_secondary_assists,
            skater_advanced_stats_penalty_kill.pk_shooting_percentage,
            skater_advanced_stats_penalty_kill.pk_shots,
            skater_advanced_stats_penalty_kill.pk_time_on_ice,
            skater_advanced_stats_penalty_kill.pk_time_on_ice_per_game,
            skater_advanced_stats_penalty_kill.pk_time_on_ice_percentage
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_penalty_kill table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_penalty_kill (
                id, year, team_id, pk_assists, pk_goals, pk_individual_corsi_for, pk_primary_assists,
                pk_secondary_assists, pk_shooting_percentage, pk_shots, pk_time_on_ice, pk_time_on_ice_per_game, pk_time_on_ice_percentage
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_penalty_kill table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_penalty_kill SET
                team_id = %s,
                pk_assists = %s,
                pk_goals = %s,
                pk_individual_corsi_for = %s,
                pk_primary_assists = %s,
                pk_secondary_assists = %s,
                pk_shooting_percentage = %s,
                pk_shots = %s,
                pk_time_on_ice = %s,
                pk_time_on_ice_per_game = %s,
                pk_time_on_ice_percentage = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_penalty_kill exists in the skater_advanced_stats_penalty_kill table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_penalty_kill WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsPowerplayApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsPowerplay object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsPowerplay object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "ppAssists": "pp_assists",
            "ppGoals": "pp_goals",
            "ppIndividualSatFor": "pp_individual_corsi_for",
            "ppPrimaryAssists": "pp_primary_assists",
            "ppSecondaryAssists": "pp_secondary_assists",
            "ppShootingPct": "pp_shooting_percentage",
            "ppShots": "pp_shots",
            "ppTimeOnIce": "pp_time_on_ice",
            "ppTimeOnIcePerGame": "pp_time_on_ice_per_game",
            "ppTimeOnIcePctPerGame": "pp_time_on_ice_percentage",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsPowerplay(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsPowerplayDatabaseMapper:
    """
    Maps SkaterAdvancedStatsPowerplay objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_powerplay: SkaterAdvancedStatsPowerplay) -> tuple:
        """
        Maps a SkaterAdvancedStatsPowerplay object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_powerplay (SkaterAdvancedStatsPowerplay): The SkaterAdvancedStatsPowerplay object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_powerplay.player_id,
            skater_advanced_stats_powerplay.year,
            skater_advanced_stats_powerplay.team_id,
            skater_advanced_stats_powerplay.pp_assists,
            skater_advanced_stats_powerplay.pp_goals,
            skater_advanced_stats_powerplay.pp_individual_corsi_for,
            skater_advanced_stats_powerplay.pp_primary_assists,
            skater_advanced_stats_powerplay.pp_secondary_assists,
            skater_advanced_stats_powerplay.pp_shooting_percentage,
            skater_advanced_stats_powerplay.pp_shots,
            skater_advanced_stats_powerplay.pp_time_on_ice,
            skater_advanced_stats_powerplay.pp_time_on_ice_per_game,
            skater_advanced_stats_powerplay.pp_time_on_ice_percentage
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_powerplay table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_powerplay (
                id, year, team_id, pp_assists, pp_goals, pp_individual_corsi_for, pp_primary_assists,
                pp_secondary_assists, pp_shooting_percentage, pp_shots, pp_time_on_ice, pp_time_on_ice_per_game, pp_time_on_ice_percentage
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_powerplay table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_powerplay SET
                team_id = %s,
                pp_assists = %s,
                pp_goals = %s,
                pp_individual_corsi_for = %s,
                pp_primary_assists = %s,
                pp_secondary_assists = %s,
                pp_shooting_percentage = %s,
                pp_shots = %s,
                pp_time_on_ice = %s,
                pp_time_on_ice_per_game = %s,
                pp_time_on_ice_percentage = %s
            WHERE id = %s AND year = %s AND team_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_powerplay exists in the skater_advanced_stats_powerplay table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_powerplay WHERE id = %s AND year = %s AND team_id = %s"
    
class SkaterAdvancedStatsScoringApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsScoring object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsScoring object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "goalsBackhand": "goals_backhand",
            "goalsBat": "goals_bat",
            "goalsBetweenLegs": "goals_between_legs",
            "goalsCradle": "goals_cradle",
            "goalsDeflected": "goals_deflected",
            "goalsPoke": "goals_poke",
            "goalsSlap": "goals_slap",
            "goalsSnap": "goals_snap",
            "goalsTipIn": "goals_tip",
            "goalsWrapAround": "goals_wrap_around",
            "goalsWrist": "goals_wrist",
            "shotsOnNetBackhand": "shots_backhand",
            "shotsOnNetBat": "shots_bat",
            "shotsOnNetBetweenLegs": "shots_between_legs",
            "shotsOnNetCradle": "shots_cradle",
            "shotsOnNetDeflected": "shots_deflected",
            "shotsOnNetPoke": "shots_poke",
            "shotsOnNetSlap": "shots_slap",
            "shotsOnNetSnap": "shots_snap",
            "shotsOnNetTipIn": "shots_tip",
            "shotsOnNetWrapAround": "shots_wrap_around",
            "shotsOnNetWrist": "shots_wrist",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsScoring(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats

class SkaterAdvancedStatsScoringDatabaseMapper:
    """
    Maps SkaterAdvancedStatsScoring objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_scoring: SkaterAdvancedStatsScoring) -> tuple:
        """
        Maps a SkaterAdvancedStatsScoring object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_scoring (SkaterAdvancedStatsScoring): The SkaterAdvancedStatsScoring object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_scoring.player_id,
            skater_advanced_stats_scoring.year,
            skater_advanced_stats_scoring.team_id,
            skater_advanced_stats_scoring.goals_backhand,
            skater_advanced_stats_scoring.goals_bat,
            skater_advanced_stats_scoring.goals_between_legs,
            skater_advanced_stats_scoring.goals_cradle,
            skater_advanced_stats_scoring.goals_deflected,
            skater_advanced_stats_scoring.goals_poke,
            skater_advanced_stats_scoring.goals_slap,
            skater_advanced_stats_scoring.goals_snap,
            skater_advanced_stats_scoring.goals_tip,
            skater_advanced_stats_scoring.goals_wrap_around,
            skater_advanced_stats_scoring.goals_wrist,
            skater_advanced_stats_scoring.shots_backhand,
            skater_advanced_stats_scoring.shots_bat,
            skater_advanced_stats_scoring.shots_between_legs,
            skater_advanced_stats_scoring.shots_cradle,
            skater_advanced_stats_scoring.shots_deflected,
            skater_advanced_stats_scoring.shots_poke,
            skater_advanced_stats_scoring.shots_slap,
            skater_advanced_stats_scoring.shots_snap,
            skater_advanced_stats_scoring.shots_tip,
            skater_advanced_stats_scoring.shots_wrap_around,
            skater_advanced_stats_scoring.shots_wrist
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_scoring table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_scoring (
                id, year, team_id, goals_backhand, goals_bat, goals_between_legs, goals_cradle,
                goals_deflected, goals_poke, goals_slap, goals_snap, goals_tip, goals_wrap_around, goals_wrist,
                shots_backhand, shots_bat, shots_between_legs, shots_cradle, shots_deflected, shots_poke,
                shots_slap, shots_snap, shots_tip, shots_wrap_around, shots_wrist
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_scoring table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_scoring SET
                team_id = %s,
                goals_backhand = %s,
                goals_bat = %s,
                goals_between_legs = %s,
                goals_cradle = %s,
                goals_deflected = %s,
                goals_poke = %s,
                goals_slap = %s,
                goals_snap = %s,
                goals_tip = %s,
                goals_wrap_around = %s,
                goals_wrist = %s,
                shots_backhand = %s,
                shots_bat = %s,
                shots_between_legs = %s,
                shots_cradle = %s,
                shots_deflected = %s,
                shots_poke = %s,
                shots_slap = %s,
                shots_snap = %s,
                shots_tip = %s,
                shots_wrap_around = %s,
                shots_wrist = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_scoring exists in the skater_advanced_stats_scoring table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_scoring WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsShootoutApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsShootout object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsShootout object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "careerShootoutGameDecidingGoals": "career_shootout_game_deciding_goals",
            "careerShootoutGamesPlayed": "career_shootout_games_played",
            "careerShootoutGoals": "career_shootout_goals",
            "careerShootoutShootingPct": "career_shootout_percentage",
            "careerShootoutShots": "career_shootout_shots",
            "shootoutGameDecidingGoals": "shootout_game_deciding_goals",
            "shootoutGamesPlayed": "shootout_games_played",
            "shootoutGoals": "shootout_goals",
            "shootoutShootingPct": "shootout_percentage",
            "shootoutShots": "shootout_shots",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_stats = SkaterAdvancedStatsShootout(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrevs", "none"))
                if value is None:
                    value = 0
            setattr(skater_stats, attr_name, value)
        return skater_stats
    
class SkaterAdvancedStatsShootoutDatabaseMapper:
    """
    Maps SkaterAdvancedStatsShootout objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_shootout: SkaterAdvancedStatsShootout) -> tuple:
        """
        Maps a SkaterAdvancedStatsShootout object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_shootout (SkaterAdvancedStatsShootout): The SkaterAdvancedStatsShootout object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_shootout.player_id,
            skater_advanced_stats_shootout.year,
            skater_advanced_stats_shootout.team_id,
            skater_advanced_stats_shootout.career_shootout_game_deciding_goals,
            skater_advanced_stats_shootout.career_shootout_games_played,
            skater_advanced_stats_shootout.career_shootout_goals,
            skater_advanced_stats_shootout.career_shootout_percentage,
            skater_advanced_stats_shootout.career_shootout_shots,
            skater_advanced_stats_shootout.shootout_game_deciding_goals,
            skater_advanced_stats_shootout.shootout_games_played,
            skater_advanced_stats_shootout.shootout_goals,
            skater_advanced_stats_shootout.shootout_percentage,
            skater_advanced_stats_shootout.shootout_shots
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_shootout table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_shootout (
                id, year, team_id, career_shootout_game_deciding_goals, career_shootout_games_played, 
                career_shootout_goals, career_shootout_percentage, career_shootout_shots, shootout_game_deciding_goals, 
                shootout_games_played, shootout_goals, shootout_percentage, shootout_shots
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_shootout table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_shootout SET
                team_id = %s,
                career_shootout_game_deciding_goals = %s,
                career_shootout_games_played = %s,
                career_shootout_goals = %s,
                career_shootout_percentage = %s,
                career_shootout_shots = %s,
                shootout_game_deciding_goals = %s,
                shootout_games_played = %s,
                shootout_goals = %s,
                shootout_percentage = %s,
                shootout_shots = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_shootout exists in the skater_advanced_stats_shootout table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_shootout WHERE id = %s AND year = %s"
    
class SkaterAdvancedStatsTOIApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a SkaterAdvancedStatsTOI object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the SkaterAdvancedStatsTOI object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "seasonId": "year",
            "teamAbbrevs": "team_id",
            "evTimeOnIce": "ev_time_on_ice",
            "gamesPlayed": "games_played",
            "otTimeOnIce": "ot_time_on_ice",
            "otTimeOnIcePerOtGame": "ot_time_on_ice_per_ot_game",
            "ppTimeOnIce": "pp_time_on_ice",
            "shTimeOnIce": "sh_time_on_ice",
            "shifts": "shifts",
            "timeOnIce": "time_on_ice",
            "teamAbbrevs": "team_id"
        }

    def map(self, source: dict) -> object:
        skater_toi = SkaterAdvancedStatsTOI(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(value)
                if value is None:
                    value = 0
            setattr(skater_toi, attr_name, value)
        return skater_toi
    
class SkaterAdvancedStatsTOIDatabaseMapper:
    """
    Maps SkaterAdvancedStatsTOI objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(skater_advanced_stats_toi: SkaterAdvancedStatsTOI) -> tuple:
        """
        Maps a SkaterAdvancedStatsTOI object to a tuple of parameters for database operations.

        Args:
            skater_advanced_stats_toi (SkaterAdvancedStatsTOI): The SkaterAdvancedStatsTOI object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            skater_advanced_stats_toi.player_id,
            skater_advanced_stats_toi.year,
            skater_advanced_stats_toi.team_id,
            skater_advanced_stats_toi.ev_time_on_ice,
            skater_advanced_stats_toi.games_played,
            skater_advanced_stats_toi.ot_time_on_ice,
            skater_advanced_stats_toi.ot_time_on_ice_per_ot_game,
            skater_advanced_stats_toi.pp_time_on_ice,
            skater_advanced_stats_toi.sh_time_on_ice,
            skater_advanced_stats_toi.shifts,
            skater_advanced_stats_toi.time_on_ice
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the skater_advanced_stats_toi table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO skater_advanced_stats_toi (
                id, year, team_id, ev_time_on_ice, games_played, ot_time_on_ice, ot_time_on_ice_per_ot_game,
                pp_time_on_ice, sh_time_on_ice, shifts, time_on_ice
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the skater_advanced_stats_toi table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE skater_advanced_stats_toi SET
                team_id = %s,
                ev_time_on_ice = %s,
                games_played = %s,
                ot_time_on_ice = %s,
                ot_time_on_ice_per_ot_game = %s,
                pp_time_on_ice = %s,
                sh_time_on_ice = %s,
                shifts = %s,
                time_on_ice = %s
            WHERE id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a skater_advanced_stats_toi exists in the skater_advanced_stats_toi table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM skater_advanced_stats_toi WHERE id = %s AND year = %s"
    
class PlayersDatabaseMapper:
    """
    Maps Player objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(player: Player) -> tuple:
        """
        Maps a Player object to a tuple of parameters for database operations.

        Args:
            player (Player): The Player object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            player.player_id,
            player.team_id,
            player.is_active
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the players table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO players (
                id, team_id, is_active
            ) VALUES (%s, %s, %s)
        """
    
    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the players table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE players SET
                team_id = %s,
                is_active = %s
            WHERE id = %s
        """
    
    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a player exists in the players table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM players WHERE id = %s"

class PlayerAwardsApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a PlayerAwards object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the PlayerAwards object.
    """

    def __init__(self, data_parser):
        self.data_parser = data_parser
        self.field_map = {
            "playerId": "player_id",
            "trophy": "award",
            "seasonId": "year"
        }

    def map(self, source: dict) -> object:
        player_awards = PlayerAwards(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(player_awards, attr_name, value)
        return player_awards
    
class PlayerAwardsDatabaseMapper:
    """
    Maps PlayerAwards objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(player_awards: PlayerAwards) -> tuple:
        """
        Maps a PlayerAwards object to a tuple of parameters for database operations.

        Args:
            player_awards (PlayerAwards): The PlayerAwards object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            player_awards.player_id,
            player_awards.award,
            player_awards.year
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the player_awards table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO player_awards (id, award_name, year) VALUES (%s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the player_awards table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE player_awards SET award_name = %s WHERE id = %s AND year = %s AND award_name = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a player_awards exists in the player_awards table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM player_awards WHERE id = %s AND year = %s AND award_name = %s"
    
class PlayerDetailsApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a PlayerDetails object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the PlayerDetails object.
    """

    def __init__(self, data_parser):
        self.data_parser = data_parser
        self.field_map = {
            "playerId": "player_id",
            "firstName": "first_name",
            "lastName": "last_name",
            "sweaterNumber": "jersey_number",
            "position": "position",
            "headshot": "headshot",
            "heroImage": "hero_image",
            "heightInInches": "height_inches",
            "weightInPounds": "weight_pounds",
            "birthDate": "birth_date",
            "birthCity": "birth_city",
            "birthCountry": "birth_country",
            "birthStateProvince": "birth_state_province",
            "shootsCatches": "shoots_catches",
            "inTop100AllTime": "in_top_100_all_time",
            "inHHOF": "in_hhof"
        }

    def map(self, source: dict) -> object:
        player_details = PlayerDetails(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "first_name":
                value = self.data_parser.double_parse(source, "firstName", "default", "none")
            elif attr_name == "last_name":
                value = self.data_parser.double_parse(source, "lastName", "default", "none")
            elif attr_name == "birth_city":
                value = self.data_parser.double_parse(source, "birthCity", "default", "none")
            elif attr_name == "birth_state_province":
                value = self.data_parser.double_parse(source, "birthStateProvince", "default", "none")
            setattr(player_details, attr_name, value)
        return player_details
    
class PlayerDetailsDatabaseMapper:
    """
    Maps PlayerDetails objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(player_details: PlayerDetails) -> tuple:
        """
        Maps a PlayerDetails object to a tuple of parameters for database operations.

        Args:
            player_details (PlayerDetails): The PlayerDetails object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            player_details.player_id,
            player_details.first_name,
            player_details.last_name,
            player_details.jersey_number,
            player_details.position,
            player_details.headshot,
            player_details.hero_image,
            player_details.height_inches,
            player_details.weight_pounds,
            player_details.birth_date,
            player_details.birth_city,
            player_details.birth_state_province,
            player_details.birth_country,
            player_details.shoots_catches,
            player_details.in_top_100_all_time,
            player_details.in_hhof
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the player_details table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO player_details (
                id, first_name, last_name, jersey_number, position, headshot, hero_image, height_inches, 
                weight_pounds, birth_date, birth_city, birth_state_province, birth_country, shoots_catches, 
                in_top_100_all_time, in_hhof
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the player_details table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE player_details SET
                first_name = %s,
                last_name = %s,
                jersey_number = %s,
                position = %s,
                headshot = %s,
                hero_image = %s,
                height_inches = %s,
                weight_pounds = %s,
                birth_date = %s,
                birth_city = %s,
                birth_state_province = %s,
                birth_country = %s,
                shoots_catches = %s,
                in_top_100_all_time = %s,
                in_hhof = %s
            WHERE id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a player_details entry exists in the player_details table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM player_details WHERE id = %s"
    
class PlayerDraftApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a PlayerDraft object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the PlayerDraft object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "playerId": "player_id",
            "year": "year",
            "teamAbbrev": "team_id",
            "round": "round",
            "pickInRound": "pick_in_round",
            "overallPick": "overall_pick"
        }

    def map(self, source: dict) -> object:
        player_draft = PlayerDraft(self.data_parser.parse(source, "playerId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "team_id":
                value = self.util.get_team_id_from_abbrev(self.data_parser.parse(source, "teamAbbrev", "none"))
            setattr(player_draft, attr_name, value)
        return player_draft
    
class PlayerDraftDatabaseMapper:
    """
    Maps PlayerDraft objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(player_draft: PlayerDraft) -> tuple:
        """
        Maps a PlayerDraft object to a tuple of parameters for database operations.

        Args:
            player_draft (PlayerDraft): The PlayerDraft object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            player_draft.player_id,
            player_draft.year,
            player_draft.team_id,
            player_draft.round,
            player_draft.pick_in_round,
            player_draft.overall_pick
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the player_draft table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO player_draft (
                id, year, team_id, round, pick_in_round, overall_pick
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the player_draft table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE player_draft SET
                year = %s,
                team_id = %s,
                round = %s,
                pick_in_round = %s,
                overall_pick = %s
            WHERE id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a player_draft entry exists in the player_draft table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM player_draft WHERE id = %s"
    
class TeamStatsApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamStats object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamStats object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "gameTypeId": "game_type_id",
            "gamesPlayed": "games_played",
            "goalAgainst": "goals_against",
            "goalFor": "goals_for",
            "losses": "losses",
            "otLosses": "ot_losses",
            "points": "points",
            "shootoutLosses": "shootout_losses",
            "shootoutWins": "shootout_wins",
            "streakCode": "streak_code",
            "streakCount": "streak_count",
            "ties": "ties",
            "waiversSequence": "waiver_sequence",
            "regulationWins": "regulation_wins",
            "regulationPlusOtWins": "regulation_plus_ot_wins",
            "homeGamesPlayed": "home_games_played",
            "homeGoalsAgainst": "home_goals_against",
            "homeGoalsFor": "home_goals_for",
            "homeLosses": "home_losses",
            "homeOtLosses": "home_ot_losses",
            "homePoints": "home_points",
            "homeRegulationWins": "home_regulation_wins",
            "homeRegulationPlusOtWins": "home_regulation_plus_ot_wins",
            "homeTies": "home_ties",
            "homeWins": "home_wins",
            "l10GamesPlayed": "last_10_games_played",
            "l10GoalsAgainst": "last_10_goals_against",
            "l10GoalsFor": "last_10_goals_for",
            "l10Losses": "last_10_losses",
            "l10OtLosses": "last_10_ot_losses",
            "l10Points": "last_10_points",
            "l10RegulationWins": "last_10_regulation_wins",
            "l10RegulationPlusOtWins": "last_10_regulation_plus_ot_wins",
            "l10Ties": "last_10_ties",
            "l10Wins": "last_10_wins",
            "roadGamesPlayed": "road_games_played",
            "roadGoalsAgainst": "road_goals_against",
            "roadGoalsFor": "road_goals_for",
            "roadLosses": "road_losses",
            "roadOtLosses": "road_ot_losses",
            "roadPoints": "road_points",
            "roadRegulationWins": "road_regulation_wins",
            "roadRegulationPlusOtWins": "road_regulation_plus_ot_wins",
            "roadTies": "road_ties",
            "roadWins": "road_wins"
        }

    def map(self, source: dict) -> object:
        team_stats = TeamStats(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_stats, attr_name, value)
        return team_stats
    
class TeamStatsDatabaseMapper:
    """
    Maps TeamStats objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_stats: TeamStats) -> tuple:
        """
        Maps a TeamStats object to a tuple of parameters for database operations.

        Args:
            team_stats (TeamStats): The TeamStats object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_stats.team_id,
            team_stats.year,
            team_stats.game_type_id,
            team_stats.games_played,
            team_stats.goals_against,
            team_stats.goals_for,
            team_stats.losses,
            team_stats.ot_losses,
            team_stats.points,
            team_stats.shootout_losses,
            team_stats.shootout_wins,
            team_stats.streak_code,
            team_stats.streak_count,
            team_stats.ties,
            team_stats.waiver_sequence,
            team_stats.regulation_wins,
            team_stats.regulation_plus_ot_wins,
            team_stats.home_games_played,
            team_stats.home_goals_against,
            team_stats.home_goals_for,
            team_stats.home_losses,
            team_stats.home_ot_losses,
            team_stats.home_points,
            team_stats.home_regulation_wins,
            team_stats.home_regulation_plus_ot_wins,
            team_stats.home_ties,
            team_stats.home_wins,
            team_stats.last_10_games_played,
            team_stats.last_10_goals_against,
            team_stats.last_10_goals_for,
            team_stats.last_10_losses,
            team_stats.last_10_ot_losses,
            team_stats.last_10_points,
            team_stats.last_10_regulation_wins,
            team_stats.last_10_regulation_plus_ot_wins,
            team_stats.last_10_ties,
            team_stats.last_10_wins,
            team_stats.road_games_played,
            team_stats.road_goals_against,
            team_stats.road_goals_for,
            team_stats.road_losses,
            team_stats.road_ot_losses,
            team_stats.road_points,
            team_stats.road_regulation_wins,
            team_stats.road_regulation_plus_ot_wins,
            team_stats.road_ties,
            team_stats.road_wins
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_stats (
                team_id, year, game_type_id, games_played, goals_against, goals_for, losses, ot_losses, points,
                shootout_losses, shootout_wins, streak_code, streak_count, ties, waiver_sequence, regulation_wins,
                regulation_plus_ot_wins, home_games_played, home_goals_against, home_goals_for, home_losses, home_ot_losses,
                home_points, home_regulation_wins, home_regulation_plus_ot_wins, home_ties, home_wins,
                last_10_games_played, last_10_goals_against, last_10_goals_for, last_10_losses, last_10_ot_losses,
                last_10_points, last_10_regulation_wins, last_10_regulation_plus_ot_wins, last_10_ties, last_10_wins,
                road_games_played, road_goals_against, road_goals_for, road_losses, road_ot_losses, road_points,
                road_regulation_wins, road_regulation_plus_ot_wins, road_ties, road_wins
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_stats SET
                games_played = %s,
                goals_against = %s,
                goals_for = %s,
                losses = %s,
                ot_losses = %s,
                points = %s,
                shootout_losses = %s,
                shootout_wins = %s,
                streak_code = %s,
                streak_count = %s,
                ties = %s,
                waiver_sequence = %s,
                regulation_wins = %s,
                regulation_plus_ot_wins = %s,
                home_games_played = %s,
                home_goals_against = %s,
                home_goals_for = %s,
                home_losses = %s,
                home_ot_losses = %s,
                home_points = %s,
                home_regulation_wins = %s,
                home_regulation_plus_ot_wins = %s,
                home_ties = %s,
                home_wins = %s,
                last_10_games_played = %s,
                last_10_goals_against = %s,
                last_10_goals_for = %s,
                last_10_losses = %s,
                last_10_ot_losses = %s,
                last_10_points = %s,
                last_10_regulation_wins = %s,
                last_10_regulation_plus_ot_wins = %s,
                last_10_ties = %s,
                last_10_wins = %s,
                road_games_played = %s,
                road_goals_against = %s,
                road_goals_for = %s,
                road_losses = %s,
                road_ot_losses = %s,
                road_points = %s,
                road_regulation_wins = %s,
                road_regulation_plus_ot_wins = %s,
                road_ties = %s,
                road_wins = %s
                WHERE team_id = %s AND year = %s AND game_type_id = %s
                """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_stats entry exists in the team_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_stats WHERE team_id = %s AND year = %s"
    
class TeamDataApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamData object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamData object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "conferenceName": "conference_name",
            "divisionName": "division_name",
            "placeName": "place_name",
            "teamName": "team_name",
            "teamAbbrev": "team_abbreviation",
            "teamLogo": "team_logo",
            "teamColor1": "team_color_1",
            "teamColor2": "team_color_2"
        }

    def map(self, source: dict) -> object:
        team_data = TeamData(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            if attr_name == "team_name":
                value = self.data_parser.double_parse(source, "teamName", "default", "none")
            elif attr_name =="place_name":
                value = self.data_parser.double_parse(source, "placeName", "default", "none")
            elif attr_name == "team_abbreviation":
                value = self.data_parser.double_parse(source, "teamAbbrev", "default", "none")
            else:
                value = self.data_parser.parse(source, json_key, "none")
            setattr(team_data, attr_name, value)
        return team_data
    
class TeamDataDatabaseMapper:
    """
    Maps TeamData objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_data: TeamData) -> tuple:
        """
        Maps a TeamData object to a tuple of parameters for database operations.

        Args:
            team_data (TeamData): The TeamData object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_data.team_id,
            team_data.year,
            team_data.conference_name,
            team_data.division_name,
            team_data.place_name,
            team_data.team_name,
            team_data.team_abbreviation,
            team_data.team_logo,
            team_data.team_color_1,
            team_data.team_color_2
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_data table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO teams (
                team_id, year, conference_name, division_name, place_name, team_name, team_abbreviation, 
                team_logo, team_color_1, team_color_2
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_data table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE teams SET
                conference_name = %s,
                division_name = %s,
                place_name = %s,
                team_name = %s,
                team_abbreviation = %s,
                team_logo = %s,
                team_color_1 = %s,
                team_color_2 = %s
            WHERE team_id = %s and year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_data entry exists in the team_data table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM teams WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsTeamGoalGamesApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsTeamGoalGames object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsTeamGoalGames object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "lossesOneGoalGames": "losses_one_goal_games",
            "lossesTwoGoalGames": "losses_two_goal_games",
            "lossesThreeGoalGames": "losses_three_goal_games",
            "otLossesOneGoalGames": "ot_losses_one_goal_games",
            "winPctOneGoalGames": "win_percent_one_goal_games",
            "winPctTwoGoalGames": "win_percent_two_goal_games",
            "winPctThreeGoalGames": "win_percent_three_goal_games",
            "winsOneGoalGames": "wins_one_goal_games",
            "winsTwoGoalGames": "wins_two_goal_games",
            "winsThreeGoalGames": "wins_three_goal_games"
        }

    def map(self, source: dict) -> object:
        team_goal_games = TeamAdvancedStatsTeamGoalGames(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_goal_games, attr_name, value)
        return team_goal_games
    
class TeamAdvancedStatsTeamGoalGamesDatabaseMapper:
    """
    Maps TeamAdvancedStatsTeamGoalGames objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_goal_games: TeamAdvancedStatsTeamGoalGames) -> tuple:
        """
        Maps a TeamAdvancedStatsTeamGoalGames object to a tuple of parameters for database operations.

        Args:
            team_goal_games (TeamAdvancedStatsTeamGoalGames): The TeamAdvancedStatsTeamGoalGames object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_goal_games.team_id,
            team_goal_games.year,
            team_goal_games.losses_one_goal_games,
            team_goal_games.losses_two_goal_games,
            team_goal_games.losses_three_goal_games,
            team_goal_games.ot_losses_one_goal_games,
            team_goal_games.win_percent_one_goal_games,
            team_goal_games.win_percent_two_goal_games,
            team_goal_games.win_percent_three_goal_games,
            team_goal_games.wins_one_goal_games,
            team_goal_games.wins_two_goal_games,
            team_goal_games.wins_three_goal_games
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_goal_games table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_team_goal_games (
                team_id, year, losses_one_goal_games, losses_two_goal_games, losses_three_goal_games, 
                ot_losses_one_goal_games, win_percent_one_goal_games, win_percent_two_goal_games, 
                win_percent_three_goal_games, wins_one_goal_games, wins_two_goal_games, wins_three_goal_games
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_goal_games table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_team_goal_games SET
                losses_one_goal_games = %s,
                losses_two_goal_games = %s,
                losses_three_goal_games = %s,
                ot_losses_one_goal_games = %s,
                win_percent_one_goal_games = %s,
                win_percent_two_goal_games = %s,
                win_percent_three_goal_games = %s,
                wins_one_goal_games = %s,
                wins_two_goal_games = %s,
                wins_three_goal_games = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_goal_games entry exists in the team_goal_games table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_team_goal_games WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsShotTypeApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsShotType object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsShotType object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "goalsBackhand": "goals_backhand",
            "goalsDeflected": "goals_deflected",
            "goalsFor": "goals_for",
            "goalsSlap": "goals_slap",
            "goalsSnap": "goals_snap",
            "goalsTipIn": "goals_tip_in",
            "goalsWrapAround": "goals_wrap_around",
            "goalsWrist": "goals_wrist",
            "shootingPctBackhand": "shooting_percent_backhand",
            "shootingPctDeflected": "shooting_percent_deflected",
            "shootingPctSlap": "shooting_percent_slap",
            "shootingPctSnap": "shooting_percent_snap",
            "shootingPctTipIn": "shooting_percent_tip_in",
            "shootingPctWrapAround": "shooting_percent_wrap_around",
            "shootingPctWrist": "shooting_percent_wrist",
            "shotsOnNetBackhand": "shots_on_net_backhand",
            "shotsOnNetDeflected": "shots_on_net_deflected",
            "shotsOnNetSlap": "shots_on_net_slap",
            "shotsOnNetSnap": "shots_on_net_snap",
            "shotsOnNetTipIn": "shots_on_net_tip_in",
            "shotsOnNetWrapAround": "shots_on_net_wrap_around",
            "shotsOnNetWrist": "shots_on_net_wrist",
            "shotsAttemptedBackhand": "shots_attempted_backhand",
            "shotsAttemptedDeflected": "shots_attempted_deflected"
        }

    def map(self, source: dict) -> object:
        team_shot_type = TeamAdvancedStatsShotType(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_shot_type, attr_name, value)
        return team_shot_type
    
class TeamAdvancedStatsShotTypeDatabaseMapper:
    """
    Maps TeamAdvancedStatsShotType objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_shot_type: TeamAdvancedStatsShotType) -> tuple:
        """
        Maps a TeamAdvancedStatsShotType object to a tuple of parameters for database operations.

        Args:
            team_shot_type (TeamAdvancedStatsShotType): The TeamAdvancedStatsShotType object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_shot_type.team_id,
            team_shot_type.year,
            team_shot_type.goals_backhand,
            team_shot_type.goals_deflected,
            team_shot_type.goals_for,
            team_shot_type.goals_slap,
            team_shot_type.goals_snap,
            team_shot_type.goals_tip_in,
            team_shot_type.goals_wrap_around,
            team_shot_type.goals_wrist,
            team_shot_type.shooting_percent_backhand,
            team_shot_type.shooting_percent_deflected,
            team_shot_type.shooting_percent_slap,
            team_shot_type.shooting_percent_snap,
            team_shot_type.shooting_percent_tip_in,
            team_shot_type.shooting_percent_wrap_around,
            team_shot_type.shooting_percent_wrist,
            team_shot_type.shots_on_net_backhand,
            team_shot_type.shots_on_net_deflected,
            team_shot_type.shots_on_net_slap,
            team_shot_type.shots_on_net_snap,
            team_shot_type.shots_on_net_tip_in,
            team_shot_type.shots_on_net_wrap_around,
            team_shot_type.shots_on_net_wrist
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_shot_type table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_shot_type (
                team_id, year, goals_backhand, goals_deflected, goals_for, goals_slap, goals_snap, 
                goals_tip_in, goals_wrap_around, goals_wrist, shooting_percent_backhand, shooting_percent_deflected, 
                shooting_percent_slap, shooting_percent_snap, shooting_percent_tip_in, shooting_percent_wrap_around, 
                shooting_percent_wrist, shots_on_net_backhand, shots_on_net_deflected, shots_on_net_slap, 
                shots_on_net_snap, shots_on_net_tip_in, shots_on_net_wrap_around, shots_on_net_wrist
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_shot_type table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_shot_type SET
                goals_backhand = %s,
                goals_deflected = %s,
                goals_for = %s,
                goals_slap = %s,
                goals_snap = %s,
                goals_tip_in = %s,
                goals_wrap_around = %s,
                goals_wrist = %s,
                shooting_percent_backhand = %s,
                shooting_percent_deflected = %s,
                shooting_percent_slap = %s,
                shooting_percent_snap = %s,
                shooting_percent_tip_in = %s,
                shooting_percent_wrap_around = %s,
                shooting_percent_wrist = %s,
                shots_on_net_backhand = %s,
                shots_on_net_deflected = %s,
                shots_on_net_slap = %s,
                shots_on_net_snap = %s,
                shots_on_net_tip_in = %s,
                shots_on_net_wrap_around = %s,
                shots_on_net_wrist = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_shot_type entry exists in the team_shot_type table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_shot_type WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsScoringFirstApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsScoringFirst object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsScoringFirst object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "lossesScoringFirst": "losses_scoring_first",
            "lossesTrailingFirst": "losses_trailing_first",
            "otLossesScoringFirst": "ot_losses_scoring_first",
            "otLossesTrailingFirst": "ot_losses_trailing_first",
            "scoringFirstGamesPlayed": "scoring_first_games_played",
            "tiesScoringFirst": "ties_scoring_first",
            "tiesTrailingFirst": "ties_trailing_first",
            "trailingFirstGamesPlayed": "trailing_first_games_played",
            "winPctScoringFirst": "win_percent_scoring_first",
            "winPctTrailingFirst": "win_percent_trailing_first",
            "winsScoringFirst": "wins_scoring_first",
            "winsTrailingFirst": "wins_trailing_first"
        }

    def map(self, source: dict) -> object:
        team_scoring_first = TeamAdvancedStatsScoringFirst(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_scoring_first, attr_name, value)
        return team_scoring_first
    
class TeamAdvancedStatsScoringFirstDatabaseMapper:
    """
    Maps TeamAdvancedStatsScoringFirst objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_scoring_first: TeamAdvancedStatsScoringFirst) -> tuple:
        """
        Maps a TeamAdvancedStatsScoringFirst object to a tuple of parameters for database operations.

        Args:
            team_scoring_first (TeamAdvancedStatsScoringFirst): The TeamAdvancedStatsScoringFirst object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_scoring_first.team_id,
            team_scoring_first.year,
            team_scoring_first.losses_scoring_first,
            team_scoring_first.losses_trailing_first,
            team_scoring_first.ot_losses_scoring_first,
            team_scoring_first.ot_losses_trailing_first,
            team_scoring_first.scoring_first_games_played,
            team_scoring_first.ties_scoring_first,
            team_scoring_first.ties_trailing_first,
            team_scoring_first.trailing_first_games_played,
            team_scoring_first.win_percent_scoring_first,
            team_scoring_first.win_percent_trailing_first,
            team_scoring_first.wins_scoring_first,
            team_scoring_first.wins_trailing_first
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_scoring_first table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_scoring_first (
                team_id, year, losses_scoring_first, losses_trailing_first, ot_losses_scoring_first,
                ot_losses_trailing_first, scoring_first_games_played, ties_scoring_first, ties_trailing_first,
                trailing_first_games_played, win_percent_scoring_first, win_percent_trailing_first,
                wins_scoring_first, wins_trailing_first
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_scoring_first table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_scoring_first SET
                losses_scoring_first = %s,
                losses_trailing_first = %s,
                ot_losses_scoring_first = %s,
                ot_losses_trailing_first = %s,
                scoring_first_games_played = %s,
                ties_scoring_first = %s,
                ties_trailing_first = %s,
                trailing_first_games_played = %s,
                win_percent_scoring_first = %s,
                win_percent_trailing_first = %s,
                wins_scoring_first = %s,
                wins_trailing_first = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_scoring_first entry exists in the team_scoring_first table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_scoring_first WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsPowerplayPenaltyKillApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsPowerplayPenaltyKill object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsPowerplayPenaltyKill object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "penaltyKillNetPct": "pk_net_percent",
            "penaltyKillPct": "pk_percent",
            "pkNetGoals": "pk_net_goals",
            "pkNetGoalsPerGame": "pk_net_goals_for_per_game",
            "pkTimeOnIcePerGame": "pk_time_on_ice_per_game",
            "ppGoalsAgainst": "pk_goals_against",
            "ppGoalsAgainstPerGame": "pk_goals_against_per_game",
            "shGoalsFor": "pk_goals_for",
            "shGoalsForPerGame": "pk_goals_for_per_game",
            "timesShorthanded": "times_shorthanded",
            "timesShorthandedPerGame": "times_shorthanded_per_game",
            "overallPenaltyKillPct": "overall_penalty_kill_percent",
            "penaltyKillPct3v4": "penalty_kill_percent_3on4",
            "penaltyKillPct3v5": "penalty_kill_percent_3on5",
            "penaltyKillPct4v5": "penalty_kill_percent_4on5",
            "timeOnIce3v4": "time_on_ice_3on4",
            "timeOnIce3v5": "time_on_ice_3on5",
            "timeOnIce4v5": "time_on_ice_4on5",
            "timeOnIceShorthanded": "time_on_ice_shorthanded",
            "timesShorthanded3v4": "time_shorthanded_3v4",
            "timesShorthanded3v5": "time_shorthanded_3v5",
            "timesShorthanded4v5": "time_shorthanded_4v5",
            "powerPlayGoalsFor": "pp_goals_for",
            "powerPlayNetPct": "pp_net_percent",
            "powerPlayPct": "pp_percent",
            "ppGoalsPerGame": "pp_goals_per_game",
            "ppNetGoals": "pp_net_goals",
            "ppNetGoalsPerGame": "pp_net_goals_for_per_game",
            "ppOpportunities": "pp_opportunites",
            "ppOpportunitiesPerGame": "pp_opportunities_per_game",
            "ppTimeOnIcePerGame": "pp_time_on_ice_per_game",
            "shGoalsAgainst": "pp_goals_against",
            "shGoalsAgainstPerGame": "pp_goals_against_per_game",
            "opportunities4v3": "opportunities_4on3",
            "opportunities5v3": "opportunities_5on3",
            "opportunities5v4": "opportunities_5on4",
            "powerPlayPct4v3": "pp_percent_4on3",
            "powerPlayPct5v3": "pp_percent_5on3",
            "powerPlayPct5v4": "pp_percent_5on4",
            "timeOnIce4v3": "time_on_ice_4on3",
            "timeOnIce5v3": "time_on_ice_5on3",
            "timeOnIce5v4": "time_on_ice_5on4",
            "timeOnIcePp": "pp_time_on_ice",
            "goalsAgainst3v4": "goals_against_3on4",
            "goalsAgainst3v5": "goals_against_3on5",
            "goalsAgainst4v5": "goals_against_4on5"
        }

    def map(self, source: dict) -> object:
        team_pp_pk_stats = TeamAdvancedStatsPowerplayPenaltyKill(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_pp_pk_stats, attr_name, value)
        return team_pp_pk_stats
    
class TeamAdvancedStatsPowerplayPenaltyKillDatabaseMapper:
    """
    Maps TeamAdvancedStatsPowerplayPenaltyKill objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_pp_pk_stats: TeamAdvancedStatsPowerplayPenaltyKill) -> tuple:
        """
        Maps a TeamAdvancedStatsPowerplayPenaltyKill object to a tuple of parameters for database operations.

        Args:
            team_pp_pk_stats (TeamAdvancedStatsPowerplayPenaltyKill): The TeamAdvancedStatsPowerplayPenaltyKill object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_pp_pk_stats.team_id,
            team_pp_pk_stats.year,
            team_pp_pk_stats.pk_net_percent,
            team_pp_pk_stats.pk_percent,
            team_pp_pk_stats.pk_net_goals,
            team_pp_pk_stats.pk_net_goals_for_per_game,
            team_pp_pk_stats.pk_time_on_ice_per_game,
            team_pp_pk_stats.pk_goals_against,
            team_pp_pk_stats.pk_goals_against_per_game,
            team_pp_pk_stats.pk_goals_for,
            team_pp_pk_stats.pk_goals_for_per_game,
            team_pp_pk_stats.times_shorthanded,
            team_pp_pk_stats.times_shorthanded_per_game,
            team_pp_pk_stats.overall_penalty_kill_percent,
            team_pp_pk_stats.penalty_kill_percent_3on4,
            team_pp_pk_stats.penalty_kill_percent_3on5,
            team_pp_pk_stats.penalty_kill_percent_4on5,
            team_pp_pk_stats.time_on_ice_3on4,
            team_pp_pk_stats.time_on_ice_3on5,
            team_pp_pk_stats.time_on_ice_4on5,
            team_pp_pk_stats.time_on_ice_shorthanded,
            team_pp_pk_stats.time_shorthanded_3v4,
            team_pp_pk_stats.time_shorthanded_3v5,
            team_pp_pk_stats.time_shorthanded_4v5,
            team_pp_pk_stats.pp_goals_for,
            team_pp_pk_stats.pp_net_percent,
            team_pp_pk_stats.pp_percent,
            team_pp_pk_stats.pp_goals_per_game,
            team_pp_pk_stats.pp_net_goals,
            team_pp_pk_stats.pp_net_goals_for_per_game,
            team_pp_pk_stats.pp_opportunites,
            team_pp_pk_stats.pp_opportunities_per_game,
            team_pp_pk_stats.pp_time_on_ice_per_game,
            team_pp_pk_stats.pp_goals_against,
            team_pp_pk_stats.pp_goals_against_per_game,
            team_pp_pk_stats.opportunities_4on3,
            team_pp_pk_stats.opportunities_5on3,
            team_pp_pk_stats.opportunities_5on4,
            team_pp_pk_stats.pp_percent_4on3,
            team_pp_pk_stats.pp_percent_5on3,
            team_pp_pk_stats.pp_percent_5on4,
            team_pp_pk_stats.time_on_ice_4on3,
            team_pp_pk_stats.time_on_ice_5on3,
            team_pp_pk_stats.time_on_ice_5on4,
            team_pp_pk_stats.pp_time_on_ice,
            team_pp_pk_stats.goals_against_3on4,
            team_pp_pk_stats.goals_against_3on5,
            team_pp_pk_stats.goals_against_4on5,
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_pp_pk_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_powerplay_penalty_kill(
                team_id, year, pk_net_percent, pk_percent, pk_net_goals_for, pk_net_goals_for_per_game,
                pk_time_on_ice_per_game, pk_goals_against, pk_goals_against_per_game, pk_goals_for,
                pk_goals_for_per_game, times_shorthanded, times_shorthanded_per_game, overall_penalty_kill_percent,
                penalty_kill_percent_3on4, penalty_kill_percent_3on5, penalty_kill_percent_4on5, time_on_ice_3on4,
                time_on_ice_3on5, time_on_ice_4on5, time_on_ice_shorthanded, time_shorthanded_3v4,
                time_shorthanded_3v5, time_shorthanded_4v5, pp_goals_for, pp_net_percent, pp_percent, pp_goals_per_game,
                pp_net_goals_for, pp_net_goals_for_per_game, pp_opportunities, pp_opportunities_per_game,
                pp_time_on_ice_per_game, pp_goals_against,pp_goals_against_per_game, opportunities_4on3,
                opportunities_5on3, opportunities_5on4, pp_percent_4on3, pp_percent_5on3, pp_percent_5on4,
                time_on_ice_4on3, time_on_ice_5on3, time_on_ice_5on4, pp_time_on_ice, goals_against_3on4,
                goals_against_3on5, goals_against_4on5
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    
    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_pp_pk_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_powerplay_penalty_kill SET
                pk_net_percent = %s,
                pk_percent = %s,
                pk_net_goals_for = %s,
                pk_net_goals_for_per_game = %s,
                pk_time_on_ice_per_game = %s,
                pk_goals_against = %s,
                pk_goals_against_per_game = %s,
                pk_goals_for = %s,
                pk_goals_for_per_game = %s,
                times_shorthanded = %s,
                times_shorthanded_per_game = %s,
                overall_penalty_kill_percent = %s,
                penalty_kill_percent_3on4 = %s,
                penalty_kill_percent_3on5 = %s,
                penalty_kill_percent_4on5 = %s,
                time_on_ice_3on4 = %s,
                time_on_ice_3on5 = %s,
                time_on_ice_4on5 = %s,
                time_on_ice_shorthanded = %s,
                time_shorthanded_3v4 = %s,
                time_shorthanded_3v5 = %s,
                time_shorthanded_4v5 = %s,
                pp_goals_for = %s,
                pp_net_percent = %s,
                pp_percent = %s,
                pp_goals_per_game = %s,
                pp_net_goals_for = %s,
                pp_net_goals_for_per_game = %s,
                pp_opportunities = %s,
                pp_opportunities_per_game = %s,
                pp_time_on_ice_per_game = %s,
                pp_goals_against = %s,
                pp_goals_against_per_game = %s,
                opportunities_4on3 = %s,
                opportunities_5on3 = %s,
                opportunities_5on4 = %s,
                pp_percent_4on3 = %s,
                pp_percent_5on3 = %s,
                pp_percent_5on4 = %s,
                time_on_ice_4on3 = %s,
                time_on_ice_5on3 = %s,
                time_on_ice_5on4 = %s,
                pp_time_on_ice = %s,
                goals_against_3on4 = %s,
                goals_against_3on5 = %s,
                goals_against_4on5 = %s
            WHERE team_id = %s AND year = %s
            """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_pp_pk_stats entry exists in the team_pp_pk_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_powerplay_penalty_kill WHERE team_id = %s AND year = %s"
        
class TeamAdvancedStatsPenaltiesApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsPenalties object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsPenalties object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "benchMinorPenalties": "bench_minor_penalties",
            "gameMisconducts": "game_misconducts",
            "majors": "majors",
            "matchPenalties": "match_penalties",
            "minors": "minors",
            "misconducts": "misconducts",
            "netPenalties": "net_penalties",
            "penalties": "penalties",
            "penaltyMinutes": "penalty_minutes",
            "penaltySecondsPerGame": "penalty_seconds_per_game",
            "totalPenaltiesDrawn": "total_penalties_drawn"
        }

    def map(self, source: dict) -> object:
        team_penalties_stats = TeamAdvancedStatsPenalties(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_penalties_stats, attr_name, value)
        return team_penalties_stats
    
class TeamAdvancedStatsPenaltiesDatabaseMapper:
    """
    Maps TeamAdvancedStatsPenalties objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_penalties_stats: TeamAdvancedStatsPenalties) -> tuple:
        """
        Maps a TeamAdvancedStatsPenalties object to a tuple of parameters for database operations.

        Args:
            team_penalties_stats (TeamAdvancedStatsPenalties): The TeamAdvancedStatsPenalties object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_penalties_stats.team_id,
            team_penalties_stats.year,
            team_penalties_stats.bench_minor_penalties,
            team_penalties_stats.game_misconducts,
            team_penalties_stats.majors,
            team_penalties_stats.match_penalties,
            team_penalties_stats.minors,
            team_penalties_stats.misconducts,
            team_penalties_stats.net_penalties,
            team_penalties_stats.penalties,
            team_penalties_stats.penalty_minutes,
            team_penalties_stats.penalty_seconds_per_game,
            team_penalties_stats.total_penalties_drawn
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_penalties_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_penalties (
                team_id, year, bench_minor_penalties, game_misconducts, majors, match_penalties, minors,
                misconducts, net_penalties, penalties, penalty_minutes, penalty_seconds_per_game, total_penalties_drawn
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_penalties_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_penalties SET
                bench_minor_penalties = %s,
                game_misconducts = %s,
                majors = %s,
                match_penalties = %s,
                minors = %s,
                misconducts = %s,
                net_penalties = %s,
                penalties = %s,
                penalty_minutes = %s,
                penalty_seconds_per_game = %s,
                total_penalties_drawn = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_penalties_stats entry exists in the team_penalties_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_penalties WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsOutshootOutshotApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsOutshootOutshot object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsOutshootOutshot object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "lossesEvenShots": "losses_even_shots",
            "lossesOutshootOpponent": "losses_outshoot",
            "lossesOutshotByOpponent": "losses_outshot",
            "netShotsPerGame": "net_shots_per_game",
            "otLossesEvenShots": "ot_losses_even_shots",
            "otLossesOutshootOpponent": "ot_losses_outshoot",
            "otLossesOutshotByOpponent": "ot_losses_outshot",
            "shotsAgainstPerGame": "shots_against_per_game",
            "shotsForPerGame": "shots_for_per_game",
            "tiesEvenShots": "ties_even_shots",
            "tiesOutshootOpponent": "ties_outshoot",
            "tiesOutshotByOpponent": "ties_outshot",
            "winsEvenShots": "wins_even_shots",
            "winsOutshootOpponent": "wins_outshoot",
            "winsOutshotByOpponent": "wins_outshot"
        }

    def map(self, source: dict) -> object:
        team_outshoot_outshot_stats = TeamAdvancedStatsOutshootOutshot(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_outshoot_outshot_stats, attr_name, value)
        return team_outshoot_outshot_stats
    
class TeamAdvancedStatsOutshootOutshotDatabaseMapper:
    """
    Maps TeamAdvancedStatsOutshootOutshot objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_outshoot_outshot_stats: TeamAdvancedStatsOutshootOutshot) -> tuple:
        """
        Maps a TeamAdvancedStatsOutshootOutshot object to a tuple of parameters for database operations.

        Args:
            team_outshoot_outshot_stats (TeamAdvancedStatsOutshootOutshot): The TeamAdvancedStatsOutshootOutshot object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_outshoot_outshot_stats.team_id,
            team_outshoot_outshot_stats.year,
            team_outshoot_outshot_stats.losses_even_shots,
            team_outshoot_outshot_stats.losses_outshoot,
            team_outshoot_outshot_stats.losses_outshot,
            team_outshoot_outshot_stats.net_shots_per_game,
            team_outshoot_outshot_stats.ot_losses_even_shots,
            team_outshoot_outshot_stats.ot_losses_outshoot,
            team_outshoot_outshot_stats.ot_losses_outshot,
            team_outshoot_outshot_stats.shots_against_per_game,
            team_outshoot_outshot_stats.shots_for_per_game,
            team_outshoot_outshot_stats.ties_even_shots,
            team_outshoot_outshot_stats.ties_outshoot,
            team_outshoot_outshot_stats.ties_outshot,
            team_outshoot_outshot_stats.wins_even_shots,
            team_outshoot_outshot_stats.wins_outshoot,
            team_outshoot_outshot_stats.wins_outshot
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_outshoot_outshot_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_outshoot_outshot (
                team_id, year, losses_even_shots, losses_outshoot, losses_outshot, net_shots_per_game, ot_losses_even_shots, 
                ot_losses_outshoot, ot_losses_outshot, shots_against_per_game, shots_for_per_game, ties_even_shots, 
                ties_outshoot, ties_outshot, wins_even_shots, wins_outshoot, wins_outshot
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_outshoot_outshot_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_outshoot_outshot SET
                losses_even_shots = %s,
                losses_outshoot = %s,
                losses_outshot = %s,
                net_shots_per_game = %s,
                ot_losses_even_shots = %s,
                ot_losses_outshoot = %s,
                ot_losses_outshot = %s,
                shots_against_per_game = %s,
                shots_for_per_game = %s,
                ties_even_shots = %s,
                ties_outshoot = %s,
                ties_outshot = %s,
                wins_even_shots = %s,
                wins_outshoot = %s,
                wins_outshot = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_outshoot_outshot_stats entry exists in the team_outshoot_outshot_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_outshoot_outshot WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsMiscApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsMisc object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsMisc object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "blockedShots": "blocked_shots",
            "emptyNetGoals": "empty_net_goals",
            "giveaways": "giveaways",
            "hits": "hits",
            "missedShots": "missed_shots",
            "takeaways": "takeaways",
            "timeOnIcePerGame5v5": "time_on_ice_per_game_5on5"
        }

    def map(self, source: dict) -> object:
        team_misc_stats = TeamAdvancedStatsMisc(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_misc_stats, attr_name, value)
        return team_misc_stats
    
class TeamAdvancedStatsMiscDatabaseMapper:
    """
    Maps TeamAdvancedStatsMisc objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_misc_stats: TeamAdvancedStatsMisc) -> tuple:
        """
        Maps a TeamAdvancedStatsMisc object to a tuple of parameters for database operations.

        Args:
            team_misc_stats (TeamAdvancedStatsMisc): The TeamAdvancedStatsMisc object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_misc_stats.team_id,
            team_misc_stats.year,
            team_misc_stats.blocked_shots,
            team_misc_stats.empty_net_goals,
            team_misc_stats.giveaways,
            team_misc_stats.hits,
            team_misc_stats.missed_shots,
            team_misc_stats.takeaways,
            team_misc_stats.time_on_ice_per_game_5on5
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_misc_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_misc (
                team_id, year, blocked_shots, empty_net_goals, giveaways, hits, missed_shots, takeaways, time_on_ice_per_game_5v5
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_misc_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_misc SET
                blocked_shots = %s,
                empty_net_goals = %s,
                giveaways = %s,
                hits = %s,
                missed_shots = %s,
                takeaways = %s,
                time_on_ice_per_game_5v5 = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_misc_stats entry exists in the team_misc_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_misc WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsLeadingTrailingApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsLeadingTrailing object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsLeadingTrailing object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "lossLeadPeriod1": "loss_lead_period_1",
            "lossLeadPeriod2": "loss_lead_period_2",
            "lossTrailPeriod1": "loss_trail_period_1",
            "lossTrailPeriod2": "loss_trail_period_2",
            "otLossLeadPeriod1": "ot_loss_lead_period_1",
            "otLossLeadPeriod2": "ot_loss_lead_period_2",
            "otLossTrailPeriod1": "ot_loss_trail_period_1",
            "otLossTrailPeriod2": "ot_loss_trail_period_2",
            "period1GoalsAgainst": "period_1_goals_against",
            "period1GoalsFor": "period_1_goals_for",
            "period2GoalsAgainst": "period_2_goals_against",
            "period2GoalsFor": "period_2_goals_for",
            "tiesLeadPeriod1": "ties_lead_period_1",
            "tiesLeadPeriod2": "ties_lead_period_2",
            "tiesTrailPeriod1": "ties_trail_period_1",
            "tiesTrailPeriod2": "ties_trail_period_2",
            "winPctLeadPeriod1": "win_percent_lead_period_1",
            "winPctLeadPeriod2": "win_percent_lead_period_2",
            "winPctTrailPeriod1": "win_percent_trail_period_1",
            "winPctTrailPeriod2": "win_percent_trail_period_2",
            "winsLeadPeriod1": "wins_lead_period_1",
            "winsLeadPeriod2": "wins_lead_period_2",
            "winsTrailPeriod1": "wins_trail_period_1",
            "winsTrailPeriod2": "wins_trail_period_2"
        }

    def map(self, source: dict) -> object:
        team_leading_trailing_stats = TeamAdvancedStatsLeadingTrailing(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_leading_trailing_stats, attr_name, value)
        return team_leading_trailing_stats
    
class TeamAdvancedStatsLeadingTrailingDatabaseMapper:
    """
    Maps TeamAdvancedStatsLeadingTrailing objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_leading_trailing_stats: TeamAdvancedStatsLeadingTrailing) -> tuple:
        """
        Maps a TeamAdvancedStatsLeadingTrailing object to a tuple of parameters for database operations.

        Args:
            team_leading_trailing_stats (TeamAdvancedStatsLeadingTrailing): The TeamAdvancedStatsLeadingTrailing object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_leading_trailing_stats.team_id,
            team_leading_trailing_stats.year,
            team_leading_trailing_stats.loss_lead_period_1,
            team_leading_trailing_stats.loss_lead_period_2,
            team_leading_trailing_stats.loss_trail_period_1,
            team_leading_trailing_stats.loss_trail_period_2,
            team_leading_trailing_stats.ot_loss_lead_period_1,
            team_leading_trailing_stats.ot_loss_lead_period_2,
            team_leading_trailing_stats.ot_loss_trail_period_1,
            team_leading_trailing_stats.ot_loss_trail_period_2,
            team_leading_trailing_stats.period_1_goals_against,
            team_leading_trailing_stats.period_1_goals_for,
            team_leading_trailing_stats.period_2_goals_against,
            team_leading_trailing_stats.period_2_goals_for,
            team_leading_trailing_stats.ties_lead_period_1,
            team_leading_trailing_stats.ties_lead_period_2,
            team_leading_trailing_stats.ties_trail_period_1,
            team_leading_trailing_stats.ties_trail_period_2,
            team_leading_trailing_stats.win_percent_lead_period_1,
            team_leading_trailing_stats.win_percent_lead_period_2,
            team_leading_trailing_stats.win_percent_trail_period_1,
            team_leading_trailing_stats.win_percent_trail_period_2,
            team_leading_trailing_stats.wins_lead_period_1,
            team_leading_trailing_stats.wins_lead_period_2,
            team_leading_trailing_stats.wins_trail_period_1,
            team_leading_trailing_stats.wins_trail_period_2
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_leading_trailing_stats table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_leading_trailing (
                team_id, year, loss_lead_period_1, loss_lead_period_2, loss_trail_period_1, loss_trail_period_2,
                ot_loss_lead_period_1, ot_loss_lead_period_2, ot_loss_trail_period_1, ot_loss_trail_period_2,
                period_1_goals_against, period_1_goals_for, period_2_goals_against, period_2_goals_for,
                ties_lead_period_1, ties_lead_period_2, ties_trail_period_1, ties_trail_period_2,
                win_percent_lead_period_1, win_percent_lead_period_2, win_percent_trail_period_1,
                win_percent_trail_period_2, wins_lead_period_1, wins_lead_period_2, wins_trail_period_1,
                wins_trail_period_2
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_leading_trailing_stats table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_leading_trailing SET
                loss_lead_period_1 = %s,
                loss_lead_period_2 = %s,
                loss_trail_period_1 = %s,
                loss_trail_period_2 = %s,
                ot_loss_lead_period_1 = %s,
                ot_loss_lead_period_2 = %s,
                ot_loss_trail_period_1 = %s,
                ot_loss_trail_period_2 = %s,
                period_1_goals_against = %s,
                period_1_goals_for = %s,
                period_2_goals_against = %s,
                period_2_goals_for = %s,
                ties_lead_period_1 = %s,
                ties_lead_period_2 = %s,
                ties_trail_period_1 = %s,
                ties_trail_period_2 = %s,
                win_percent_lead_period_1 = %s,
                win_percent_lead_period_2 = %s,
                win_percent_trail_period_1 = %s,
                win_percent_trail_period_2 = %s,
                wins_lead_period_1 = %s,
                wins_lead_period_2 = %s,
                wins_trail_period_1 = %s,
                wins_trail_period_2 = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_leading_trailing_stats entry exists in the team_leading_trailing_stats table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_leading_trailing WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsGoalsByStrengthApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsGoalsByStrength object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsGoalsByStrength object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "goalsFor3On3": "goals_for_3on3",
            "goalsFor3On4": "goals_for_3on4",
            "goalsFor3On5": "goals_for_3on5",
            "goalsFor3On6": "goals_for_3on6",
            "goalsFor4On3": "goals_for_4on3",
            "goalsFor4On4": "goals_for_4on4",
            "goalsFor4On5": "goals_for_4on5",
            "goalsFor4On6": "goals_for_4on6",
            "goalsFor5On3": "goals_for_5on3",
            "goalsFor5On4": "goals_for_5on4",
            "goalsFor5On5": "goals_for_5on5",
            "goalsFor5On6": "goals_for_5on6",
            "goalsFor6On3": "goals_for_6on3",
            "goalsFor6On4": "goals_for_6on4",
            "goalsFor6On5": "goals_for_6on5",
            "goalsForPenaltyShots": "goals_for_penalty_shots"
        }

    def map(self, source: dict) -> object:
        team_goals_by_strength = TeamAdvancedStatsGoalsByStrength(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_goals_by_strength, attr_name, value)
        return team_goals_by_strength
    
class TeamAdvancedStatsGoalsByStrengthDatabaseMapper:
    """
    Maps TeamAdvancedStatsGoalsByStrength objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_goals_by_strength: TeamAdvancedStatsGoalsByStrength) -> tuple:
        """
        Maps a TeamAdvancedStatsGoalsByStrength object to a tuple of parameters for database operations.

        Args:
            team_goals_by_strength (TeamAdvancedStatsGoalsByStrength): The TeamAdvancedStatsGoalsByStrength object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_goals_by_strength.team_id,
            team_goals_by_strength.year,
            team_goals_by_strength.goals_for_3on3,
            team_goals_by_strength.goals_for_3on4,
            team_goals_by_strength.goals_for_3on5,
            team_goals_by_strength.goals_for_3on6,
            team_goals_by_strength.goals_for_4on3,
            team_goals_by_strength.goals_for_4on4,
            team_goals_by_strength.goals_for_4on5,
            team_goals_by_strength.goals_for_4on6,
            team_goals_by_strength.goals_for_5on3,
            team_goals_by_strength.goals_for_5on4,
            team_goals_by_strength.goals_for_5on5,
            team_goals_by_strength.goals_for_5on6,
            team_goals_by_strength.goals_for_6on3,
            team_goals_by_strength.goals_for_6on4,
            team_goals_by_strength.goals_for_6on5,
            team_goals_by_strength.goals_for_penalty_shots
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_goals_by_strength table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_goals_by_strength (
                team_id, year, goals_for_3on3, goals_for_3on4, goals_for_3on5, goals_for_3on6, goals_for_4on3,
                goals_for_4on4, goals_for_4on5, goals_for_4on6, goals_for_5on3, goals_for_5on4, goals_for_5on5,
                goals_for_5on6, goals_for_6on3, goals_for_6on4, goals_for_6on5, goals_for_penalty_shots
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_goals_by_strength table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_goals_by_strength SET
                goals_for_3on3 = %s,
                goals_for_3on4 = %s,
                goals_for_3on5 = %s,
                goals_for_3on6 = %s,
                goals_for_4on3 = %s,
                goals_for_4on4 = %s,
                goals_for_4on5 = %s,
                goals_for_4on6 = %s,
                goals_for_5on3 = %s,
                goals_for_5on4 = %s,
                goals_for_5on5 = %s,
                goals_for_5on6 = %s,
                goals_for_6on3 = %s,
                goals_for_6on4 = %s,
                goals_for_6on5 = %s,
                goals_for_penalty_shots = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_goals_by_strength entry exists in the team_goals_by_strength table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_goals_by_strength WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsGoalsByPeriodApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsGoalsByPeriod object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsGoalsByPeriod object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "evGoalsFor": "ev_goals_for",
            "period1GoalsAgainst": "period_1_goals_against",
            "period1GoalsFor": "period_1_goals_for",
            "period2GoalsAgainst": "period_2_goals_against",
            "period2GoalsFor": "period_2_goals_for",
            "period3GoalsAgainst": "period_3_goals_against",
            "period3GoalsFor": "period_3_goals_for",
            "periodOtGoalsAgainst": "period_ot_goals_against",
            "periodOtGoalsFor": "period_ot_goals_for",
            "ppGoalsFor": "pp_goals_for",
            "shGoalsFor": "pk_goals_for"
        }

    def map(self, source: dict) -> object:
        team_goals_by_period = TeamAdvancedStatsGoalsByPeriod(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_goals_by_period, attr_name, value)
        return team_goals_by_period
    
class TeamAdvancedStatsGoalsByPeriodDatabaseMapper:
    """
    Maps TeamAdvancedStatsGoalsByPeriod objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_goals_by_period: TeamAdvancedStatsGoalsByPeriod) -> tuple:
        """
        Maps a TeamAdvancedStatsGoalsByPeriod object to a tuple of parameters for database operations.

        Args:
            team_goals_by_period (TeamAdvancedStatsGoalsByPeriod): The TeamAdvancedStatsGoalsByPeriod object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_goals_by_period.team_id,
            team_goals_by_period.year,
            team_goals_by_period.ev_goals_for,
            team_goals_by_period.period_1_goals_against,
            team_goals_by_period.period_1_goals_for,
            team_goals_by_period.period_2_goals_against,
            team_goals_by_period.period_2_goals_for,
            team_goals_by_period.period_3_goals_against,
            team_goals_by_period.period_3_goals_for,
            team_goals_by_period.period_ot_goals_against,
            team_goals_by_period.period_ot_goals_for,
            team_goals_by_period.pp_goals_for,
            team_goals_by_period.pk_goals_for
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_goals_by_period table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_goals_by_period (
                team_id, year, ev_goals_for, period_1_goals_against, period_1_goals_for, 
                period_2_goals_against, period_2_goals_for, period_3_goals_against, 
                period_3_goals_for, period_ot_goals_against, period_ot_goals_for, 
                pp_goals_for, pk_goals_for
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_goals_by_period table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_goals_by_period SET
                ev_goals_for = %s,
                period_1_goals_against = %s,
                period_1_goals_for = %s,
                period_2_goals_against = %s,
                period_2_goals_for = %s,
                period_3_goals_against = %s,
                period_3_goals_for = %s,
                period_ot_goals_against = %s,
                period_ot_goals_for = %s,
                pp_goals_for = %s,
                pk_goals_for = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_goals_by_period entry exists in the team_goals_by_period table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_goals_by_period WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsFaceoffPercentApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsFaceoffPercent object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsFaceoffPercent object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "defensiveZoneFaceoffPct": "defensive_zone_faceoff_percent",
            "defensiveZoneFaceoffs": "defensive_zone_faceoffs",
            "evFaceoffPct": "ev_faceoff_percent",
            "evFaceoffs": "ev_faceoffs",
            "faceoffWinPct": "faceoff_win_percent",
            "neutralZoneFaceoffPct": "neutral_zone_faceoff_percent",
            "neutralZoneFaceoffs": "neutral_zone_faceoffs",
            "offensiveZoneFaceoffPct": "offensive_zone_faceoff_percent",
            "offensiveZoneFaceoffs": "offensive_zone_faceoffs",
            "ppFaceoffPct": "pp_faceoff_percent",
            "ppFaceoffs": "pp_faceoffs",
            "shFaceoffPct": "pk_faceoff_percent",
            "shFaceoffs": "pk_faceoffs",
            "totalFaceoffs": "total_faceoffs"
        }

    def map(self, source: dict) -> object:
        team_faceoff_percent = TeamAdvancedStatsFaceoffPercent(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_faceoff_percent, attr_name, value)
        return team_faceoff_percent
    
class TeamAdvancedStatsFaceoffPercentDatabaseMapper:
    """
    Maps TeamAdvancedStatsFaceoffPercent objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_faceoff_percent: TeamAdvancedStatsFaceoffPercent) -> tuple:
        """
        Maps a TeamAdvancedStatsFaceoffPercent object to a tuple of parameters for database operations.

        Args:
            team_faceoff_percent (TeamAdvancedStatsFaceoffPercent): The TeamAdvancedStatsFaceoffPercent object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_faceoff_percent.team_id,
            team_faceoff_percent.year,
            team_faceoff_percent.defensive_zone_faceoff_percent,
            team_faceoff_percent.defensive_zone_faceoffs,
            team_faceoff_percent.ev_faceoff_percent,
            team_faceoff_percent.ev_faceoffs,
            team_faceoff_percent.faceoff_win_percent,
            team_faceoff_percent.neutral_zone_faceoff_percent,
            team_faceoff_percent.neutral_zone_faceoffs,
            team_faceoff_percent.offensive_zone_faceoff_percent,
            team_faceoff_percent.offensive_zone_faceoffs,
            team_faceoff_percent.pp_faceoff_percent,
            team_faceoff_percent.pp_faceoffs,
            team_faceoff_percent.pk_faceoff_percent,
            team_faceoff_percent.pk_faceoffs,
            team_faceoff_percent.total_faceoffs
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_faceoff_percent table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_faceoff_percent (
                team_id, year, defensive_zone_faceoff_percent, defensive_zone_faceoffs, ev_faceoff_percent,
                ev_faceoffs, faceoff_win_percent, neutral_zone_faceoff_percent, neutral_zone_faceoffs,
                offensive_zone_faceoff_percent, offensive_zone_faceoffs, pp_faceoff_percent, pp_faceoffs,
                pk_faceoff_percent, pk_faceoffs, total_faceoffs
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_faceoff_percent table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_faceoff_percent SET
                defensive_zone_faceoff_percent = %s,
                defensive_zone_faceoffs = %s,
                ev_faceoff_percent = %s,
                ev_faceoffs = %s,
                faceoff_win_percent = %s,
                neutral_zone_faceoff_percent = %s,
                neutral_zone_faceoffs = %s,
                offensive_zone_faceoff_percent = %s,
                offensive_zone_faceoffs = %s,
                pp_faceoff_percent = %s,
                pp_faceoffs = %s,
                pk_faceoff_percent = %s,
                pk_faceoffs = %s,
                total_faceoffs = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_faceoff_percent entry exists in the team_faceoff_percent table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_faceoff_percent WHERE team_id = %s AND year = %s"
    
class TeamAdvancedStatsDaysRestApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsDaysRest object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsDaysRest object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "daysRest": "days_rest",
            "gamesPlayed": "games_played",
            "faceoffWinPct": "faceoff_percent",
            "goalsAgainstPerGame": "goals_against_per_game",
            "goalsForPerGame": "goals_for_per_game",
            "losses": "losses",
            "netGoalsPerGame": "net_goals_per_game",
            "otLosses": "ot_losses",
            "penaltyKillPct": "penalty_kill_percent",
            "pointPct": "point_percent",
            "points": "points",
            "powerPlayPct": "power_play_percent",
            "ppOpportunitiesPerGame": "power_play_opportunities_per_game",
            "shotDifferentialPerGame": "shot_differential_per_game",
            "shotsAgainstPerGame": "shots_against_per_game",
            "shotsForPerGame": "shots_for_per_game",
            "ties": "ties",
            "timesShorthandedPerGame": "times_shorthanded_per_game",
            "wins": "wins"
        }

    def map(self, source: dict) -> object:
        team_days_rest = TeamAdvancedStatsDaysRest(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_days_rest, attr_name, value)
        return team_days_rest
    
class TeamAdvancedStatsDaysRestDatabaseMapper:
    """
    Maps TeamAdvancedStatsDaysRest objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_days_rest: TeamAdvancedStatsDaysRest) -> tuple:
        """
        Maps a TeamAdvancedStatsDaysRest object to a tuple of parameters for database operations.

        Args:
            team_days_rest (TeamAdvancedStatsDaysRest): The TeamAdvancedStatsDaysRest object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_days_rest.team_id,
            team_days_rest.year,
            team_days_rest.days_rest,
            team_days_rest.games_played,
            team_days_rest.faceoff_percent,
            team_days_rest.goals_against_per_game,
            team_days_rest.goals_for_per_game,
            team_days_rest.losses,
            team_days_rest.net_goals_per_game,
            team_days_rest.ot_losses,
            team_days_rest.penalty_kill_percent,
            team_days_rest.point_percent,
            team_days_rest.points,
            team_days_rest.power_play_percent,
            team_days_rest.power_play_opportunities_per_game,
            team_days_rest.shot_differential_per_game,
            team_days_rest.shots_against_per_game,
            team_days_rest.shots_for_per_game,
            team_days_rest.ties,
            team_days_rest.times_shorthanded_per_game,
            team_days_rest.wins
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_days_rest table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_days_rest (
                team_id, year, days_rest, games_played, faceoff_percent, goals_against_per_game, goals_for_per_game, 
                losses, net_goals_per_game, ot_losses, penalty_kill_percent, point_percent, points, power_play_percent, 
                power_play_opportunities_per_game, shot_differential_per_game, shots_against_per_game, shots_for_per_game, 
                ties, times_shorthanded_per_game, wins
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_days_rest table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_days_rest SET
                games_played = %s,
                faceoff_percent = %s,
                goals_against_per_game = %s,
                goals_for_per_game = %s,
                losses = %s,
                net_goals_per_game = %s,
                ot_losses = %s,
                penalty_kill_percent = %s,
                point_percent = %s,
                points = %s,
                power_play_percent = %s,
                power_play_opportunities_per_game = %s,
                shot_differential_per_game = %s,
                shots_against_per_game = %s,
                shots_for_per_game = %s,
                ties = %s,
                times_shorthanded_per_game = %s,
                wins = %s
            WHERE team_id = %s AND year = %s AND days_rest = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_days_rest entry exists in the team_days_rest table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_days_rest WHERE team_id = %s AND year = %s AND days_rest = %s"
    
class TeamAdvancedStatsCorsiFenwickApiMapper(ApiMapper):
    """
    Maps data between a dictionary and a TeamAdvancedStatsCorsiFenwick object.

    Attributes:
        field_map (dict): A mapping of JSON keys to attribute names in the TeamAdvancedStatsCorsiFenwick object.
    """

    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "teamId": "team_id",
            "seasonId": "year",
            "gamesPlayed": "games_played",
            "satAgainst": "corsi_against",
            "satAhead": "corsi_ahead",
            "satBehind": "corsi_behind",
            "satClose": "corsi_close",
            "satFor": "corsi_for",
            "satTied": "corsi_tied",
            "satTotal": "corsi_total",
            "usatAgainst": "fenwick_against",
            "usatAhead": "fenwick_ahead",
            "usatBehind": "fenwick_behind",
            "usatClose": "fenwick_close",
            "usatFor": "fenwick_for",
            "usatRelative": "fenwick_relative",
            "usatTied": "fenwick_tied",
            "usatTotal": "fenwick_total",
            "satPct": "corsi_percent",
            "satPctAhead": "corsi_ahead_percent",
            "satPctBehind": "corsi_behind_percent",
            "satPctClose": "corsi_close_percent",
            "satPctTied": "corsi_tied_percent",
            "satRelative": "corsi_relative",
            "shootingPct5v5": "shooting_percent_5on5",
            "savePct5v5": "save_percent_5on5",
            "shootingPlusSavePct5v5": "shooting_plus_save_percent_5on5",
            "usatPctTied": "fenwick_tied_percent",
            "usatPctAhead": "fenwick_ahead_percent",
            "usatPctBehind": "fenwick_behind_percent",
            "usatPctClose": "fenwick_close_percent",
            "zoneStartPct5v5": "zone_start_5on5_percent",
            "usatPct": "fenwick_percent"
        }

    def map(self, source: dict) -> object:
        team_corsi_fenwick = TeamAdvancedStatsCorsiFenwick(self.data_parser.parse(source, "teamId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(team_corsi_fenwick, attr_name, value)
        return team_corsi_fenwick
    
class TeamAdvancedStatsCorsiFenwickDatabaseMapper:
    """
    Maps TeamAdvancedStatsCorsiFenwick objects to database rows and vice versa.
    """

    @staticmethod
    def to_database_params(team_corsi_fenwick: TeamAdvancedStatsCorsiFenwick) -> tuple:
        """
        Maps a TeamAdvancedStatsCorsiFenwick object to a tuple of parameters for database operations.

        Args:
            team_corsi_fenwick (TeamAdvancedStatsCorsiFenwick): The TeamAdvancedStatsCorsiFenwick object to be mapped.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        return (
            team_corsi_fenwick.team_id,
            team_corsi_fenwick.year,
            team_corsi_fenwick.games_played,
            team_corsi_fenwick.corsi_against,
            team_corsi_fenwick.corsi_ahead,
            team_corsi_fenwick.corsi_behind,
            team_corsi_fenwick.corsi_close,
            team_corsi_fenwick.corsi_for,
            team_corsi_fenwick.corsi_tied,
            team_corsi_fenwick.corsi_total,
            team_corsi_fenwick.fenwick_against,
            team_corsi_fenwick.fenwick_ahead,
            team_corsi_fenwick.fenwick_behind,
            team_corsi_fenwick.fenwick_close,
            team_corsi_fenwick.fenwick_for,
            team_corsi_fenwick.fenwick_relative,
            team_corsi_fenwick.fenwick_tied,
            team_corsi_fenwick.fenwick_total,
            team_corsi_fenwick.corsi_percent,
            team_corsi_fenwick.corsi_ahead_percent,
            team_corsi_fenwick.corsi_behind_percent,
            team_corsi_fenwick.corsi_close_percent,
            team_corsi_fenwick.corsi_tied_percent,
            team_corsi_fenwick.corsi_relative,
            team_corsi_fenwick.shooting_percent_5on5,
            team_corsi_fenwick.save_percent_5on5,
            team_corsi_fenwick.shooting_plus_save_percent_5on5,
            team_corsi_fenwick.fenwick_tied_percent,
            team_corsi_fenwick.fenwick_ahead_percent,
            team_corsi_fenwick.fenwick_behind_percent,
            team_corsi_fenwick.fenwick_close_percent,
            team_corsi_fenwick.zone_start_5on5_percent,
            team_corsi_fenwick.fenwick_percent
        )

    @staticmethod
    def create_insert_query() -> str:
        """
        Creates an insert query for the team_corsi_fenwick table.

        Returns:
            str: The insert query string.
        """
        return """
            INSERT INTO team_advanced_stats_corsi_fenwick (
                team_id, year, games_played, corsi_against, corsi_ahead, corsi_behind, corsi_close, corsi_for,
                corsi_tied, corsi_total, fenwick_against, fenwick_ahead, fenwick_behind, fenwick_close,
                fenwick_for, fenwick_relative, fenwick_tied, fenwick_total, corsi_percent, corsi_ahead_percent,
                corsi_behind_percent, corsi_close_percent, corsi_tied_percent, corsi_relative, shooting_percent_5on5,
                save_percent_5on5, shooting_plus_save_percent_5on5, fenwick_tied_percent, fenwick_ahead_percent,
                fenwick_behind_percent, fenwick_close_percent, zone_start_5on5_percent, fenwick_percent
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        """
        Creates an update query for the team_corsi_fenwick table.

        Returns:
            str: The update query string.
        """
        return """
            UPDATE team_advanced_stats_corsi_fenwick SET
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
                save_percent_5on5 = %s,
                shooting_plus_save_percent_5on5 = %s,
                fenwick_tied_percent = %s,
                fenwick_ahead_percent = %s,
                fenwick_behind_percent = %s,
                fenwick_close_percent = %s,
                zone_start_5on5_percent = %s,
                fenwick_percent = %s
            WHERE team_id = %s AND year = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        """
        Creates a query to check if a team_corsi_fenwick entry exists in the team_corsi_fenwick table.

        Returns:
            str: The existence check query string.
        """
        return "SELECT 1 FROM team_advanced_stats_corsi_fenwick WHERE team_id = %s AND year = %s"
    
class GamesApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "id": "game_id",
            "season": "year",
            "gameType": "game_type_id",
            "gameDate": "game_date",
            "venue": "venue_name", #double parse with default
            "startTimeUTC": "start_time_utc",
            "easternUTCOffset": "eastern_utc_offset",
            "venueUTCOffset": "venue_utc_offset",
            "venueTimezone": "venue_time_zone",
            "gameState": "game_state",
            "gameScheduleState": "game_schedule_state",
            "awayTeam": "away_team_id", #double parse with id
            "homeTeam": "home_team_id", #double parse with id
            "shootoutInUse": "shootout_in_use",
            "regPeriods": "regulation_periods",
            "otInUse": "ot_in_use",
            "tiesInUse": "ties_in_use",
            "gameVideo": "video_3_min_recap_id", #double parse with threeMinRecap
            "gameVideo": "video_condensed_game", #double parse with condensedGame
        }

    def map(self, source: dict) -> object:
        game = Games(self.data_parser.parse(source, "id", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            if attr_name == "venue_name":
                value = self.data_parser.double_parse(source, "venue", "default", "none")
            elif attr_name == "away_team_id":
                value = self.data_parser.double_parse(source, "awayTeam", "id", "none")
                if value == None:
                    value = 0
            elif attr_name == "home_team_id":
                value = self.data_parser.double_parse(source, "homeTeam", "id", "none")
                if value == None:
                    value = 0
            elif attr_name == "video_3_min_recap_id":
                value = self.data_parser.double_parse(source, "gameVideo", "threeMinRecap", "none")
            elif attr_name == "video_condensed_game":
                value = self.data_parser.double_parse(source, "gameVideo", "condensedGame", "none")
            setattr(game, attr_name, value)
        return game
        
class GamesDatabaseMapper:

    @staticmethod
    def to_database_params(game: Games) -> tuple:
        return (
            game.game_id,
            game.year,
            game.game_type_id,
            game.game_date,
            game.venue_name,
            game.start_time_utc,
            game.eastern_utc_offset,
            game.venue_utc_offset,
            game.venue_time_zone,
            game.game_state,
            game.game_schedule_state,
            game.away_team_id,
            game.home_team_id,
            game.shootout_in_use,
            game.regulation_periods,
            game.ot_in_use,
            game.ties_in_use,
            game.video_3_min_recap_id,
            game.video_condensed_game
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO games (
                game_id, year, game_type_id, game_date, venue_name, start_time_utc, eastern_utc_offset, venue_utc_offset,
                venue_time_zone, game_state, game_schedule_state, away_team_id, home_team_id, shootout_in_use,
                regulation_periods, ot_in_use, ties_in_use, video_3_min_recap_id, video_condensed_game
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE games SET
                game_type_id = %s,
                game_date = %s,
                venue_name = %s,
                start_time_utc = %s,
                eastern_utc_offset = %s,
                venue_utc_offset = %s,
                venue_time_zone = %s,
                game_state = %s,
                game_schedule_state = %s,
                away_team_id = %s,
                home_team_id = %s,
                shootout_in_use = %s,
                regulation_periods = %s,
                ot_in_use = %s,
                ties_in_use = %s,
                video_3_min_recap_id = %s,
                video_condensed_game = %s
            WHERE game_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM games WHERE game_id = %s"

class GameThreeStarsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "id": "game_id",
            "star1": "star_1",
            "star2": "star_2",
            "star3": "star_3"
        }

    def map(self, source: dict) -> object:
        game_three_stars = GameThreeStars(self.data_parser.parse(source, "id", "none"))
        star_json = self.data_parser.double_parse(source, "summary", "threeStars", "empty_list")
        if len(star_json) == 0:
            game_three_stars.star_1 = 0
            game_three_stars.star_2 = 0
            game_three_stars.star_3 = 0
        else:
            game_three_stars.star_1 = self.data_parser.parse(star_json[0], "playerId", "none")
            game_three_stars.star_2 = self.data_parser.parse(star_json[1], "playerId", "none")
            game_three_stars.star_3 = self.data_parser.parse(star_json[2], "playerId", "none")

        return game_three_stars

class GameThreeStarsDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameThreeStars) -> tuple:
        return (
            game.game_id,
            game.star_1,
            game.star_2,
            game.star_3
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_three_stars (
                game_id, star_1, star_2, star_3
            ) VALUES (%s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_three_stars SET
                star_1 = %s,
                star_2 = %s,
                star_3 = %s
            WHERE game_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_three_stars WHERE game_id = %s"

class GameSkaterStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "playerId": "player_id",
            "teamId": "team_id",
            "goals": "goals",
            "assists": "assists",
            "points": "points",
            "plusMinus": "plus_minus",
            "pim": "penalty_minutes",
            "hits": "hits",
            "powerPlayGoals": "power_play_goals",
            "shots": "shots",
            "faceoffWinningPctg": "faceoffs",
            "toi": "time_on_ice",
        }

    def map(self, source: dict) -> object:
        game_skater_stats = GameSkaterStats(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_skater_stats, attr_name, value)
        return game_skater_stats

class GameSkaterStatsDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameSkaterStats) -> tuple:
        return (
            game.game_id,
            game.player_id,
            game.team_id,
            game.goals,
            game.assists,
            game.points,
            game.plus_minus,
            game.penalty_minutes,
            game.hits,
            game.power_play_goals,
            game.shots,
            game.faceoffs,
            game.time_on_ice
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_skater_stats (
                game_id, player_id, team_id, goals, assists, points, plus_minus, penalty_minutes, hits,
                power_play_goals, shots, faceoffs, time_on_ice
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_skater_stats SET
                goals = %s,
                assists = %s,
                points = %s,
                plus_minus = %s,
                penalty_minutes = %s,
                hits = %s,
                power_play_goals = %s,
                shots = %s,
                faceoffs = %s,
                time_on_ice = %s
            WHERE game_id = %s AND player_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_skater_stats WHERE game_id = %s AND player_id = %s"

class GameScoreboardApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "homeScore": "home_score",
            "awayScore": "away_score",
            "homeShots": "home_shots",
            "awayShots": "away_shots",
            "timeRemaining": "time_remaining",
            "period": "period",
            "secondsRemaining": "seconds_remaining",
            "running": "running",
            "inIntermission": "in_intermission"
        }

    def map(self, source: dict) -> object:
        game_scoreboard = GameScoreboard(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_scoreboard, attr_name, value)
        return game_scoreboard

class GameScoreboardDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameScoreboard) -> tuple:
        return (
            game.game_id,
            game.home_score,
            game.away_score,
            game.home_shots,
            game.away_shots,
            game.time_remaining,
            game.period,
            game.seconds_remaining,
            game.running,
            game.in_intermission
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_scoreboard (game_id, home_score, away_score, home_shots, away_shots,
                time_remaining, period, seconds_remaining, running, in_intermission) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_scoreboard SET
                home_score = %s,
                away_score = %s,
                home_shots = %s,
                away_shots = %s,
                time_remaining = %s,
                period = %s,
                seconds_remaining = %s,
                running = %s,
                in_intermission = %s
            WHERE game_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_scoreboard WHERE game_id = %s"

class GameRosterApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "teamId": "team_id",
            "playerId": "player_id",
            "scratched": "scratched",
            "starting": "starting",
        }

    def map(self, source: dict) -> object:
        game_roster = GameRoster(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_roster, attr_name, value)
        return game_roster

class GameRosterDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameRoster) -> tuple:
        return (
            game.game_id,
            game.team_id,
            game.player_id,
            game.scratched,
            game.starting
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_roster (
                game_id, team_id, player_id, scratched, is_starting
            ) VALUES (%s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_roster SET
                scratched = %s,
                is_starting = %s
            WHERE game_id = %s AND team_id = %s AND player_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_roster WHERE game_id = %s AND team_id = %s AND player_id = %s"

class GamePlaysApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "eventId": "event_id",
            "teamId": "team_id",
            "ownerPlayerId": "owner_player_id",
            "receivingPlayerId": "receiving_player_id",
            "assist1PlayerId": "assist_1_player_id",
            "assist2PlayerId": "assist_2_player_id",
            "periodNumber": "period_number",
            "periodType": "period_type",
            "timeInPeriod": "time_in_period",
            "timeRemaining": "time_remaining",
            "situationCode": "situation_code",
            "homeTeamDefendingSide": "home_team_defending_side",
            "typeCode": "type_code",
            "typeDescKey": "type_description_key",
            "descKey": "desc_key",
            "duration": "duration",
            "sortOrder": "sort_order",
            "xCoord": "x_coord",
            "yCoord": "y_coord",
            "zoneCode": "zone_code",
            "shotType": "shot_type",
            "reason": "reason",
        }

    def map(self, source: dict) -> object:
        game_plays = GamePlays(self.data_parser.parse(source, "game_id", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_plays, attr_name, value)
        return game_plays
        
class GamePlaysDatabaseMapper:
    @staticmethod
    def to_database_params(game: GamePlays) -> tuple:
        return (
            game.game_id,
            game.event_id,
            game.team_id,
            game.owner_player_id,
            game.receiving_player_id,
            game.assist_1_player_id,
            game.assist_2_player_id,
            game.period_number,
            game.period_type,
            game.time_in_period,
            game.time_remaining,
            game.situation_code,
            game.home_team_defending_side,
            game.type_code,
            game.type_description_key,
            game.desc_key,
            game.duration,
            game.sort_order,
            game.x_coord,
            game.y_coord,
            game.zone_code,
            game.shot_type,
            game.reason
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_plays (
                game_id, event_id, team_id, owner_player_id, receiving_player_id, assist_1_player_id, assist_2_player_id,
                period_number, period_type, time_in_period, time_remaining, situation_code, home_team_defending_side,
                type_code, type_description_key, desc_key, duration, sort_order, x_coord, y_coord, zone_code, shot_type, reason
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_plays SET
                team_id = %s,
                owner_player_id = %s,
                receiving_player_id = %s,
                assist_1_player_id = %s,
                assist_2_player_id = %s,
                period_number = %s,
                period_type = %s,
                time_in_period = %s,
                time_remaining = %s,
                situation_code = %s,
                home_team_defending_side = %s,
                type_code = %s,
                type_description_key = %s,
                desc_key = %s,
                duration = %s,
                sort_order = %s,
                x_coord = %s,
                y_coord = %s,
                zone_code = %s,
                shot_type = %s,
                reason = %s
            WHERE game_id = %s AND event_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_plays WHERE game_id = %s AND event_id = %s"

class GameGoalsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "situationCode": "situation_code",
            "strength": "strength",
            "playerId": "player_id",
            "teamId": "team_id",
            "highlightClip": "highlight_clip_id",
            "goalsToDate": "goals_to_date",
            "awayScore": "away_score",
            "homeScore": "home_score",
            "leadingTeamId": "leading_team_id",
            "timeInPeriod": "time_in_period",
            "period": "period",
            "shotType": "shot_type",
            "goalModifier": "goal_modifier",
            "assist1PlayerId": "assist_1_player_id",
            "assist2PlayerId": "assist_2_player_id",
        }

    def map(self, source: dict) -> object:
        game_goals = GameGoals(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_goals, attr_name, value)
        return game_goals

class GameGoalsDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameGoals) -> tuple:
        return (
            game.game_id,
            game.situation_code,
            game.strength,
            game.player_id,
            game.team_id if game.team_id != None else 0,
            game.highlight_clip_id,
            game.goals_to_date,
            game.away_score,
            game.home_score,
            game.leading_team_id if game.leading_team_id != None else 0,
            game.time_in_period,
            game.period,
            game.shot_type,
            game.goal_modifier,
            game.assist_1_player_id,
            game.assist_2_player_id
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_goals (
                game_id, situation_code, strength, player_id, team_id, highlight_clip_id, goals_to_date, away_score,
                home_score, leading_team_id, time_in_period, period, shot_type, goal_modifier, assist_1_player_id, assist_2_player_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_goals SET
                situation_code = %s,
                strength = %s,
                player_id = %s,
                team_id = %s,
                highlight_clip_id = %s,
                goals_to_date = %s,
                away_score = %s,
                home_score = %s,
                leading_team_id = %s,
                time_in_period = %s,
                period = %s,
                shot_type = %s,
                goal_modifier = %s,
                assist_1_player_id = %s,
                assist_2_player_id = %s
            WHERE game_id = %s AND away_score = %s AND home_score = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_goals WHERE game_id = %s AND away_score = %s AND home_score = %s"

class GameGoalieStatsApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "playerId": "player_id",
            "teamId": "team_id",
            "evenStrengthShotsAgainst": "even_strength_shots_against",
            "powerPlayShotsAgainst": "power_play_shots_against",
            "shorthandedShotsAgainst": "shorthanded_shots_against",
            "saveShotsAgainst": "saves_shots_against",
            "evenStrengthGoalsAgainst": "even_strength_goals_against",
            "powerPlayGoalsAgainst": "power_play_goals_against",
            "shorthandedGoalsAgainst": "shorthanded_goals_against",
            "pim": "penalty_minutes",
            "goalsAgainst": "goals_against",
            "toi": "time_on_ice",
            "starter": "starter",
        }

    def map(self, source: dict) -> object:
        game_goalie_stats = GameGoalieStats(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_goalie_stats, attr_name, value)
        return game_goalie_stats

class GameGoalieStatsDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameGoalieStats) -> tuple:
        return (
            game.game_id,
            game.player_id,
            game.team_id,
            game.even_strength_shots_against,
            game.power_play_shots_against,
            game.shorthanded_shots_against,
            game.saves_shots_against,
            game.even_strength_goals_against,
            game.power_play_goals_against,
            game.shorthanded_goals_against,
            game.penalty_minutes,
            game.goals_against,
            game.time_on_ice,
            game.starter
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_goalie_stats (
                game_id, player_id, team_id, even_strength_shots_against, power_play_shots_against, shorthanded_shots_against,
                saves_shots_against, even_strength_goals_against, power_play_goals_against, shorthanded_goals_against,
                penalty_minutes, goals_against, time_on_ice, starter
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_goalie_stats SET
                even_strength_shots_against = %s,
                power_play_shots_against = %s,
                shorthanded_shots_against = %s,
                saves_shots_against = %s,
                even_strength_goals_against = %s,
                power_play_goals_against = %s,
                shorthanded_goals_against = %s,
                penalty_minutes = %s,
                goals_against = %s,
                time_on_ice = %s,
                starter = %s
            WHERE game_id = %s AND player_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_goalie_stats WHERE game_id = %s AND player_id = %s"

class GameBoxscoreApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "awayTeamId": "away_team_id",
            "awayGoals": "away_goals",
            "awaysog": "away_shots",
            "awayfaceoffWinningPctg": "away_faceoff_percent",
            "awaypowerPlay": "away_power_play_conversions",
            "awaypim": "away_penalty_minutes",
            "awayhits": "away_hits",
            "awayblockedShots": "away_blocked_shots",
            "awaygiveaways": "away_giveaways",
            "awaytakeaways": "away_takeaways",
            "homeTeamId": "home_team_id",
            "homeGoals": "home_goals",
            "homesog": "home_shots",
            "homefaceoffWinningPctg": "home_faceoff_percent",
            "homepowerPlay": "home_power_play_conversions",
            "homepim": "home_penalty_minutes",
            "homehits": "home_hits",
            "homeblockedShots": "home_blocked_shots",
            "homegiveaways": "home_giveaways",
            "hometakeaways": "home_takeaways",
            "homepowerPlay": "home_power_play_conversion",
            "awaypowerPlay": "away_power_play_conversion"
        }

    def map(self, source: dict) -> object:
        game_boxscore = GameBoxscore(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(game_boxscore, attr_name, value)
        return game_boxscore

class GameBoxscoreDatabaseMapper:
    @staticmethod
    def to_database_params(game: GameBoxscore) -> tuple:
        return (
            game.game_id,
            game.away_team_id,
            game.away_goals,
            game.away_shots,
            game.away_faceoff_percent,
            game.away_power_play_conversion,
            game.away_penalty_minutes,
            game.away_hits,
            game.away_blocked_shots,
            game.away_giveaways,
            game.away_takeaways,
            game.home_team_id,
            game.home_goals,
            game.home_shots,
            game.home_faceoff_percent,
            game.home_power_play_conversion,
            game.home_penalty_minutes,
            game.home_hits,
            game.home_blocked_shots,
            game.home_giveaways,
            game.home_takeaways
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO game_boxscore (
                game_id, away_team_id, away_goals, away_shots, away_faceoff_percent, away_power_play_conversion,
                away_penalty_minutes, away_hits, away_blocked_shots, away_giveaways, away_takeaways, home_team_id, home_goals, home_shots,
                home_faceoff_percent, home_power_play_conversion, home_penalty_minutes, home_hits, home_blocked_shots, home_giveaways, home_takeaways
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE game_boxscore SET
                away_team_id = %s,
                away_goals = %s,
                away_shots = %s,
                away_faceoff_percent = %s,
                away_power_play_conversion = %s,
                away_penalty_minutes = %s,
                away_hits = %s,
                away_blocked_shots = %s,
                away_giveaways = %s,
                away_takeaways = %s,
                home_team_id = %s,
                home_goals = %s,
                home_shots = %s,
                home_faceoff_percent = %s,
                home_power_play_conversion = %s,
                home_penalty_minutes = %s,
                home_hits = %s,
                home_blocked_shots = %s,
                home_giveaways = %s,
                home_takeaways = %s
            WHERE game_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM game_boxscore WHERE game_id = %s"

class PlayoffBracketApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {}

    def map(self, source: dict) -> object:
        pass

class PlayoffBracketDatabaseMapper:
    @staticmethod
    def to_database_params(game: PlayoffBracket) -> tuple:
        pass

    @staticmethod
    def create_insert_query() -> str:
        pass

    @staticmethod
    def create_update_query() -> str:
        pass

    @staticmethod
    def create_check_existence_query() -> str:
        pass

class RefereesApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "gameId": "game_id",
            "referee1Name": "referee_1_name",
            "referee2Name": "referee_2_name",
            "linesman1Name": "linesman_1_name",
            "linesman2Name": "linesman_2_name"
        }

    def map(self, source: dict) -> object:
        referees = Referees(self.data_parser.parse(source, "gameId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(referees, attr_name, value)
        return referees

class RefereesDatabaseMapper:
    @staticmethod
    def to_database_params(game: Referees) -> tuple:
        return (
            game.game_id,
            game.referee_1_name,
            game.referee_2_name,
            game.linesman_1_name,
            game.linesman_2_name
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO referees (
                game_id, referee_1_name, referee_2_name, linesman_1_name, linesman_2_name
            ) VALUES (%s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE referees SET
                referee_1_name = %s,
                referee_2_name = %s,
                linesman_1_name = %s,
                linesman_2_name = %s
            WHERE game_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM referees WHERE game_id = %s"

class ShiftDataApiMapper(ApiMapper):
    def __init__(self, data_parser, util):
        self.data_parser = data_parser
        self.util = util
        self.field_map = {
            "id": "shift_id",
            "gameId": "game_id",
            "playerId": "player_id",
            "teamId": "team_id",
            "detailCode": "detail_code",
            "duration": "duration",
            "endTime": "end_time",
            "startTime": "start_time",
            "eventDescription": "event_description",
            "eventDetail": "event_details",
            "eventNumber": "event_number",
            "period": "period_number",
            "shiftNumber": "shift_number",
            "typeCode": "type_code",
        }

    def map(self, source: dict) -> object:
        shift_data = ShiftData(self.data_parser.parse(source, "shiftId", "none"))
        for json_key, attr_name in self.field_map.items():
            value = self.data_parser.parse(source, json_key, "none")
            setattr(shift_data, attr_name, value)
        return shift_data

class ShiftDataDatabaseMapper:
    @staticmethod
    def to_database_params(game: ShiftData) -> tuple:
        return (
            game.shift_id,
            game.game_id,
            game.player_id,
            game.team_id,
            game.detail_code,
            game.duration,
            game.end_time,
            game.start_time,
            game.event_description,
            game.event_details,
            game.event_number,
            game.period_number,
            game.shift_number,
            game.type_code
        )

    @staticmethod
    def create_insert_query() -> str:
        return """
            INSERT INTO shift_data (
                shift_id, game_id, player_id, team_id, detail_code, duration, end_time, start_time,
                event_description, event_details, event_number, period, shift_number, type_code
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    @staticmethod
    def create_update_query() -> str:
        return """
            UPDATE shift_data SET
                player_id = %s,
                team_id = %s,
                detail_code = %s,
                duration = %s,
                end_time = %s,
                start_time = %s,
                event_description = %s,
                event_details = %s,
                event_number = %s,
                period = %s,
                shift_number = %s,
                type_code = %s
            WHERE shift_id = %s
        """

    @staticmethod
    def create_check_existence_query() -> str:
        return "SELECT 1 FROM shift_data WHERE shift_id = %s"


 