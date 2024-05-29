from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.models.goalies.goalie import Goalie
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util
from fantasyhockey.data_fetching.players.models.goalies.goalie_stats import GoalieStats
from fantasyhockey.data_fetching.players.models.goalies.goalie_youth_stats import GoalieYouthStats
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats import GoalieAdvancedStats
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_start_relieved import GoalieAdvancedStatsStartRelieved
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_shootout import GoalieAdvancedStatsShootout
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_saves_by_strength import GoalieAdvancedStatsSavesByStrength
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_penalty_shots import GoalieAdvancedStatsPenaltyShots
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_days_rest import GoalieAdvancedStatsDaysRest


class FetchGoalies:
    def __init__(self):
        self.__goalies = []
        self.__goalie_ids = []
        self.__database_operator = DatabaseOperator()
        self.__api_connector = APIConnector()
        self.__data_parser = DataParser()
        self.__util = Util()

    def get_goalies(self):
        if not self.__goalies:
            self.__fetch()
        return self.__goalies

    def __fetch(self):
        self.__get_all_goalies()

        self.__get_goalie_data()


    def __get_goalie_data(self):
        count = 0
        for goalie_id in self.__goalie_ids:
            count += 1
            print(f"Fetching goalie {count} of {len(self.__goalie_ids)}")
            goalie = Goalie(goalie_id)
            goalie_youth_stats, goalie_stats = self.__get_goalie_stats(goalie_id)
            goalie.set_goalie_stats(goalie_stats)
            goalie.set_goalie_youth_stats(goalie_youth_stats)
            goalie_advanced_stats = self.__get_goalie_advanced_stats(goalie_id)
            goalie.set_goalie_advanced_stats(goalie_advanced_stats)
            goalie_advanced_stats_start_relieved = self.__get_goalie_advanced_stats_start_relieved(goalie_id)
            goalie.set_goalie_advanced_stats_start_relieved(goalie_advanced_stats_start_relieved)
            goalie_advanced_stats_shootout = self.__get_goalie_advanced_stats_shootout(goalie_id)
            goalie.set_goalie_advanced_stats_shootout(goalie_advanced_stats_shootout)
            goalie_advanced_stats_saves_by_strength = self.__get_goalie_advanced_stats_saves_by_strength(goalie_id)
            goalie.set_goalie_advanced_stats_saves_by_strength(goalie_advanced_stats_saves_by_strength)
            goalie_advanced_stats_penalty_shots = self.__get_goalie_advanced_stats_penalty_shots(goalie_id)
            goalie.set_goalie_advanced_stats_penalty_shots(goalie_advanced_stats_penalty_shots)
            goalie_advanced_stats_days_rest = self.__get_goalie_advanced_stats_days_rest(goalie_id)
            goalie.set_goalie_advanced_stats_days_rest(goalie_advanced_stats_days_rest)


            self.__goalies.append(goalie)

    def __get_goalie_stats(self, goalie_id) -> tuple[list[GoalieStats], list[GoalieYouthStats]]:
        url = f"https://api-web.nhle.com/v1/player/{goalie_id}/landing"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "seasonTotals", "empty_list")

        stat_seasons = []
        youth_seasons = []

        for season in seasons:
            if season["leagueAbbrev"] != "NHL":
                youthStats = GoalieYouthStats(goalie_id)

                year = self.__data_parser.parse(season, "season", "none")
                youthStats.set_year(year)

                team_name = self.__data_parser.double_parse(season, "teamName", "default", "none")
                youthStats.set_team_name(team_name)

                league_name = self.__data_parser.parse(season, "leagueAbbrev", "none")
                youthStats.set_league_name(league_name)

                game_type_id = self.__data_parser.parse(season, "gameTypeId", "none")
                youthStats.set_game_type_id(game_type_id)

                sequence = self.__data_parser.parse(season, "sequence", "none")
                youthStats.set_sequence(sequence)

                games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
                youthStats.set_games_played(games_played)

                save_percentage = self.__data_parser.parse(season, "savePctg", "none")
                youthStats.set_save_percentage(save_percentage)

                goals_against_average = self.__data_parser.parse(season, "goalsAgainstAvg", "none")
                youthStats.set_goals_against_average(goals_against_average)

                goals_against = self.__data_parser.parse(season, "goalsAgainst", "none")
                youthStats.set_goals_against(goals_against)

                wins = self.__data_parser.parse(season, "wins", "none")
                youthStats.set_wins(wins)

                losses = self.__data_parser.parse(season, "losses", "none")
                youthStats.set_losses(losses)

                time_on_ice = self.__data_parser.parse(season, "toi", "none")
                youthStats.set_time_on_ice(time_on_ice)

                ties = self.__data_parser.parse(season, "ties", "none")
                youthStats.set_ties(ties)

                youth_seasons.append(youthStats)
            else:
                goalieStats = GoalieStats(goalie_id)
                
                team_id = self.__util.get_team_id_from_name(self.__data_parser.double_parse(season, "teamName", "default", "none"))
                goalieStats.set_team_id(team_id)

                year = self.__data_parser.parse(season, "season", "none")
                goalieStats.set_year(year)

                game_type_id = self.__data_parser.parse(season, "gameTypeId", "none")
                goalieStats.set_game_type_id(game_type_id)

                sequence = self.__data_parser.parse(season, "sequence", "none")
                goalieStats.set_sequence(sequence)

                games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
                goalieStats.set_games_played(games_played)

                goals = self.__data_parser.parse(season, "goals", "none")
                goalieStats.set_goals(goals)

                assists = self.__data_parser.parse(season, "assists", "none")
                goalieStats.set_assists(assists)

                games_started = self.__data_parser.parse(season, "gamesStarted", "none")
                goalieStats.set_games_started(games_started)

                wins = self.__data_parser.parse(season, "wins", "none")
                goalieStats.set_wins(wins)

                losses = self.__data_parser.parse(season, "losses", "none")
                goalieStats.set_losses(losses)

                ot_losses = self.__data_parser.parse(season, "otLosses", "none")
                goalieStats.set_ot_losses(ot_losses)

                shots_against = self.__data_parser.parse(season, "shotsAgainst", "none")
                goalieStats.set_shots_against(shots_against)

                goals_against = self.__data_parser.parse(season, "goalsAgainst", "none")
                goalieStats.set_goals_against(goals_against)

                save_percent = self.__data_parser.parse(season, "savePctg", "none")
                goalieStats.set_save_percent(save_percent)

                shutouts = self.__data_parser.parse(season, "shutouts", "none")
                goalieStats.set_shutouts(shutouts)

                time_on_ice = self.__data_parser.parse(season, "timeOnIce", "none")
                goalieStats.set_time_on_ice(time_on_ice)

                penalty_minutes = self.__data_parser.parse(season, "penaltyMinutes", "none")
                goalieStats.set_penalty_minutes(penalty_minutes)

                goals_against_average = self.__data_parser.parse(season, "goalsAgainstAvg", "none")
                goalieStats.set_goals_against_average(goals_against_average)

                stat_seasons.append(goalieStats)

        return youth_seasons, stat_seasons
    
    def __get_goalie_advanced_stats(self, goalie_id) -> list[GoalieAdvancedStats]:
        url = f"https://api.nhle.com/stats/rest/en/goalie/advanced?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")

        advanced_stats = []
        for season in seasons:
            goalieAdvancedStats = GoalieAdvancedStats(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStats.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStats.set_team_id(team_id)

            complete_game_percentage = self.__data_parser.parse(season, "completeGamePctg", "none")
            goalieAdvancedStats.set_complete_game_percentage(complete_game_percentage)

            complete_games = self.__data_parser.parse(season, "completeGames", "none")
            goalieAdvancedStats.set_complete_games(complete_games)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            goalieAdvancedStats.set_games_played(games_played)

            games_started = self.__data_parser.parse(season, "gamesStarted", "none")
            goalieAdvancedStats.set_games_started(games_started)

            goals_against = self.__data_parser.parse(season, "goalsAgainst", "none")
            goalieAdvancedStats.set_goals_against(goals_against)

            goals_against_average = self.__data_parser.parse(season, "goalsAgainstAverage", "none")
            goalieAdvancedStats.set_goals_against_average(goals_against_average)

            goals_for = self.__data_parser.parse(season, "goalsFor", "none")
            goalieAdvancedStats.set_goals_for(goals_for)

            goals_for_average = self.__data_parser.parse(season, "goalsForAverage", "none")
            goalieAdvancedStats.set_goals_for_average(goals_for_average)

            incomplete_games = self.__data_parser.parse(season, "incompleteGames", "none")
            goalieAdvancedStats.set_incomplete_games(incomplete_games)

            quality_starts = self.__data_parser.parse(season, "qualityStart", "none")
            goalieAdvancedStats.set_quality_starts(quality_starts)

            quality_starts_percentage = self.__data_parser.parse(season, "qualityStartsPct", "none")
            goalieAdvancedStats.set_quality_starts_percentage(quality_starts_percentage)

            regulation_losses = self.__data_parser.parse(season, "regulationLosses", "none")
            goalieAdvancedStats.set_regulation_losses(regulation_losses)

            regulation_wins = self.__data_parser.parse(season, "regulationWins", "none")
            goalieAdvancedStats.set_regulation_wins(regulation_wins)

            advanced_stats.append(goalieAdvancedStats)

        return advanced_stats


    def __get_goalie_advanced_stats_start_relieved(self, goalie_id) -> list[GoalieAdvancedStatsStartRelieved]: 
        url = f"https://api.nhle.com/stats/rest/en/goalie/startedVsRelieved?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")
        
        advanced_stats = []
        for season in seasons:
            goalieAdvancedStatsStartRelieved = GoalieAdvancedStatsStartRelieved(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStatsStartRelieved.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStatsStartRelieved.set_team_id(team_id)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            goalieAdvancedStatsStartRelieved.set_games_played(games_played)

            games_relieved = self.__data_parser.parse(season, "gamesRelieved", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved(games_relieved)

            games_relieved_goals_against = self.__data_parser.parse(season, "gamesRelievedGoalsAgainst", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_goals_against(games_relieved_goals_against)

            games_relieved_losses = self.__data_parser.parse(season, "gamesRelievedLosses", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_losses(games_relieved_losses)

            games_relieved_ot_losses = self.__data_parser.parse(season, "gamesRelievedOtLosses", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_ot_losses(games_relieved_ot_losses)

            games_relieved_save_percent = self.__data_parser.parse(season, "gamesRelievedSavePct", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_save_percent(games_relieved_save_percent)

            games_relieved_saves = self.__data_parser.parse(season, "gamesRelievedSaves", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_saves(games_relieved_saves)

            games_relieved_shots_against = self.__data_parser.parse(season, "gamesRelievedShotsAgainst", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_shots_against(games_relieved_shots_against)

            games_relieved_ties = self.__data_parser.parse(season, "gamesRelievedTies", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_ties(games_relieved_ties)

            games_relieved_wins = self.__data_parser.parse(season, "gamesRelievedWins", "none")
            goalieAdvancedStatsStartRelieved.set_games_relieved_wins(games_relieved_wins)

            games_started = self.__data_parser.parse(season, "gamesStarted", "none")
            goalieAdvancedStatsStartRelieved.set_games_started(games_started)

            games_started_goals_against = self.__data_parser.parse(season, "gamesStartedGoalsAgainst", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_goals_against(games_started_goals_against)

            games_started_losses = self.__data_parser.parse(season, "gamesStartedLosses", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_losses(games_started_losses)

            games_started_ot_losses = self.__data_parser.parse(season, "gamesStartedOtLosses", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_ot_losses(games_started_ot_losses)
            
            games_started_save_percent = self.__data_parser.parse(season, "gamesStartedSavePct", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_save_percent(games_started_save_percent)

            games_started_saves = self.__data_parser.parse(season, "gamesStartedSaves", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_saves(games_started_saves)

            games_started_shots_against = self.__data_parser.parse(season, "gamesStartedShotsAgainst", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_shots_against(games_started_shots_against)

            games_started_ties = self.__data_parser.parse(season, "gamesStartedTies", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_ties(games_started_ties)

            games_started_wins = self.__data_parser.parse(season, "gamesStartedWins", "none")
            goalieAdvancedStatsStartRelieved.set_games_started_wins(games_started_wins)

            advanced_stats.append(goalieAdvancedStatsStartRelieved)

        return advanced_stats

    def __get_goalie_advanced_stats_shootout(self, goalie_id) -> list[GoalieAdvancedStatsShootout]:
        url = f"https://api.nhle.com/stats/rest/en/goalie/shootout?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")

        advanced_stats = []
        for season in seasons:
            goalieAdvancedStatsShootout = GoalieAdvancedStatsShootout(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStatsShootout.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStatsShootout.set_team_id(team_id)

            career_shootout_games_played = self.__data_parser.parse(season, "careerShootoutGamesPlayed", "none")
            goalieAdvancedStatsShootout.set_career_shootout_games_played(career_shootout_games_played)

            career_shootout_goals_allowed = self.__data_parser.parse(season, "careerShootoutGoalsAllowed", "none")
            goalieAdvancedStatsShootout.set_career_shootout_goals_allowed(career_shootout_goals_allowed)

            career_shootout_losses = self.__data_parser.parse(season, "careerShootoutLosses", "none")
            goalieAdvancedStatsShootout.set_career_shootout_losses(career_shootout_losses)

            career_shootout_save_percentage = self.__data_parser.parse(season, "careerShootoutSavePct", "none")
            goalieAdvancedStatsShootout.set_career_shootout_save_percentage(career_shootout_save_percentage)

            career_shooutout_saves = self.__data_parser.parse(season, "careerShootoutSaves", "none")
            goalieAdvancedStatsShootout.set_career_shooutout_saves(career_shooutout_saves)

            career_shootout_shots_against = self.__data_parser.parse(season, "careerShootoutShotsAgainst", "none")
            goalieAdvancedStatsShootout.set_career_shootout_shots_against(career_shootout_shots_against)

            shootout_goals_against = self.__data_parser.parse(season, "shootoutGoalsAgainst", "none")
            goalieAdvancedStatsShootout.set_shootout_goals_against(shootout_goals_against)

            shootout_losses = self.__data_parser.parse(season, "shootoutLosses", "none")
            goalieAdvancedStatsShootout.set_shootout_losses(shootout_losses)

            shootout_save_percent = self.__data_parser.parse(season, "shootoutSavePct", "none")
            goalieAdvancedStatsShootout.set_shootout_save_percent(shootout_save_percent)

            shootout_saves = self.__data_parser.parse(season, "shootoutSaves", "none")
            goalieAdvancedStatsShootout.set_shootout_saves(shootout_saves)
            
            shootout_shots_against = self.__data_parser.parse(season, "shootoutShotsAgainst", "none")
            goalieAdvancedStatsShootout.set_shootout_shots_against(shootout_shots_against)

            shootout_wins = self.__data_parser.parse(season, "shootoutWins", "none")
            goalieAdvancedStatsShootout.set_shootout_wins(shootout_wins)

            advanced_stats.append(goalieAdvancedStatsShootout)

        return advanced_stats
    
    def __get_goalie_advanced_stats_saves_by_strength(self, goalie_id) -> list[GoalieAdvancedStatsSavesByStrength]:
        url = f"https://api.nhle.com/stats/rest/en/goalie/savesByStrength?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")

        advanced_stats = []
        for season in seasons:
            goalieAdvancedStatsSavesByStrength = GoalieAdvancedStatsSavesByStrength(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStatsSavesByStrength.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStatsSavesByStrength.set_team_id(team_id)

            ev_goals_against = self.__data_parser.parse(season, "evGoalsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_ev_goals_against(ev_goals_against)

            ev_save_percent = self.__data_parser.parse(season, "evSavePct", "none")
            goalieAdvancedStatsSavesByStrength.set_ev_save_percent(ev_save_percent)

            ev_saves = self.__data_parser.parse(season, "evSaves", "none")
            goalieAdvancedStatsSavesByStrength.set_ev_saves(ev_saves)

            ev_shots_against = self.__data_parser.parse(season, "evShotsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_ev_shots_against(ev_shots_against)

            pp_goals_against = self.__data_parser.parse(season, "ppGoalsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_pp_goals_against(pp_goals_against)

            pp_save_percent = self.__data_parser.parse(season, "ppSavePct", "none")
            goalieAdvancedStatsSavesByStrength.set_pp_save_percent(pp_save_percent)

            pp_saves = self.__data_parser.parse(season, "ppSaves", "none")
            goalieAdvancedStatsSavesByStrength.set_pp_saves(pp_saves)

            pp_shots_against = self.__data_parser.parse(season, "ppShotsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_pp_shots_against(pp_shots_against)

            pk_goals_against = self.__data_parser.parse(season, "shGoalsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_pk_goals_against(pk_goals_against)

            pk_save_percent = self.__data_parser.parse(season, "shSavePct", "none")
            goalieAdvancedStatsSavesByStrength.set_pk_save_percent(pk_save_percent)

            pk_saves = self.__data_parser.parse(season, "shSaves", "none")
            goalieAdvancedStatsSavesByStrength.set_pk_saves(pk_saves)

            pk_shots_against = self.__data_parser.parse(season, "shShotsAgainst", "none")
            goalieAdvancedStatsSavesByStrength.set_pk_shots_against(pk_shots_against)

            advanced_stats.append(goalieAdvancedStatsSavesByStrength)

        return advanced_stats

    def __get_goalie_advanced_stats_penalty_shots(self, goalie_id) -> list[GoalieAdvancedStatsPenaltyShots]:
        url = f"https://api.nhle.com/stats/rest/en/goalie/penaltyShots?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")

        advanced_stats = []
        for season in seasons: 
            goalieAdvancedStatsPenaltyShots = GoalieAdvancedStatsPenaltyShots(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStatsPenaltyShots.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStatsPenaltyShots.set_team_id(team_id)

            penalty_shot_save_percent = self.__data_parser.parse(season, "penaltyShotSavePct", "none")
            goalieAdvancedStatsPenaltyShots.set_penalty_shot_save_percent(penalty_shot_save_percent)

            penalty_shot_against = self.__data_parser.parse(season, "penaltyShotsAgainst", "none")
            goalieAdvancedStatsPenaltyShots.set_penalty_shot_against(penalty_shot_against)

            penalty_shot_goals_against = self.__data_parser.parse(season, "penaltyShotsGoalsAgainst", "none")
            goalieAdvancedStatsPenaltyShots.set_penalty_shot_goals_against(penalty_shot_goals_against)

            penalty_shot_saves = self.__data_parser.parse(season, "penaltyShotsSaves", "none")
            goalieAdvancedStatsPenaltyShots.set_penalty_shot_saves(penalty_shot_saves)

            advanced_stats.append(goalieAdvancedStatsPenaltyShots)

        return advanced_stats
    
    def __get_goalie_advanced_stats_days_rest(self, goalie_id) -> list[GoalieAdvancedStatsDaysRest]:
        url = f"https://api.nhle.com/stats/rest/en/goalie/daysrest?cayenneExp=playerId={goalie_id}"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "data", "empty_list")

        advanced_stats = []
        for season in seasons: 
            goalieAdvancedStatsDaysRest = GoalieAdvancedStatsDaysRest(goalie_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            goalieAdvancedStatsDaysRest.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            goalieAdvancedStatsDaysRest.set_team_id(team_id)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            goalieAdvancedStatsDaysRest.set_games_played(games_played)

            games_played_days_rest_0 = self.__data_parser.parse(season, "gamesPlayedDaysRest0", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_0(games_played_days_rest_0)

            games_played_days_rest_1 = self.__data_parser.parse(season, "gamesPlayedDaysRest1", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_1(games_played_days_rest_1)

            games_played_days_rest_2 = self.__data_parser.parse(season, "gamesPlayedDaysRest2", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_2(games_played_days_rest_2)

            games_played_days_rest_3 = self.__data_parser.parse(season, "gamesPlayedDaysRest3", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_3(games_played_days_rest_3)

            games_played_days_rest_4 = self.__data_parser.parse(season, "gamesPlayedDaysRest4", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_4(games_played_days_rest_4)

            games_played_days_rest_4_plus = self.__data_parser.parse(season, "gamesPlayedDaysRest4Plus", "none")
            goalieAdvancedStatsDaysRest.set_games_played_days_rest_4_plus(games_played_days_rest_4_plus)

            games_started = self.__data_parser.parse(season, "gamesStarted", "none")
            goalieAdvancedStatsDaysRest.set_games_started(games_started)

            losses = self.__data_parser.parse(season, "losses", "none")
            goalieAdvancedStatsDaysRest.set_losses(losses)

            ot_losses = self.__data_parser.parse(season, "otLosses", "none")
            goalieAdvancedStatsDaysRest.set_ot_losses(ot_losses)

            save_percent = self.__data_parser.parse(season, "savePct", "none")
            goalieAdvancedStatsDaysRest.set_save_percent(save_percent)

            save_percent_days_rest_0 = self.__data_parser.parse(season, "savePctDaysRest0", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_0(save_percent_days_rest_0)

            save_percent_days_rest_1 = self.__data_parser.parse(season, "savePctDaysRest1", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_1(save_percent_days_rest_1)

            save_percent_days_rest_2 = self.__data_parser.parse(season, "savePctDaysRest2", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_2(save_percent_days_rest_2)

            save_percent_days_rest_3 = self.__data_parser.parse(season, "savePctDaysRest3", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_3(save_percent_days_rest_3)

            save_percent_days_rest_4 = self.__data_parser.parse(season, "savePctDaysRest4", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_4(save_percent_days_rest_4)

            save_percent_days_rest_4_plus = self.__data_parser.parse(season, "savePctDaysRest4Plus", "none")
            goalieAdvancedStatsDaysRest.set_save_percent_days_rest_4_plus(save_percent_days_rest_4_plus)

            advanced_stats.append(goalieAdvancedStatsDaysRest)

        return advanced_stats

    def __get_all_goalies(self):
        query = "SELECT id FROM player_details WHERE position = 'G';"
        res = self.__database_operator.read(query)
        goalie_ids = []
        for row in res:
            goalie_ids.append(row[0])
        self.__goalie_ids = goalie_ids

