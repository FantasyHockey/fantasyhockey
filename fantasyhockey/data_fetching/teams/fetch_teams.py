from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.teams.models.team import Team
from fantasyhockey.data_fetching.teams.models.team_data import TeamData
from fantasyhockey.data_fetching.teams.models.team_stats import TeamStats
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_days_rest import TeamAdvancedStatsDaysRest
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_corsi_fenwick import TeamAdvancedStatsCorsiFenwick
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_shot_type import TeamAdvancedStatsShotType
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_outshoot_outshot import TeamAdvancedStatsOutshootOutshot
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_faceoff_percent import TeamAdvancedStatsFaceoffPercent
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_goals_by_period import TeamAdvancedStatsGoalsByPeriod
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_goals_by_strength import TeamAdvancedStatsGoalsByStrength
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_leading_trailing import TeamAdvancedStatsLeadingTrailing
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_misc import TeamAdvancedStatsMisc
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_penalties import TeamAdvancedStatsPenalties
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_powerplay_penalty_kill import TeamAdvancedStatsPowerplayPenaltyKill
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_scoring_first import TeamAdvancedStatsScoringFirst
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_team_goal_games import TeamAdvancedStatsTeamGoalGames

from fantasyhockey.util.util import obsolete

from fantasyhockey.util.data_parser import DataParser

# TODO: The classes are messed up. The team details and stats are retrieved year by year, but should be retreived all at once the same structure as the advanced stats.

