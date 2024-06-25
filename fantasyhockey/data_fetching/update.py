from abc import ABC, abstractmethod
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.fetch import *
from fantasyhockey.data_fetching.maps import *
import concurrent.futures
import os


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

    def update_in_db(self):
        """
        Fetches the data and updates the draft_rankings table in the database.
        """
        draft_rankings = self.fetch_entities()
        for draft_ranking in draft_rankings:
            if self.entity_exists(draft_ranking):
                query = self.create_update_query()
                params = self.to_database_params(draft_ranking)
                self.database_operator.write(query, params[1:] + (params[0], params[1], params[2], params[3]))
            else:
                query = self.create_insert_query()
                params = self.to_database_params(draft_ranking)
                self.database_operator.write(query, params)
    
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
        batch_insert = {
            'team_data': [],
            'team_stats': []
        }

        batch_update = {
            'team_data': [],
            'team_stats': []
        }

        teams = self.fetch_entities()
        for team in teams:
            # Update team data
            if self.entity_exists(team, 'team_data'):
                query = self.create_update_query('team_data')
                params = self.to_database_params(team, 'team_data')
                batch_update['team_data'].append(params[2:] + (params[0], params[1]))
                #self.database_operator.write(query, params[2:] + (params[0], params[1]))
            else:
                query = self.create_insert_query('team_data')
                params = self.to_database_params(team, 'team_data')
                batch_insert['team_data'].append(params)
                self.database_operator.write(query, params)

            # Update team stats
            if team.team_stats is not None:
                if self.entity_exists(team, 'team_stats'):
                    query = self.create_update_query('team_stats')
                    params = self.to_database_params(team, 'team_stats')
                    batch_update['team_stats'].append(params[3:] + (params[0], params[1], params[2]))
                    #self.database_operator.write(query, params[3:] + (params[0], params[1], params[2]))
                else:
                    query = self.create_insert_query('team_stats')
                    params = self.to_database_params(team, 'team_stats')
                    batch_insert['team_stats'].append(params)
                    #self.database_operator.write(query, params)

        for key in batch_update:
            if batch_update[key]:
                query = self.create_update_query(key)
                self.database_operator.batch_write(query, batch_update[key])

        for key in batch_insert:
            if batch_insert[key]:
                query = self.create_insert_query(key)
                self.database_operator.batch_write(query, batch_insert[key])


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

        batch_insert = {
            'team_advanced_stats_days_rest': [],
            'team_advanced_stats_corsi_fenwick': [],
            'team_advanced_stats_faceoff_percent': [],
            'team_advanced_stats_shot_type': [],
            'team_advanced_stats_outshoot_outshot': [],
            'team_advanced_stats_goals_by_period': [],
            'team_advanced_stats_goals_by_strength': [],
            'team_advanced_stats_leading_trailing': [],
            'team_advanced_stats_misc': [],
            'team_advanced_stats_penalties': [],
            'team_advanced_stats_powerplay_penalty_kill': [],
            'team_advanced_stats_team_goal_games': [],
            'team_advanced_stats_scoring_first': []
        }

        batch_update = {
            'team_advanced_stats_days_rest': [],
            'team_advanced_stats_corsi_fenwick': [],
            'team_advanced_stats_faceoff_percent': [],
            'team_advanced_stats_shot_type': [],
            'team_advanced_stats_outshoot_outshot': [],
            'team_advanced_stats_goals_by_period': [],
            'team_advanced_stats_goals_by_strength': [],
            'team_advanced_stats_leading_trailing': [],
            'team_advanced_stats_misc': [],
            'team_advanced_stats_penalties': [],
            'team_advanced_stats_powerplay_penalty_kill': [],
            'team_advanced_stats_team_goal_games': [],
            'team_advanced_stats_scoring_first': []
        }

        teams = self.fetch_entities()
        for team in teams:
            
            for days_rest in team.team_advanced_stats_days_rest:
                if self.entity_exists(days_rest, 'team_advanced_stats_days_rest'):
                    query = self.create_update_query('team_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'team_advanced_stats_days_rest')
                    batch_update['team_advanced_stats_days_rest'].append(params[3:] + (params[0], params[1], params[2]))
                    #self.database_operator.write(query, params[3:] + (params[0], params[1], params[2]))
                else:
                    print("Inserting days rest")
                    query = self.create_insert_query('team_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'team_advanced_stats_days_rest')
                    batch_insert['team_advanced_stats_days_rest'].append(params)
                    #self.database_operator.write(query, params)

            for corsi_fenwick in team.team_advanced_stats_corsi_fenwick:
                if self.entity_exists(corsi_fenwick, 'team_advanced_stats_corsi_fenwick'):
                    query = self.create_update_query('team_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'team_advanced_stats_corsi_fenwick')
                    batch_update['team_advanced_stats_corsi_fenwick'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'team_advanced_stats_corsi_fenwick')
                    batch_insert['team_advanced_stats_corsi_fenwick'].append(params)
                    #self.database_operator.write(query, params)

            for faceoff_percent in team.team_advanced_stats_faceoff_percent:
                if self.entity_exists(faceoff_percent, 'team_advanced_stats_faceoff_percent'):
                    query = self.create_update_query('team_advanced_stats_faceoff_percent')
                    params = self.to_database_params(faceoff_percent, 'team_advanced_stats_faceoff_percent')
                    batch_update['team_advanced_stats_faceoff_percent'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_faceoff_percent')
                    params = self.to_database_params(faceoff_percent, 'team_advanced_stats_faceoff_percent')
                    batch_insert['team_advanced_stats_faceoff_percent'].append(params)
                    #self.database_operator.write(query, params)

            for shot_type in team.team_advanced_stats_shot_type:
                if self.entity_exists(shot_type, 'team_advanced_stats_shot_type'):
                    query = self.create_update_query('team_advanced_stats_shot_type')
                    params = self.to_database_params(shot_type, 'team_advanced_stats_shot_type')
                    batch_update['team_advanced_stats_shot_type'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_shot_type')
                    params = self.to_database_params(shot_type, 'team_advanced_stats_shot_type')
                    batch_insert['team_advanced_stats_shot_type'].append(params)
                    #self.database_operator.write(query, params)
            
            for outshoot_outshot in team.team_advanced_stats_outshoot_outshot:
                if self.entity_exists(outshoot_outshot, 'team_advanced_stats_outshoot_outshot'):
                    query = self.create_update_query('team_advanced_stats_outshoot_outshot')
                    params = self.to_database_params(outshoot_outshot, 'team_advanced_stats_outshoot_outshot')
                    batch_update['team_advanced_stats_outshoot_outshot'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_outshoot_outshot')
                    params = self.to_database_params(outshoot_outshot, 'team_advanced_stats_outshoot_outshot')
                    batch_insert['team_advanced_stats_outshoot_outshot'].append(params)
                    #self.database_operator.write(query, params)

            for goals_by_period in team.team_advanced_stats_goals_by_period:
                if self.entity_exists(goals_by_period, 'team_advanced_stats_goals_by_period'):
                    query = self.create_update_query('team_advanced_stats_goals_by_period')
                    params = self.to_database_params(goals_by_period, 'team_advanced_stats_goals_by_period')
                    batch_update['team_advanced_stats_goals_by_period'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_goals_by_period')
                    params = self.to_database_params(goals_by_period, 'team_advanced_stats_goals_by_period')
                    batch_insert['team_advanced_stats_goals_by_period'].append(params)
                    #self.database_operator.write(query, params)

            for goals_by_strength in team.team_advanced_stats_goals_by_strength:
                if self.entity_exists(goals_by_strength, 'team_advanced_stats_goals_by_strength'):
                    query = self.create_update_query('team_advanced_stats_goals_by_strength')
                    params = self.to_database_params(goals_by_strength, 'team_advanced_stats_goals_by_strength')
                    batch_update['team_advanced_stats_goals_by_strength'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_goals_by_strength')
                    params = self.to_database_params(goals_by_strength, 'team_advanced_stats_goals_by_strength')
                    batch_insert['team_advanced_stats_goals_by_strength'].append(params)
                    #self.database_operator.write(query, params)

            for leading_trailing in team.team_advanced_stats_leading_trailing:
                if self.entity_exists(leading_trailing, 'team_advanced_stats_leading_trailing'):
                    query = self.create_update_query('team_advanced_stats_leading_trailing')
                    params = self.to_database_params(leading_trailing, 'team_advanced_stats_leading_trailing')
                    batch_update['team_advanced_stats_leading_trailing'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_leading_trailing')
                    params = self.to_database_params(leading_trailing, 'team_advanced_stats_leading_trailing')
                    batch_insert['team_advanced_stats_leading_trailing'].append(params)
                    #self.database_operator.write(query, params)

            for misc in team.team_advanced_stats_misc:
                if self.entity_exists(misc, 'team_advanced_stats_misc'):
                    query = self.create_update_query('team_advanced_stats_misc')
                    params = self.to_database_params(misc, 'team_advanced_stats_misc')
                    batch_update['team_advanced_stats_misc'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_misc')
                    params = self.to_database_params(misc, 'team_advanced_stats_misc')
                    batch_insert['team_advanced_stats_misc'].append(params)
                    #self.database_operator.write(query, params)

            for penalties in team.team_advanced_stats_penalties:
                if self.entity_exists(penalties, 'team_advanced_stats_penalties'):
                    query = self.create_update_query('team_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'team_advanced_stats_penalties')
                    batch_update['team_advanced_stats_penalties'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'team_advanced_stats_penalties')
                    batch_insert['team_advanced_stats_penalties'].append(params)
                    #self.database_operator.write(query, params)

            for powerplay_penalty_kill in team.team_advanced_stats_powerplay_penalty_kill:
                if self.entity_exists(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill'):
                    query = self.create_update_query('team_advanced_stats_powerplay_penalty_kill')
                    params = self.to_database_params(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill')
                    batch_update['team_advanced_stats_powerplay_penalty_kill'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_powerplay_penalty_kill')
                    params = self.to_database_params(powerplay_penalty_kill, 'team_advanced_stats_powerplay_penalty_kill')
                    batch_insert['team_advanced_stats_powerplay_penalty_kill'].append(params)
                    #self.database_operator.write(query, params)

            for team_goal_games in team.team_advanced_stats_team_goal_games:
                if self.entity_exists(team_goal_games, 'team_advanced_stats_team_goal_games'):
                    query = self.create_update_query('team_advanced_stats_team_goal_games')
                    params = self.to_database_params(team_goal_games, 'team_advanced_stats_team_goal_games')
                    batch_update['team_advanced_stats_team_goal_games'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_team_goal_games')
                    params = self.to_database_params(team_goal_games, 'team_advanced_stats_team_goal_games')
                    batch_insert['team_advanced_stats_team_goal_games'].append(params)
                    #self.database_operator.write(query, params)

            for scoring_first in team.team_advanced_stats_scoring_first:
                if self.entity_exists(scoring_first, 'team_advanced_stats_scoring_first'):
                    query = self.create_update_query('team_advanced_stats_scoring_first')
                    params = self.to_database_params(scoring_first, 'team_advanced_stats_scoring_first')
                    batch_update['team_advanced_stats_scoring_first'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('team_advanced_stats_scoring_first')
                    params = self.to_database_params(scoring_first, 'team_advanced_stats_scoring_first')
                    batch_insert['team_advanced_stats_scoring_first'].append(params)
                    #self.database_operator.write(query, params)

        for key in batch_update:
            if batch_update[key]:
                query = self.create_update_query(key)
                try:
                    self.database_operator.batch_write(query, batch_update[key])
                except Exception as e:
                    print(e)
                    print("updating individually")
                    for params in batch_update[key]:
                        try:
                            self.database_operator.write(query, params)
                        except Exception as e:
                            print("Error updating, here is the query")
                            print(query)
                            print(params)
                            print(e)
                            continue


        for key in batch_insert:
            if batch_insert[key]:
                query = self.create_insert_query(key)
                try:
                    self.database_operator.batch_write(query, batch_insert[key])
                except Exception as e:
                    print(e)
                    print("inserting individually")
                    for params in batch_insert[key]:
                        try:
                            self.database_operator.write(query, params)
                        except Exception as e:
                            print("Error inserting, here is the query")
                            print(query)
                            print(params)
                            continue


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
        batch_updates = {
            "players": [],
            "player_details": [],
            "player_awards": [],
            "player_draft": []
        }

        batch_insert = {
            "players": [],
            "player_details": [],
            "player_awards": [],
            "player_draft": []
        }

        players = self.fetch_entities()
        for player in players:
            if self.entity_exists(player, 'players'):
                if player.team_id == None:
                    player.team_id = 0
                query = self.create_update_query('players')
                params = self.to_database_params(player, 'players')
                batch_updates['players'].append(params[1:] + (params[0],))
                #self.database_operator.write(query, params[1:] + (params[0],))
            else:
                query = self.create_insert_query('players')
                params = self.to_database_params(player, 'players')
                batch_insert['players'].append(params)
                #self.database_operator.write(query, params)

            # Update player details
            if self.entity_exists(player.player_details, 'player_details'):
                query = self.create_update_query('player_details')
                params = self.to_database_params(player.player_details, 'player_details')
                batch_updates['player_details'].append(params[1:] + (params[0],))
                #self.database_operator.write(query, params[1:] + (params[0],))
            else:
                query = self.create_insert_query('player_details')
                params = self.to_database_params(player.player_details, 'player_details')
                batch_insert['player_details'].append(params)
                #self.database_operator.write(query, params)

            # Update player awards
            for award in player.player_awards:
                if self.entity_exists(award, 'player_awards'):
                    query = self.create_update_query('player_awards')
                    params = self.to_database_params(award, 'player_awards')
                    batch_updates['player_awards'].append(params[2:] + (params[0], params[1], params[2]))
                    #self.database_operator.write(query, (params[2], params[0], params[1], params[2]))
                else:
                    print("Inserting awards")
                    query = self.create_insert_query('player_awards')
                    params = self.to_database_params(award, 'player_awards')
                    batch_insert['player_awards'].append(params)
                    #self.database_operator.write(query, params)
            
            # Update player draft
            if self.entity_exists(player.player_draft, 'player_draft'):
                query = self.create_update_query('player_draft')
                params = self.to_database_params(player.player_draft, 'player_draft')
                batch_updates['player_draft'].append(params[1:] + (params[0],))
                #self.database_operator.write(query, params[1:] + (params[0],))
            else:
                print("Inserting draft")
                query = self.create_insert_query('player_draft')
                params = self.to_database_params(player.player_draft, 'player_draft')
                batch_insert['player_draft'].append(params)
                #self.database_operator.write(query, params)

        for key in batch_updates:
            if batch_updates[key]:
                query = self.create_update_query(key)
                for i in range(0, len(batch_updates[key]), 1000):
                    chunk = batch_updates[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Updating chunk {i/1000} individually")
                        for params in batch_updates[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error updating, here is the query")
                                print(query)
                                print(params)
                                continue

        for key in batch_insert:
            if batch_insert[key]:
                query = self.create_insert_query(key)
                for i in range(0, len(batch_insert[key]), 1000):
                    chunk = batch_insert[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Inserting chunk {i/1000} individually")
                        for params in batch_insert[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error inserting, here is the query")
                                print(query)
                                print(params)
                                continue

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
        Fetches the data and updates the corresponding tables in the database in batches.
        """
        skaters = self.fetch_entities()

        # Partition the games into chunks for parallel processing
        num_cpu_cores = os.cpu_count()
        num_workers = num_cpu_cores + 2
        print(num_workers)
        chunk_size = len(skaters) // num_workers
        chunks = [skaters[i:i + chunk_size] for i in range(0, len(skaters), chunk_size)]


        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(self.process_chunk, chunk) for chunk in chunks]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Ensure any exceptions are raised

    def process_chunk(self, chunk):
        """
        Fetches the data and updates the corresponding tables in the database.
        """
        batch_insert = {
            'skater_stats': [],
            'skater_youth_stats': [],
            'skater_advanced_stats_corsi_fenwick': [],
            'skater_advanced_stats_faceoffs': [],
            'skater_advanced_stats_goals': [],
            'skater_advanced_stats_misc': [],
            'skater_advanced_stats_penalties': [],
            'skater_advanced_stats_penalty_kill': [],
            'skater_advanced_stats_powerplay': [],
            'skater_advanced_stats_scoring': [],
            'skater_advanced_stats_shootout': [],
            'skater_advanced_stats_toi': []
        }

        batch_update = {
            'skater_stats': [],
            'skater_youth_stats': [],
            'skater_advanced_stats_corsi_fenwick': [],
            'skater_advanced_stats_faceoffs': [],
            'skater_advanced_stats_goals': [],
            'skater_advanced_stats_misc': [],
            'skater_advanced_stats_penalties': [],
            'skater_advanced_stats_penalty_kill': [],
            'skater_advanced_stats_powerplay': [],
            'skater_advanced_stats_scoring': [],
            'skater_advanced_stats_shootout': [],
            'skater_advanced_stats_toi': []
        }

        for skater in skaters:
            for skater_stats in skater.skater_stats:
                if self.entity_exists(skater_stats, 'skater_stats'):
                    query = self.create_update_query('skater_stats')
                    params = self.to_database_params(skater_stats, 'skater_stats')
                    batch_update['skater_stats'].append(params[2:] + (params[0], params[1], params[2], params[18], params[19]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1], params[2], params[18], params[19]))
                else:
                    query = self.create_insert_query('skater_stats')
                    params = self.to_database_params(skater_stats, 'skater_stats')
                    batch_insert['skater_stats'].append(params)
                    #self.database_operator.write(query, params)

            for skater_youth_stats in skater.youth_stats:
                if self.entity_exists(skater_youth_stats, 'skater_youth_stats'):
                    query = self.create_update_query('skater_youth_stats')
                    params = self.to_database_params(skater_youth_stats, 'skater_youth_stats')
                    batch_update['skater_youth_stats'].append(params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                else:
                    query = self.create_insert_query('skater_youth_stats')
                    params = self.to_database_params(skater_youth_stats, 'skater_youth_stats')
                    batch_insert['skater_youth_stats'].append(params)
                    #self.database_operator.write(query, params)
            
            for corsi_fenwick in skater.advanced_stats_corsi_fenwick:
                if self.entity_exists(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick'):
                    query = self.create_update_query('skater_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick')
                    batch_update['skater_advanced_stats_corsi_fenwick'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_corsi_fenwick')
                    params = self.to_database_params(corsi_fenwick, 'skater_advanced_stats_corsi_fenwick')
                    batch_insert['skater_advanced_stats_corsi_fenwick'].append(params)
                    #self.database_operator.write(query, params)
            
            for faceoffs in skater.advanced_stats_faceoffs:
                if self.entity_exists(faceoffs, 'skater_advanced_stats_faceoffs'):
                    query = self.create_update_query('skater_advanced_stats_faceoffs')
                    params = self.to_database_params(faceoffs, 'skater_advanced_stats_faceoffs')
                    batch_update['skater_advanced_stats_faceoffs'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_faceoffs')
                    params = self.to_database_params(faceoffs, 'skater_advanced_stats_faceoffs')
                    batch_insert['skater_advanced_stats_faceoffs'].append(params)
                    #self.database_operator.write(query, params)
            
            for goals in skater.advanced_stats_goals:
                if self.entity_exists(goals, 'skater_advanced_stats_goals'):
                    query = self.create_update_query('skater_advanced_stats_goals')
                    params = self.to_database_params(goals, 'skater_advanced_stats_goals')
                    batch_update['skater_advanced_stats_goals'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_goals')
                    params = self.to_database_params(goals, 'skater_advanced_stats_goals')
                    batch_insert['skater_advanced_stats_goals'].append(params)
                    #self.database_operator.write(query, params)

            
            for misc in skater.advanced_stats_misc:
                if self.entity_exists(misc, 'skater_advanced_stats_misc'):
                    query = self.create_update_query('skater_advanced_stats_misc')
                    params = self.to_database_params(misc, 'skater_advanced_stats_misc')
                    batch_update['skater_advanced_stats_misc'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_misc')
                    params = self.to_database_params(misc, 'skater_advanced_stats_misc')
                    batch_insert['skater_advanced_stats_misc'].append(params)
                    #self.database_operator.write(query, params)

            for penalties in skater.advanced_stats_penalties:
                if self.entity_exists(penalties, 'skater_advanced_stats_penalties'):
                    query = self.create_update_query('skater_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'skater_advanced_stats_penalties')
                    batch_update['skater_advanced_stats_penalties'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_penalties')
                    params = self.to_database_params(penalties, 'skater_advanced_stats_penalties')
                    batch_insert['skater_advanced_stats_penalties'].append(params)
                    #self.database_operator.write(query, params)

            for penalty_kill in skater.advanced_stats_penalty_kill:
                if self.entity_exists(penalty_kill, 'skater_advanced_stats_penalty_kill'):
                    query = self.create_update_query('skater_advanced_stats_penalty_kill')
                    params = self.to_database_params(penalty_kill, 'skater_advanced_stats_penalty_kill')
                    batch_update['skater_advanced_stats_penalty_kill'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_penalty_kill')
                    params = self.to_database_params(penalty_kill, 'skater_advanced_stats_penalty_kill')
                    batch_insert['skater_advanced_stats_penalty_kill'].append(params)
                    #self.database_operator.write(query, params)

            for powerplay in skater.advanced_stats_powerplay:
                if self.entity_exists(powerplay, 'skater_advanced_stats_powerplay'):
                    query = self.create_update_query('skater_advanced_stats_powerplay')
                    params = self.to_database_params(powerplay, 'skater_advanced_stats_powerplay')
                    batch_update['skater_advanced_stats_powerplay'].append(params[2:] + (params[0], params[1], params[2]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1], params[2]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_powerplay')
                    params = self.to_database_params(powerplay, 'skater_advanced_stats_powerplay')
                    batch_insert['skater_advanced_stats_powerplay'].append(params)
                    #self.database_operator.write(query, params)

            for scoring in skater.advanced_stats_scoring:
                if self.entity_exists(scoring, 'skater_advanced_stats_scoring'):
                    query = self.create_update_query('skater_advanced_stats_scoring')
                    params = self.to_database_params(scoring, 'skater_advanced_stats_scoring')
                    batch_update['skater_advanced_stats_scoring'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_scoring')
                    params = self.to_database_params(scoring, 'skater_advanced_stats_scoring')
                    batch_insert['skater_advanced_stats_scoring'].append(params)
                    #self.database_operator.write(query, params)
            
            for shootout in skater.advanced_stats_shootout:
                if self.entity_exists(shootout, 'skater_advanced_stats_shootout'):
                    query = self.create_update_query('skater_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'skater_advanced_stats_shootout')
                    batch_update['skater_advanced_stats_shootout'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'skater_advanced_stats_shootout')
                    batch_insert['skater_advanced_stats_shootout'].append(params)
                    #self.database_operator.write(query, params)

            for toi in skater.advanced_stats_toi:
                if self.entity_exists(toi, 'skater_advanced_stats_toi'):
                    query = self.create_update_query('skater_advanced_stats_toi')
                    params = self.to_database_params(toi, 'skater_advanced_stats_toi')
                    batch_update['skater_advanced_stats_toi'].append(params[2:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('skater_advanced_stats_toi')
                    params = self.to_database_params(toi, 'skater_advanced_stats_toi')
                    batch_insert['skater_advanced_stats_toi'].append(params)
                    #self.database_operator.write(query, params)

        for key in batch_update:
            if batch_update[key]:
                query = self.create_update_query(key)
                for i in range(0, len(batch_update[key]), 1000):
                    chunk = batch_update[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Updating chunk {i/1000} individually")
                        for params in batch_update[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error updating, here is the query")
                                print(query)
                                print(params)
                                continue

        for key in batch_insert:
            if batch_insert[key]:
                query = self.create_insert_query(key)
                for i in range(0, len(batch_insert[key]), 1000):
                    chunk = batch_insert[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Inserting chunk {i/1000} individually")
                        for params in batch_insert[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error inserting, here is the query")
                                print(query)
                                print(params)
                                continue

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
        """
        Fetches the data and updates the corresponding tables in the database in batches.
        """
        games = self.fetch_entities()

        # Partition the games into chunks for parallel processing
        num_cpu_cores = os.cpu_count()
        num_workers = num_cpu_cores + 2
        print(num_workers)
        chunk_size = len(games) // num_workers
        chunks = [games[i:i + chunk_size] for i in range(0, len(games), chunk_size)]


        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(self.process_chunk, chunk) for chunk in chunks]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Ensure any exceptions are raised

    def process_chunk(self, chunk):

        batch_insert = {
            'goalie_stats': [],
            'goalie_youth_stats': [],
            'goalie_advanced_stats': [],
            'goalie_advanced_stats_days_rest': [],
            'goalie_advanced_stats_penalty_shots': [],
            'goalie_advanced_stats_saves_by_strength': [],
            'goalie_advanced_stats_shootout': [],
            'goalie_advanced_stats_start_relieved': []
        }

        batch_update = {
            'goalie_stats': [],
            'goalie_youth_stats': [],
            'goalie_advanced_stats': [],
            'goalie_advanced_stats_days_rest': [],
            'goalie_advanced_stats_penalty_shots': [],
            'goalie_advanced_stats_saves_by_strength': [],
            'goalie_advanced_stats_shootout': [],
            'goalie_advanced_stats_start_relieved': []
        }

        for goalie in chunk:
            for goalie_stats in goalie.goalie_stats:
                if self.entity_exists(goalie_stats, 'goalie_stats'):
                    query = self.create_update_query('goalie_stats')
                    params = self.to_database_params(goalie_stats, 'goalie_stats')
                    batch_update['goalie_stats'].append(params[2:] + (params[0], params[1], params[2], params[3], params[4]))
                    #self.database_operator.write(query, params[2:] + (params[0], params[1], params[2], params[3], params[4]))
                else:
                    query = self.create_insert_query('goalie_stats')
                    params = self.to_database_params(goalie_stats, 'goalie_stats')
                    batch_insert['goalie_stats'].append(params)
                    #self.database_operator.write(query, params)

            for goalie_youth_stats in goalie.goalie_youth_stats:
                if self.entity_exists(goalie_youth_stats, 'goalie_youth_stats'):
                    query = self.create_update_query('goalie_youth_stats')
                    params = self.to_database_params(goalie_youth_stats, 'goalie_youth_stats')
                    batch_update['goalie_youth_stats'].append(params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1], params[2], params[3], params[4], params[5]))
                else:
                    query = self.create_insert_query('goalie_youth_stats')
                    params = self.to_database_params(goalie_youth_stats, 'goalie_youth_stats')
                    batch_insert['goalie_youth_stats'].append(params)
                    #self.database_operator.write(query, params)
            
            for advanced_stats in goalie.goalie_advanced_stats:
                if self.entity_exists(advanced_stats, 'goalie_advanced_stats'):
                    query = self.create_update_query('goalie_advanced_stats')
                    params = self.to_database_params(advanced_stats, 'goalie_advanced_stats')
                    batch_update['goalie_advanced_stats'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats')
                    params = self.to_database_params(advanced_stats, 'goalie_advanced_stats')
                    batch_insert['goalie_advanced_stats'].append(params)
                    #self.database_operator.write(query, params)
            
            for days_rest in goalie.goalie_advanced_stats_days_rest:
                if self.entity_exists(days_rest, 'goalie_advanced_stats_days_rest'):
                    query = self.create_update_query('goalie_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'goalie_advanced_stats_days_rest')
                    batch_update['goalie_advanced_stats_days_rest'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_days_rest')
                    params = self.to_database_params(days_rest, 'goalie_advanced_stats_days_rest')
                    batch_insert['goalie_advanced_stats_days_rest'].append(params)
                    #self.database_operator.write(query, params)

            for penalty_shots in goalie.goalie_advanced_stats_penalty_shots:
                if self.entity_exists(penalty_shots, 'goalie_advanced_stats_penalty_shots'):
                    query = self.create_update_query('goalie_advanced_stats_penalty_shots')
                    params = self.to_database_params(penalty_shots, 'goalie_advanced_stats_penalty_shots')
                    batch_update['goalie_advanced_stats_penalty_shots'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_penalty_shots')
                    params = self.to_database_params(penalty_shots, 'goalie_advanced_stats_penalty_shots')
                    batch_insert['goalie_advanced_stats_penalty_shots'].append(params)
                    #self.database_operator.write(query, params)

            for saves_by_strength in goalie.goalie_advanced_stats_saves_by_strength:
                if self.entity_exists(saves_by_strength, 'goalie_advanced_stats_saves_by_strength'):
                    query = self.create_update_query('goalie_advanced_stats_saves_by_strength')
                    params = self.to_database_params(saves_by_strength, 'goalie_advanced_stats_saves_by_strength')
                    batch_update['goalie_advanced_stats_saves_by_strength'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_saves_by_strength')
                    params = self.to_database_params(saves_by_strength, 'goalie_advanced_stats_saves_by_strength')
                    batch_insert['goalie_advanced_stats_saves_by_strength'].append(params)
                    #self.database_operator.write(query, params)

            for shootout in goalie.goalie_advanced_stats_shootout:
                if self.entity_exists(shootout, 'goalie_advanced_stats_shootout'):
                    query = self.create_update_query('goalie_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'goalie_advanced_stats_shootout')
                    batch_update['goalie_advanced_stats_shootout'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_shootout')
                    params = self.to_database_params(shootout, 'goalie_advanced_stats_shootout')
                    batch_insert['goalie_advanced_stats_shootout'].append(params)
                    #self.database_operator.write(query, params)

            for start_relieved in goalie.goalie_advanced_stats_start_relieved:
                if self.entity_exists(start_relieved, 'goalie_advanced_stats_start_relieved'):
                    query = self.create_update_query('goalie_advanced_stats_start_relieved')
                    params = self.to_database_params(start_relieved, 'goalie_advanced_stats_start_relieved')
                    batch_update['goalie_advanced_stats_start_relieved'].append(params[1:] + (params[0], params[1]))
                    #self.database_operator.write(query, params[1:] + (params[0], params[1]))
                else:
                    query = self.create_insert_query('goalie_advanced_stats_start_relieved')
                    params = self.to_database_params(start_relieved, 'goalie_advanced_stats_start_relieved')
                    batch_insert['goalie_advanced_stats_start_relieved'].append(params)
                    #self.database_operator.write(query, params)

        for key in batch_update:
            if batch_update[key]:
                query = self.create_update_query(key)
                for i in range(0, len(batch_update[key]), 1000):
                    chunk = batch_update[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Updating chunk {i/1000} individually")
                        for params in batch_update[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error updating, here is the query")
                                print(query)
                                print(params)
                                continue

        for key in batch_insert:
            if batch_insert[key]:
                query = self.create_insert_query(key)
                for i in range(0, len(batch_insert[key]), 1000):
                    chunk = batch_insert[key][i:i+1000]
                    try:
                        self.database_operator.batch_write(query, chunk)
                    except Exception as e:
                        print(e)
                        print(f"Inserting chunk {i/1000} individually")
                        for params in batch_insert[key]:
                            try:
                                self.database_operator.write(query, params)
                            except Exception as e:
                                print("Error inserting, here is the query")
                                print(query)
                                print(params)
                                continue

class UpdateGames(AbstractUpdater):
    """
    A class to update the player details and team stats tables in the database.
    """

    def __init__(self, database_operator: DatabaseOperator, fetch_games: FetchGames):
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
        self.fetch_games = fetch_games

    def fetch_entities(self):
        """
        Fetches the players to be updated.
        
        Returns:
            list: A list of Player objects to be updated.
        """
        return self.fetch_games.get_data()
    
    def entity_exists(self, entity, table: str) -> bool:
        if table == 'games':
            query = GamesDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id,))
        elif table == 'game_three_stars':
            query = GameThreeStarsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id,))
        elif table == 'game_skater_stats':
            query = GameSkaterStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id, entity.player_id))
        elif table == 'game_goalie_stats':
            query = GameGoalieStatsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id, entity.player_id))
        elif table == 'game_roster':
            query = GameRosterDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id, entity.team_id, entity.player_id))
        elif table == 'referees':
            query = RefereesDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id,))
        elif table == 'game_scoreboard':
            query = GameScoreboardDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id,))
        elif table == 'game_boxscore':
            query = GameBoxscoreDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id,))
        elif table == 'game_plays':
            query = GamePlaysDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id, entity.event_id))
        elif table == 'shift_data':
            query = ShiftDataDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.shift_id,))
        elif table == "game_goals":
            query = GameGoalsDatabaseMapper.create_check_existence_query()
            result = self.database_operator.read(query, (entity.game_id, entity.away_score, entity.home_score))

        return bool(result)
        
    def create_insert_query(self, table: str) -> str:
        if table == 'games':
            return GamesDatabaseMapper.create_insert_query()
        elif table == 'game_three_stars':
            return GameThreeStarsDatabaseMapper.create_insert_query()
        elif table == 'game_skater_stats':
            return GameSkaterStatsDatabaseMapper.create_insert_query()
        elif table == 'game_goalie_stats':
            return GameGoalieStatsDatabaseMapper.create_insert_query()
        elif table == 'game_roster':
            return GameRosterDatabaseMapper.create_insert_query()
        elif table == 'referees':
            return RefereesDatabaseMapper.create_insert_query()
        elif table == 'game_scoreboard':
            return GameScoreboardDatabaseMapper.create_insert_query()
        elif table == 'game_boxscore':
            return GameBoxscoreDatabaseMapper.create_insert_query()
        elif table == 'game_plays':
            return GamePlaysDatabaseMapper.create_insert_query()
        elif table == 'shift_data':
            return ShiftDataDatabaseMapper.create_insert_query()
        elif table == "game_goals":
            return GameGoalsDatabaseMapper.create_insert_query()
   
    def create_update_query(self, table: str) -> str:
        if table == 'games':
            return GamesDatabaseMapper.create_update_query()
        elif table == 'game_three_stars':
            return GameThreeStarsDatabaseMapper.create_update_query()
        elif table == 'game_skater_stats':
            return GameSkaterStatsDatabaseMapper.create_update_query()
        elif table == 'game_goalie_stats':
            return GameGoalieStatsDatabaseMapper.create_update_query()
        elif table == 'game_roster':
            return GameRosterDatabaseMapper.create_update_query()
        elif table == 'referees':
            return RefereesDatabaseMapper.create_update_query()
        elif table == 'game_scoreboard':
            return GameScoreboardDatabaseMapper.create_update_query()
        elif table == 'game_boxscore':
            return GameBoxscoreDatabaseMapper.create_update_query()
        elif table == 'game_plays':
            return GamePlaysDatabaseMapper.create_update_query()
        elif table == 'shift_data':
            return ShiftDataDatabaseMapper.create_update_query()
        elif table == "game_goals":
            return GameGoalsDatabaseMapper.create_update_query()
        
    def to_database_params(self, entity, table: str) -> tuple:
        if table == 'games':
            return GamesDatabaseMapper.to_database_params(entity)
        elif table == 'game_three_stars':
            return GameThreeStarsDatabaseMapper.to_database_params(entity)
        elif table == 'game_skater_stats':
            return GameSkaterStatsDatabaseMapper.to_database_params(entity)
        elif table == 'game_goalie_stats':
            return GameGoalieStatsDatabaseMapper.to_database_params(entity)
        elif table == 'game_roster':
            return GameRosterDatabaseMapper.to_database_params(entity)
        elif table == 'referees':
            return RefereesDatabaseMapper.to_database_params(entity)
        elif table == 'game_scoreboard':
            return GameScoreboardDatabaseMapper.to_database_params(entity)
        elif table == 'game_boxscore':
            return GameBoxscoreDatabaseMapper.to_database_params(entity)
        elif table == 'game_plays':
            return GamePlaysDatabaseMapper.to_database_params(entity)
        elif table == 'shift_data':
            return ShiftDataDatabaseMapper.to_database_params(entity)
        elif table == "game_goals":
            return GameGoalsDatabaseMapper.to_database_params(entity)
        
    def update_in_db(self):
        """
        Fetches the data and updates the corresponding tables in the database in batches.
        """
        games = self.fetch_entities()

        # Partition the games into chunks for parallel processing
        num_cpu_cores = os.cpu_count()
        num_workers = 1
        print(num_workers)
        chunk_size = len(games) // num_workers
        chunks = [games[i:i + chunk_size] for i in range(0, len(games), chunk_size)]


        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(self.process_chunk, chunk) for chunk in chunks]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Ensure any exceptions are raised

    def process_chunk(self, games_chunk):
            batch_insert = {
                'games': [],
                'game_three_stars': [],
                'game_skater_stats': [],
                'game_goalie_stats': [],
                'game_roster': [],
                'referees': [],
                'game_scoreboard': [],
                'game_boxscore': [],
                'game_plays': [],
                'shift_data': [],
                'game_goals': []
            }

            batch_update = {
                'games': [],
                'game_three_stars': [],
                'game_skater_stats': [],
                'game_goalie_stats': [],
                'game_roster': [],
                'referees': [],
                'game_scoreboard': [],
                'game_boxscore': [],
                'game_plays': [],
                'shift_data': [],
                'game_goals': []
            }

            for game in games_chunk:
                query = self.create_insert_query('games')
                params = self.to_database_params(game, 'games')
                batch_insert['games'].append(params)
                """if self.entity_exists(game, 'games'):
                    query = self.create_update_query('games')
                    params = self.to_database_params(game, 'games')
                    batch_update['games'].append(params[2:] + (params[0],))
                else:
                    query = self.create_insert_query('games')
                    params = self.to_database_params(game, 'games')
                    batch_insert['games'].append(params)"""
                
                params = self.to_database_params(game.game_three_stars, 'game_three_stars')
                batch_insert['game_three_stars'].append(params)

                """if self.entity_exists(game, 'game_three_stars'):
                    query = self.create_update_query('game_three_stars')
                    params = self.to_database_params(game.game_three_stars, 'game_three_stars')
                    batch_update['game_three_stars'].append(params[1:] + (params[0],))
                else:
                    query = self.create_insert_query('game_three_stars')
                    params = self.to_database_params(game.game_three_stars, 'game_three_stars')
                    batch_insert['game_three_stars'].append(params)"""

                for skater_stat in game.game_skater_stats:
                    query = GameSkaterStatsDatabaseMapper.create_insert_query()
                    params = GameSkaterStatsDatabaseMapper.to_database_params(skater_stat)
                    batch_insert['game_skater_stats'].append(params)
                    """if self.entity_exists(skater_stat, 'game_skater_stats'):
                        query = GameSkaterStatsDatabaseMapper.create_update_query()
                        params = GameSkaterStatsDatabaseMapper.to_database_params(skater_stat)
                        batch_update['game_skater_stats'].append(params[3:] + (params[0], params[1]))
                    else:
                        query = GameSkaterStatsDatabaseMapper.create_insert_query()
                        params = GameSkaterStatsDatabaseMapper.to_database_params(skater_stat)
                        batch_insert['game_skater_stats'].append(params)"""

                for goalie_stat in game.game_goalie_stats:
                    query = GameGoalieStatsDatabaseMapper.create_insert_query()
                    params = GameGoalieStatsDatabaseMapper.to_database_params(goalie_stat)
                    batch_insert['game_goalie_stats'].append(params)

                    """if self.entity_exists(goalie_stat, 'game_goalie_stats'):
                        query = GameGoalieStatsDatabaseMapper.create_update_query()
                        params = GameGoalieStatsDatabaseMapper.to_database_params(goalie_stat)
                        batch_update['game_goalie_stats'].append(params[3:] + (params[0], params[1]))
                    else:
                        query = GameGoalieStatsDatabaseMapper.create_insert_query()
                        params = GameGoalieStatsDatabaseMapper.to_database_params(goalie_stat)
                        batch_insert['game_goalie_stats'].append(params)"""

                for roster_spot in game.game_roster:
                    query = GameRosterDatabaseMapper.create_insert_query()
                    params = GameRosterDatabaseMapper.to_database_params(roster_spot)
                    batch_insert['game_roster'].append(params)
                    """if self.entity_exists(roster_spot, 'game_roster'):
                        query = GameRosterDatabaseMapper.create_update_query()
                        params = GameRosterDatabaseMapper.to_database_params(roster_spot)
                        batch_update['game_roster'].append(params[3:] + (params[0], params[1], params[2]))
                    else:
                        query = GameRosterDatabaseMapper.create_insert_query()
                        params = GameRosterDatabaseMapper.to_database_params(roster_spot)
                        batch_insert['game_roster'].append(params)"""

                ref_obj = game.game_referees
                query = RefereesDatabaseMapper.create_insert_query()
                params = RefereesDatabaseMapper.to_database_params(ref_obj)
                batch_insert['referees'].append(params)
                """if self.entity_exists(ref_obj, 'referees'):
                    query = RefereesDatabaseMapper.create_update_query()
                    params = RefereesDatabaseMapper.to_database_params(ref_obj)
                    batch_update['referees'].append(params[1:] + (params[0],))
                else:
                    query = RefereesDatabaseMapper.create_insert_query()
                    params = RefereesDatabaseMapper.to_database_params(ref_obj)
                    batch_insert['referees'].append(params)"""

                scoreboard_obj = game.game_scoreboard
                query = GameScoreboardDatabaseMapper.create_insert_query()
                params = GameScoreboardDatabaseMapper.to_database_params(scoreboard_obj)
                batch_insert['game_scoreboard'].append(params)
                """if self.entity_exists(scoreboard_obj, 'game_scoreboard'):
                    query = GameScoreboardDatabaseMapper.create_update_query()
                    params = GameScoreboardDatabaseMapper.to_database_params(scoreboard_obj)
                    batch_update['game_scoreboard'].append(params[1:] + (params[0],))
                else:
                    query = GameScoreboardDatabaseMapper.create_insert_query()
                    params = GameScoreboardDatabaseMapper.to_database_params(scoreboard_obj)
                    batch_insert['game_scoreboard'].append(params)"""

                boxscore_obj = game.game_boxscore
                query = GameBoxscoreDatabaseMapper.create_insert_query()
                params = GameBoxscoreDatabaseMapper.to_database_params(boxscore_obj)
                batch_insert['game_boxscore'].append(params)
                """if self.entity_exists(boxscore_obj, 'game_boxscore'):
                    query = GameBoxscoreDatabaseMapper.create_update_query()
                    params = GameBoxscoreDatabaseMapper.to_database_params(boxscore_obj)
                    batch_update['game_boxscore'].append(params[1:] + (params[0],))
                else:
                    query = GameBoxscoreDatabaseMapper.create_insert_query()
                    params = GameBoxscoreDatabaseMapper.to_database_params(boxscore_obj)
                    batch_insert['game_boxscore'].append(params)"""

                for play in game.game_plays:
                    query = GamePlaysDatabaseMapper.create_insert_query()
                    params = GamePlaysDatabaseMapper.to_database_params(play)
                    batch_insert['game_plays'].append(params)
                    """if self.entity_exists(play, 'game_plays'):
                        query = GamePlaysDatabaseMapper.create_update_query()
                        params = GamePlaysDatabaseMapper.to_database_params(play)
                        batch_update['game_plays'].append(params[2:] + (params[0], params[1]))
                    else:
                        query = GamePlaysDatabaseMapper.create_insert_query()
                        params = GamePlaysDatabaseMapper.to_database_params(play)
                        batch_insert['game_plays'].append(params)"""

                for shift in game.game_shifts:
                    query = ShiftDataDatabaseMapper.create_insert_query()
                    params = ShiftDataDatabaseMapper.to_database_params(shift)
                    batch_insert['shift_data'].append(params)
                    """if self.entity_exists(shift, 'shift_data'):
                        query = ShiftDataDatabaseMapper.create_update_query()
                        params = ShiftDataDatabaseMapper.to_database_params(shift)
                        batch_update['shift_data'].append(params[2:] + (params[0],))
                    else:
                        query = ShiftDataDatabaseMapper.create_insert_query()
                        params = ShiftDataDatabaseMapper.to_database_params(shift)
                        batch_insert['shift_data'].append(params)"""

                for goal in game.game_goals:
                    query = GameGoalsDatabaseMapper.create_insert_query()
                    params = GameGoalsDatabaseMapper.to_database_params(goal)
                    batch_insert['game_goals'].append(params)
                    """if self.entity_exists(goal, 'game_goals'):
                        query = GameGoalsDatabaseMapper.create_update_query()
                        params = GameGoalsDatabaseMapper.to_database_params(goal)
                        batch_update['game_goals'].append(params[1:] + (params[0], params[7], params[8]))
                    else:
                        query = GameGoalsDatabaseMapper.create_insert_query()
                        params = GameGoalsDatabaseMapper.to_database_params(goal)
                        batch_insert['game_goals'].append(params)"""
                    
            


            # Insert and update in batches
            for key in batch_update:
                if batch_update[key]:
                    query = self.create_update_query(key)
                    for i in range(0, len(batch_update[key]), 100):
                        chunk = batch_update[key][i:i+100]
                        try:
                            self.database_operator.batch_write(query, chunk)
                        except Exception as e:
                            print(e)
                            print(f"Updating chunk {i // 100} individually")
                            for params in chunk:
                                try:
                                    self.database_operator.write(query, params)
                                except Exception as e:
                                    print("Error updating, here is the query")
                                    print(query)
                                    print(params)
                                    continue

            for key in batch_insert:
                if batch_insert[key]:
                    query = self.create_insert_query(key)
                    for i in range(0, len(batch_insert[key]), 100):
                        chunk = batch_insert[key][i:i+100]
                        try:
                            self.database_operator.batch_write(query, chunk)
                        except Exception as e:
                            print(e)
                            print(f"Inserting chunk {i // 100} individually")
                            for params in chunk:
                                try:
                                    self.database_operator.write(query, params)
                                except Exception as e:
                                    print("Error inserting, here is the query")
                                    print(query)
                                    print(params)
                                    continue