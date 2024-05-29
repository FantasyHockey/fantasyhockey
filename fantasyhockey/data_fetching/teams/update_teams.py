from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.teams.fetch_teams import FetchTeams

class UpdateTeams:
    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_teams = FetchTeams()

    def write_in_db(self):
        teams = self.fetch_teams.get_teams()
        for team in teams:
            #teams_query, teams_params = self.__create_teams_query(team)
            #team_stats_query, team_stats_params = self.__create_team_stats_query(team)
            #self.database_operator.write(teams_query, teams_params)
            #self.database_operator.write(team_stats_query, team_stats_params)

            advanced_stats_days_rest = team.get_team_advanced_stats_days_rest()
            for season in advanced_stats_days_rest:
                try:
                    query, params = self.__create_team_advanced_stats_days_rest_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats days rest for team " + season.get_team_id())
                    print(e)
                    continue

            '''advanced_stats_corsi_fenwick = team.get_team_advanced_stats_corsi_fenwick()
            for season in advanced_stats_corsi_fenwick:
                try:
                    query, params = self.__create_team_advanced_stats_corsi_fenwick_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats corsi fenwick for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_shot_type = team.get_team_advanced_stats_shot_type()
            for season in advanced_stats_shot_type:
                try:
                    query, params = self.__create_team_advanced_stats_shot_type_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats shot type for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_outshoot_outshot = team.get_team_advanced_stats_outshoot_outshot()
            for season in advanced_stats_outshoot_outshot:
                try:
                    query, params = self.__create_team_advanced_stats_outshoot_outshot_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats outshoot outshot for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_faceoff_percent = team.get_team_advanced_stats_faceoff_percent()
            for season in advanced_stats_faceoff_percent:
                try:
                    query, params = self.__create_team_advanced_stats_faceoff_percent_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats faceoff percent for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_goals_by_period = team.get_team_advanced_stats_goals_by_period()
            for season in advanced_stats_goals_by_period:
                try:
                    query, params = self.__create_team_advanced_stats_goals_by_period_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats goals by period for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_goals_by_strength = team.get_team_advanced_stats_goals_by_strength()
            for season in advanced_stats_goals_by_strength:
                try:
                    query, params = self.__create_team_advanced_stats_goals_by_strength_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats goals by strength for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_leading_trailing = team.get_team_advanced_stats_leading_trailing()
            for season in advanced_stats_leading_trailing:
                try:
                    query, params = self.__create_team_advanced_stats_leading_trailing_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats leading trailing for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_misc = team.get_team_advanced_stats_misc()
            for season in advanced_stats_misc:
                try:
                    query, params = self.__create_team_advanced_stats_misc_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats misc for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_penalties = team.get_team_advanced_penalties()
            for season in advanced_penalties:
                try:
                    query, params = self.__create_team_advanced_penalties_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced penalties for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_powerplay_penalty_kill = team.get_team_advanced_stats_powerplay_penalty_kill()
            for season in advanced_stats_powerplay_penalty_kill:
                try:
                    query, params = self.__create_team_advanced_stats_powerplay_penalty_kill_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats powerplay penalty kill for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_scoring_first = team.get_team_advanced_stats_scoring_first()
            for season in advanced_stats_scoring_first:
                try:
                    query, params = self.__create_team_advanced_stats_scoring_first_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats scoring first for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue

            advanced_stats_team_goal_games = team.get_team_advanced_stats_team_goal_games()
            for season in advanced_stats_team_goal_games:
                try:
                    query, params = self.__create_team_advanced_stats_team_goal_games_query(season)
                    self.database_operator.write(query, params)
                except Exception as e:
                    print("Error in writing advanced stats team goal games for team " + team.get_team_data().get_team_id())
                    print(e)
                    continue'''


    def update_in_db(self):
        teams = self.fetch_teams.get_teams()
        for team in teams:
            teams_query, teams_params = self.__update_teams_query(team)
            team_stats_query, team_stats_params = self.__update_team_stats_query(team)
            #self.database_operator.write(teams_query, teams_params)
            #self.database_operator.write(team_stats_query, team_stats_params)

    def __create_teams_query(self, team):
        query = "INSERT INTO teams (team_id, year, conference_name, division_name, place_name, team_name, team_abbreviation, team_logo,\
                team_color_1, team_color_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (team.get_team_id(), team.get_team_data().get_year(), team.get_team_data().get_conference_name(), 
                    team.get_team_data().get_division_name(), team.get_team_data().get_location_name(), team.get_team_data().get_team_name(),
                    team.get_team_data().get_team_abbreviation(), team.get_team_data().get_team_logo(), team.get_team_data().get_team_color_1(),
                    team.get_team_data().get_team_color_2())
        return query, params

    def __create_team_stats_query(self, team):
        query = "INSERT INTO team_stats (team_id, year, game_type_id, games_played, goals_against, goals_for, losses, ot_losses, points,\
                shootout_losses, shootout_wins, streak_code, streak_count, ties, waiver_sequence, regulation_wins, regulation_plus_ot_wins,\
                home_games_played, home_goals_against, home_goals_for, home_losses, home_ot_losses, home_points, home_regulation_wins,\
                home_regulation_plus_ot_wins, home_ties, home_wins, last_10_games_played, last_10_goals_against, last_10_goals_for,\
                last_10_losses, last_10_ot_losses, last_10_points, last_10_regulation_wins, last_10_regulation_plus_ot_wins, last_10_ties,\
                last_10_wins, road_games_played, road_goals_against, road_goals_for, road_losses, road_ot_losses, road_points,\
                road_regulation_wins, road_regulation_plus_ot_wins, road_ties, road_wins)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (team.get_team_id(), team.get_team_stats().get_year(), team.get_team_stats().get_game_type_id(), team.get_team_stats().get_games_played(),
                    team.get_team_stats().get_goals_against(), team.get_team_stats().get_goals_for(), team.get_team_stats().get_losses(),
                    team.get_team_stats().get_ot_losses(), team.get_team_stats().get_points(), team.get_team_stats().get_shootout_losses(),
                    team.get_team_stats().get_shootout_wins(), team.get_team_stats().get_streak_code(), team.get_team_stats().get_streak_count(),
                    team.get_team_stats().get_ties(), team.get_team_stats().get_waiver_sequence(), team.get_team_stats().get_regulation_wins(),
                    team.get_team_stats().get_regulation_plus_ot_wins(), team.get_team_stats().get_home_games_played(), team.get_team_stats().get_home_goals_against(),
                    team.get_team_stats().get_home_goals_for(), team.get_team_stats().get_home_losses(), team.get_team_stats().get_home_ot_losses(),
                    team.get_team_stats().get_home_points(), team.get_team_stats().get_home_regulation_wins(), team.get_team_stats().get_home_regulation_plus_ot_wins(),
                    team.get_team_stats().get_home_ties(), team.get_team_stats().get_home_wins(), team.get_team_stats().get_last_10_games_played(),
                    team.get_team_stats().get_last_10_goals_against(), team.get_team_stats().get_last_10_goals_for(), team.get_team_stats().get_last_10_losses(),
                    team.get_team_stats().get_last_10_ot_losses(), team.get_team_stats().get_last_10_points(), team.get_team_stats().get_last_10_regulation_wins(),
                    team.get_team_stats().get_last_10_regulation_plus_ot_wins(), team.get_team_stats().get_last_10_ties(), team.get_team_stats().get_last_10_wins(),
                    team.get_team_stats().get_road_games_played(), team.get_team_stats().get_road_goals_against(), team.get_team_stats().get_road_goals_for(),
                    team.get_team_stats().get_road_losses(), team.get_team_stats().get_road_ot_losses(), team.get_team_stats().get_road_points(),
                    team.get_team_stats().get_road_regulation_wins(), team.get_team_stats().get_road_regulation_plus_ot_wins(), team.get_team_stats().get_road_ties(),
                    team.get_team_stats().get_road_wins())
        
        return query, params

    def __update_teams_query(self, team):
        query = "UPDATE teams SET year = %s, conference_name = %s, division_name = %s, place_name = %s, team_name = %s, team_abbreviation = %s,\
                team_logo = %s, team_color_1 = %s, team_color_2 = %s WHERE team_id = %s"
        params = (team.get_team_data().get_year(), team.get_team_data().get_conference_name(), team.get_team_data().get_division_name(), 
                    team.get_team_data().get_location_name(), team.get_team_data().get_team_name(), team.get_team_data().get_team_abbreviation(),
                    team.get_team_data().get_team_logo(), team.get_team_data().get_team_color_1(), team.get_team_data().get_team_color_2(),
                    team.get_team_id())
        return query, params
    
    def __update_team_stats_query(self, team):
        query = "UPDATE team_stats SET year = %s, game_type_id = %s, games_played = %s, goals_against = %s, goals_for = %s, losses = %s,\
                ot_losses = %s, points = %s, shootout_losses = %s, shootout_wins = %s, streak_code = %s, streak_count = %s, ties = %s,\
                waiver_sequence = %s, regulation_wins = %s, regulation_plus_ot_wins = %s, home_games_played = %s, home_goals_against = %s,\
                home_goals_for = %s, home_losses = %s, home_ot_losses = %s, home_points = %s, home_regulation_wins = %s, home_regulation_plus_ot_wins = %s,\
                home_ties = %s, home_wins = %s, last_10_games_played = %s, last_10_goals_against = %s, last_10_goals_for = %s, last_10_losses = %s,\
                last_10_ot_losses = %s, last_10_points = %s, last_10_regulation_wins = %s, last_10_regulation_plus_ot_wins = %s, last_10_ties = %s,\
                last_10_wins = %s, road_games_played = %s, road_goals_against = %s, road_goals_for = %s, road_losses = %s, road_ot_losses = %s,\
                road_points = %s, road_regulation_wins = %s, road_regulation_plus_ot_wins = %s, road_ties = %s, road_wins = %s WHERE team_id = %s AND year = %s AND game_type_id = %s"
        params = (team.get_team_stats().get_year(), team.get_team_stats().get_game_type_id(), team.get_team_stats().get_games_played(),
                    team.get_team_stats().get_goals_against(), team.get_team_stats().get_goals_for(), team.get_team_stats().get_losses(),
                    team.get_team_stats().get_ot_losses(), team.get_team_stats().get_points(), team.get_team_stats().get_shootout_losses(),
                    team.get_team_stats().get_shootout_wins(), team.get_team_stats().get_streak_code(), team.get_team_stats().get_streak_count(),
                    team.get_team_stats().get_ties(), team.get_team_stats().get_waiver_sequence(), team.get_team_stats().get_regulation_wins(),
                    team.get_team_stats().get_regulation_plus_ot_wins(), team.get_team_stats().get_home_games_played(), team.get_team_stats().get_home_goals_against(),
                    team.get_team_stats().get_home_goals_for(), team.get_team_stats().get_home_losses(), team.get_team_stats().get_home_ot_losses(),
                    team.get_team_stats().get_home_points(), team.get_team_stats().get_home_regulation_wins(), team.get_team_stats().get_home_regulation_plus_ot_wins(),
                    team.get_team_stats().get_home_ties(), team.get_team_stats().get_home_wins(), team.get_team_stats().get_last_10_games_played(),
                    team.get_team_stats().get_last_10_goals_against(), team.get_team_stats().get_last_10_goals_for(), team.get_team_stats().get_last_10_losses(),
                    team.get_team_stats().get_last_10_ot_losses(), team.get_team_stats().get_last_10_points(), team.get_team_stats().get_last_10_regulation_wins(),
                    team.get_team_stats().get_last_10_regulation_plus_ot_wins(), team.get_team_stats().get_last_10_ties(), team.get_team_stats().get_last_10_wins(),
                    team.get_team_stats().get_road_games_played(), team.get_team_stats().get_road_goals_against(), team.get_team_stats().get_road_goals_for(),
                    team.get_team_stats().get_road_losses(), team.get_team_stats().get_road_ot_losses(), team.get_team_stats().get_road_points(),
                    team.get_team_stats().get_road_regulation_wins(), team.get_team_stats().get_road_regulation_plus_ot_wins(), team.get_team_stats().get_road_ties(),
                    team.get_team_stats().get_road_wins(), team.get_team_id(), team.get_team_stats().get_year(), team.get_team_stats().get_game_type_id())
        return query, params
    
    def __create_team_advanced_stats_days_rest_query(self, season):
        query = "INSERT INTO team_advanced_stats_days_rest (team_id, year, days_rest, games_played, faceoff_percent, goals_against_per_game,\
                goals_for_per_game, losses, net_goals_per_game, ot_losses, penalty_kill_percent, point_percent, points, power_play_percent,\
                power_play_opportunities_per_game, shot_differential_per_game, shots_against_per_game, shots_for_per_game, ties,\
                times_shorthanded_per_game, wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_days_rest(), season.get_games_played(), season.get_faceoff_percent(),
                    season.get_goals_against_per_game(), season.get_goals_for_per_game(), season.get_losses(), season.get_net_goals_per_game(),
                    season.get_ot_losses(), season.get_penalty_kill_percent(), season.get_point_percent(), season.get_points(), season.get_power_play_percent(),
                    season.get_power_play_opportunities_per_game(), season.get_shot_differential_per_game(), season.get_shots_against_per_game(),
                    season.get_shots_for_per_game(), season.get_ties(), season.get_times_shorthanded_per_game(), season.get_wins())
        
        return query, params
    
    def __create_team_advanced_stats_corsi_fenwick_query(self, season):
        query = "INSERT INTO team_advanced_stats_corsi_fenwick (team_id, year, games_played, corsi_against, corsi_ahead, corsi_behind,\
            corsi_close, corsi_for, corsi_tied, corsi_total, fenwick_against, fenwick_ahead, fenwick_behind, fenwick_close,\
            fenwick_for, fenwick_relative, fenwick_tied, fenwick_total, corsi_percent, corsi_ahead_percent, corsi_behind_percent,\
            corsi_close_percent, corsi_tied_percent, corsi_relative, shooting_percent_5on5, save_percent_5on5, shooting_plus_save_percent_5on5,\
            fenwick_percent, fenwick_ahead_percent, fenwick_behind_percent, fenwick_close_percent, fenwick_tied_percent, zone_start_5on5_percent,\
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_games_played(), season.get_corsi_against(), season.get_corsi_ahead(),
                    season.get_corsi_behind(), season.get_corsi_close(), season.get_corsi_for(), season.get_corsi_tied(), season.get_corsi_total(),
                    season.get_fenwick_against(), season.get_fenwick_ahead(), season.get_fenwick_behind(), season.get_fenwick_close(),
                    season.get_fenwick_for(), season.get_fenwick_relative(), season.get_fenwick_tied(), season.get_fenwick_total(), season.get_corsi_percent(),
                    season.get_corsi_ahead_percent(), season.get_corsi_behind_percent(), season.get_corsi_close_percent(), season.get_corsi_tied_percent(),
                    season.get_corsi_relative(), season.get_shooting_percent_5on5(), season.get_save_percent_5on5(), season.get_shooting_plus_save_percent_5on5(),
                    season.get_fenwick_percent(), season.get_fenwick_ahead_percent(), season.get_fenwick_behind_percent(), season.get_fenwick_close_percent(),
                    season.get_fenwick_tied_percent(), season.get_zone_start_5on5_percent())
        
        return query, params

    def __create_team_advanced_stats_shot_type_query(self, season):
        query = "INSERT INTO team_advanced_stats_shot_type (team_id, year, goals_backhand, goals_deflected, goals_for, goals_slap, goals_snap,\
            goals_tip_in, goals_wrap_around, goals_wrist, shooting_percent_backhand, shooting_percent_deflected, shooting_percent_slap,\
            shooting_percent_snap, shooting_percent_tip_in, shooting_percent_wrap_around, shooting_percent_wrist, shots_on_net_backhand,\
            shots_on_net_deflected, shots_on_net_slap, shots_on_net_snap, shots_on_net_tip_in, shots_on_net_wrap_around, shots_on_net_wrist) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_goals_backhand(), season.get_goals_deflected(), season.get_goals_for(),
                    season.get_goals_slap(), season.get_goals_snap(), season.get_goals_tip_in(), season.get_goals_wrap_around(), season.get_goals_wrist(),
                    season.get_shooting_percent_backhand(), season.get_shooting_percent_deflected(), season.get_shooting_percent_slap(),
                    season.get_shooting_percent_snap(), season.get_shooting_percent_tip_in(), season.get_shooting_percent_wrap_around(),
                    season.get_shooting_percent_wrist(), season.get_shots_on_net_backhand(), season.get_shots_on_net_deflected(), season.get_shots_on_net_slap(),
                    season.get_shots_on_net_snap(), season.get_shots_on_net_tip_in(), season.get_shots_on_net_wrap_around(), season.get_shots_on_net_wrist())
        
        return query, params

    def __create_team_advanced_stats_outshoot_outshot_query(self, season):
        query = "INSERT INTO team_advanced_stats_outshoot_outshot (team_id, year, losses_even_shots, losses_outshoot, losses_outshot, net_shots_per_game,\
                ot_losses_even_shots, ot_losses_outshoot, ot_losses_outshot, shots_against_per_game, shots_for_per_game, ties_even_shots, ties_outshoot,\
                ties_outshot, wins_even_shots, wins_outshoot, wins_outshot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_losses_even_shots(), season.get_losses_outshoot(), season.get_losses_outshot(),
                    season.get_net_shots_per_game(), season.get_ot_losses_even_shots(), season.get_ot_losses_outshoot(), season.get_ot_losses_outshot(),
                    season.get_shots_against_per_game(), season.get_shots_for_per_game(), season.get_ties_even_shots(), season.get_ties_outshoot(),
                    season.get_ties_outshot(), season.get_wins_even_shots(), season.get_wins_outshoot(), season.get_wins_outshot())
        
        return query, params

    def __create_team_advanced_stats_faceoff_percent_query(self, season):
        query = "INSERT INTO team_advanced_stats_faceoff_percent (team_id, year, defensive_zone_faceoff_percent, defensive_zone_faceoffs, ev_faceoff_percent,\
            ev_faceoffs, faceoff_win_percent, neutral_zone_faceoff_percent, neutral_zone_faceoffs, offensive_zone_faceoff_percent, offensive_zone_faceoffs,\
            pp_faceoff_percent, pp_faceoffs, pk_faceoff_percent, pk_faceoffs, total_faceoffs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_defensive_zone_faceoff_percent(), season.get_defensive_zone_faceoffs(),
                    season.get_ev_faceoff_percent(), season.get_ev_faceoffs(), season.get_faceoff_win_percent(), season.get_neutral_zone_faceoff_percent(),
                    season.get_neutral_zone_faceoffs(), season.get_offensive_zone_faceoff_percent(), season.get_offensive_zone_faceoffs(),
                    season.get_pp_faceoff_percent(), season.get_pp_faceoffs(), season.get_pk_faceoff_percent(), season.get_pk_faceoffs(),
                    season.get_total_faceoffs())
        
        return query, params

    def __create_team_advanced_stats_goals_by_period_query(self, season):
        query = "INSERT INTO team_advanced_stats_goals_by_period (team_id, year, ev_goals_for, period_1_goals_against, period_1_goals_for, period_2_goals_against,\
            period_2_goals_for, period_3_goals_against, period_3_goals_for, period_ot_goals_against, period_ot_goals_for, pp_goals_for, pk_goals_for)\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_ev_goals_for(), season.get_period_1_goals_against(), season.get_period_1_goals_for(),
                    season.get_period_2_goals_against(), season.get_period_2_goals_for(), season.get_period_3_goals_against(), season.get_period_3_goals_for(),
                    season.get_period_ot_goals_against(), season.get_period_ot_goals_for(), season.get_pp_goals_for(), season.get_pk_goals_for())
        
        return query, params

    def __create_team_advanced_stats_goals_by_strength_query(self, season):
        query = "INSERT INTO team_advanced_stats_goals_by_strength (team_id, year, goals_for_3on3, goals_for_3on4, goals_for_3on5, goals_for_3on6,\
                goals_for_4on3, goals_for_4on4, goals_for_4on5, goals_for_4on6, goals_for_5on3, goals_for_5on4, goals_for_5on5, goals_for_5on6,\
                goals_for_6on3, goals_for_6on4, goals_for_6on5, goals_for_penalty_shots) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_goals_for_3on3(), season.get_goals_for_3on4(), season.get_goals_for_3on5(),
                    season.get_goals_for_3on6(), season.get_goals_for_4on3(), season.get_goals_for_4on4(), season.get_goals_for_4on5(),
                    season.get_goals_for_4on6(), season.get_goals_for_5on3(), season.get_goals_for_5on4(), season.get_goals_for_5on5(),
                    season.get_goals_for_5on6(), season.get_goals_for_6on3(), season.get_goals_for_6on4(), season.get_goals_for_6on5(),
                    season.get_goals_for_penalty_shots())
        
        return query, params

    def __create_team_advanced_stats_leading_trailing_query(self, season):
        query = "INSERT INTO team_advanced_stats_leading_trailing (team_id, year, loss_lead_period_1, loss_lead_period_2, loss_trail_period_1,\
                loss_trail_period_2, ot_loss_lead_period_1, ot_loss_lead_period_2, ot_loss_trail_period_1, ot_loss_trail_period_2,\
                period_1_goals_against, period_1_goals_for, period_2_goals_against, period_2_goals_for, ties_lead_period_1, ties_lead_period_2,\
                ties_trail_period_1, ties_trail_period_2, win_percent_lead_period_1, win_percent_lead_period_2, win_percent_trail_period_1,\
                win_percent_trail_period_2, wins_lead_period_1, wins_lead_period_2, wins_trail_period_1, wins_trail_period_2) VALUES (%s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_loss_lead_period_1(), season.get_loss_lead_period_2(), season.get_loss_trail_period_1(),
                    season.get_loss_trail_period_2(), season.get_ot_loss_lead_period_1(), season.get_ot_loss_lead_period_2(), season.get_ot_loss_trail_period_1(),
                    season.get_ot_loss_trail_period_2(), season.get_period_1_goals_against(), season.get_period_1_goals_for(), season.get_period_2_goals_against(),
                    season.get_period_2_goals_for(), season.get_ties_lead_period_1(), season.get_ties_lead_period_2(), season.get_ties_trail_period_1(),
                    season.get_ties_trail_period_2(), season.get_win_percent_lead_period_1(), season.get_win_percent_lead_period_2(), season.get_win_percent_trail_period_1(),
                    season.get_win_percent_trail_period_2(), season.get_wins_lead_period_1(), season.get_wins_lead_period_2(), season.get_wins_trail_period_1(),
                    season.get_wins_trail_period_2())
        
        return query, params
    
    def __create_team_advanced_stats_misc_query(self, season):
        query = "INSERT INTO team_advanced_stats_misc (team_id, year, blocked_shots, empty_net_goals, giveaways, hits, missed_shots, takeaways,\
                time_on_ice_per_game_5on5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_blocked_shots(), season.get_empty_net_goals(), season.get_giveaways(),
                    season.get_hits(), season.get_missed_shots(), season.get_takeaways(), season.get_time_on_ice_per_game_5on5())
        
        return query, params

    def __create_team_advanced_penalties_query(self, season):
        query = "INSERT INTO team_advanced_penalties (team_id, year, bench_minor_penalties, game_misconducts, majors, match_penalties, minors, misconducts,\
                net_penalties, penalties, penalty_minutes, penalty_seconds_per_game, total_penalties_drawn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_bench_minor_penalties(), season.get_game_misconducts(), season.get_majors(),
                    season.get_match_penalties(), season.get_minors(), season.get_misconducts(), season.get_net_penalties(), season.get_penalties(),
                    season.get_penalty_minutes(), season.get_penalty_seconds_per_game(), season.get_total_penalties_drawn())
        
        return query, params

    def __create_team_advanced_stats_powerplay_penalty_kill_query(self, season):
        query = "INSERT INTO team_advanced_stats_powerplay_penalty_kill (team_id, year, pk_net_percent, pk_percent, pk_net_goals_for, pk_net_goals_for_per_game,\
                pk_time_on_ice_per_game, pk_goals_against, pk_goals_against_per_game, pk_goals_for, pk_goals_for_per_game, times_shorthanded,\
                times_shorthanded_per_game, overall_penalty_kill_percent, penalty_kill_percent_3on4, penalty_kill_percent_3on5, penalty_kill_percent_4on5,\
                time_on_ice_3on4, time_on_ice_3on5, time_on_ice_4on5, time_on_ice_shorthanded, time_shorthanded_3v4, time_shorthanded_3v5, time_shorthanded_4v5,\
                pp_goals_for, pp_net_percent, pp_percent, pp_goalsper_game, pp_net_goals_for, pp_net_goals_for_per_game, pp_opportunities,\
                pp_opportunities_per_game, pp_time_on_ice_per_game, pp_goals_against, pp_goals_against_per_game, opportunities_4on3, opportunities_5on3,\
                opportunities_5on4, pp_percent_4on3, pp_percent_5on3, pp_percent_5on4, time_on_ice_4on3, time_on_ice_5on3, time_on_ice_5on4,\
                pp_time_on_ice, goals_against_3on4, goals_against_3on5, goals_against_4on5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s)"

        params = (season.get_team_id(), season.get_year(), season.get_pk_net_percent(), season.get_pk_percent(), season.get_pk_net_goals_for(),
                    season.get_pk_net_goals_for_per_game(), season.get_pk_time_on_ice_per_game(), season.get_pk_goals_against(), season.get_pk_goals_against_per_game(),
                    season.get_pk_goals_for(), season.get_pk_goals_for_per_game(), season.get_times_shorthanded(), season.get_times_shorthanded_per_game(),
                    season.get_overall_penalty_kill_percent(), season.get_penalty_kill_percent_3on4(), season.get_penalty_kill_percent_3on5(), season.get_penalty_kill_percent_4on5(),
                    season.get_time_on_ice_3on4(), season.get_time_on_ice_3on5(), season.get_time_on_ice_4on5(), season.get_time_on_ice_shorthanded(), season.get_time_shorthanded_3v4(),
                    season.get_time_shorthanded_3v5(), season.get_time_shorthanded_4v5(), season.get_pp_goals_for(), season.get_pp_net_percent(), season.get_pp_percent(),
                    season.get_pp_goalsper_game(), season.get_pp_net_goals_for(), season.get_pp_net_goals_for_per_game(), season.get_pp_opportunities(),
                    season.get_pp_opportunities_per_game(), season.get_pp_time_on_ice_per_game(), season.get_pp_goals_against(), season.get_pp_goals_against_per_game(),
                    season.get_opportunities_4on3(), season.get_opportunities_5on3(), season.get_opportunities_5on4(), season.get_pp_percent_4on3(), season.get_pp_percent_5on3(),
                    season.get_pp_percent_5on4(), season.get_time_on_ice_4on3(), season.get_time_on_ice_5on3(), season.get_time_on_ice_5on4(), season.get_pp_time_on_ice(),
                    season.get_goals_against_3on4(), season.get_goals_against_3on5(), season.get_goals_against_4on5())
        
        return query, params

    def __create_team_advanced_stats_scoring_first_query(self, season):
        query = "INSERT INTO team_advanced_stats_scoring_first (team_id, year, losses_scoring_first, losses_trailing_first, ot_losses_scoring_first,\
                ot_losses_trailing_first, scoring_first_games_played, ties_scoring_first, ties_trailing_first, trailing_first_games_played,\
                win_percent_scoring_first, win_percent_trailing_first, wins_scoring_first, wins_trailing_first) VALUES (%s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_losses_scoring_first(), season.get_losses_trailing_first(), season.get_ot_losses_scoring_first(),
                    season.get_ot_losses_trailing_first(), season.get_scoring_first_games_played(), season.get_ties_scoring_first(), season.get_ties_trailing_first(),
                    season.get_trailing_first_games_played(), season.get_win_percent_scoring_first(), season.get_win_percent_trailing_first(), season.get_wins_scoring_first(),
                    season.get_wins_trailing_first())
        
        return query, params

    def __create_team_advanced_stats_team_goal_games_query(self, season):
        query = "INSERT INTO team_advanced_stats_team_goal_games (team_id, year, losses_one_goal_games, losses_two_goal_games, losses_three_goal_games,\
                ot_losses_one_goal_games, win_percent_one_goal_games, win_percent_two_goal_games, win_percent_three_goal_games, wins_one_goal_games,\
                wins_two_goal_games, wins_three_goal_games) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (season.get_team_id(), season.get_year(), season.get_losses_one_goal_games(), season.get_losses_two_goal_games(), season.get_losses_three_goal_games(),
                    season.get_ot_losses_one_goal_games(), season.get_win_percent_one_goal_games(), season.get_win_percent_two_goal_games(), season.get_win_percent_three_goal_games(),
                    season.get_wins_one_goal_games(), season.get_wins_two_goal_games(), season.get_wins_three_goal_games())
        
        return query, params