class FetchTeams:
    """
    A class that fetches and stores NHL team data.
    
    Attributes:
        api_connector (APIConnector): An instance of the APIConnector class for making API requests.
        teams (list): A list to store the fetched Team objects.
        __TEAM_URL (str): The URL for fetching team standings data.
        __ROSTER_SEASON_URL (str): The URL for fetching roster season data.
        __TEAM_ID_URL (str): The URL for fetching team ID data.
        team_id_lookup (dict): A dictionary to store the team ID lookup data.
    """
    
    def __init__(self):
        self.api_connector = APIConnector()
        self.data_parser = DataParser()
        self.teams = []
        self.__TEAM_URL = "https://api-web.nhle.com/v1/standings/"
        self.__ROSTER_SEASON_URL = "https://api-web.nhle.com/v1/roster-season/mtl"
        self.__TEAM_ID_URL = "https://api.nhle.com/stats/rest/en/team"

        self.team_id_lookup = None    

    def get_teams(self):
        """
        Fetches and returns the list of Team objects.
        
        If the teams list is empty, it calls the __fetch() method to fetch the data.
        
        Returns:
            list: A list of Team objects.
        """
        if not self.teams:
            self.__fetch()
        return self.teams
    
    def __get_team_id_lookup(self):
        """
        Fetches and stores the team ID lookup data.
        """
        data = self.api_connector.get_json(self.__TEAM_ID_URL)

        self.team_id_lookup = data["data"]

    def __fetch(self):
        """
        Fetches team data for each year and creates Team objects.
        """
        self.__get_team_id_lookup()

        '''year_data = self.api_connector.get_json(self.__ROSTER_SEASON_URL)
        for year in year_data:
            self.__fetch_year_data(year)'''
        
        self.teams = [Team(1)]

        self.__parse_team_advanced_stats()

    def __parse_team_advanced_stats(self):
        for team in self.teams:
            team_id = team.get_team_id()
            team.set_team_advanced_stats_days_rest(self.__get_team_advanced_stats_days_rest(team_id))
            '''team.set_team_advanced_stats_corsi_fenwick(self.__get_team_advanced_stats_corsi_fenwick(team_id))
            team.set_team_advanced_stats_shot_type(self.__get_team_advanced_stats_shot_type(team_id))
            team.set_team_advanced_stats_outshoot_outshot(self.__get_team_advanced_stats_outshoot_outshot(team_id))
            team.set_team_advanced_stats_faceoff_percent(self.__get_team_advanced_stats_faceoff_percent(team_id))
            team.set_team_advanced_stats_goals_by_period(self.__get_team_advanced_stats_goals_by_period(team_id))
            team.set_team_advanced_stats_goals_by_strength(self.__get_team_advanced_stats_goals_by_strength(team_id))
            team.set_team_advanced_stats_leading_trailing(self.__get_team_advanced_stats_leading_trailing(team_id))
            team.set_team_advanced_stats_misc(self.__get_team_advanced_stats_misc(team_id))
            team.set_team_advanced_stats_penalties(self.__get_team_advanced_stats_penalties(team_id))
            team.set_team_advanced_stats_powerplay_penalty_kill(self.__get_team_advanced_stats_powerplay_penalty_kill(team_id))
            team.set_team_advanced_stats_scoring_first(self.__get_team_advanced_stats_scoring_first(team_id))
            team.set_team_advanced_stats_team_goal_games(self.__get_team_advanced_stats_team_goal_games(team_id))'''

    def __fetch_year_data(self, year):
        """
        Fetches team data for a specific year and creates a Team object for each team.
        Args:
            year (int): The year for which to fetch the team data.
        """
        data = self.api_connector.get_json(self.__TEAM_URL + str(year)[4:] + "-04-18")
        for team_json in data["standings"]:
            team_abbrev = self.data_parser.double_parse(team_json, "teamAbbrev", "default", "none")
            
            team_id = self.__find_team_id(team_abbrev)
            team = Team(team_id)
            #team.set_team_data(self.__parse_team_details(team_id, year, team_abbrev, team_json))
            #team.set_team_stats(self.__parse_team_stats(team_json, team_id, year))

            for added_teams in self.teams:
                if added_teams.get_team_id() != team.get_team_id():
                    self.teams.append(team)
            
    def __fetch_team_data(self, year):
        pass

    def __parse_team_details(self, team_id, year, team_abbrev, team_json) -> TeamData:
        """
        Parses and returns the team details from the team JSON data.
        
        Args:
            team_id (int): The ID of the team.
            year (int): The year for which the team data is being parsed.
            team_abbrev (str): The team abbreviation.
            team_json (dict): The JSON data for the team.
        
        Returns:
            TeamData: An instance of the TeamData class containing the parsed team details.
        """
        team_data = TeamData(team_id)
        team_data.set_year(year)
        team_data.set_conference_name(self.data_parser.parse(team_json, "conferenceName", "none"))
        team_data.set_division_name(self.data_parser.parse(team_json, "divisionName", "none"))
        team_data.set_location_name(self.data_parser.double_parse(team_json, "placeName", "default", "none"))
        team_data.set_team_name(self.data_parser.double_parse(team_json, "teamName", "default", "none"))
        team_data.set_team_abbreviation(team_abbrev)
        team_data.set_team_logo(self.data_parser.parse(team_json, "teamLogo", "none"))
        team_data.set_team_color_1(self.__get_team_colors(team_abbrev)["primary_color"])
        team_data.set_team_color_2(self.__get_team_colors(team_abbrev)["secondary_color"])
        return team_data

    def __parse_team_stats(self, team_json, team_id, year) -> TeamStats:
        """
        Parses and returns the team stats from the team JSON data.
        
        Args:
            team_json (dict): The JSON data for the team.
            team_id (int): The ID of the team.
            year (int): The year for which the team data is being parsed.
        
        Returns:
            TeamStats: An instance of the TeamStats class containing the parsed team stats.
        """
        team_stats = TeamStats(team_id)
        team_stats.set_year(year)
        team_stats.set_game_type_id(self.data_parser.parse(team_json, "gameTypeId", "none"))
        team_stats.set_games_played(self.data_parser.parse(team_json, "gamesPlayed", "none"))
        team_stats.set_goals_against(self.data_parser.parse(team_json, "goalAgainst", "none"))
        team_stats.set_goals_for(self.data_parser.parse(team_json, "goalFor", "none"))
        team_stats.set_losses(self.data_parser.parse(team_json, "losses", "none"))
        team_stats.set_ot_losses(self.data_parser.parse(team_json, "otLosses", "none"))
        team_stats.set_points(self.data_parser.parse(team_json, "points", "none"))
        team_stats.set_shootout_losses(self.data_parser.parse(team_json, "shootoutLosses", "none"))
        team_stats.set_shootout_wins(self.data_parser.parse(team_json, "shootoutWins", "none"))
        team_stats.set_streak_code(self.data_parser.parse(team_json, "streakCode", "none"))
        team_stats.set_streak_count(self.data_parser.parse(team_json, "streakCount", "none"))
        team_stats.set_ties(self.data_parser.parse(team_json, "ties", "none"))
        team_stats.set_waiver_sequence(self.data_parser.parse(team_json, "waiversSequence", "none"))
        team_stats.set_regulation_wins(self.data_parser.parse(team_json, "regulationWins", "none"))
        team_stats.set_regulation_plus_ot_wins(self.data_parser.parse(team_json, "regulationPlusOtWins", "none"))
        team_stats.set_home_games_played(self.data_parser.parse(team_json, "homeGamesPlayed", "none"))
        team_stats.set_home_goals_against(self.data_parser.parse(team_json, "homeGoalsAgainst", "none"))
        team_stats.set_home_goals_for(self.data_parser.parse(team_json, "homeGoalsFor", "none"))
        team_stats.set_home_losses(self.data_parser.parse(team_json, "homeLosses", "none"))
        team_stats.set_home_ot_losses(self.data_parser.parse(team_json, "homeOtLosses", "none"))
        team_stats.set_home_points(self.data_parser.parse(team_json, "homePoints", "none"))
        team_stats.set_home_regulation_wins(self.data_parser.parse(team_json, "homeRegulationWins", "none"))
        team_stats.set_home_regulation_plus_ot_wins(self.data_parser.parse(team_json, "homeRegulationPlusOtWins", "none"))
        team_stats.set_home_ties(self.data_parser.parse(team_json, "homeTies", "none"))
        team_stats.set_home_wins(self.data_parser.parse(team_json, "homeWins", "none"))
        team_stats.set_last_10_games_played(self.data_parser.parse(team_json, "l10GamesPlayed", "none"))
        team_stats.set_last_10_goals_against(self.data_parser.parse(team_json, "l10GoalsAgainst", "none"))
        team_stats.set_last_10_goals_for(self.data_parser.parse(team_json, "l10GoalsFor", "none"))
        team_stats.set_last_10_losses(self.data_parser.parse(team_json, "l10Losses", "none"))
        team_stats.set_last_10_ot_losses(self.data_parser.parse(team_json, "l10OtLosses", "none"))
        team_stats.set_last_10_points(self.data_parser.parse(team_json, "l10Points", "none"))
        team_stats.set_last_10_regulation_wins(self.data_parser.parse(team_json, "l10RegulationWins"))
        team_stats.set_last_10_regulation_plus_ot_wins(self.data_parser.parse(team_json, "l10RegulationPlusOtWins", "none"))
        team_stats.set_last_10_ties(self.data_parser.parse(team_json, "l10Ties", "none"))
        team_stats.set_last_10_wins(self.data_parser.parse(team_json, "l10Wins", "none"))
        team_stats.set_road_games_played(self.data_parser.parse(team_json, "roadGamesPlayed", "none"))
        team_stats.set_road_goals_against(self.data_parser.parse(team_json, "roadGoalsAgainst", "none"))
        team_stats.set_road_goals_for(self.data_parser.parse(team_json, "roadGoalsFor", "none"))
        team_stats.set_road_losses(self.data_parser.parse(team_json, "roadLosses", "none"))
        team_stats.set_road_ot_losses(self.data_parser.parse(team_json, "roadOtLosses", "none"))
        team_stats.set_road_points(self.data_parser.parse(team_json, "roadPoints", "none"))
        team_stats.set_road_regulation_wins(self.data_parser.parse(team_json, "roadRegulationWins", "none"))
        team_stats.set_road_regulation_plus_ot_wins(self.data_parser.parse(team_json, "roadRegulationPlusOtWins", "none"))
        team_stats.set_road_ties(self.data_parser.parse(team_json, "roadTies", "none"))
        team_stats.set_road_wins(self.data_parser.parse(team_json, "roadWins", "none"))
        return team_stats

    def __get_team_advanced_stats_days_rest(self, team_id, start=0, stats=None) -> list[TeamAdvancedStatsDaysRest]:
        if stats is None:
            stats = []

        url = f"https://api.nhle.com/stats/rest/en/team/daysbetweengames?start={start}&cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        season_count = data["total"]
        for season in data["data"]:
            team_advanced_stats_days_rest = TeamAdvancedStatsDaysRest(team_id)
            team_advanced_stats_days_rest.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_days_rest.set_days_rest(self.data_parser.parse(season, "daysRest", "none"))
            team_advanced_stats_days_rest.set_games_played(self.data_parser.parse(season, "gamesPlayed", "none"))
            team_advanced_stats_days_rest.set_faceoff_percent(self.data_parser.parse(season, "faceoffWinPct", "none"))
            team_advanced_stats_days_rest.set_goals_against_per_game(self.data_parser.parse(season, "goalsAgainstPerGame", "none"))
            team_advanced_stats_days_rest.set_goals_for_per_game(self.data_parser.parse(season, "goalsForPerGame", "none"))
            team_advanced_stats_days_rest.set_losses(self.data_parser.parse(season, "losses", "none"))
            team_advanced_stats_days_rest.set_net_goals_per_game(self.data_parser.parse(season, "netGoalsPerGame", "none"))
            team_advanced_stats_days_rest.set_ot_losses(self.data_parser.parse(season, "otLosses", "none"))
            team_advanced_stats_days_rest.set_penalty_kill_percent(self.data_parser.parse(season, "penaltyKillPct", "none"))
            team_advanced_stats_days_rest.set_point_percent(self.data_parser.parse(season, "pointPct", "none"))
            team_advanced_stats_days_rest.set_points(self.data_parser.parse(season, "points", "none"))
            team_advanced_stats_days_rest.set_power_play_percent(self.data_parser.parse(season, "powerPlayPct", "none"))
            team_advanced_stats_days_rest.set_power_play_opportunities_per_game(self.data_parser.parse(season, "ppOpportunitiesPerGame", "none"))
            team_advanced_stats_days_rest.set_shot_differential_per_game(self.data_parser.parse(season, "shotDifferentialPerGame", "none"))
            team_advanced_stats_days_rest.set_shots_against_per_game(self.data_parser.parse(season, "shotsAgainstPerGame", "none"))
            team_advanced_stats_days_rest.set_shots_for_per_game(self.data_parser.parse(season, "shotsForPerGame", "none"))
            team_advanced_stats_days_rest.set_ties(self.data_parser.parse(season, "ties", "none"))
            team_advanced_stats_days_rest.set_times_shorthanded_per_game(self.data_parser.parse(season, "timesShorthandedPerGame", "none"))
            team_advanced_stats_days_rest.set_wins(self.data_parser.parse(season, "wins", "none"))

            stats.append(team_advanced_stats_days_rest)

        if start + len(data["data"]) < season_count:
            return self.__get_team_advanced_stats_days_rest(team_id, start + len(data["data"]), stats)
        else:
            return stats

    def __get_team_advanced_stats_corsi_fenwick(self, team_id) -> list[TeamAdvancedStatsCorsiFenwick]:
        url_counts = f"https://api.nhle.com/stats/rest/en/team/summaryshooting?cayenneExp=teamId={team_id}"
        url_percents = f"https://api.nhle.com/stats/rest/en/team/percentages?cayenneExp=teamId={team_id}"
        
        data_counts = self.api_connector.get_json(url_counts)
        data_percents = self.api_connector.get_json(url_percents)

        seasons = []

        for count_szn, percent_szn in zip(self.data_parser.parse(data_counts, "data", "empty_list"), self.data_parser.parse(data_percents, "data", "empty_list")):
            teamAdvancedStatsCorsiFenwick = TeamAdvancedStatsCorsiFenwick(team_id)
            year = self.data_parser.parse(count_szn, "seasonId", "none")
            teamAdvancedStatsCorsiFenwick.set_year(year)

            games_played = self.data_parser.parse(count_szn, "gamesPlayed", "none")
            teamAdvancedStatsCorsiFenwick.set_games_played(games_played)

            corsi_against = self.data_parser.parse(count_szn, "satAgainst", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_against(corsi_against)

            corsi_ahead = self.data_parser.parse(count_szn, "satAhead", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_ahead(corsi_ahead)

            corsi_behind = self.data_parser.parse(count_szn, "satBehind", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_behind(corsi_behind)

            corsi_close = self.data_parser.parse(count_szn, "satClose", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_close(corsi_close)

            corsi_for = self.data_parser.parse(count_szn, "satFor", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_for(corsi_for)

            corsi_tied = self.data_parser.parse(count_szn, "satTied", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_tied(corsi_tied)

            corsi_total = self.data_parser.parse(count_szn, "satTotal", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_total(corsi_total)

            corsi_relative = self.data_parser.parse(count_szn, "satRelative", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_relative(corsi_relative)

            fenwick_against = self.data_parser.parse(count_szn, "usatAgainst", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_against(fenwick_against)

            fenwick_ahead = self.data_parser.parse(count_szn, "usatAhead", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_ahead(fenwick_ahead)

            fenwick_behind = self.data_parser.parse(count_szn, "usatBehind", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_behind(fenwick_behind)

            fenwick_close = self.data_parser.parse(count_szn, "usatClose", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_close(fenwick_close)

            fenwick_for = self.data_parser.parse(count_szn, "usatFor", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_for(fenwick_for)

            fenwick_tied = self.data_parser.parse(count_szn, "usatTied", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_tied(fenwick_tied)

            fenwick_total = self.data_parser.parse(count_szn, "usatTotal", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_total(fenwick_total)

            fenwick_relative = self.data_parser.parse(count_szn, "usatRelative", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_relative(fenwick_relative)

            corsi_percentage = self.data_parser.parse(percent_szn, "satPercentage", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_percent(corsi_percentage)

            corsi_ahead_percentage = self.data_parser.parse(percent_szn, "satPercentageAhead", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_ahead_percent(corsi_ahead_percentage)

            corsi_behind_percentage = self.data_parser.parse(percent_szn, "satPercentageBehind", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_behind_percent(corsi_behind_percentage)

            corsi_close_percentage = self.data_parser.parse(percent_szn, "satPercentageClose", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_close_percent(corsi_close_percentage)

            corsi_tied_percentage = self.data_parser.parse(percent_szn, "satPercentageTied", "none")
            teamAdvancedStatsCorsiFenwick.set_corsi_tied_percent(corsi_tied_percentage)

            shooting_percent_5on5 = self.data_parser.parse(percent_szn, "shootingPct5v5", "none")
            teamAdvancedStatsCorsiFenwick.set_shooting_percent_5on5(shooting_percent_5on5)

            skater_save_percent_5on5 = self.data_parser.parse(percent_szn, "skaterSavePct5v5", "none")
            teamAdvancedStatsCorsiFenwick.set_save_percent_5on5(skater_save_percent_5on5)

            skater_shooting_plus_save_percent_5on5 = self.data_parser.parse(percent_szn, "skaterShootingPlusSavePct5v5", "none")
            teamAdvancedStatsCorsiFenwick.set_shooting_plus_save_percent_5on5(skater_shooting_plus_save_percent_5on5)

            fenwick_percentage = self.data_parser.parse(percent_szn, "usatPercentage", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_percent(fenwick_percentage)

            fenwick_ahead_percentage = self.data_parser.parse(percent_szn, "usatPercentageAhead", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_ahead_percent(fenwick_ahead_percentage)

            fenwick_behind_percentage = self.data_parser.parse(percent_szn, "usatPercentageBehind", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_behind_percent(fenwick_behind_percentage)

            fenwick_close_percentage = self.data_parser.parse(percent_szn, "usatPrecentageClose", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_close_percent(fenwick_close_percentage)

            fenwick_tied_percentage = self.data_parser.parse(percent_szn, "usatPercentageTied", "none")
            teamAdvancedStatsCorsiFenwick.set_fenwick_tied_percent(fenwick_tied_percentage)

            zone_start_percentage_offensive = self.data_parser.parse(percent_szn, "zoneStartPct5v5", "none")
            teamAdvancedStatsCorsiFenwick.set_zone_start_5on5_percent(zone_start_percentage_offensive)

            seasons.append(teamAdvancedStatsCorsiFenwick)

        return seasons

    def __get_team_advanced_stats_shot_type(self, team_id) -> TeamAdvancedStatsShotType:
        url = f"https://api.nhle.com/stats/rest/en/team/shottype?cayenneExp=teamId={team_id}"

        data = self.api_connector.get_json(url)
        stats = []

        for season in data["data"]:
            team_advanced_stats_shot_type = TeamAdvancedStatsShotType(team_id)
            team_advanced_stats_shot_type.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_shot_type.set_goals_backhand(self.data_parser.parse(season, "goalsBackhand", "none"))
            team_advanced_stats_shot_type.set_goals_deflected(self.data_parser.parse(season, "goalsDeflected", "none"))
            team_advanced_stats_shot_type.set_goals_for(self.data_parser.parse(season, "goalsFor", "none"))
            team_advanced_stats_shot_type.set_goals_slap(self.data_parser.parse(season, "goalsSlap", "none"))
            team_advanced_stats_shot_type.set_goals_snap(self.data_parser.parse(season, "goalsSnap", "none"))
            team_advanced_stats_shot_type.set_goals_tip_in(self.data_parser.parse(season, "goalsTipIn", "none"))
            team_advanced_stats_shot_type.set_goals_wrap_around(self.data_parser.parse(season, "goalsWrapAround", "none"))
            team_advanced_stats_shot_type.set_goals_wrist(self.data_parser.parse(season, "goalsWrist", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_backhand(self.data_parser.parse(season, "shootingPctBackhand", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_deflected(self.data_parser.parse(season, "shootingPctDeflected", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_slap(self.data_parser.parse(season, "shootingPctSlap", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_snap(self.data_parser.parse(season, "shootingPctSnap", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_tip_in(self.data_parser.parse(season, "shootingPctTipIn", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_wrap_around(self.data_parser.parse(season, "shootingPctWrapAround", "none"))
            team_advanced_stats_shot_type.set_shooting_percent_wrist(self.data_parser.parse(season, "shootingPctWrist", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_backhand(self.data_parser.parse(season, "shotsOnNetBackhand", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_deflected(self.data_parser.parse(season, "shotsOnNetDeflected", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_slap(self.data_parser.parse(season, "shotsOnNetSlap", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_snap(self.data_parser.parse(season, "shotsOnNetSnap", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_tip_in(self.data_parser.parse(season, "shotsOnNetTipIn", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_wrap_around(self.data_parser.parse(season, "shotsOnNetWrapAround", "none"))
            team_advanced_stats_shot_type.set_shots_on_net_wrist(self.data_parser.parse(season, "shotsOnNetWrist", "none"))
            stats.append(team_advanced_stats_shot_type)

        return stats

    def __get_team_advanced_stats_outshoot_outshot(self, team_id) -> TeamAdvancedStatsOutshootOutshot:
        url = f"https://api.nhle.com/stats/rest/en/team/outshootoutshotby?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)
        stats = []

        for season in data["data"]:
            team_advanced_stats_outshoot_outshot = TeamAdvancedStatsOutshootOutshot(team_id)
            team_advanced_stats_outshoot_outshot.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_outshoot_outshot.set_losses_even_shots(self.data_parser.parse(season, "lossesEvenShots", "none"))
            team_advanced_stats_outshoot_outshot.set_losses_outshoot(self.data_parser.parse(season, "lossesOutshootOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_losses_outshot(self.data_parser.parse(season, "lossesOutshotByOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_net_shots_per_game(self.data_parser.parse(season, "netShotsPerGame", "none"))
            team_advanced_stats_outshoot_outshot.set_ot_losses_even_shots(self.data_parser.parse(season, "otLossesEvenShots", "none"))
            team_advanced_stats_outshoot_outshot.set_ot_losses_outshoot(self.data_parser.parse(season, "otLossesOutshootOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_ot_losses_outshot(self.data_parser.parse(season, "otLossesOutshotByOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_shots_against_per_game(self.data_parser.parse(season, "shotsAgainstPerGame", "none"))
            team_advanced_stats_outshoot_outshot.set_shots_for_per_game(self.data_parser.parse(season, "shotsForPerGame", "none"))
            team_advanced_stats_outshoot_outshot.set_ties_even_shots(self.data_parser.parse(season, "tiesEvenShots", "none"))
            team_advanced_stats_outshoot_outshot.set_ties_outshoot(self.data_parser.parse(season, "tiesOutshootOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_ties_outshot(self.data_parser.parse(season, "tiesOutshotByOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_wins_even_shots(self.data_parser.parse(season, "winsEvenShots", "none"))
            team_advanced_stats_outshoot_outshot.set_wins_outshoot(self.data_parser.parse(season, "winsOutshootOpponent", "none"))
            team_advanced_stats_outshoot_outshot.set_wins_outshot(self.data_parser.parse(season, "winsOutshotByOpponent", "none"))
            stats.append(team_advanced_stats_outshoot_outshot)

        return stats

    def __get_team_advanced_stats_faceoff_percent(self, team_id) -> TeamAdvancedStatsFaceoffPercent:
        url = f"https://api.nhle.com/stats/rest/en/team/faceoffpercentages?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)
        stats = []

        for season in data["data"]:
            team_advanced_stats_faceoff_percent = TeamAdvancedStatsFaceoffPercent(team_id)
            team_advanced_stats_faceoff_percent.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_faceoff_percent.set_defensive_zone_faceoff_percent(self.data_parser.parse(season, "defensiveZoneFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_defensive_zone_faceoffs(self.data_parser.parse(season, "defensiveZoneFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_ev_faceoff_percent(self.data_parser.parse(season, "evFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_ev_faceoffs(self.data_parser.parse(season, "evFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_faceoff_win_percent(self.data_parser.parse(season, "faceoffWinPct", "none"))
            team_advanced_stats_faceoff_percent.set_neutral_zone_faceoff_percent(self.data_parser.parse(season, "neutralZoneFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_neutral_zone_faceoffs(self.data_parser.parse(season, "neutralZoneFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_offensive_zone_faceoff_percent(self.data_parser.parse(season, "offensiveZoneFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_offensive_zone_faceoffs(self.data_parser.parse(season, "offensiveZoneFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_pp_faceoff_percent(self.data_parser.parse(season, "ppFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_pp_faceoffs(self.data_parser.parse(season, "ppFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_pk_faceoff_percent(self.data_parser.parse(season, "shFaceoffPct", "none"))
            team_advanced_stats_faceoff_percent.set_pk_faceoffs(self.data_parser.parse(season, "shFaceoffs", "none"))
            team_advanced_stats_faceoff_percent.set_total_faceoffs(self.data_parser.parse(season, "totalFaceoffs", "none"))
            stats.append(team_advanced_stats_faceoff_percent)

        return stats
        
    def __get_team_advanced_stats_goals_by_period(self, team_id) -> TeamAdvancedStatsGoalsByPeriod:
        url = f"https://api.nhle.com/stats/rest/en/team/goalsbyperiod?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)
        stats = []

        for season in data["data"]:
            team_advanced_stats_goals_by_period = TeamAdvancedStatsGoalsByPeriod(team_id)
            team_advanced_stats_goals_by_period.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_goals_by_period.set_ev_goals_for(self.data_parser.parse(season, "evGoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_period_1_goals_against(self.data_parser.parse(season, "period1GoalsAgainst", "none"))
            team_advanced_stats_goals_by_period.set_period_1_goals_for(self.data_parser.parse(season, "period1GoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_period_2_goals_against(self.data_parser.parse(season, "period2GoalsAgainst", "none"))
            team_advanced_stats_goals_by_period.set_period_2_goals_for(self.data_parser.parse(season, "period2GoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_period_3_goals_against(self.data_parser.parse(season, "period3GoalsAgainst", "none"))
            team_advanced_stats_goals_by_period.set_period_3_goals_for(self.data_parser.parse(season, "period3GoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_period_ot_goals_against(self.data_parser.parse(season, "periodOtGoalsAgainst", "none"))
            team_advanced_stats_goals_by_period.set_period_ot_goals_for(self.data_parser.parse(season, "periodOtGoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_pp_goals_for(self.data_parser.parse(season, "ppGoalsFor", "none"))
            team_advanced_stats_goals_by_period.set_pk_goals_for(self.data_parser.parse(season, "shGoalsFor", "none"))
            stats.append(team_advanced_stats_goals_by_period)

        return stats

    def __get_team_advanced_stats_goals_by_strength(self, team_id) -> TeamAdvancedStatsGoalsByStrength:
        url = f"https://api.nhle.com/stats/rest/en/team/goalsforbystrength?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_goals_by_strength = TeamAdvancedStatsGoalsByStrength(team_id)
            team_advanced_stats_goals_by_strength.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_3on3(self.data_parser.parse(season, "goalsFor3on3", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_3on4(self.data_parser.parse(season, "goalsFor3on4", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_3on5(self.data_parser.parse(season, "goalsFor3on5", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_3on6(self.data_parser.parse(season, "goalsFor3on6", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_4on3(self.data_parser.parse(season, "goalsFor4on3", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_4on4(self.data_parser.parse(season, "goalsFor4on4", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_4on5(self.data_parser.parse(season, "goalsFor4on5", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_4on6(self.data_parser.parse(season, "goalsFor4on6", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_5on3(self.data_parser.parse(season, "goalsFor5on3", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_5on4(self.data_parser.parse(season, "goalsFor5on4", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_5on5(self.data_parser.parse(season, "goalsFor5on5", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_5on6(self.data_parser.parse(season, "goalsFor5on6", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_6on3(self.data_parser.parse(season, "goalsFor6on3", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_6on4(self.data_parser.parse(season, "goalsFor6on4", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_6on5(self.data_parser.parse(season, "goalsFor6on5", "none"))
            team_advanced_stats_goals_by_strength.set_goals_for_penalty_shots(self.data_parser.parse(season, "goalsForPenaltyShots", "none"))
            stats.append(team_advanced_stats_goals_by_strength)

        return stats

    def __get_team_advanced_stats_leading_trailing(self, team_id) -> TeamAdvancedStatsLeadingTrailing:
        url = f"https://api.nhle.com/stats/rest/en/team/leadingtrailing?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_leading_trailing = TeamAdvancedStatsLeadingTrailing(team_id)
            team_advanced_stats_leading_trailing.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_leading_trailing.set_loss_lead_period_1(self.data_parser.parse(season, "lossLeadPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_loss_lead_period_2(self.data_parser.parse(season, "lossLeadPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_loss_trail_period_1(self.data_parser.parse(season, "lossTrailPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_loss_trail_period_2(self.data_parser.parse(season, "lossTrailPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_ot_loss_lead_period_1(self.data_parser.parse(season, "otLossLeadPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_ot_loss_lead_period_2(self.data_parser.parse(season, "otLossLeadPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_ot_loss_trail_period_1(self.data_parser.parse(season, "otLossTrailPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_ot_loss_trail_period_2(self.data_parser.parse(season, "otLossTrailPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_period_1_goals_against(self.data_parser.parse(season, "period1GoalsAgainst", "none"))
            team_advanced_stats_leading_trailing.set_period_1_goals_for(self.data_parser.parse(season, "period1GoalsFor", "none"))
            team_advanced_stats_leading_trailing.set_period_2_goals_against(self.data_parser.parse(season, "period2GoalsAgainst", "none"))
            team_advanced_stats_leading_trailing.set_period_2_goals_for(self.data_parser.parse(season, "period2GoalsFor", "none"))
            team_advanced_stats_leading_trailing.set_ties_lead_period_1(self.data_parser.parse(season, "tiesLeadPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_ties_lead_period_2(self.data_parser.parse(season, "tiesLeadPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_ties_trail_period_1(self.data_parser.parse(season, "tiesTrailPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_ties_trail_period_2(self.data_parser.parse(season, "tiesTrailPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_win_percent_lead_period_1(self.data_parser.parse(season, "winPctLeadPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_win_percent_lead_period_2(self.data_parser.parse(season, "winPctLeadPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_win_percent_trail_period_1(self.data_parser.parse(season, "winPctTrailPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_win_percent_trail_period_2(self.data_parser.parse(season, "winPctTrailPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_wins_lead_period_1(self.data_parser.parse(season, "winsLeadPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_wins_lead_period_2(self.data_parser.parse(season, "winsLeadPeriod2", "none"))
            team_advanced_stats_leading_trailing.set_wins_trail_period_1(self.data_parser.parse(season, "winsTrailPeriod1", "none"))
            team_advanced_stats_leading_trailing.set_wins_trail_period_2(self.data_parser.parse(season, "winsTrailPeriod2", "none"))
            stats.append(team_advanced_stats_leading_trailing)

        return stats

    def __get_team_advanced_stats_misc(self, team_id) -> TeamAdvancedStatsMisc:
        url = f"https://api.nhle.com/stats/rest/en/team/realtime?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_misc = TeamAdvancedStatsMisc(team_id)
            team_advanced_stats_misc.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_misc.set_blocked_shots(self.data_parser.parse(season, "blockedShots", "none"))
            team_advanced_stats_misc.set_empty_net_goals(self.data_parser.parse(season, "emptyNetGoals", "none"))
            team_advanced_stats_misc.set_giveaways(self.data_parser.parse(season, "giveaways", "none"))
            team_advanced_stats_misc.set_hits(self.data_parser.parse(season, "hits", "none"))
            team_advanced_stats_misc.set_missed_shots(self.data_parser.parse(season, "missedShots", "none"))
            team_advanced_stats_misc.set_takeaways(self.data_parser.parse(season, "takeaways", "none"))
            team_advanced_stats_misc.set_time_on_ice_per_game_5on5(self.data_parser.parse(season, "timeOnIcePerGame5b5", "none"))
            stats.append(team_advanced_stats_misc)

        return stats

    def __get_team_advanced_stats_penalties(self, team_id) -> TeamAdvancedStatsPenalties:
        url = f"https://api.nhle.com/stats/rest/en/team/penalties?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_penalties = TeamAdvancedStatsPenalties(team_id)
            team_advanced_stats_penalties.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_penalties.set_bench_minor_penalties(self.data_parser.parse(season, "benchMinorPenalties", "none"))
            team_advanced_stats_penalties.set_game_misconducts(self.data_parser.parse(season, "gameMisconducts", "none"))
            team_advanced_stats_penalties.set_majors(self.data_parser.parse(season, "majors", "none"))
            team_advanced_stats_penalties.set_match_penalties(self.data_parser.parse(season, "matchPenalties", "none"))
            team_advanced_stats_penalties.set_minors(self.data_parser.parse(season, "minors", "none"))
            team_advanced_stats_penalties.set_misconducts(self.data_parser.parse(season, "misconducts", "none"))
            team_advanced_stats_penalties.set_net_penalties(self.data_parser.parse(season, "netPenalties", "none"))
            team_advanced_stats_penalties.set_penalties(self.data_parser.parse(season, "penalties", "none"))
            team_advanced_stats_penalties.set_penalty_minutes(self.data_parser.parse(season, "penaltyMinutes", "none"))
            team_advanced_stats_penalties.set_penalty_seconds_per_game(self.data_parser.parse(season, "penaltySecondsPerGame", "none"))
            team_advanced_stats_penalties.set_total_penalties_drawn(self.data_parser.parse(season, "totalPenaltiesDrawn", "none"))

            stats.append(team_advanced_stats_penalties)

        return stats

    def __get_team_advanced_stats_powerplay_penalty_kill(self, team_id) -> TeamAdvancedStatsPowerplayPenaltyKill:
        url_pk = f"https://api.nhle.com/stats/rest/en/team/penaltykill?cayenneExp=teamId={team_id}"
        url_pk_time = f"https://api.nhle.com/stats/rest/en/team/penaltykilltime?cayenneExp=teamId={team_id}"
        url_pp = f"https://api.nhle.com/stats/rest/en/team/powerplay?cayenneExp=teamId={team_id}"
        url_pp_time = f"https://api.nhle.com/stats/rest/en/team/powerplaytime?cayenneExp=teamId={team_id}"

        data_pk = self.api_connector.get_json(url_pk)
        data_pk_time = self.api_connector.get_json(url_pk_time)
        data_pp = self.api_connector.get_json(url_pp)
        data_pp_time = self.api_connector.get_json(url_pp_time)

        stats = []
        for pk_szn, pk_time_szn, pp_szn, pp_time_szn in zip(self.data_parser.parse(data_pk, "data", "empty_list"), self.data_parser.parse(data_pk_time, "data", "empty_list"), 
                                       self.data_parser.parse(data_pp, "data", "empty_list"), self.data_parser.parse(data_pp_time, "data", "empty_list")):
            team_advanced_stats_powerplay_penalty_kill = TeamAdvancedStatsPowerplayPenaltyKill(team_id)
            team_advanced_stats_powerplay_penalty_kill.set_year(self.data_parser.parse(pk_szn, "seasonId", "none"))

            team_advanced_stats_powerplay_penalty_kill.set_pk_net_percent(self.data_parser.parse(pk_szn, "penaltyKillNetPct", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_percent(self.data_parser.parse(pk_szn, "penaltyKillPct", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_net_goals(self.data_parser.parse(pk_szn, "pkNetGoals", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_net_goals_for_per_game(self.data_parser.parse(pk_szn, "pkNetGoalsPerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_time_on_ice_per_game(self.data_parser.parse(pk_szn, "pkTimeOnIcePerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_goals_against(self.data_parser.parse(pk_szn, "ppGoalsAgainst", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_goals_against_per_game(self.data_parser.parse(pk_szn, "ppGoalsAgainstPerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_goals_for(self.data_parser.parse(pk_szn, "shGoalsFor", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pk_goals_for_per_game(self.data_parser.parse(pk_szn, "shGoalsForPerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_times_shorthanded(self.data_parser.parse(pk_szn, "timesShorthanded", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_times_shorthanded_per_game(self.data_parser.parse(pk_szn, "timesShorthandedPerGame", "none"))

            team_advanced_stats_powerplay_penalty_kill.set_goals_against_3on4(self.data_parser.parse(pk_time_szn, "goalsAgainst3v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_goals_against_3on5(self.data_parser.parse(pk_time_szn, "goalsAgainst3v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_goals_against_4on5(self.data_parser.parse(pk_time_szn, "goalsAgainst4v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_overall_penalty_kill_percent(self.data_parser.parse(pk_time_szn, "overallPenaltyKillPct", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_penalty_kill_percent_3on4(self.data_parser.parse(pk_time_szn, "penaltyKillPct3v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_penalty_kill_percent_3on5(self.data_parser.parse(pk_time_szn, "penaltyKillPct3v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_penalty_kill_percent_4on5(self.data_parser.parse(pk_time_szn, "penaltyKillPct4v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_3on4(self.data_parser.parse(pk_time_szn, "timeOnIce3v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_3on5(self.data_parser.parse(pk_time_szn, "timeOnIce3v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_4on5(self.data_parser.parse(pk_time_szn, "timeOnIce4on5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_shorthanded(self.data_parser.parse(pk_time_szn, "timeOnIceShorthanded", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_3on4(self.data_parser.parse(pk_time_szn, "timeOnIce3v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_shorthanded_3v4(self.data_parser.parse(pk_time_szn, "timesShorthanded3v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_shorthanded_3v5(self.data_parser.parse(pk_time_szn, "timesShorthanded3v5", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_shorthanded_4v5(self.data_parser.parse(pk_time_szn, "timesShorthanded4v5", "none"))

            team_advanced_stats_powerplay_penalty_kill.set_pp_goals_for(self.data_parser.parse(pp_szn, "powerPlayGoalsFor", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_net_percent(self.data_parser.parse(pp_szn, "powerPlayNetPct", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_percent(self.data_parser.parse(pp_szn, "powerPlayPct", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_goals_per_game(self.data_parser.parse(pp_szn, "ppGoalsPerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_net_goals(self.data_parser.parse(pp_szn, "ppNetGoals", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_net_goals_for_per_game(self.data_parser.parse(pp_szn, "ppNetGoalsPetGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_opportunites(self.data_parser.parse(pp_szn, "ppOpportunities", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_opportunities_per_game(self.data_parser.parse(pp_szn, "ppOpportunitiesPerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_time_on_ice_per_game(self.data_parser.parse(pp_szn, "ppTimeOnIcePerGame", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_goals_against(self.data_parser.parse(pp_szn, "shGoalsAgainst", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_goals_against_per_game(self.data_parser.parse(pp_szn, "shGoalsAgainstPerGame", "none"))

            team_advanced_stats_powerplay_penalty_kill.set_goals_4on3(self.data_parser.parse(pp_time_szn, "goals4v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_goals_5on3(self.data_parser.parse(pp_time_szn, "goals5v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_goals_5on4(self.data_parser.parse(pp_time_szn, "goals5v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_opportunities_4on3(self.data_parser.parse(pp_time_szn, "opportunities4v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_opportunities_5on3(self.data_parser.parse(pp_time_szn, "opportunities5v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_opportunities_5on4(self.data_parser.parse(pp_time_szn, "opportunities5v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_percent_4on3(self.data_parser.parse(pp_time_szn, "powerPlayPct4v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_percent_5on3(self.data_parser.parse(pp_time_szn, "powerPlayPct5v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_percent_5on4(self.data_parser.parse(pp_time_szn, "powerPlayPct5v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_4on3(self.data_parser.parse(pp_time_szn, "timeOnIce4on3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_5on3(self.data_parser.parse(pp_time_szn, "timeOnIce5v3", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_time_on_ice_5on4(self.data_parser.parse(pp_time_szn, "timeOnIce5v4", "none"))
            team_advanced_stats_powerplay_penalty_kill.set_pp_time_on_ice(self.data_parser.parse(pp_time_szn, "timeOnIcePp", "none"))

            stats.append(team_advanced_stats_powerplay_penalty_kill)

        return stats

    def __get_team_advanced_stats_scoring_first(self, team_id) -> TeamAdvancedStatsScoringFirst:
        url = f"https://api.nhle.com/stats/rest/en/team/scoretrailfirst?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_scoring_first = TeamAdvancedStatsScoringFirst(team_id)
            team_advanced_stats_scoring_first.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_scoring_first.set_losses_scoring_first(self.data_parser.parse(season, "lossesScoringFirst", "none"))
            team_advanced_stats_scoring_first.set_losses_trailing_first(self.data_parser.parse(season, "lossesTrailingFirst", "none"))
            team_advanced_stats_scoring_first.set_ot_losses_scoring_first(self.data_parser.parse(season, "otLossesScoringFirst", "none"))
            team_advanced_stats_scoring_first.set_ot_losses_trailing_first(self.data_parser.parse(season, "otLossesTrailingFirst", "none"))
            team_advanced_stats_scoring_first.set_scoring_first_games_played(self.data_parser.parse(season, "scoringFirstGamesPlayed", "none"))
            team_advanced_stats_scoring_first.set_ties_scoring_first(self.data_parser.parse(season, "tiesScoringFirst", "none"))
            team_advanced_stats_scoring_first.set_ties_trailing_first(self.data_parser.parse(season, "tiesTrailingFirst", "none"))
            team_advanced_stats_scoring_first.set_trailing_first_games_played(self.data_parser.parse(season, "trailingFirstGamesPlayed", "none"))
            team_advanced_stats_scoring_first.set_win_percent_scoring_first(self.data_parser.parse(season, "winPctScoringFirst", "none"))
            team_advanced_stats_scoring_first.set_win_percent_trailing_first(self.data_parser.parse(season, "winPctTrailingFirst", "none"))
            team_advanced_stats_scoring_first.set_wins_scoring_first(self.data_parser.parse(season, "winsScoringFirst", "none"))
            team_advanced_stats_scoring_first.set_wins_trailing_first(self.data_parser.parse(season, "winsTrailingFirst", "none"))

            stats.append(team_advanced_stats_scoring_first)

        return stats

    def __get_team_advanced_stats_team_goal_games(self, team_id) -> TeamAdvancedStatsTeamGoalGames:
        url = f"https://api.nhle.com/stats/rest/en/team/goalgames?cayenneExp=teamId={team_id}"
        data = self.api_connector.get_json(url)

        stats = []
        for season in data["data"]:
            team_advanced_stats_goal_games = TeamAdvancedStatsTeamGoalGames(team_id)
            team_advanced_stats_goal_games.set_year(self.data_parser.parse(season, "seasonId", "none"))
            team_advanced_stats_goal_games.set_losses_one_goal_games(self.data_parser.parse(season, "lossesOneGoalGames", "none"))
            team_advanced_stats_goal_games.set_losses_two_goal_games(self.data_parser.parse(season, "lossesTwoGoalGames", "none"))
            team_advanced_stats_goal_games.set_losses_three_goal_games(self.data_parser.parse(season, "lossesThreeGoalGames", "none"))
            team_advanced_stats_goal_games.set_ot_losses_one_goal_games(self.data_parser.parse(season, "otLossesOneGoalGames", "none"))
            team_advanced_stats_goal_games.set_win_percent_one_goal_games(self.data_parser.parse(season, "winPctOneGoalGames", "none"))
            team_advanced_stats_goal_games.set_win_percent_two_goal_games(self.data_parser.parse(season, "winPctTwoGoalGames", "none"))
            team_advanced_stats_goal_games.set_win_percent_three_goal_games(self.data_parser.parse(season, "winPctThreeGoalGames", "none"))
            team_advanced_stats_goal_games.set_wins_one_goal_games(self.data_parser.parse(season, "winsOneGoalGames", "none"))
            team_advanced_stats_goal_games.set_wins_two_goal_games(self.data_parser.parse(season, "winsTwoGoalGames", "none"))
            team_advanced_stats_goal_games.set_wins_three_goal_games(self.data_parser.parse(season, "winsThreeGoalGames", "none"))

            stats.append(team_advanced_stats_goal_games)

        return stats

    def __find_team_id(self, team_abbrev):
        """
        Finds and returns the team ID for a given team abbreviation.
        
        Args:
            team_abbrev (str): The abbreviation of the team.
        
        Returns:
            int: The ID of the team, or None if not found.
        """
        for team in self.team_id_lookup:
            if team["triCode"] == team_abbrev:
                return team["id"]
        return None
    
    def __get_team_colors(self, team_id):
        """
        Returns the primary and secondary colors for a given team ID.
        
        Args:
            team_id (str): The ID of the team.
        
        Returns:
            dict: A dictionary containing the primary and secondary colors of the team.
        """
        team_colors = {
            "NYR": {"primary_color": "Blue", "secondary_color": "Red"},
            "DAL": {"primary_color": "Green", "secondary_color": "Black"},
            "CAR": {"primary_color": "Red", "secondary_color": "Black"},
            "WPG": {"primary_color": "Blue", "secondary_color": "Silver"},
            "FLA": {"primary_color": "Red", "secondary_color": "Blue"},
            "VAN": {"primary_color": "Blue", "secondary_color": "Green"},
            "BOS": {"primary_color": "Black", "secondary_color": "Gold"},
            "COL": {"primary_color": "Burgundy", "secondary_color": "Blue"},
            "EDM": {"primary_color": "Blue", "secondary_color": "Orange"},
            "TOR": {"primary_color": "Blue", "secondary_color": "White"},
            "NSH": {"primary_color": "Yellow", "secondary_color": "Blue"},
            "LAK": {"primary_color": "Black", "secondary_color": "Silver"},
            "TBL": {"primary_color": "Blue", "secondary_color": "White"},
            "VGK": {"primary_color": "Gold", "secondary_color": "Black"},
            "NYI": {"primary_color": "Blue", "secondary_color": "Orange"},
            "STL": {"primary_color": "Blue", "secondary_color": "Gold"},
            "WSH": {"primary_color": "Red", "secondary_color": "Blue"},
            "DET": {"primary_color": "Red", "secondary_color": "White"},
            "PIT": {"primary_color": "Black", "secondary_color": "Gold"},
            "MIN": {"primary_color": "Green", "secondary_color": "Red"},
            "PHI": {"primary_color": "Orange", "secondary_color": "Black"},
            "BUF": {"primary_color": "Blue", "secondary_color": "Gold"},
            "NJD": {"primary_color": "Red", "secondary_color": "Black"},
            "ARI": {"primary_color": "Red", "secondary_color": "Green"},
            "MTL": {"primary_color": "Red", "secondary_color": "Blue"},
            "CBJ": {"primary_color": "Blue", "secondary_color": "Red"},
            "ANA": {"primary_color": "Black", "secondary_color": "Gold"},
            "CHI": {"primary_color": "Red", "secondary_color": "Black"},
            "SJS": {"primary_color": "Teal", "secondary_color": "Black"}
        }
        
        return team_colors.get(team_id, {"primary_color": "Unknown", "secondary_color": "Unknown"})