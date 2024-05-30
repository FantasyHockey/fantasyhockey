from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.models.skaters.skater import Skater
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_corsi_fenwick import SkaterAdvancedStatsCorsiFenwick
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util
from fantasyhockey.data_fetching.players.models.skaters.skater_stats import SkaterStats
from fantasyhockey.data_fetching.players.models.skaters.youth_skater_stats import YouthSkaterStats
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_faceoffs import SkaterAdvancedStatsFaceoffs
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_goals import SkaterAdvancedStatsGoals
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_misc import SkaterAdvancedStatsMisc
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_penalties import SkaterAdvancedStatsPenalties
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_penalty_kill import SkaterAdvancedStatsPenaltyKill
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_powerplay import SkaterAdvancedStatsPowerplay
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_scoring import SkaterAdvancedStatsScoring
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_shootout import SkaterAdvancedStatsShootout
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_toi import SkaterAdvancedStatsTOI

class FetchSkaters:
    def __init__(self):
        self.__skaters = []
        self.__skater_ids = []
        self.__database_operator = DatabaseOperator()
        self.__api_connector = APIConnector()
        self.__data_parser = DataParser()
        self.__util = Util()

    def get_skaters(self):
        if not self.__skaters:
            self.__fetch()
        return self.__skaters

    def __fetch(self):
        self.__get_all_skaters()
        self.__get_skater_data()

    def __get_skater_data(self):
        count = 0
        for skater_id in self.__skater_ids:
            count += 1
            print(f"Fetching skater {count} of {len(self.__skater_ids)}")
            skater = Skater(skater_id)

            skaterAdvancedStatsCorsiFenwick = self.__get_skater_advanced_stats_corsi_fenwick(skater_id)
            skater.set_advanced_stats_corsi_fenwick(skaterAdvancedStatsCorsiFenwick)
            youth_seasons, nhl_seasons = self.__get_skater_stats(skater_id)
            skater.set_skater_stats(nhl_seasons)
            skater.set_youth_stats(youth_seasons)
            skater.set_advanced_stats_toi(self.__get_skater_advanced_stats_toi(skater_id))
            skater.set_advanced_stats_shootout(self.__get_skater_advanced_stats_shootout(skater_id))
            skater.set_advanced_stats_scoring(self.__get_skater_advanced_stats_scoring(skater_id))
            skater.set_advanced_stats_powerplay(self.__get_skater_advanced_stats_powerplay(skater_id))
            skater.set_advanced_stats_penalty_kill(self.__get_skater_advanced_stats_penalty_kill(skater_id))
            skater.set_advanced_stats_penalties(self.__get_skater_advanced_stats_penalties(skater_id))
            skater.set_advanced_stats_misc(self.__get_skater_advanced_stats_misc(skater_id))
            skater.set_advanced_stats_goals(self.__get_skater_advanced_stats_goals(skater_id))
            skater.set_advanced_stats_faceoffs(self.__get_skater_advanced_stats_faceoffs(skater_id))

            self.__skaters.append(skater)

    def __get_skater_stats(self, skater_id) -> tuple[list[SkaterStats], list[YouthSkaterStats]]:
        url = f"https://api-web.nhle.com/v1/player/{skater_id}/landing"
        data = self.__api_connector.get_json(url)
        seasons = self.__data_parser.parse(data, "seasonTotals", "empty_list")

        stat_seasons = []
        youth_seasons = []

        for season in seasons:
            if season["leagueAbbrev"] != "NHL":
                youthStats = YouthSkaterStats(skater_id)

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

                goals = self.__data_parser.parse(season, "goals", "none")
                youthStats.set_goals(goals)

                assists = self.__data_parser.parse(season, "assists", "none")
                youthStats.set_assists(assists)

                points = self.__data_parser.parse(season, "points", "none")
                youthStats.set_points(points)

                pim = self.__data_parser.parse(season, "pim", "none")
                youthStats.set_pim(pim)

                youth_seasons.append(youthStats)

            else:

                skaterStats = SkaterStats(skater_id)
                
                year = self.__data_parser.parse(season, "season", "none")
                skaterStats.set_year(year)

                team_id = self.__util.get_team_id_from_name(self.__data_parser.double_parse(season, "teamName", "default", "none"))
                skaterStats.set_team_id(team_id)

                games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
                skaterStats.set_games_played(games_played)

                goals = self.__data_parser.parse(season, "goals", "none")
                skaterStats.set_goals(goals)

                assists = self.__data_parser.parse(season, "assists", "none")
                skaterStats.set_assists(assists)

                points = self.__data_parser.parse(season, "points", "none")
                skaterStats.set_points(points)

                plus_minus = self.__data_parser.parse(season, "plusMinus", "none")
                skaterStats.set_plus_minus(plus_minus)

                penalty_minutes = self.__data_parser.parse(season, "pim", "none")
                skaterStats.set_penalty_minutes(penalty_minutes)

                game_winning_goals = self.__data_parser.parse(season, "gameWinningGoals", "none")
                skaterStats.set_game_winning_goals(game_winning_goals)

                ot_goals = self.__data_parser.parse(season, "otGoals", "none")
                skaterStats.set_ot_goals(ot_goals)

                power_play_goals = self.__data_parser.parse(season, "powerPlayGoals", "none")
                skaterStats.set_power_play_goals(power_play_goals)

                power_play_points = self.__data_parser.parse(season, "powerPlayPoints", "none")
                skaterStats.set_power_play_points(power_play_points)

                shooting_percentage = self.__data_parser.parse(season, "shootingPctg", "none")
                skaterStats.set_shooting_percentage(shooting_percentage)

                shorthanded_goals = self.__data_parser.parse(season, "shorthandedGoals", "none")
                skaterStats.set_shorthanded_goals(shorthanded_goals)

                shorthanded_points = self.__data_parser.parse(season, "shorthandedPoints", "none")
                skaterStats.set_shorthanded_points(shorthanded_points)

                shots = self.__data_parser.parse(season, "shots", "none")
                skaterStats.set_shots(shots)

                time_on_ice = self.__data_parser.parse(season, "avgToi", "none")
                skaterStats.set_time_on_ice(time_on_ice)

                game_type_id = self.__data_parser.parse(season, "gameTypeId", "none")
                skaterStats.set_game_type_id(game_type_id)

                sequence = self.__data_parser.parse(season, "sequence", "none")
                skaterStats.set_sequence(sequence)

                faceoff_percentage = self.__data_parser.parse(season, "faceoffWinningPctg", "none")
                skaterStats.set_faceoff_percentage(faceoff_percentage)

                stat_seasons.append(skaterStats)

        return youth_seasons, stat_seasons
        
    def __get_skater_advanced_stats_corsi_fenwick(self, skater_id) -> list[SkaterAdvancedStatsCorsiFenwick]:
        
        url_counts = f"https://api.nhle.com/stats/rest/en/skater/summaryshooting?cayenneExp=playerId={skater_id}"
        url_percents = f"https://api.nhle.com/stats/rest/en/skater/percentages?cayenneExp=playerId={skater_id}"
        
        data_counts = self.__api_connector.get_json(url_counts)
        data_percents = self.__api_connector.get_json(url_percents)

        seasons = []

        for count_szn, percent_szn in zip(self.__data_parser.parse(data_counts, "data", "empty_list"), self.__data_parser.parse(data_percents, "data", "empty_list")):
            skaterAdvancedStatsCorsiFenwick = SkaterAdvancedStatsCorsiFenwick(skater_id)
            year = self.__data_parser.parse(count_szn, "seasonId", "none")
            skaterAdvancedStatsCorsiFenwick.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(count_szn, "teamAbbrevs", "none"))
            skaterAdvancedStatsCorsiFenwick.set_team_id(team_id)

            games_played = self.__data_parser.parse(count_szn, "gamesPlayed", "none")
            skaterAdvancedStatsCorsiFenwick.set_games_played(games_played)

            corsi_against = self.__data_parser.parse(count_szn, "satAgainst", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_against(corsi_against)

            corsi_ahead = self.__data_parser.parse(count_szn, "satAhead", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_ahead(corsi_ahead)

            corsi_behind = self.__data_parser.parse(count_szn, "satBehind", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_behind(corsi_behind)

            corsi_close = self.__data_parser.parse(count_szn, "satClose", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_close(corsi_close)

            corsi_for = self.__data_parser.parse(count_szn, "satFor", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_for(corsi_for)

            corsi_tied = self.__data_parser.parse(count_szn, "satTied", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_tied(corsi_tied)

            corsi_total = self.__data_parser.parse(count_szn, "satTotal", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_total(corsi_total)

            corsi_relative = self.__data_parser.parse(count_szn, "satRelative", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_relative(corsi_relative)

            fenwick_against = self.__data_parser.parse(count_szn, "usatAgainst", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_against(fenwick_against)

            fenwick_ahead = self.__data_parser.parse(count_szn, "usatAhead", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_ahead(fenwick_ahead)

            fenwick_behind = self.__data_parser.parse(count_szn, "usatBehind", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_behind(fenwick_behind)

            fenwick_close = self.__data_parser.parse(count_szn, "usatClose", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_close(fenwick_close)

            fenwick_for = self.__data_parser.parse(count_szn, "usatFor", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_for(fenwick_for)

            fenwick_tied = self.__data_parser.parse(count_szn, "usatTied", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_tied(fenwick_tied)

            fenwick_total = self.__data_parser.parse(count_szn, "usatTotal", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_total(fenwick_total)

            fenwick_relative = self.__data_parser.parse(count_szn, "usatRelative", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_relative(fenwick_relative)

            time_on_ice_5on5_per_game = self.__data_parser.parse(count_szn, "timeOnIcePerGame5v5", "none")
            skaterAdvancedStatsCorsiFenwick.set_time_on_ice_5on5_per_game(time_on_ice_5on5_per_game)

            corsi_percentage = self.__data_parser.parse(percent_szn, "satPercentage", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_percentage(corsi_percentage)

            corsi_ahead_percentage = self.__data_parser.parse(percent_szn, "satPercentageAhead", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_ahead_percentage(corsi_ahead_percentage)

            corsi_behind_percentage = self.__data_parser.parse(percent_szn, "satPercentageBehind", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_behind_percentage(corsi_behind_percentage)

            corsi_close_percentage = self.__data_parser.parse(percent_szn, "satPercentageClose", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_close_percentage(corsi_close_percentage)

            corsi_tied_percentage = self.__data_parser.parse(percent_szn, "satPercentageTied", "none")
            skaterAdvancedStatsCorsiFenwick.set_corsi_tied_percentage(corsi_tied_percentage)

            shooting_percent_5on5 = self.__data_parser.parse(percent_szn, "shootingPct5v5", "none")
            skaterAdvancedStatsCorsiFenwick.set_shooting_percent_5on5(shooting_percent_5on5)

            skater_save_percent_5on5 = self.__data_parser.parse(percent_szn, "skaterSavePct5v5", "none")
            skaterAdvancedStatsCorsiFenwick.set_skater_save_percent_5on5(skater_save_percent_5on5)

            skater_shooting_plus_save_percent_5on5 = self.__data_parser.parse(percent_szn, "skaterShootingPlusSavePct5v5", "none")
            skaterAdvancedStatsCorsiFenwick.set_skater_shooting_plus_save_percent_5on5(skater_shooting_plus_save_percent_5on5)

            fenwick_percentage = self.__data_parser.parse(percent_szn, "usatPercentage", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_percentage(fenwick_percentage)

            fenwick_ahead_percentage = self.__data_parser.parse(percent_szn, "usatPercentageAhead", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_ahead_percentage(fenwick_ahead_percentage)

            fenwick_behind_percentage = self.__data_parser.parse(percent_szn, "usatPercentageBehind", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_behind_percentage(fenwick_behind_percentage)

            fenwick_close_percentage = self.__data_parser.parse(percent_szn, "usatPrecentageClose", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_close_percentage(fenwick_close_percentage)

            fenwick_tied_percentage = self.__data_parser.parse(percent_szn, "usatPercentageTied", "none")
            skaterAdvancedStatsCorsiFenwick.set_fenwick_tied_percentage(fenwick_tied_percentage)

            zone_start_percentage_offensive = self.__data_parser.parse(percent_szn, "zoneStartPct5v5", "none")
            skaterAdvancedStatsCorsiFenwick.set_zone_start_5on5_percentage(zone_start_percentage_offensive)

            seasons.append(skaterAdvancedStatsCorsiFenwick)

        return seasons

    def __get_skater_advanced_stats_faceoffs(self, skater_id) -> list[SkaterAdvancedStatsFaceoffs]:
        url = f"https://api.nhle.com/stats/rest/en/skater/faceoffwins?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStastFaceoffs = SkaterAdvancedStatsFaceoffs(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStastFaceoffs.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStastFaceoffs.set_team_id(team_id)

            defensive_zone_faceoffs = self.__data_parser.parse(season, "defensiveZoneFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_defensive_zone_faceoffs(defensive_zone_faceoffs)

            defensive_zone_faceoffs_won = self.__data_parser.parse(season, "defensiveZoneFaceoffWins", "none")
            skaterAdvancedStastFaceoffs.set_defensive_zone_faceoffs_won(defensive_zone_faceoffs_won)

            defensive_zone_faceoffs_lost = self.__data_parser.parse(season, "defensiveZoneFaceoffLosses", "none")
            skaterAdvancedStastFaceoffs.set_defensive_zone_faceoffs_lost(defensive_zone_faceoffs_lost)

            ev_faceoffs = self.__data_parser.parse(season, "evFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_ev_faceoffs(ev_faceoffs)

            ev_faceoffs_won = self.__data_parser.parse(season, "evFaceoffsWon", "none")
            skaterAdvancedStastFaceoffs.set_ev_faceoffs_won(ev_faceoffs_won)

            ev_faceoffs_lost = self.__data_parser.parse(season, "evFaceoffsLost", "none")
            skaterAdvancedStastFaceoffs.set_ev_faceoffs_lost(ev_faceoffs_lost)

            faceoff_percentage = self.__data_parser.parse(season, "faceoffWinPct", "none")
            skaterAdvancedStastFaceoffs.set_faceoff_percentage(faceoff_percentage)

            neutral_zone_faceoffs = self.__data_parser.parse(season, "neutralZoneFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_neutral_zone_faceoffs(neutral_zone_faceoffs)

            neutral_zone_faceoffs_won = self.__data_parser.parse(season, "neutralZoneFaceoffWins", "none")
            skaterAdvancedStastFaceoffs.set_neutral_zone_faceoffs_won(neutral_zone_faceoffs_won)

            neutral_zone_faceoffs_lost = self.__data_parser.parse(season, "neutralZoneFaceoffLosses", "none")
            skaterAdvancedStastFaceoffs.set_neutral_zone_faceoffs_lost(neutral_zone_faceoffs_lost)

            offensive_zone_faceoffs = self.__data_parser.parse(season, "offensiveZoneFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_offensive_zone_faceoffs(offensive_zone_faceoffs)

            offensive_zone_faceoffs_won = self.__data_parser.parse(season, "offensiveZoneFaceoffWins", "none")
            skaterAdvancedStastFaceoffs.set_offensive_zone_faceoffs_won(offensive_zone_faceoffs_won)

            offensive_zone_faceoffs_lost = self.__data_parser.parse(season, "offensiveZoneFaceoffLosses", "none")
            skaterAdvancedStastFaceoffs.set_offensive_zone_faceoffs_lost(offensive_zone_faceoffs_lost)

            pp_faceoffs = self.__data_parser.parse(season, "ppFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_pp_faceoffs(pp_faceoffs)

            pp_faceoffs_won = self.__data_parser.parse(season, "ppFaceoffsWon", "none")
            skaterAdvancedStastFaceoffs.set_pp_faceoffs_won(pp_faceoffs_won)

            pp_faceoffs_lost = self.__data_parser.parse(season, "ppFaceoffsLost", "none")
            skaterAdvancedStastFaceoffs.set_pp_faceoffs_lost(pp_faceoffs_lost)

            pk_faceoffs = self.__data_parser.parse(season, "shFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_pk_faceoffs(pk_faceoffs)

            pk_faceoffs_won = self.__data_parser.parse(season, "shFaceoffsWon", "none")
            skaterAdvancedStastFaceoffs.set_pk_faceoffs_won(pk_faceoffs_won)

            pk_faceoffs_lost = self.__data_parser.parse(season, "shFaceoffsLost", "none")
            skaterAdvancedStastFaceoffs.set_pk_faceoffs_lost(pk_faceoffs_lost)

            total_faceoffs = self.__data_parser.parse(season, "totalFaceoffs", "none")
            skaterAdvancedStastFaceoffs.set_total_faceoffs(total_faceoffs)

            total_faceoffs_won = self.__data_parser.parse(season, "totalFaceoffWins", "none")
            skaterAdvancedStastFaceoffs.set_total_faceoffs_won(total_faceoffs_won)

            total_faceoffs_lost = self.__data_parser.parse(season, "totalFaceoffLosses", "none")
            skaterAdvancedStastFaceoffs.set_total_faceoffs_lost(total_faceoffs_lost)

            seasons.append(skaterAdvancedStastFaceoffs)

        return seasons

    def __get_skater_advanced_stats_goals(self, skater_id) -> list[SkaterAdvancedStatsGoals]:
        url = f"https://api.nhle.com/stats/rest/en/skater/goalsForAgainst?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsGoals = SkaterAdvancedStatsGoals(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsGoals.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsGoals.set_team_id(team_id)

            even_strength_goal_difference = self.__data_parser.parse(season, "evenStrengthGoalDifference", "none")
            skaterAdvancedStatsGoals.set_even_strength_goal_difference(even_strength_goal_difference)

            even_strength_goals_against = self.__data_parser.parse(season, "evenStrengthGoalsAgainst", "none")
            skaterAdvancedStatsGoals.set_even_strength_goals_against(even_strength_goals_against)

            even_strength_goals_for = self.__data_parser.parse(season, "evenStrengthGoalsFor", "none")
            skaterAdvancedStatsGoals.set_even_strength_goals_for(even_strength_goals_for)

            even_strength_time_on_ice_per_game = self.__data_parser.parse(season, "evenStrengthTimeOnIcePerGame", "none")
            skaterAdvancedStatsGoals.set_even_strength_time_on_ice_per_game(even_strength_time_on_ice_per_game)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            skaterAdvancedStatsGoals.set_games_played(games_played)

            pp_goals_for = self.__data_parser.parse(season, "powerPlayGoalFor", "none")
            skaterAdvancedStatsGoals.set_pp_goals_for(pp_goals_for)

            pp_goals_against = self.__data_parser.parse(season, "powerPlayGoalsAgainst", "none")
            skaterAdvancedStatsGoals.set_pp_goals_against(pp_goals_against)

            pk_goals_for = self.__data_parser.parse(season, "shortHandedGoalsFor", "none")
            skaterAdvancedStatsGoals.set_pk_goals_for(pk_goals_for)

            pk_goals_against = self.__data_parser.parse(season, "shortHandedGoalsAgainst", "none")
            skaterAdvancedStatsGoals.set_pk_goals_against(pk_goals_against)

            seasons.append(skaterAdvancedStatsGoals)

        return seasons

    def __get_skater_advanced_stats_misc(self, skater_id) -> list[SkaterAdvancedStatsMisc]:
        url = f"https://api.nhle.com/stats/rest/en/skater/realtime?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsMisc = SkaterAdvancedStatsMisc(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsMisc.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsMisc.set_team_id(team_id)

            blocked_shots = self.__data_parser.parse(season, "blockedShots", "none")
            skaterAdvancedStatsMisc.set_blocked_shots(blocked_shots)

            empty_net_assists = self.__data_parser.parse(season, "emptyNetAssists", "none")
            skaterAdvancedStatsMisc.set_empty_net_assists(empty_net_assists)

            empty_net_goals = self.__data_parser.parse(season, "emptyNetGoals", "none")
            skaterAdvancedStatsMisc.set_empty_net_goals(empty_net_goals)

            empty_net_points = self.__data_parser.parse(season, "emptyNetPoints", "none")
            skaterAdvancedStatsMisc.set_empty_net_points(empty_net_points)

            first_goals = self.__data_parser.parse(season, "firstGoals", "none")
            skaterAdvancedStatsMisc.set_first_goals(first_goals)

            giveaways = self.__data_parser.parse(season, "giveaways", "none")
            skaterAdvancedStatsMisc.set_giveaways(giveaways)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            skaterAdvancedStatsMisc.set_games_played(games_played)

            hits = self.__data_parser.parse(season, "hits", "none")
            skaterAdvancedStatsMisc.set_hits(hits)

            missed_shot_crossbar = self.__data_parser.parse(season, "missedShotCrossbar", "none")
            skaterAdvancedStatsMisc.set_missed_shot_crossbar(missed_shot_crossbar)

            missed_shot_goalpost = self.__data_parser.parse(season, "missedShotGoalpost", "none")
            skaterAdvancedStatsMisc.set_missed_shot_goalpost(missed_shot_goalpost)

            missed_shot_over = self.__data_parser.parse(season, "missedShotOverNet", "none")
            skaterAdvancedStatsMisc.set_missed_shot_over(missed_shot_over)

            missed_shot_wide = self.__data_parser.parse(season, "missedShotWideOfNet", "none")
            skaterAdvancedStatsMisc.set_missed_shot_wide(missed_shot_wide)

            missed_shots = self.__data_parser.parse(season, "missedShots", "none")
            skaterAdvancedStatsMisc.set_missed_shots(missed_shots)

            ot_goals = self.__data_parser.parse(season, "otGoals", "none")
            skaterAdvancedStatsMisc.set_ot_goals(ot_goals)

            takeaways = self.__data_parser.parse(season, "takeaways", "none")
            skaterAdvancedStatsMisc.set_takeaways(takeaways)

            time_on_ice_per_game = self.__data_parser.parse(season, "timeOnIcePerGame", "none")
            skaterAdvancedStatsMisc.set_time_on_ice_per_game(time_on_ice_per_game)

            seasons.append(skaterAdvancedStatsMisc)

        return seasons

    def __get_skater_advanced_stats_penalties(self, skater_id) -> list[SkaterAdvancedStatsPenalties]:
        url = f"https://api.nhle.com/stats/rest/en/skater/penalties?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsPenalties = SkaterAdvancedStatsPenalties(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsPenalties.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsPenalties.set_team_id(team_id)

            game_misconduct_penalties = self.__data_parser.parse(season, "gameMisconductPenalties", "none")
            skaterAdvancedStatsPenalties.set_game_misconduct_penalties(game_misconduct_penalties)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            skaterAdvancedStatsPenalties.set_games_played(games_played)

            major_penalties = self.__data_parser.parse(season, "majorPenalties", "none")
            skaterAdvancedStatsPenalties.set_major_penalties(major_penalties)

            match_penalties = self.__data_parser.parse(season, "matchPenalties", "none")
            skaterAdvancedStatsPenalties.set_match_penalties(match_penalties)

            minor_penalties = self.__data_parser.parse(season, "minorPenalties", "none")
            skaterAdvancedStatsPenalties.set_minor_penalties(minor_penalties)

            misconduct_penalties = self.__data_parser.parse(season, "misconductPenalties", "none")
            skaterAdvancedStatsPenalties.set_misconduct_penalties(misconduct_penalties)

            net_penalties = self.__data_parser.parse(season, "netPenalties", "none")
            skaterAdvancedStatsPenalties.set_net_penalties(net_penalties)

            penalties = self.__data_parser.parse(season, "penalties", "none")
            skaterAdvancedStatsPenalties.set_penalties(penalties)

            penalties_drawn = self.__data_parser.parse(season, "penaltiesDrawn", "none")
            skaterAdvancedStatsPenalties.set_penalties_drawn(penalties_drawn)

            penalty_minutes = self.__data_parser.parse(season, "penaltyMinutes", "none")
            skaterAdvancedStatsPenalties.set_penalty_minutes(penalty_minutes)

            time_on_ice_per_game = self.__data_parser.parse(season, "timeOnIcePerGame", "none")
            skaterAdvancedStatsPenalties.set_time_on_ice_per_game(time_on_ice_per_game)

            seasons.append(skaterAdvancedStatsPenalties)

        return seasons

    def __get_skater_advanced_stats_penalty_kill(self, skater_id) -> list[SkaterAdvancedStatsPenaltyKill]:
        url = f"https://api.nhle.com/stats/rest/en/skater/penaltykill?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsPenaltyKill = SkaterAdvancedStatsPenaltyKill(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsPenaltyKill.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsPenaltyKill.set_team_id(team_id)

            pk_assists = self.__data_parser.parse(season, "shAssists", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_assists(pk_assists)

            pk_goals = self.__data_parser.parse(season, "shGoals", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_goals(pk_goals)

            #TODO: Fix this, its actually for not against
            pk_individual_corsi_against = self.__data_parser.parse(season, "shIndividualSatFor", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_individual_corsi_against(pk_individual_corsi_against)

            pk_primary_assists = self.__data_parser.parse(season, "shPrimaryAssists", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_primary_assists(pk_primary_assists)

            pk_secondary_assists = self.__data_parser.parse(season, "shSecondaryAssists", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_secondary_assists(pk_secondary_assists)

            pk_shooting_percentage = self.__data_parser.parse(season, "shShootingPct", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_shooting_percentage(pk_shooting_percentage)

            pk_shots = self.__data_parser.parse(season, "shShots", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_shots(pk_shots)

            pk_time_on_ice = self.__data_parser.parse(season, "shTimeOnIce", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_time_on_ice(pk_time_on_ice)

            pk_time_on_ice_per_game = self.__data_parser.parse(season, "shTimeOnIcePerGame", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_time_on_ice_per_game(pk_time_on_ice_per_game)

            pk_time_on_ice_percentage = self.__data_parser.parse(season, "shTimeOnIcePctPerGame", "none")
            skaterAdvancedStatsPenaltyKill.set_pk_time_on_ice_percentage(pk_time_on_ice_percentage)

            seasons.append(skaterAdvancedStatsPenaltyKill)

        return seasons

    def __get_skater_advanced_stats_powerplay(self, skater_id) -> list[SkaterAdvancedStatsPowerplay]:
        url = f"https://api.nhle.com/stats/rest/en/skater/powerplay?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsPowerplay = SkaterAdvancedStatsPowerplay(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsPowerplay.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsPowerplay.set_team_id(team_id)

            pp_assists = self.__data_parser.parse(season, "ppAssists", "none")
            skaterAdvancedStatsPowerplay.set_pp_assists(pp_assists)

            pp_goals = self.__data_parser.parse(season, "ppGoals", "none")
            skaterAdvancedStatsPowerplay.set_pp_goals(pp_goals)

            pp_individual_corsi_for = self.__data_parser.parse(season, "ppIndividualSatFor", "none")
            skaterAdvancedStatsPowerplay.set_pp_individual_corsi_for(pp_individual_corsi_for)

            pp_primary_assists = self.__data_parser.parse(season, "ppPrimaryAssists", "none")
            skaterAdvancedStatsPowerplay.set_pp_primary_assists(pp_primary_assists)

            pp_secondary_assists = self.__data_parser.parse(season, "ppSecondaryAssists", "none")
            skaterAdvancedStatsPowerplay.set_pp_secondary_assists(pp_secondary_assists)

            pp_shooting_percentage = self.__data_parser.parse(season, "ppShootingPct", "none")
            skaterAdvancedStatsPowerplay.set_pp_shooting_percentage(pp_shooting_percentage)

            pp_shots = self.__data_parser.parse(season, "ppShots", "none")
            skaterAdvancedStatsPowerplay.set_pp_shots(pp_shots)

            pp_time_on_ice = self.__data_parser.parse(season, "ppTimeOnIce", "none")
            skaterAdvancedStatsPowerplay.set_pp_time_on_ice(pp_time_on_ice)

            pp_time_on_ice_per_game = self.__data_parser.parse(season, "ppTimeOnIcePerGame", "none")
            skaterAdvancedStatsPowerplay.set_pp_time_on_ice_per_game(pp_time_on_ice_per_game)

            pp_time_on_ice_percentage = self.__data_parser.parse(season, "ppTimeOnIcePctPerGame", "none")
            skaterAdvancedStatsPowerplay.set_pp_time_on_ice_percentage(pp_time_on_ice_percentage)

            seasons.append(skaterAdvancedStatsPowerplay)

        return seasons
                                                    
    def __get_skater_advanced_stats_scoring(self, skater_id) -> list[SkaterAdvancedStatsScoring]:
        url = f"https://api.nhle.com/stats/rest/en/skater/shottype?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsScoring = SkaterAdvancedStatsScoring(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsScoring.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsScoring.set_team_id(team_id)

            goals_backhand = self.__data_parser.parse(season, "goalsBackhand", "none")
            skaterAdvancedStatsScoring.set_goals_backhand(goals_backhand)

            goals_bat = self.__data_parser.parse(season, "goalsBat", "none")
            skaterAdvancedStatsScoring.set_goals_bat(goals_bat)

            goals_between_legs = self.__data_parser.parse(season, "goalsBetweenLegs", "none")
            skaterAdvancedStatsScoring.set_goals_between_legs(goals_between_legs)

            goals_cradle = self.__data_parser.parse(season, "goalsCradle", "none")
            skaterAdvancedStatsScoring.set_goals_cradle(goals_cradle)

            goals_deflected = self.__data_parser.parse(season, "goalsDeflected", "none")
            skaterAdvancedStatsScoring.set_goals_deflected(goals_deflected)

            goals_poke = self.__data_parser.parse(season, "goalsPoke", "none")
            skaterAdvancedStatsScoring.set_goals_poke(goals_poke)

            goals_slap = self.__data_parser.parse(season, "goalsSlap", "none")
            skaterAdvancedStatsScoring.set_goals_slap(goals_slap)

            goals_snap = self.__data_parser.parse(season, "goalsSnap", "none")
            skaterAdvancedStatsScoring.set_goals_snap(goals_snap)

            goals_tip = self.__data_parser.parse(season, "goalsTipIn", "none")
            skaterAdvancedStatsScoring.set_goals_tip(goals_tip)

            goals_wrap_around = self.__data_parser.parse(season, "goalsWrapAround", "none")
            skaterAdvancedStatsScoring.set_goals_wrap_around(goals_wrap_around)

            goals_wrist = self.__data_parser.parse(season, "goalsWrist", "none")
            skaterAdvancedStatsScoring.set_goals_wrist(goals_wrist)

            shots_backhand = self.__data_parser.parse(season, "shotsOnNetBackhand", "none")
            skaterAdvancedStatsScoring.set_shots_backhand(shots_backhand)

            shots_bat = self.__data_parser.parse(season, "shotsOnNetBat", "none")
            skaterAdvancedStatsScoring.set_shots_bat(shots_bat)

            shots_between_legs = self.__data_parser.parse(season, "shotsOnNetBetweenLegs", "none")
            skaterAdvancedStatsScoring.set_shots_between_legs(shots_between_legs)

            shots_cradle = self.__data_parser.parse(season, "shotsOnNetCradle", "none")
            skaterAdvancedStatsScoring.set_shots_cradle(shots_cradle)

            shots_deflected = self.__data_parser.parse(season, "shotsOnNetDeflected", "none")
            skaterAdvancedStatsScoring.set_shots_deflected(shots_deflected)

            shots_poke = self.__data_parser.parse(season, "shotsOnNetPoke", "none")
            skaterAdvancedStatsScoring.set_shots_poke(shots_poke)

            shots_slap = self.__data_parser.parse(season, "shotsOnNetSlap", "none")
            skaterAdvancedStatsScoring.set_shots_slap(shots_slap)

            shots_snap = self.__data_parser.parse(season, "shotsOnNetSnap", "none")
            skaterAdvancedStatsScoring.set_shots_snap(shots_snap)

            shots_tip = self.__data_parser.parse(season, "shotsOnNetTipIn", "none")
            skaterAdvancedStatsScoring.set_shots_tip(shots_tip)

            shots_wrap_around = self.__data_parser.parse(season, "shotsOnNetWrapAround", "none")
            skaterAdvancedStatsScoring.set_shots_wrap_around(shots_wrap_around)

            shots_wrist = self.__data_parser.parse(season, "shotsOnNetWrist", "none")
            skaterAdvancedStatsScoring.set_shots_wrist(shots_wrist)

            seasons.append(skaterAdvancedStatsScoring)

        return seasons

    def __get_skater_advanced_stats_shootout(self, skater_id) -> list[SkaterAdvancedStatsShootout]:
        url = f"https://api.nhle.com/stats/rest/en/skater/shootout?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsShootout = SkaterAdvancedStatsShootout(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsShootout.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsShootout.set_team_id(team_id)

            career_shootout_game_deciding_goals = self.__data_parser.parse(season, "careerShootoutGameDecidingGoals", "none")
            skaterAdvancedStatsShootout.set_career_shootout_game_deciding_goals(career_shootout_game_deciding_goals)

            career_shootout_games_played = self.__data_parser.parse(season, "careerShootoutGamesPlayed", "none")
            skaterAdvancedStatsShootout.set_career_shootout_games_played(career_shootout_games_played)

            career_shootout_goals = self.__data_parser.parse(season, "careerShootoutGoals", "none")
            skaterAdvancedStatsShootout.set_career_shootout_goals(career_shootout_goals)

            career_shootout_goals_percentage = self.__data_parser.parse(season, "careerShootoutShootingPct", "none")
            skaterAdvancedStatsShootout.set_career_shootout_percentage(career_shootout_goals_percentage)

            career_shootout_shots = self.__data_parser.parse(season, "careerShootoutShots", "none")
            skaterAdvancedStatsShootout.set_career_shootout_shots(career_shootout_shots)

            shootout_game_deciding_goals = self.__data_parser.parse(season, "shootoutGameDecidingGoals", "none")
            skaterAdvancedStatsShootout.set_shootout_game_deciding_goals(shootout_game_deciding_goals)

            shootout_games_played = self.__data_parser.parse(season, "shootoutGamesPlayed", "none")
            skaterAdvancedStatsShootout.set_shootout_games_played(shootout_games_played)

            shootout_goals = self.__data_parser.parse(season, "shootoutGoals", "none")
            skaterAdvancedStatsShootout.set_shootout_goals(shootout_goals)

            shootout_goals_percentage = self.__data_parser.parse(season, "shootoutShootingPct", "none")
            skaterAdvancedStatsShootout.set_shootout_percentage(shootout_goals_percentage)

            shootout_shots = self.__data_parser.parse(season, "shootoutShots", "none")
            skaterAdvancedStatsShootout.set_shootout_shots(shootout_shots)


            seasons.append(skaterAdvancedStatsShootout)

        return seasons

    def __get_skater_advanced_stats_toi(self, skater_id) -> list[SkaterAdvancedStatsTOI]:
        url = f"https://api.nhle.com/stats/rest/en/skater/timeonice?cayenneExp=playerId={skater_id}"
        data = self.__api_connector.get_json(url)

        seasons = []

        for season in self.__data_parser.parse(data, "data", "empty_list"):
            skaterAdvancedStatsTOI = SkaterAdvancedStatsTOI(skater_id)

            year = self.__data_parser.parse(season, "seasonId", "none")
            skaterAdvancedStatsTOI.set_year(year)

            team_id = self.__util.get_team_id_from_abbrev(self.__data_parser.parse(season, "teamAbbrevs", "none"))
            skaterAdvancedStatsTOI.set_team_id(team_id)

            ev_time_on_ice = self.__data_parser.parse(season, "evTimeOnIce", "none")
            skaterAdvancedStatsTOI.set_ev_time_on_ice(ev_time_on_ice)

            games_played = self.__data_parser.parse(season, "gamesPlayed", "none")
            skaterAdvancedStatsTOI.set_games_played(games_played)

            ot_time_on_ice = self.__data_parser.parse(season, "otTimeOnIce", "none")
            skaterAdvancedStatsTOI.set_ot_time_on_ice(ot_time_on_ice)

            ot_time_on_ice_per_ot_game = self.__data_parser.parse(season, "otTimeOnIcePerOtGame", "none")
            skaterAdvancedStatsTOI.set_ot_time_on_ice_per_ot_game(ot_time_on_ice_per_ot_game)

            pp_time_on_ice = self.__data_parser.parse(season, "ppTimeOnIce", "none")
            skaterAdvancedStatsTOI.set_pp_time_on_ice(pp_time_on_ice)

            sh_time_on_ice = self.__data_parser.parse(season, "shTimeOnIce", "none")
            skaterAdvancedStatsTOI.set_sh_time_on_ice(sh_time_on_ice)

            shifts = self.__data_parser.parse(season, "shifts", "none")
            skaterAdvancedStatsTOI.set_shifts(shifts)

            time_on_ice = self.__data_parser.parse(season, "timeOnIce", "none")
            skaterAdvancedStatsTOI.set_time_on_ice(time_on_ice)

            seasons.append(skaterAdvancedStatsTOI)

        return seasons

    def __get_all_skaters(self):
        query = "SELECT id FROM player_details WHERE position <> 'G';"
        res = self.__database_operator.read(query)
        skater_ids = []
        for row in res:
            skater_ids.append(row[0])
        self.__skater_ids = skater_ids

