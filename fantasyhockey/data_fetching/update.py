from abc import ABC, abstractmethod
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.fetch import *
from fantasyhockey.data_fetching.maps import *


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
    
class UpdateTeams(AbstractUpdater):
    """
    A class to update the team details and team stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_teams: FetchTeams):
        """
        Initializes the UpdateTeamsAndStats instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.

        fetch_teams : FetchTeams
            An instance of the FetchTeams class to fetch the teams data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_teams = fetch_teams

    def fetch_entities(self):
        """
        Fetches the teams to be updated.
        
        Returns:
            list: A list of Team objects to be updated.
        """
        return self.fetch_teams.get_data()

    def entity_exists(self, team, table: str) -> bool:
        """
        Checks if a team or team stats exist in the respective table.
        
        Parameters
        ----------
        team : Team
            The Team object to check.
        table : str
            The table name to check ('team_data' or 'team_stats').

        Returns:
            bool: True if the team or team stats exist, False otherwise.
        """
        if table == 'team_data':
            query = TeamDataDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (team.team_data.team_id, team.team_data.year))
        elif table == 'team_stats':
            query = TeamStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (team.team_stats.team_id, team.team_stats.year))
        return bool(result)

    def create_insert_query(self, table: str) -> str:
        """
        Creates an insert query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('team_data' or 'team_stats').

        Returns:
            str: The insert query string.
        """
        if table == 'team_data':
            return TeamDataDatabaseMapper.create_insert_query()
        elif table == 'team_stats':
            return TeamStatsDatabaseMapper.create_insert_query()

    def create_update_query(self, table: str) -> str:
        """
        Creates an update query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('team_data' or 'team_stats').

        Returns:
            str: The update query string.
        """
        if table == 'team_data':
            return TeamDataDatabaseMapper.create_update_query()
        elif table == 'team_stats':
            return TeamStatsDatabaseMapper.create_update_query()

    def to_database_params(self, team, table: str) -> tuple:
        """
        Maps a Team object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        team : Team
            The Team object to be mapped.
        table : str
            The table name ('team_data' or 'team_stats').

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        if table == 'team_data':
            return TeamDataDatabaseMapper.to_database_params(team.team_data)
        elif table == 'team_stats':
            return TeamStatsDatabaseMapper.to_database_params(team.team_stats)

    def update_in_db(self):
        """
        Fetches the data and updates the corresponding tables in the database.
        """
        teams = self.fetch_entities()
        for team in teams:
            # Update team data
            if self.entity_exists(team, 'team_data'):
                query = self.create_update_query('team_data')
                params = self.to_database_params(team, 'team_data')

                self.database_operator.write(query, params[2:] + (params[0], params[1]))
            else:
                query = self.create_insert_query('team_data')
                params = self.to_database_params(team, 'team_data')
                self.database_operator.write(query, params)

            # Update team stats
            if team.team_stats is not None:
                if self.entity_exists(team, 'team_stats'):
                    query = self.create_update_query('team_stats')
                    params = self.to_database_params(team, 'team_stats')
                    self.database_operator.write(query, params[3:] + (params[0], params[1], params[2]))
                else:
                    query = self.create_insert_query('team_stats')
                    params = self.to_database_params(team, 'team_stats')
                    self.database_operator.write(query, params)

class UpdateTeamAdvancedStats(AbstractUpdater):
    """
    A class to update the team advanced stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_teams: FetchTeamAdvancedStats):
        """
        Initializes the UpdateTeamAdvancedStats instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.

        fetch_teams : FetchTeams
            An instance of the FetchTeams class to fetch the teams data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_teams = fetch_teams

    def fetch_entities(self):
        """
        Fetches the team advanced stats to be updated.
        
        Returns:
            list: A list of TeamAdvancedStats objects to be updated.
        """
        return self.fetch_teams.get_data()

    def entity_exists(self, stats: TeamAdvancedStats, table: str) -> bool:
        """
        Checks if a team advanced stat exists in the respective table.
        
        Parameters
        ----------
        advanced_stats : object
            The advanced stats object to check.
        table : str
            The table name to check.

        Returns:
            bool: True if the advanced stat exists, False otherwise.
        """
        if table == 'team_advanced_stats_days_rest':
            query = TeamAdvancedStatsDaysRestDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year, stats.days_rest))
        elif table == 'team_advanced_stats_corsi_fenwick':
            query = TeamAdvancedStatsCorsiFenwickDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_faceoff_percent':
            query = TeamAdvancedStatsFaceoffPercentDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_shot_type':
            query = TeamAdvancedStatsShotTypeDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_outshoot_outshot':
            query = TeamAdvancedStatsOutshootOutshotDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_goals_by_period': 
            query = TeamAdvancedStatsGoalsByPeriodDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_goals_by_strength':
            query = TeamAdvancedStatsGoalsByStrengthDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_leading_trailing':
            query = TeamAdvancedStatsLeadingTrailingDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_misc':
            query = TeamAdvancedStatsMiscDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_penalties':
            query = TeamAdvancedStatsPenaltiesDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_powerplay_penalty_kill':
            query = TeamAdvancedStatsPowerplayPenaltyKillDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_team_goal_games':
            query = TeamAdvancedStatsTeamGoalGamesDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        elif table == 'team_advanced_stats_scoring_first':
            query = TeamAdvancedStatsScoringFirstDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (stats.team_id, stats.year))
        
        return bool(result)

    def create_insert_query(self, table: str) -> str:
        """
        Creates an insert query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name.

        Returns:
            str: The insert query string.
        """
        if table == 'team_advanced_stats_days_rest':
            return TeamAdvancedStatsDaysRestDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_corsi_fenwick':
            return TeamAdvancedStatsCorsiFenwickDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_faceoff_percent':
            return TeamAdvancedStatsFaceoffPercentDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_shot_type':
            return TeamAdvancedStatsShotTypeDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_outshoot_outshot':
            return TeamAdvancedStatsOutshootOutshotDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_goals_by_period':
            return TeamAdvancedStatsGoalsByPeriodDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_goals_by_strength':
            return TeamAdvancedStatsGoalsByStrengthDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_leading_trailing':
            return TeamAdvancedStatsLeadingTrailingDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_misc':
            return TeamAdvancedStatsMiscDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_penalties':
            return TeamAdvancedStatsPenaltiesDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_powerplay_penalty_kill':
            return TeamAdvancedStatsPowerplayPenaltyKillDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_team_goal_games':
            return TeamAdvancedStatsTeamGoalGamesDatabaseMapper.create_insert_query()
        elif table == 'team_advanced_stats_scoring_first':
            return TeamAdvancedStatsScoringFirstDatabaseMapper.create_insert_query()

    def create_update_query(self, table: str) -> str:
        """
        Creates an update query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name.

        Returns:
            str: The update query string.
        """
        if table == 'team_advanced_stats_days_rest':
            return TeamAdvancedStatsDaysRestDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_corsi_fenwick':
            return TeamAdvancedStatsCorsiFenwickDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_faceoff_percent':
            return TeamAdvancedStatsFaceoffPercentDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_shot_type':
            return TeamAdvancedStatsShotTypeDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_outshoot_outshot':
            return TeamAdvancedStatsOutshootOutshotDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_goals_by_period':
            return TeamAdvancedStatsGoalsByPeriodDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_goals_by_strength':
            return TeamAdvancedStatsGoalsByStrengthDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_leading_trailing':
            return TeamAdvancedStatsLeadingTrailingDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_misc':
            return TeamAdvancedStatsMiscDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_penalties':
            return TeamAdvancedStatsPenaltiesDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_powerplay_penalty_kill':
            return TeamAdvancedStatsPowerplayPenaltyKillDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_team_goal_games':
            return TeamAdvancedStatsTeamGoalGamesDatabaseMapper.create_update_query()
        elif table == 'team_advanced_stats_scoring_first':
            return TeamAdvancedStatsScoringFirstDatabaseMapper.create_update_query()
        

    def to_database_params(self, advanced_stats, table: str) -> tuple:
        """
        Maps an advanced stats object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        advanced_stats : object
            The advanced stats object to be mapped.
        table : str
            The table name.

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        if table == 'team_advanced_stats_days_rest':
            return TeamAdvancedStatsDaysRestDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_corsi_fenwick':
            return TeamAdvancedStatsCorsiFenwickDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_faceoff_percent':
            return TeamAdvancedStatsFaceoffPercentDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_shot_type':
            return TeamAdvancedStatsShotTypeDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_outshoot_outshot':
            return TeamAdvancedStatsOutshootOutshotDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_goals_by_period':
            return TeamAdvancedStatsGoalsByPeriodDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_goals_by_strength':
            return TeamAdvancedStatsGoalsByStrengthDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_leading_trailing':
            return TeamAdvancedStatsLeadingTrailingDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_misc':
            return TeamAdvancedStatsMiscDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_penalties':
            return TeamAdvancedStatsPenaltiesDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_powerplay_penalty_kill':
            return TeamAdvancedStatsPowerplayPenaltyKillDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_team_goal_games':
            return TeamAdvancedStatsTeamGoalGamesDatabaseMapper.to_database_params(advanced_stats)
        elif table == 'team_advanced_stats_scoring_first':
            return TeamAdvancedStatsScoringFirstDatabaseMapper.to_database_params(advanced_stats)
        

    def update_in_db(self):
        """
        Fetches the data and updates the corresponding tables in the database.
        """
        teams = self.fetch_entities()
        for team in teams:
            
            for days_rest in team.team_advanced_stats_days_rest:
                if self.entity_exists(days_rest, 'team_advanced_stats_days_rest'):
                    query = self.create_update_query('team_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'team_advanced_stats_days_rest')
                    self.database_operator.write(query, params[3:] + (params[0], params[1], params[2]))
                else:
                    print("Inserting days rest")
                    query = self.create_insert_query('team_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'team_advanced_stats_days_rest')
                    self.database_operator.write(query, params)

            for corsi_fenwick in team.team_advanced_stats_corsi_fenwick:
                if self.entity_exists(corsi_fenwick, 'team_advanced_stats_corsi_fenwick'):
                    query = self.create_update_query('team_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'team_advanced_stats_corsi_fenwick')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'team_advanced_stats_corsi_fenwick')
                    self.database_operator.write(query, params)

            for faceoff_percent in team.team_advanced_stats_faceoff_percent:
                if self.entity_exists(faceoff_percent, 'team_advanced_stats_faceoff_percent'):
                    query = self.create_update_query('team_advanced_stats_faceoff_percent')
                    params = self.to_database_params(faceoff_percent, 'team_advanced_stats_faceoff_percent')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_faceoff_percent')
                    params = self.to_database_params(faceoff_percent, 'team_advanced_stats_faceoff_percent')
                    self.database_operator.write(query, params)

            for shot_type in team.team_advanced_stats_shot_type:
                if self.entity_exists(shot_type, 'team_advanced_stats_shot_type'):
                    query = self.create_update_query('team_advanced_stats_shot_type')
                    params = self.to_database_params(shot_type, 'team_advanced_stats_shot_type')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_shot_type')
                    params = self.to_database_params(shot_type, 'team_advanced_stats_shot_type')
                    self.database_operator.write(query, params)
            
            for outshoot_outshot in team.team_advanced_stats_outshoot_outshot:
                if self.entity_exists(outshoot_outshot, 'team_advanced_stats_outshoot_outshot'):
                    query = self.create_update_query('team_advanced_stats_outshoot_outshot')
                    params = self.to_database_params(outshoot_outshot, 'team_advanced_stats_outshoot_outshot')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_outshoot_outshot')
                    params = self.to_database_params(outshoot_outshot, 'team_advanced_stats_outshoot_outshot')
                    self.database_operator.write(query, params)

            for goals_by_period in team.team_advanced_stats_goals_by_period:
                if self.entity_exists(goals_by_period, 'team_advanced_stats_goals_by_period'):
                    query = self.create_update_query('team_advanced_stats_goals_by_period')
                    params = self.to_database_params(goals_by_period, 'team_advanced_stats_goals_by_period')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_goals_by_period')
                    params = self.to_database_params(goals_by_period, 'team_advanced_stats_goals_by_period')
                    self.database_operator.write(query, params)

            for goals_by_strength in team.team_advanced_stats_goals_by_strength:
                if self.entity_exists(goals_by_strength, 'team_advanced_stats_goals_by_strength'):
                    query = self.create_update_query('team_advanced_stats_goals_by_strength')
                    params = self.to_database_params(goals_by_strength, 'team_advanced_stats_goals_by_strength')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_goals_by_strength')
                    params = self.to_database_params(goals_by_strength, 'team_advanced_stats_goals_by_strength')
                    self.database_operator.write(query, params)

            for leading_trailing in team.team_advanced_stats_leading_trailing:
                if self.entity_exists(leading_trailing, 'team_advanced_stats_leading_trailing'):
                    query = self.create_update_query('team_advanced_stats_leading_trailing')
                    params = self.to_database_params(leading_trailing, 'team_advanced_stats_leading_trailing')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_leading_trailing')
                    params = self.to_database_params(leading_trailing, 'team_advanced_stats_leading_trailing')
                    self.database_operator.write(query, params)

            for misc in team.team_advanced_stats_misc:
                if self.entity_exists(misc, 'team_advanced_stats_misc'):
                    query = self.create_update_query('team_advanced_stats_misc')
                    params = self.to_database_params(misc, 'team_advanced_stats_misc')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_misc')
                    params = self.to_database_params(misc, 'team_advanced_stats_misc')
                    self.database_operator.write(query, params)

            for penalties in team.team_advanced_stats_penalties:
                if self.entity_exists(penalties, 'team_advanced_stats_penalties'):
                    query = self.create_update_query('team_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'team_advanced_stats_penalties')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'team_advanced_stats_penalties')
                    self.database_operator.write(query, params)

            for powerplay_penalty_kill in team.team_advanced_stats_powerplay_penalty_kill:
                if self.entity_exists(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill'):
                    query = self.create_update_query('team_advanced_stats_powerplay_penalty_kill')
                    params = self.to_database_params(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_powerplay_penalty_kill')
                    params = self.to_database_params(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill')
                    self.database_operator.write(query, params)

            for team_goal_games in team.team_advanced_stats_team_goal_games:
                if self.entity_exists(team_goal_games, 'team_advanced_stats_team_goal_games'):
                    query = self.create_update_query('team_advanced_stats_team_goal_games')
                    params = self.to_database_params(team_goal_games, 'team_advanced_stats_team_goal_games')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_team_goal_games')
                    params = self.to_database_params(team_goal_games, 'team_advanced_stats_team_goal_games')
                    self.database_operator.write(query, params)

            for scoring_first in team.team_advanced_stats_scoring_first:
                if self.entity_exists(scoring_first, 'team_advanced_stats_scoring_first'):
                    query = self.create_update_query('team_advanced_stats_scoring_first')
                    params = self.to_database_params(scoring_first, 'team_advanced_stats_scoring_first')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_scoring_first')
                    params = self.to_database_params(scoring_first, 'team_advanced_stats_scoring_first')
                    self.database_operator.write(query, params)

class UpdatePlayers(AbstractUpdater):
    """
    A class to update the player details and team stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_players: FetchPlayers):
        """
        Initializes the UpdatePlayers instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.

        fetch_players : FetchPlayers
            An instance of the FetchPlayers class to fetch the players data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_players = fetch_players

    def fetch_entities(self):
        """
        Fetches the players to be updated.
        
        Returns:
            list: A list of Player objects to be updated.
        """
        return self.fetch_players.get_data()

    def entity_exists(self, entity, table: str) -> bool:
        """
        Checks if a player, player details, player awards, or player draft entry exists in the respective table.
        
        Parameters
        ----------
        entity : object
            The entity object to check (Player, PlayerDetails, PlayerAward, PlayerDraft).
        table : str
            The table name to check ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            bool: True if the entity exists, False otherwise.
        """
        if table == 'players':
            query = PlayersDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id,))
        elif table == 'player_details':
            query = PlayerDetailsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id,))
        elif table == 'player_awards':
            query = PlayerAwardsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year, entity.award))
        elif table == 'player_draft':
            query = PlayerDraftDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id,))
        return bool(result)

    def create_insert_query(self, table: str) -> str:
        """
        Creates an insert query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            str: The insert query string.
        """
        if table == 'players':
            return PlayersDatabaseMapper.create_insert_query()
        elif table == 'player_details':
            return PlayerDetailsDatabaseMapper.create_insert_query()
        elif table == 'player_awards':
            return PlayerAwardsDatabaseMapper.create_insert_query()
        elif table == 'player_draft':
            return PlayerDraftDatabaseMapper.create_insert_query()

    def create_update_query(self, table: str) -> str:
        """
        Creates an update query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            str: The update query string.
        """
        if table == 'players':
            return PlayersDatabaseMapper.create_update_query()
        elif table == 'player_details':
            return PlayerDetailsDatabaseMapper.create_update_query()
        elif table == 'player_awards':
            return PlayerAwardsDatabaseMapper.create_update_query()
        elif table == 'player_draft':
            return PlayerDraftDatabaseMapper.create_update_query()

    def to_database_params(self, entity, table: str) -> tuple:
        """
        Maps a Player object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        entity : object
            The entity object to be mapped (Player, PlayerDetails, PlayerAward, PlayerDraft).
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        if table == 'players':
            return PlayersDatabaseMapper.to_database_params(entity)
        elif table == 'player_details':
            return PlayerDetailsDatabaseMapper.to_database_params(entity)
        elif table == 'player_awards':
            return PlayerAwardsDatabaseMapper.to_database_params(entity)
        elif table == 'player_draft':
            return PlayerDraftDatabaseMapper.to_database_params(entity)

    def update_in_db(self):
        """
        Fetches the data and updates the corresponding tables in the database.
        """
        players = self.fetch_entities()
        for player in players:
            # Update players data
            if self.entity_exists(player, 'players'):
                if player.team_id == None:
                    player.team_id = 0
                query = self.create_update_query('players')
                params = self.to_database_params(player, 'players')
                self.database_operator.write(query, params[1:] + (params[0],))
            else:
                print("Inserting player")
                query = self.create_insert_query('players')
                params = self.to_database_params(player, 'players')
                self.database_operator.write(query, params)

            # Update player details
            if self.entity_exists(player.player_details, 'player_details'):
                query = self.create_update_query('player_details')
                params = self.to_database_params(player.player_details, 'player_details')
                self.database_operator.write(query, params[1:] + (params[0],))
            else:
                #print("Inserting player details")
                query = self.create_insert_query('player_details')
                params = self.to_database_params(player.player_details, 'player_details')
                self.database_operator.write(query, params)

            # Update player awards
            for award in player.player_awards:
                if self.entity_exists(award, 'player_awards'):
                    query = self.create_update_query('player_awards')
                    params = self.to_database_params(award, 'player_awards')
                    self.database_operator.write(query, (params[2], params[0], params[1], params[2]))
                else:
                    print("Inserting awards")
                    query = self.create_insert_query('player_awards')
                    params = self.to_database_params(award, 'player_awards')
                    self.database_operator.write(query, params)
            
            # Update player draft
            if self.entity_exists(player.player_draft, 'player_draft'):
                query = self.create_update_query('player_draft')
                params = self.to_database_params(player.player_draft, 'player_draft')
                self.database_operator.write(query, params[1:] + (params[0],))
            else:
                print("Inserting draft")
                query = self.create_insert_query('player_draft')
                params = self.to_database_params(player.player_draft, 'player_draft')
                self.database_operator.write(query, params)

class UpdateSkaters(AbstractUpdater):
    """
    A class to update the player details and team stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_skaters: FetchSkaters):
        """
        Initializes the UpdatePlayers instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact with the database.

        fetch_players : FetchPlayers
            An instance of the FetchPlayers class to fetch the players data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_skaters = fetch_skaters

    def fetch_entities(self):
        """
        Fetches the players to be updated.
        
        Returns:
            list: A list of Player objects to be updated.
        """
        return self.fetch_skaters.get_data()

    def entity_exists(self, entity, table: str) -> bool:
        """
        Checks if a player, player details, player awards, or player draft entry exists in the respective table.
        
        Parameters
        ----------
        entity : object
            The entity object to check (Player, PlayerDetails, PlayerAward, PlayerDraft).
        table : str
            The table name to check ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            bool: True if the entity exists, False otherwise.
        """
        if table == 'skater_stats':
            query = SkaterStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.team_id, entity.year, entity.game_type_id, entity.sequence))
        elif table == 'skater_youth_stats':
            query = SkaterYouthStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year, entity.team_name, entity.league_name, entity.game_type_id, entity.sequence))
        elif table == 'skater_advanced_stats_corsi_fenwick':
            query = SkaterAdvancedStatsCorsiFenwickDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_faceoffs':
            query = SkaterAdvancedStatsFaceoffsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_goals':
            query = SkaterAdvancedStatsGoalsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_misc':
            query = SkaterAdvancedStatsMiscDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_penalties':
            query = SkaterAdvancedStatsPenaltiesDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_penalty_kill':
            query = SkaterAdvancedStatsPenaltyKillDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_powerplay':
            query = SkaterAdvancedStatsPowerplayDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year, entity.team_id))
        elif table == 'skater_advanced_stats_scoring':
            query = SkaterAdvancedStatsScoringDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_shootout':
            query = SkaterAdvancedStatsShootoutDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'skater_advanced_stats_toi':
            query = SkaterAdvancedStatsTOIDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))

        return bool(result)

    def create_insert_query(self, table: str) -> str:
        """
        Creates an insert query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            str: The insert query string.
        """
        if table == 'skater_stats':
            return SkaterStatsDatabaseMapper.create_insert_query()
        elif table == 'skater_youth_stats':
            return SkaterYouthStatsDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_corsi_fenwick':
            return SkaterAdvancedStatsCorsiFenwickDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_faceoffs':
            return SkaterAdvancedStatsFaceoffsDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_goals':
            return SkaterAdvancedStatsGoalsDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_misc':
            return SkaterAdvancedStatsMiscDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_penalties':
            return SkaterAdvancedStatsPenaltiesDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_penalty_kill':
            return SkaterAdvancedStatsPenaltyKillDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_powerplay':
            return SkaterAdvancedStatsPowerplayDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_scoring':
            return SkaterAdvancedStatsScoringDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_shootout':
            return SkaterAdvancedStatsShootoutDatabaseMapper.create_insert_query()
        elif table == 'skater_advanced_stats_toi':
            return SkaterAdvancedStatsTOIDatabaseMapper.create_insert_query()

    def create_update_query(self, table: str) -> str:
        """
        Creates an update query for the respective table.
        
        Parameters
        ----------
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            str: The update query string.
        """
        if table == 'skater_stats':
            return SkaterStatsDatabaseMapper.create_update_query()
        elif table == 'skater_youth_stats':
            return SkaterYouthStatsDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_corsi_fenwick':
            return SkaterAdvancedStatsCorsiFenwickDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_faceoffs':
            return SkaterAdvancedStatsFaceoffsDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_goals':
            return SkaterAdvancedStatsGoalsDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_misc':
            return SkaterAdvancedStatsMiscDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_penalties':
            return SkaterAdvancedStatsPenaltiesDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_penalty_kill':
            return SkaterAdvancedStatsPenaltyKillDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_powerplay':
            return SkaterAdvancedStatsPowerplayDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_scoring':
            return SkaterAdvancedStatsScoringDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_shootout':
            return SkaterAdvancedStatsShootoutDatabaseMapper.create_update_query()
        elif table == 'skater_advanced_stats_toi':
            return SkaterAdvancedStatsTOIDatabaseMapper.create_update_query()

    def to_database_params(self, entity, table: str) -> tuple:
        """
        Maps a Player object to a tuple of parameters for database operations.
        
        Parameters
        ----------
        entity : object
            The entity object to be mapped (Player, PlayerDetails, PlayerAward, PlayerDraft).
        table : str
            The table name ('players', 'player_details', 'player_awards', 'player_draft').

        Returns:
            tuple: The tuple of parameters for database operations.
        """
        if table == 'skater_stats':
            return SkaterStatsDatabaseMapper.to_database_params(entity)
        elif table == 'skater_youth_stats':
            return SkaterYouthStatsDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_corsi_fenwick':
            return SkaterAdvancedStatsCorsiFenwickDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_faceoffs':
            return SkaterAdvancedStatsFaceoffsDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_goals':
            return SkaterAdvancedStatsGoalsDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_misc':
            return SkaterAdvancedStatsMiscDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_penalties':
            return SkaterAdvancedStatsPenaltiesDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_penalty_kill':
            return SkaterAdvancedStatsPenaltyKillDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_powerplay':
            return SkaterAdvancedStatsPowerplayDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_scoring':
            return SkaterAdvancedStatsScoringDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_shootout':
            return SkaterAdvancedStatsShootoutDatabaseMapper.to_database_params(entity)
        elif table == 'skater_advanced_stats_toi':
            return SkaterAdvancedStatsTOIDatabaseMapper.to_database_params(entity)

    def update_in_db(self):
        """
        Fetches the data and updates the corresponding tables in the database.
        """
        skaters = self.fetch_entities()
        for skater in skaters:
            for skater_stats in skater.skater_stats:
                if self.entity_exists(skater_stats, 'skater_stats'):
                    query = self.create_update_query('skater_stats')
                    params = self.to_database_params(skater_stats, 'skater_stats')
                    self.database_operator.write(query, params[2:] + (params[0], params[1], params[2], params[18], params[19]))
                else:
                    query = self.create_insert_query('skater_stats')
                    params = self.to_database_params(skater_stats, 'skater_stats')
                    self.database_operator.write(query, params)

            for skater_youth_stats in skater.youth_stats:
                if self.entity_exists(skater_youth_stats, 'skater_youth_stats'):
                    query = self.create_update_query('skater_youth_stats')
                    params = self.to_database_params(skater_youth_stats, 'skater_youth_stats')
                    self.database_operator.write(query, params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                else:
                    query = self.create_insert_query('skater_youth_stats')
                    params = self.to_database_params(skater_youth_stats, 'skater_youth_stats')
                    self.database_operator.write(query, params)
            
            for corsi_fenwick in skater.advanced_stats_corsi_fenwick:
                if self.entity_exists(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick'):
                    query = self.create_update_query('skater_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick')
                    self.database_operator.write(query, params)
            
            for faceoffs in skater.advanced_stats_faceoffs:
                if self.entity_exists(faceoffs, 'skater_advanced_stats_faceoffs'):
                    query = self.create_update_query('skater_advanced_stats_faceoffs')
                    params = self.to_database_params(faceoffs, 'skater_advanced_stats_faceoffs')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_faceoffs')
                    params = self.to_database_params(faceoffs, 'skater_advanced_stats_faceoffs')
                    self.database_operator.write(query, params)
            
            for goals in skater.advanced_stats_goals:
                if self.entity_exists(goals, 'skater_advanced_stats_goals'):
                    query = self.create_update_query('skater_advanced_stats_goals')
                    params = self.to_database_params(goals, 'skater_advanced_stats_goals')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_goals')
                    params = self.to_database_params(goals, 'skater_advanced_stats_goals')
                    self.database_operator.write(query, params)

            
            for misc in skater.advanced_stats_misc:
                if self.entity_exists(misc, 'skater_advanced_stats_misc'):
                    query = self.create_update_query('skater_advanced_stats_misc')
                    params = self.to_database_params(misc, 'skater_advanced_stats_misc')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_misc')
                    params = self.to_database_params(misc, 'skater_advanced_stats_misc')
                    self.database_operator.write(query, params)

            for penalties in skater.advanced_stats_penalties:
                if self.entity_exists(penalties, 'skater_advanced_stats_penalties'):
                    query = self.create_update_query('skater_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'skater_advanced_stats_penalties')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'skater_advanced_stats_penalties')
                    self.database_operator.write(query, params)

            for penalty_kill in skater.advanced_stats_penalty_kill:
                if self.entity_exists(penalty_kill, 'skater_advanced_stats_penalty_kill'):
                    query = self.create_update_query('skater_advanced_stats_penalty_kill')
                    params = self.to_database_params(penalty_kill, 'skater_advanced_stats_penalty_kill')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_penalty_kill')
                    params = self.to_database_params(penalty_kill, 'skater_advanced_stats_penalty_kill')
                    self.database_operator.write(query, params)

            for powerplay in skater.advanced_stats_powerplay:
                if self.entity_exists(powerplay, 'skater_advanced_stats_powerplay'):
                    query = self.create_update_query('skater_advanced_stats_powerplay')
                    params = self.to_database_params(powerplay, 'skater_advanced_stats_powerplay')
                    self.database_operator.write(query, params[2:] + (params[0], params[1], params[2]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_powerplay')
                    params = self.to_database_params(powerplay, 'skater_advanced_stats_powerplay')
                    self.database_operator.write(query, params)

            for scoring in skater.advanced_stats_scoring:
                if self.entity_exists(scoring, 'skater_advanced_stats_scoring'):
                    query = self.create_update_query('skater_advanced_stats_scoring')
                    params = self.to_database_params(scoring, 'skater_advanced_stats_scoring')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_scoring')
                    params = self.to_database_params(scoring, 'skater_advanced_stats_scoring')
                    self.database_operator.write(query, params)
            
            for shootout in skater.advanced_stats_shootout:
                if self.entity_exists(shootout, 'skater_advanced_stats_shootout'):
                    query = self.create_update_query('skater_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'skater_advanced_stats_shootout')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'skater_advanced_stats_shootout')
                    self.database_operator.write(query, params)

            for toi in skater.advanced_stats_toi:
                if self.entity_exists(toi, 'skater_advanced_stats_toi'):
                    query = self.create_update_query('skater_advanced_stats_toi')
                    params = self.to_database_params(toi, 'skater_advanced_stats_toi')
                    self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_toi')
                    params = self.to_database_params(toi, 'skater_advanced_stats_toi')
                    self.database_operator.write(query, params)

class UpdateGoalies(AbstractUpdater):
    """
    A class to update the player details and team stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_goalies: FetchGoalies):
        """
        Initializes the UpdatePlayers instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact
            with the database.

        fetch_players : FetchPlayers
            An instance of the FetchPlayers class to fetch the
            players data from the NHL API.
        """
        super().__init__(database_operator)
        self.fetch_goalies = fetch_goalies

    def fetch_entities(self):
        """
        Fetches the players to be updated.
        
        Returns:
            list: A list of Player objects to be updated.
        """
        return self.fetch_goalies.get_data()

    def entity_exists(self, entity, table: str) -> bool:
        if table == 'goalie_stats':
            query = GoalieStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year, entity.team_id, entity.game_type_id, entity.sequence))
        elif table == 'goalie_youth_stats':
            query = GoalieYouthStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year, entity.team_name, entity.league_name, entity.game_type_id, entity.sequence))
        elif table == 'goalie_advanced_stats':
            query = GoalieAdvancedStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'goalie_advanced_stats_days_rest':
            query = GoalieAdvancedStatsDaysRestDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'goalie_advanced_stats_penalty_shots':
            query = GoalieAdvancedStatsPenaltyShotsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'goalie_advanced_stats_saves_by_strength':
            query = GoalieAdvancedStatsSavesByStrengthDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'goalie_advanced_stats_shootout':
            query = GoalieAdvancedStatsShootoutDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))
        elif table == 'goalie_advanced_stats_start_relieved':
            query = GoalieAdvancedStatsStartRelievedDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.player_id, entity.year))

        return bool(result)


    def create_insert_query(self, table: str) -> str:
        if table == 'goalie_stats':
            return GoalieStatsDatabaseMapper.create_insert_query()
        elif table == 'goalie_youth_stats':
            return GoalieYouthStatsDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats':
            return GoalieAdvancedStatsDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats_days_rest':
            return GoalieAdvancedStatsDaysRestDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats_penalty_shots':
            return GoalieAdvancedStatsPenaltyShotsDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats_saves_by_strength':
            return GoalieAdvancedStatsSavesByStrengthDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats_shootout':
            return GoalieAdvancedStatsShootoutDatabaseMapper.create_insert_query()
        elif table == 'goalie_advanced_stats_start_relieved':
            return GoalieAdvancedStatsStartRelievedDatabaseMapper.create_insert_query()
        

    def create_update_query(self, table: str) -> str:
        if table == 'goalie_stats':
            return GoalieStatsDatabaseMapper.create_update_query()
        elif table == 'goalie_youth_stats':
            return GoalieYouthStatsDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats':
            return GoalieAdvancedStatsDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats_days_rest':
            return GoalieAdvancedStatsDaysRestDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats_penalty_shots':
            return GoalieAdvancedStatsPenaltyShotsDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats_saves_by_strength':
            return GoalieAdvancedStatsSavesByStrengthDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats_shootout':
            return GoalieAdvancedStatsShootoutDatabaseMapper.create_update_query()
        elif table == 'goalie_advanced_stats_start_relieved':
            return GoalieAdvancedStatsStartRelievedDatabaseMapper.create_update_query()

    def to_database_params(self, entity, table: str) -> tuple:
        if table == 'goalie_stats':
            return GoalieStatsDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_youth_stats':
            return GoalieYouthStatsDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats':
            return GoalieAdvancedStatsDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats_days_rest':
            return GoalieAdvancedStatsDaysRestDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats_penalty_shots':
            return GoalieAdvancedStatsPenaltyShotsDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats_saves_by_strength':
            return GoalieAdvancedStatsSavesByStrengthDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats_shootout':
            return GoalieAdvancedStatsShootoutDatabaseMapper.to_database_params(entity)
        elif table == 'goalie_advanced_stats_start_relieved':
            return GoalieAdvancedStatsStartRelievedDatabaseMapper.to_database_params(entity)

    def update_in_db(self):
        goalies = self.fetch_entities()
        for goalie in goalies:
            for goalie_stats in goalie.goalie_stats:
                if self.entity_exists(goalie_stats, 'goalie_stats'):
                    query = self.create_update_query('goalie_stats')
                    params = self.to_database_params(goalie_stats, 'goalie_stats')
                    self.database_operator.write(query, params[2:] + (params[0], params[1], params[2], params[3], params[4]))
                else:
                    query = self.create_insert_query('goalie_stats')
                    params = self.to_database_params(goalie_stats, 'goalie_stats')
                    self.database_operator.write(query, params)

            for goalie_youth_stats in goalie.goalie_youth_stats:
                if self.entity_exists(goalie_youth_stats, 'goalie_youth_stats'):
                    query = self.create_update_query('goalie_youth_stats')
                    params = self.to_database_params(goalie_youth_stats, 'goalie_youth_stats')
                    self.database_operator.write(query, params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                else:
                    query = self.create_insert_query('goalie_youth_stats')
                    params = self.to_database_params(goalie_youth_stats, 'goalie_youth_stats')
                    self.database_operator.write(query, params)
            
            for advanced_stats in goalie.goalie_advanced_stats:
                if self.entity_exists(advanced_stats, 'goalie_advanced_stats'):
                    query = self.create_update_query('goalie_advanced_stats')
                    params = self.to_database_params(advanced_stats, 'goalie_advanced_stats')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats')
                    params = self.to_database_params(advanced_stats, 'goalie_advanced_stats')
                    self.database_operator.write(query, params)
            
            for days_rest in goalie.goalie_advanced_stats_days_rest:
                if self.entity_exists(days_rest, 'goalie_advanced_stats_days_rest'):
                    query = self.create_update_query('goalie_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'goalie_advanced_stats_days_rest')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'goalie_advanced_stats_days_rest')
                    self.database_operator.write(query, params)

            for penalty_shots in goalie.goalie_advanced_stats_penalty_shots:
                if self.entity_exists(penalty_shots, 'goalie_advanced_stats_penalty_shots'):
                    query = self.create_update_query('goalie_advanced_stats_penalty_shots')
                    params = self.to_database_params(penalty_shots, 'goalie_advanced_stats_penalty_shots')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_penalty_shots')
                    params = self.to_database_params(penalty_shots, 'goalie_advanced_stats_penalty_shots')
                    self.database_operator.write(query, params)

            for saves_by_strength in goalie.goalie_advanced_stats_saves_by_strength:
                if self.entity_exists(saves_by_strength, 'goalie_advanced_stats_saves_by_strength'):
                    query = self.create_update_query('goalie_advanced_stats_saves_by_strength')
                    params = self.to_database_params(saves_by_strength, 'goalie_advanced_stats_saves_by_strength')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_saves_by_strength')
                    params = self.to_database_params(saves_by_strength, 'goalie_advanced_stats_saves_by_strength')
                    self.database_operator.write(query, params)

            for shootout in goalie.goalie_advanced_stats_shootout:
                if self.entity_exists(shootout, 'goalie_advanced_stats_shootout'):
                    query = self.create_update_query('goalie_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'goalie_advanced_stats_shootout')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'goalie_advanced_stats_shootout')
                    self.database_operator.write(query, params)

            for start_relieved in goalie.goalie_advanced_stats_start_relieved:
                if self.entity_exists(start_relieved, 'goalie_advanced_stats_start_relieved'):
                    query = self.create_update_query('goalie_advanced_stats_start_relieved')
                    params = self.to_database_params(start_relieved, 'goalie_advanced_stats_start_relieved')
                    self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_start_relieved')
                    params = self.to_database_params(start_relieved, 'goalie_advanced_stats_start_relieved')
                    self.database_operator.write(query, params)

            
            
            