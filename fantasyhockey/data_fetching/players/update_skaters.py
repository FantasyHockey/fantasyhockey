from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.fetch_skaters import FetchSkaters
from fantasyhockey.data_fetching.players.models.skaters.skater_stats import SkaterStats
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_toi import SkaterAdvancedStatsTOI
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_shootout import SkaterAdvancedStatsShootout
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_scoring import SkaterAdvancedStatsScoring
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_powerplay import SkaterAdvancedStatsPowerplay
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_penalty_kill import SkaterAdvancedStatsPenaltyKill
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_penalties import SkaterAdvancedStatsPenalties
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_misc import SkaterAdvancedStatsMisc
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_goals import SkaterAdvancedStatsGoals
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_faceoffs import SkaterAdvancedStatsFaceoffs
from fantasyhockey.data_fetching.players.models.skaters.skater_advanced_stats_corsi_fenwick import SkaterAdvancedStatsCorsiFenwick
from fantasyhockey.data_fetching.players.models.skaters.youth_skater_stats import YouthSkaterStats


class UpdateSkaters:
    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_skaters = FetchSkaters()


    def write_in_db(self):
        """Write player data to the database."""
        skaters = self.fetch_skaters.get_skaters()
        count = 0
        for skater in skaters:
            count += 1
            print(f"Writing skater {count} / {len(skaters)} to database.")
            try:
                skater_stats = skater.get_skater_stats()
                for stats in skater_stats:
                    query, params = self.__create_skater_stats_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} stats to database.")
                print(e)

            try:
                advanced_stats_toi = skater.get_advanced_stats_toi()
                for stats in advanced_stats_toi:
                    query, params = self.__create_skater_advanced_stats_toi_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced toi stats to database.")
                print(e)

            try:
                advanced_stats_shootout = skater.get_advanced_stats_shootout()
                for stats in advanced_stats_shootout:
                    query, params = self.__create_skater_advanced_stats_shootout_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced shootout stats to database.")
                print(e)

            try:
                advanced_stats_scoring = skater.get_advanced_stats_scoring()
                for stats in advanced_stats_scoring:
                    query, params = self.__create_skater_advanced_stats_scoring_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced scoring stats to database.")
                print(e)

            try:
                advanced_stats_powerplay = skater.get_advanced_stats_powerplay()
                for stats in advanced_stats_powerplay:
                    query, params = self.__create_skater_advanced_stats_powerplay_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced powerplay stats to database.")
                print(e)

            try:
                advanced_stats_penalty_kill = skater.get_advanced_stats_penalty_kill()
                for stats in advanced_stats_penalty_kill:
                    query, params = self.__create_skater_advanced_stats_penalty_kill_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced penalty kill stats to database.")
                print(e)

            try:
                advanced_stats_penalties = skater.get_advanced_stats_penalties()
                for stats in advanced_stats_penalties:
                    query, params = self.__create_skater_advanced_stats_penalties_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced penalties stats to database.")
                print(e)

            try:
                advanced_stats_misc = skater.get_advanced_stats_misc()
                for stats in advanced_stats_misc:
                    query, params = self.__create_skater_advanced_stats_misc_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced misc stats to database.")
                print(e)

            try:
                advanced_stats_goals = skater.get_advanced_stats_goals()
                for stats in advanced_stats_goals:
                    query, params = self.__create_skater_advanced_stats_goals_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced goals stats to database.")
                print(e)

            try:
                advanced_stats_faceoffs = skater.get_advanced_stats_faceoffs()
                for stats in advanced_stats_faceoffs:
                    query, params = self.__create_skater_advanced_stats_faceoffs_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced faceoffs stats to database.")
                print(e)

            try:
                advanced_stats_corsi_fenwick = skater.get_advanced_stats_corsi_fenwick()
                for stats in advanced_stats_corsi_fenwick:
                    query, params = self.__create_skater_advanced_stats_corsi_fenwick_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} advanced corsi fenwick stats to database.")
                print(e)

            try:
                youth_stats = skater.get_youth_stats()
                for stats in youth_stats:
                    query, params = self.__create_youth_stats_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {skater.get_id()} youth stats to database.")
                print(e)

    def update_in_db(self):
        """Update player data in the database."""
        pass

    def __create_skater_stats_query(self, skater_stats: SkaterStats) -> tuple:

        query = "INSERT INTO skater_stats (id, team_id, games_played, goals, assists, points, plus_minus, penalty_minutes,\
            game_winning_goals, ot_goals, power_play_goals, power_play_points, shooting_percent, shorthanded_goals, shorthanded_points,\
            shots, time_on_ice, game_type_id, year, sequence, faceoff_percent) VALUES (%s, %s, %s,\
            %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s, %s, %s, %s, %s, %s, %s)"
        params = (skater_stats.get_player_id(), skater_stats.get_team_id(), skater_stats.get_games_played(), skater_stats.get_goals(),\
                  skater_stats.get_assists(), skater_stats.get_points(), skater_stats.get_plus_minus(), skater_stats.get_penalty_minutes(),\
                    skater_stats.get_game_winning_goals(), skater_stats.get_ot_goals(), skater_stats.get_power_play_goals(),\
                    skater_stats.get_power_play_points(), skater_stats.get_shooting_percentage(), skater_stats.get_shorthanded_goals(),\
                    skater_stats.get_shorthanded_points(), skater_stats.get_shots(), skater_stats.get_time_on_ice(), skater_stats.get_game_type_id(),\
                    skater_stats.get_year(), skater_stats.get_sequence(), skater_stats.get_faceoff_percentage())
        
        return query, params
        


    def __create_skater_advanced_stats_toi_query(self, skater_advanced_stats_toi: SkaterAdvancedStatsTOI) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_toi (id, year, team_id, ev_time_on_ice, games_played, ot_time_on_ice,\
            ot_time_on_ice_per_ot_game, pp_time_on_ice, sh_time_on_ice, shifts, time_on_ice) VALUES (%s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (skater_advanced_stats_toi.get_player_id(), skater_advanced_stats_toi.get_year(),\
                  skater_advanced_stats_toi.get_team_id(), skater_advanced_stats_toi.get_ev_time_on_ice(),\
                skater_advanced_stats_toi.get_games_played(), skater_advanced_stats_toi.get_ot_time_on_ice(),\
                skater_advanced_stats_toi.get_ot_time_on_ice_per_ot_game(), skater_advanced_stats_toi.get_pp_time_on_ice(),\
                skater_advanced_stats_toi.get_sh_time_on_ice(), skater_advanced_stats_toi.get_shifts(),\
                skater_advanced_stats_toi.get_time_on_ice())
        
        return query, params
            
        

    def __create_skater_advanced_stats_shootout_query(self, skater_advanced_stats_shootout: SkaterAdvancedStatsShootout) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_shootout (id, year, team_id, career_shootout_game_deciding_goals,\
            career_shootout_games_played, career_shootout_goals, career_shootout_percentage, career_shootout_shots,\
            shootout_game_deciding_goals, shootout_games_played, shootout_goals, shootout_percentage, shootout_shots) VALUES (%s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (skater_advanced_stats_shootout.get_player_id(), skater_advanced_stats_shootout.get_year(),\
                    skater_advanced_stats_shootout.get_team_id(), skater_advanced_stats_shootout.get_career_shootout_game_deciding_goals(),\
                    skater_advanced_stats_shootout.get_career_shootout_games_played(), skater_advanced_stats_shootout.get_career_shootout_goals(),\
                    skater_advanced_stats_shootout.get_career_shootout_percentage(), skater_advanced_stats_shootout.get_career_shootout_shots(),\
                    skater_advanced_stats_shootout.get_shootout_game_deciding_goals(), skater_advanced_stats_shootout.get_shootout_games_played(),\
                    skater_advanced_stats_shootout.get_shootout_goals(), skater_advanced_stats_shootout.get_shootout_percentage(),\
                    skater_advanced_stats_shootout.get_shootout_shots())
        
        return query, params
        

    def __create_skater_advanced_stats_scoring_query(self, skater_advanced_stats_scoring: SkaterAdvancedStatsScoring) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_scoring (id, year, team_id, goals_backhand, goals_bat, goals_between_legs, goals_cradle,\
                goals_deflected, goals_poke, goals_slap, goals_snap, goals_tip, goals_wrap_around, goals_wrist, shots_backhand, shots_bat,\
                shots_between_legs, shots_cradle, shots_deflected, shots_poke, shots_slap, shots_snap, shots_tip, shots_wrap_around,\
                shots_wrist) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (skater_advanced_stats_scoring.get_player_id(), skater_advanced_stats_scoring.get_year(), skater_advanced_stats_scoring.get_team_id(),\
                skater_advanced_stats_scoring.get_goals_backhand(), skater_advanced_stats_scoring.get_goals_bat(), skater_advanced_stats_scoring.get_goals_between_legs(),\
                skater_advanced_stats_scoring.get_goals_cradle(), skater_advanced_stats_scoring.get_goals_deflected(), skater_advanced_stats_scoring.get_goals_poke(),\
                skater_advanced_stats_scoring.get_goals_slap(), skater_advanced_stats_scoring.get_goals_snap(), skater_advanced_stats_scoring.get_goals_tip(),\
                skater_advanced_stats_scoring.get_goals_wrap_around(), skater_advanced_stats_scoring.get_goals_wrist(), skater_advanced_stats_scoring.get_shots_backhand(),\
                skater_advanced_stats_scoring.get_shots_bat(), skater_advanced_stats_scoring.get_shots_between_legs(), skater_advanced_stats_scoring.get_shots_cradle(),\
                skater_advanced_stats_scoring.get_shots_deflected(), skater_advanced_stats_scoring.get_shots_poke(), skater_advanced_stats_scoring.get_shots_slap(),\
                skater_advanced_stats_scoring.get_shots_snap(), skater_advanced_stats_scoring.get_shots_tip(), skater_advanced_stats_scoring.get_shots_wrap_around(),\
                skater_advanced_stats_scoring.get_shots_wrist())
        
        return query, params

    def __create_skater_advanced_stats_powerplay_query(self, skater_advanced_stats_powerplay: SkaterAdvancedStatsPowerplay) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_powerplay (id, year, team_id, pp_assists, pp_goals, pp_individual_corsi_for, pp_primary_assists, pp_secondary_assists,\
                pp_shooting_percent, pp_shots, pp_time_on_ice, pp_time_on_ice_per_game, pp_time_on_ice_percent) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        
        params = (skater_advanced_stats_powerplay.get_player_id(), skater_advanced_stats_powerplay.get_year(), skater_advanced_stats_powerplay.get_team_id(),\
                skater_advanced_stats_powerplay.get_pp_assists(), skater_advanced_stats_powerplay.get_pp_goals(), skater_advanced_stats_powerplay.get_pp_individual_corsi_for(),\
                skater_advanced_stats_powerplay.get_pp_primary_assists(), skater_advanced_stats_powerplay.get_pp_secondary_assists(), skater_advanced_stats_powerplay.get_pp_shooting_percentage(),\
                skater_advanced_stats_powerplay.get_pp_shots(), skater_advanced_stats_powerplay.get_pp_time_on_ice(), skater_advanced_stats_powerplay.get_pp_time_on_ice_per_game(),\
                skater_advanced_stats_powerplay.get_pp_time_on_ice_percentage())
        
        return query, params

    def __create_skater_advanced_stats_penalty_kill_query(self, skater_advanced_stats_penalty_kill: SkaterAdvancedStatsPenaltyKill) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_penalty_kill (id, year, team_id, pk_assists, pk_goals, pk_individual_corsi_against, pk_primary_assists,\
                pk_secondary_assists, pk_shooting_percent, pk_shots, pk_time_on_ice, pk_time_on_ice_per_game, pk_time_on_ice_percent)\
                VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"

        
        params = (skater_advanced_stats_penalty_kill.get_player_id(), skater_advanced_stats_penalty_kill.get_year(), skater_advanced_stats_penalty_kill.get_team_id(),\
                skater_advanced_stats_penalty_kill.get_pk_assists(), skater_advanced_stats_penalty_kill.get_pk_goals(), skater_advanced_stats_penalty_kill.get_pk_individual_corsi_against(),\
                skater_advanced_stats_penalty_kill.get_pk_primary_assists(), skater_advanced_stats_penalty_kill.get_pk_secondary_assists(), skater_advanced_stats_penalty_kill.get_pk_shooting_percentage(),\
                skater_advanced_stats_penalty_kill.get_pk_shots(), skater_advanced_stats_penalty_kill.get_pk_time_on_ice(), skater_advanced_stats_penalty_kill.get_pk_time_on_ice_per_game(),\
                skater_advanced_stats_penalty_kill.get_pk_time_on_ice_percentage())
        
        return query, params

    def __create_skater_advanced_stats_penalties_query(self, skater_advanced_stats_penalties: SkaterAdvancedStatsPenalties) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_penalties (id, year, team_id, game_misconduct_penalties, games_played, major_penalties,\
                match_penalties, minor_penalties, misconduct_penalties, net_penalties, penalties, penalties_drawn, penalty_minutes, time_on_ice_per_game)\
                VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        
        params = (skater_advanced_stats_penalties.get_player_id(), skater_advanced_stats_penalties.get_year(), skater_advanced_stats_penalties.get_team_id(),\
                skater_advanced_stats_penalties.get_game_misconduct_penalties(), skater_advanced_stats_penalties.get_games_played(), skater_advanced_stats_penalties.get_major_penalties(),\
                skater_advanced_stats_penalties.get_match_penalties(), skater_advanced_stats_penalties.get_minor_penalties(), skater_advanced_stats_penalties.get_misconduct_penalties(),\
                skater_advanced_stats_penalties.get_net_penalties(), skater_advanced_stats_penalties.get_penalties(), skater_advanced_stats_penalties.get_penalties_drawn(),\
                skater_advanced_stats_penalties.get_penalty_minutes(), skater_advanced_stats_penalties.get_time_on_ice_per_game())
        
        return query, params

    def __create_skater_advanced_stats_misc_query(self, skater_advanced_stats_misc: SkaterAdvancedStatsMisc) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_misc (id, year, team_id, blocked_shots, empty_net_assists, empty_net_goals, empty_net_points,\
                first_goals, giveaways, games_played, hits, missed_shot_crossbar, missed_shot_goalpost, missed_shot_over, missed_shot_wide,\
                missed_shots, ot_goals, takeaways, time_on_ice_per_game) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        
        params = (skater_advanced_stats_misc.get_player_id(), skater_advanced_stats_misc.get_year(), skater_advanced_stats_misc.get_team_id(),\
                skater_advanced_stats_misc.get_blocked_shots(), skater_advanced_stats_misc.get_empty_net_assists(), skater_advanced_stats_misc.get_empty_net_goals(),\
                skater_advanced_stats_misc.get_empty_net_points(), skater_advanced_stats_misc.get_first_goals(), skater_advanced_stats_misc.get_giveaways(),\
                skater_advanced_stats_misc.get_games_played(), skater_advanced_stats_misc.get_hits(), skater_advanced_stats_misc.get_missed_shot_crossbar(),\
                skater_advanced_stats_misc.get_missed_shot_goalpost(), skater_advanced_stats_misc.get_missed_shot_over(), skater_advanced_stats_misc.get_missed_shot_wide(),\
                skater_advanced_stats_misc.get_missed_shots(), skater_advanced_stats_misc.get_ot_goals(), skater_advanced_stats_misc.get_takeaways(),\
                skater_advanced_stats_misc.get_time_on_ice_per_game())
        
        return query, params

    def __create_skater_advanced_stats_goals_query(self, skater_advanced_stats_goals: SkaterAdvancedStatsGoals) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_goals (id, year, team_id, even_strength_goal_difference, even_strength_goals_against, even_strength_goals_for,\
                even_strength_time_on_ice_per_game, games_played, pp_goals_for, pp_goals_against, pk_goals_for, pk_goals_against)\
                VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        
        params = (skater_advanced_stats_goals.get_player_id(), skater_advanced_stats_goals.get_year(), skater_advanced_stats_goals.get_team_id(),\
                skater_advanced_stats_goals.get_even_strength_goal_difference(), skater_advanced_stats_goals.get_even_strength_goals_against(), skater_advanced_stats_goals.get_even_strength_goals_for(),\
                skater_advanced_stats_goals.get_even_strength_time_on_ice_per_game(), skater_advanced_stats_goals.get_games_played(), skater_advanced_stats_goals.get_pp_goals_for(),\
                skater_advanced_stats_goals.get_pp_goals_against(), skater_advanced_stats_goals.get_pk_goals_for(), skater_advanced_stats_goals.get_pk_goals_against())
        
        return query, params

    def __create_skater_advanced_stats_faceoffs_query(self, skater_advanced_stats_faceoffs: SkaterAdvancedStatsFaceoffs) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_faceoffs (id, year, team_id, defensive_zone_faceoffs, defensive_zone_faceoffs_won, defensive_zone_faceoffs_lost,\
                ev_faceoffs, ev_faceoffs_won, ev_faceoffs_lost, faceoff_percent, neutral_zone_faceoffs, neutral_zone_faceoffs_won, neutral_zone_faceoffs_lost,\
                offensive_zone_faceoffs, offensive_zone_faceoffs_won, offensive_zone_faceoffs_lost, pp_faceoffs, pp_faceoffs_won, pp_faceoffs_lost, pk_faceoffs,\
                pk_faceoffs_won, pk_faceoffs_lost, total_faceoffs, total_faceoffs_won, total_faceoffs_lost) VALUES (%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,\
                %s,%s, %s,%s, %s,%s,%s, %s,%s, %s)"
        
        params = (skater_advanced_stats_faceoffs.get_player_id(), skater_advanced_stats_faceoffs.get_year(), skater_advanced_stats_faceoffs.get_team_id(),\
                skater_advanced_stats_faceoffs.get_defensive_zone_faceoffs(), skater_advanced_stats_faceoffs.get_defensive_zone_faceoffs_won(), skater_advanced_stats_faceoffs.get_defensive_zone_faceoffs_lost(),\
                skater_advanced_stats_faceoffs.get_ev_faceoffs(), skater_advanced_stats_faceoffs.get_ev_faceoffs_won(), skater_advanced_stats_faceoffs.get_ev_faceoffs_lost(),\
                skater_advanced_stats_faceoffs.get_faceoff_percentage(), skater_advanced_stats_faceoffs.get_neutral_zone_faceoffs(), skater_advanced_stats_faceoffs.get_neutral_zone_faceoffs_won(),\
                skater_advanced_stats_faceoffs.get_neutral_zone_faceoffs_lost(), skater_advanced_stats_faceoffs.get_offensive_zone_faceoffs(), skater_advanced_stats_faceoffs.get_offensive_zone_faceoffs_won(),\
                skater_advanced_stats_faceoffs.get_offensive_zone_faceoffs_lost(), skater_advanced_stats_faceoffs.get_pp_faceoffs(), skater_advanced_stats_faceoffs.get_pp_faceoffs_won(),\
                skater_advanced_stats_faceoffs.get_pp_faceoffs_lost(), skater_advanced_stats_faceoffs.get_pk_faceoffs(), skater_advanced_stats_faceoffs.get_pk_faceoffs_won(),\
                skater_advanced_stats_faceoffs.get_pk_faceoffs_lost(), skater_advanced_stats_faceoffs.get_total_faceoffs(), skater_advanced_stats_faceoffs.get_total_faceoffs_won(),\
                skater_advanced_stats_faceoffs.get_total_faceoffs_lost())
        
        return query, params

    def __create_skater_advanced_stats_corsi_fenwick_query(self, skater_advanced_stats_corsi_fenwick: SkaterAdvancedStatsCorsiFenwick) -> tuple:
        
        query = "INSERT INTO skater_advanced_stats_corsi_fenwick (id, year, team_id, games_played, corsi_against, corsi_ahead, corsi_behind, corsi_close,\
                corsi_for, corsi_tied, corsi_total, fenwick_against, fenwick_ahead, fenwick_behind, fenwick_close, fenwick_for, fenwick_relative, fenwick_tied,\
                fenwick_total, corsi_percent, corsi_ahead_percent, corsi_behind_percent, corsi_close_percent, corsi_tied_percent, corsi_relative, shooting_percent_5on5,\
                skater_save_percent_5on5, skater_shooting_plus_save_percent_5on5, time_on_ice_5on5_per_game, fenwick_percent, fenwick_ahead_percent, fenwick_behind_percent,\
                fenwick_close_percent, fenwick_tied_percent, zone_start_5on5_percent) VALUES (%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s,\
                %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s,%s, %s,%s, %s)"
        
        params = (skater_advanced_stats_corsi_fenwick.get_player_id(), skater_advanced_stats_corsi_fenwick.get_year(), skater_advanced_stats_corsi_fenwick.get_team_id(),\
                skater_advanced_stats_corsi_fenwick.get_games_played(), skater_advanced_stats_corsi_fenwick.get_corsi_against(), skater_advanced_stats_corsi_fenwick.get_corsi_ahead(),\
                skater_advanced_stats_corsi_fenwick.get_corsi_behind(), skater_advanced_stats_corsi_fenwick.get_corsi_close(), skater_advanced_stats_corsi_fenwick.get_corsi_for(),\
                skater_advanced_stats_corsi_fenwick.get_corsi_tied(), skater_advanced_stats_corsi_fenwick.get_corsi_total(), skater_advanced_stats_corsi_fenwick.get_fenwick_against(),\
                skater_advanced_stats_corsi_fenwick.get_fenwick_ahead(), skater_advanced_stats_corsi_fenwick.get_fenwick_behind(), skater_advanced_stats_corsi_fenwick.get_fenwick_close(),\
                skater_advanced_stats_corsi_fenwick.get_fenwick_for(), skater_advanced_stats_corsi_fenwick.get_fenwick_relative(), skater_advanced_stats_corsi_fenwick.get_fenwick_tied(),\
                skater_advanced_stats_corsi_fenwick.get_fenwick_total(), skater_advanced_stats_corsi_fenwick.get_corsi_percentage(), skater_advanced_stats_corsi_fenwick.get_corsi_ahead_percentage(),\
                skater_advanced_stats_corsi_fenwick.get_corsi_behind_percentage(), skater_advanced_stats_corsi_fenwick.get_corsi_close_percentage(), skater_advanced_stats_corsi_fenwick.get_corsi_tied_percentage(),\
                skater_advanced_stats_corsi_fenwick.get_corsi_relative(), skater_advanced_stats_corsi_fenwick.get_shooting_percent_5on5(), skater_advanced_stats_corsi_fenwick.get_skater_save_percent_5on5(),\
                skater_advanced_stats_corsi_fenwick.get_skater_shooting_plus_save_percent_5on5(), skater_advanced_stats_corsi_fenwick.get_time_on_ice_5on5_per_game(),\
                skater_advanced_stats_corsi_fenwick.get_fenwick_percentage(), skater_advanced_stats_corsi_fenwick.get_fenwick_ahead_percentage(), skater_advanced_stats_corsi_fenwick.get_fenwick_behind_percentage(),\
                skater_advanced_stats_corsi_fenwick.get_fenwick_close_percentage(), skater_advanced_stats_corsi_fenwick.get_fenwick_tied_percentage(), skater_advanced_stats_corsi_fenwick.get_zone_start_5on5_percentage())
        
        return query, params

    def __create_youth_stats_query(self, youth_stats: YouthSkaterStats) -> tuple:
        
        query = "INSERT INTO skater_youth_stats (id, year, team_name, league_name, game_type_id, sequence, games_played, goals, assists,\
                points, pim) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
        
        params = (youth_stats.get_player_id(), youth_stats.get_year(), youth_stats.get_team_name(), youth_stats.get_league_name(),\
                youth_stats.get_game_type_id(), youth_stats.get_sequence(), youth_stats.get_games_played(), youth_stats.get_goals(),\
                youth_stats.get_assists(), youth_stats.get_points(), youth_stats.get_pim())
        
        return query, params

