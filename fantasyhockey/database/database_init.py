from fantasyhockey.database.database_operator import DatabaseOperator


class DatabaseInitializer:
    def __init__(self):
        pass

    def run(self):
        self.__create()

    def __create(self):
        db_operator = DatabaseOperator()

        db_operator.write(self.__initialize_database())
        db_operator.write(self.__initialize_seasons())

        # Teams and Players
        db_operator.write(self.__initialize_teams())
        db_operator.write(self.__initialize_team_stats())
        db_operator.write(self.__initialize_players())

        db_operator.write(self.__initialize_player_details())
        db_operator.write(self.__initialize_player_draft())
        db_operator.write(self.__initialize_player_awards())

        # Player Stats
        db_operator.write(self.__initialize_skater_current_stats())
        
        db_operator.write(self.__initialize_skater_stats())
        db_operator.write(self.__initialize_skater_youth_stats())
        db_operator.write(self.__initialize_goalie_current_stats())
        db_operator.write(self.__initialize_goalie_stats())
        db_operator.write(self.__initialize_goalie_youth_stats())

        # Advanced Stats - Skaters
        db_operator.write(self.__initialize_skater_advanced_stats_toi())
        db_operator.write(self.__initialize_skater_advanced_stats_scoring())
        db_operator.write(self.__initialize_skater_advanced_stats_shootout())
        db_operator.write(self.__initialize_skater_advanced_stats_corsi_fenwick())
        db_operator.write(self.__initialize_skater_advanced_stats_powerplay())
        db_operator.write(self.__initialize_skater_advanced_stats_penalty_kill())
        db_operator.write(self.__initialize_skater_advanced_stats_penalties())
        db_operator.write(self.__initialize_skater_advanced_stats_misc())
        db_operator.write(self.__initialize_skater_advanced_stats_goals())
        db_operator.write(self.__initialize_skater_advanced_stats_faceoffs())

        # Advanced Stats - Goalies
        db_operator.write(self.__initialize_goalie_advanced_stats())
        db_operator.write(self.__initialize_goalie_advanced_stats_days_rest())
        db_operator.write(self.__initialize_goalie_advanced_stats_penalty_shots())
        db_operator.write(self.__initialize_goalie_advanced_stats_saves_by_strength())
        db_operator.write(self.__initialize_goalie_advanced_stats_shootout())
        db_operator.write(self.__initialize_goalie_advanced_stats_start_relieved())

        # Games and Seasons
        
        db_operator.write(self.__initialize_games())
        db_operator.write(self.__initialize_game_boxscore())
        db_operator.write(self.__initialize_game_roster())
        db_operator.write(self.__initialize_game_scoreboard())
        db_operator.write(self.__initialize_game_skater_stats())
        db_operator.write(self.__initialize_game_goalie_stats())
        db_operator.write(self.__initialize_game_goals())
        db_operator.write(self.__initialize_game_three_stars())
        db_operator.write(self.__initialize_game_plays())
        db_operator.write(self.__initialize_play_outcomes())
        db_operator.write(self.__initialize_play_roles())
        db_operator.write(self.__initialize_play_on_ice())

        # Referees and Playoffs
        db_operator.write(self.__initialize_referees())
        db_operator.write(self.__initialize_playoff_bracket())

        # Draft and Schedule
        db_operator.write(self.__initialize_draft_rankings())
        db_operator.write(self.__initialize_schedule())

        # Additional Data
        db_operator.write(self.__initialize_shift_data())

        return False

    def __reset(self):
        db_operator = DatabaseOperator()
        
        db_operator.write(self.__delete_player_details())
        db_operator.write(self.__delete_player_draft())
        db_operator.write(self.__delete_player_awards())
        db_operator.write(self.__delete_team_stats())

        db_operator.write(self.__delete_skater_current_stats())
        db_operator.write(self.__delete_skater_stats())
        db_operator.write(self.__delete_skater_youth_stats())
        db_operator.write(self.__delete_goalie_current_stats())
        db_operator.write(self.__delete_goalie_stats())
        db_operator.write(self.__delete_goalie_youth_stats())

        db_operator.write(self.__delete_skater_advanced_stats_toi())
        db_operator.write(self.__delete_skater_advanced_stats_scoring())
        db_operator.write(self.__delete_skater_advanced_stats_shootout())
        db_operator.write(self.__delete_skater_advanced_stats_corsi_fenwick())
        db_operator.write(self.__delete_skater_advanced_stats_powerplay())
        db_operator.write(self.__delete_skater_advanced_stats_penalty_kill())
        db_operator.write(self.__delete_skater_advanced_stats_penalties())
        db_operator.write(self.__delete_skater_advanced_stats_misc())
        db_operator.write(self.__delete_skater_advanced_stats_goals())
        db_operator.write(self.__delete_skater_advanced_stats_faceoffs())

        db_operator.write(self.__delete_goalie_advanced_stats())
        db_operator.write(self.__delete_goalie_advanced_stats_days_rest())
        db_operator.write(self.__delete_goalie_advanced_stats_penalty_shots())
        db_operator.write(self.__delete_goalie_advanced_stats_saves_by_strength())
        db_operator.write(self.__delete_goalie_advanced_stats_shootout())
        db_operator.write(self.__delete_goalie_advanced_stats_start_relieved())

        
        db_operator.write(self.__delete_games())
        db_operator.write(self.__delete_game_boxscore())
        db_operator.write(self.__delete_game_roster())
        db_operator.write(self.__delete_game_scoreboard())
        db_operator.write(self.__delete_game_skater_stats())
        db_operator.write(self.__delete_game_goalie_stats())
        db_operator.write(self.__delete_game_goals())
        db_operator.write(self.__delete_game_three_stars())
        db_operator.write(self.__delete_game_plays())
        db_operator.write(self.__delete_play_outcomes())
        db_operator.write(self.__delete_play_roles())
        db_operator.write(self.__delete_play_on_ice())

        db_operator.write(self.__delete_referees())
        db_operator.write(self.__delete_playoff_bracket())

        db_operator.write(self.__delete_draft_rankings())
        db_operator.write(self.__delete_schedule())

        db_operator.write(self.__delete_shift_data())

        db_operator.write(self.__delete_players())
        db_operator.write(self.__delete_teams())
        db_operator.write(self.__delete_seasons())
        
        

        return False

    def __clear_table(self, table_name):
        """
        Clear data in a table without dropping the table itself.
        """
        db_operator = DatabaseOperator()
        try:
            db_operator.write(f"DELETE FROM {table_name};")
        except Exception as e:
            print(e)
            return False
        return True


    def __initialize_database(self):
        return "CREATE DATABASE IF NOT EXISTS fantasyhockey"

    def __initialize_players(self):
        return "CREATE TABLE IF NOT EXISTS players  \
                (id INT PRIMARY KEY, team_id INT, is_active BOOLEAN, \
                FOREIGN KEY (team_id) REFERENCES teams(team_id)\
            );"

    def __delete_players(self):
        return "DROP TABLE IF EXISTS players"

    def __initialize_player_details(self):
        return "CREATE TABLE IF NOT EXISTS player_details \
                (id INT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), \
                jersey_number VARCHAR(255), position VARCHAR(15), headshot VARCHAR(255), hero_image VARCHAR(255), \
                height_inches INT, weight_pounds INT, birth_date DATE, \
                birth_city VARCHAR(255), birth_state_province VARCHAR(255), birth_country VARCHAR(255), shoots_catches VARCHAR(5), \
                in_top_100_all_time BOOLEAN, in_hhof BOOLEAN, \
                FOREIGN KEY (id) REFERENCES players(id)\
            );"

    def __delete_player_details(self):
        return "DROP TABLE IF EXISTS player_details"

    def __initialize_player_draft(self):
        return "CREATE TABLE IF NOT EXISTS player_draft\
                (id INT PRIMARY KEY, year VARCHAR(255), team_id INT, round INT, pick_in_round INT, overall_pick INT,\
                FOREIGN KEY (id) REFERENCES players(id),\
                FOREIGN KEY (team_id) REFERENCES teams(team_id));"

    def __delete_player_draft(self):
        return "DROP TABLE IF EXISTS player_draft"

    def __initialize_player_awards(self):
        return "CREATE TABLE IF NOT EXISTS player_awards \
                (id INT, award_name VARCHAR(255), year VARCHAR(255),\
                FOREIGN KEY (id) REFERENCES players(id), PRIMARY KEY (id, award_name, year));"

    def __delete_player_awards(self):
        return "DROP TABLE IF EXISTS player_awards"

# SKATER EXCLUSIVE TABLES   
    def __initialize_skater_current_stats(self):
        """
        Initializes the current_skater_stats table in the database.

        Primary Key - id, year, sequence, game_type_id

        Need blocks, hits, primary and secondary assists from other source
        """
        return "CREATE TABLE IF NOT EXISTS current_skater_stats\
                (id INT, team_id INT, games_played INT, goals INT, assists INT, points INT, plus_minus INT, penalty_minutes INT,\
                game_winning_goals INT, ot_goals INT, power_play_goals INT, power_play_points INT, shooting_percent FLOAT,\
                shorthanded_goals INT, shorthanded_points INT, shots INT, time_on_ice VARCHAR(255), game_type_id INT, year INT,\
                sequence INT, faceoff_percent FLOAT, league_id INT, blocks INT, hits INT, primary_assists INT, secondary_assists INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES players(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, sequence, game_type_id));"

    def __delete_skater_current_stats(self):
        return "DROP TABLE IF EXISTS current_skater_stats"

    def __initialize_skater_stats(self):
        """
        Initializes the skater_stats table in the database.

        Need blocks, hits, primary and secondary assists from other source
        """
        return "CREATE TABLE IF NOT EXISTS skater_stats \
                (id INT, team_id INT, games_played INT, goals INT, assists INT, points INT, plus_minus INT, penalty_minutes INT,\
                game_winning_goals INT, ot_goals INT, power_play_goals INT, power_play_points INT, shooting_percent FLOAT,\
                shorthanded_goals INT, shorthanded_points INT, shots INT, time_on_ice VARCHAR(255), game_type_id INT, year INT,\
                sequence INT, faceoff_percent FLOAT, league_id INT, blocks INT, hits INT, primary_assists INT, secondary_assists INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES players(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, sequence, game_type_id));"

    def __delete_skater_stats(self):
        return "DROP TABLE IF EXISTS skater_stats"

    # ADVANCED STATS TABLES

    def __initialize_skater_advanced_stats_toi(self):
        """
        Initializes the skater_advanced_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_toi \
                (id INT, year INT, team_id INT, ev_time_on_ice FLOAT, games_played INT, ot_time_on_ice FLOAT, ot_time_on_ice_per_ot_game FLOAT,\
                    pp_time_on_ice FLOAT, sh_time_on_ice FLOAT, shifts INT, time_on_ice FLOAT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_toi(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_toi"

    def __initialize_skater_advanced_stats_scoring(self):
        """
        Initializes the skater_advanced_stats_scoring table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_scoring \
                (id INT, year INT, team_id INT, goals_backhand INT, goals_bat INT, goals_between_legs INT,\
                    goals_cradle INT, goals_deflected INT, goals_poke INT, goals_slap INT, goals_snap INT, goals_tip INT, goals_wrap_around INT, goals_wrist INT,\
                    shots_backhand INT, shots_bat INT, shots_between_legs INT, shots_cradle INT, shots_deflected INT, shots_poke INT, shots_slap INT, shots_snap INT,\
                    shots_tip INT, shots_wrap_around INT, shots_wrist INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_scoring(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_scoring"
                    
    def __initialize_skater_advanced_stats_shootout(self):
        """
        Initializes the skater_advanced_stats_shootout table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_shootout \
                (id INT, year INT, team_id INT, career_shootout_game_deciding_goals INT, career_shootout_games_played INT, career_shootout_goals INT,\
                    career_shootout_percentage FLOAT, career_shootout_shots INT, shootout_game_deciding_goals INT, shootout_games_played INT,\
                    shootout_goals INT, shootout_percentage FLOAT, shootout_shots INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_shootout(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_shootout"

    def __initialize_skater_advanced_stats_corsi_fenwick(self):
        """
        Initializes the skater_advanced_stats_corsi_fenwick table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_corsi_fenwick \
                (id INT, year INT, team_id INT, games_played INT, corsi_against INT, corsi_ahead INT, corsi_behind INT,\
                corsi_close INT, corsi_for INT, corsi_tied INT, corsi_total INT, fenwick_against INT,\
                fenwick_ahead INT, fenwick_behind INT, fenwick_close INT, fenwick_for INT, fenwick_relative FLOAT,\
                fenwick_tied INT, fenwick_total INT, corsi_percent FLOAT, corsi_ahead_percent FLOAT, corsi_behind_percent FLOAT,\
                corsi_close_percent FLOAT, corsi_tied_percent FLOAT, corsi_relative FLOAT, shooting_percent_5on5 FLOAT,\
                skater_save_percent_5on5 FLOAT, skater_shooting_plus_save_percent_5on5 FLOAT, time_on_ice_5on5_per_game FLOAT,\
                fenwick_percent FLOAT, fenwick_ahead_percent FLOAT, fenwick_behind_percent FLOAT, fenwick_close_percent FLOAT,\
                fenwick_tied_percent FLOAT, zone_start_5on5_percent FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_corsi_fenwick(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_corsi_fenwick"

    def __initialize_skater_advanced_stats_powerplay(self):
        """
        Initializes the skater_advanced_stats_powerplay table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_powerplay \
                (id INT, year INT, team_id INT, pp_assists INT, pp_goals INT, pp_individual_corsi_for INT, pp_primary_assists INT,\
                pp_secondary_assists INT, pp_shooting_percent FLOAT, pp_shots INT, pp_time_on_ice FLOAT, pp_time_on_ice_per_game FLOAT,\
                pp_time_on_ice_percent FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"
    
    def __delete_skater_advanced_stats_powerplay(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_powerplay"

    def __initialize_skater_advanced_stats_penalty_kill(self):
        """
        Initializes the skater_advanced_stats_penalty_kill table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_penalty_kill \
                (id INT, year INT, team_id INT, pk_assists INT, pk_goals INT, pk_individual_corsi_against INT, pk_primary_assists INT,\
                pk_secondary_assists INT, pk_shooting_percent FLOAT, pk_shots INT, pk_time_on_ice FLOAT, pk_time_on_ice_per_game FLOAT,\
                pk_time_on_ice_percent FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_penalty_kill(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_penalty_kill"
                
    def __initialize_skater_advanced_stats_penalties(self):
        """
        Initializes the skater_advanced_stats_penalties table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_penalties \
                (id INT, year INT, team_id INT, game_misconduct_penalties INT, games_played INT, major_penalties INT,\
                match_penalties INT, minor_penalties INT, misconduct_penalties INT, net_penalties INT, penalties INT,\
                penalties_drawn INT, penalty_minutes INT, time_on_ice_per_game FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_penalties(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_penalties"

    def __initialize_skater_advanced_stats_misc(self):
        """
        Initializes the skater_advanced_stats_misc table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_misc \
                (id INT, year INT, team_id INT, blocked_shots INT, empty_net_assists INT, empty_net_goals INT,\
                empty_net_points INT, first_goals INT, giveaways INT, games_played INT, hits INT, missed_shot_crossbar INT,\
                missed_shot_goalpost INT, missed_shot_over INT, missed_shot_wide INT, missed_shots INT, ot_goals INT,\
                takeaways INT, time_on_ice_per_game FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_misc(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_misc"

    def __initialize_skater_advanced_stats_goals(self):
        """
        Initializes the skater_advanced_stats_goals table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_goals \
                (id INT, year INT, team_id INT, even_strength_goal_difference INT, even_strength_goals_against INT, even_strength_goals_for INT,\
                even_strength_time_on_ice_per_game FLOAT, games_played INT, pp_goals_for INT, pp_goals_against INT, pk_goals_for INT,\
                pk_goals_against INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_goals(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_goals"

    def __initialize_skater_advanced_stats_faceoffs(self):
        """
        Initializes the skater_advanced_stats_faceoffs table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_faceoffs \
                (id INT, year INT, team_id INT, defensive_zone_faceoffs INT, defensive_zone_faceoffs_won INT, defensive_zone_faceoffs_lost INT,\
                ev_faceoffs INT, ev_faceoffs_won INT, ev_faceoffs_lost INT, faceoff_percent FLOAT, neutral_zone_faceoffs INT, neutral_zone_faceoffs_won INT,\
                neutral_zone_faceoffs_lost INT, offensive_zone_faceoffs INT, offensive_zone_faceoffs_won INT, offensive_zone_faceoffs_lost INT,\
                pp_faceoffs INT, pp_faceoffs_won INT, pp_faceoffs_lost INT, pk_faceoffs INT, pk_faceoffs_won INT, pk_faceoffs_lost INT,\
                total_faceoffs INT, total_faceoffs_won INT, total_faceoffs_lost INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_skater_advanced_stats_faceoffs(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_faceoffs"

    def __initialize_skater_youth_stats(self):
        """
        Initializes the skater_youth_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_youth_stats \
                (id INT, year INT, team_name VARCHAR(255), league_name VARCHAR(255), game_type_id INT, sequence INT, games_played INT,\
                goals INT, assists INT, points INT, pim INT,\
                FOREIGN KEY (id) REFERENCES players(id),\
                FOREIGN KEY (year) REFERENCES seasons(year), PRIMARY KEY (id, year, team_name, league_name, game_type_id, sequence));"

    def __delete_skater_youth_stats(self):
        return "DROP TABLE IF EXISTS skater_youth_stats"

# GOALIE EXCLUSIVE TABLES

    def __initialize_goalie_current_stats(self):
        """
        Initializes the goalie_current_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_current_stats \
                (id INT, team_id INT, year INT, game_type_id INT, league_id INT, sequence INT, games_played INT, goals INT, assists INT,\
                    games_started INT, wins INT, losses INT, ot_losses INT, shots_against INT, goals_against INT, save_percent FLOAT,\
                    shutouts INT, time_on_ice VARCHAR (100), goals_against_average FLOAT, pim INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id, game_type_id, sequence));"

    def __delete_goalie_current_stats(self):
        return "DROP TABLE IF EXISTS goalie_current_stats"

    def __initialize_goalie_stats(self):
        """
        Initializes the goalie_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_stats \
                (id INT, team_id INT, year INT, game_type_id INT, league_id INT, sequence INT, games_played INT, goals INT, assists INT,\
                    games_started INT, wins INT, losses INT, ot_losses INT, shots_against INT, goals_against INT, save_percent FLOAT,\
                    shutouts INT, time_on_ice VARCHAR (100), goals_against_average FLOAT, penalty_minues INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id, game_type_id, sequence));"

    def __delete_goalie_stats(self):
        return "DROP TABLE IF EXISTS goalie_stats"

    def __initialize_goalie_advanced_stats(self):
        """
        Initializes the goalie_advanced_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats \
                (id INT, year INT, team_id INT, complete_game_percent FLOAT, complete_games INT, games_played INT, games_started INT,\
                goals_against INT, goals_against_average FLOAT, goals_for INT, goals_for_average FLOAT, incomplete_games INT, quality_start INT,\
                quality_starts_percent FLOAT, regulation_losses INT, regulation_wins INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats"

    def __initialize_goalie_youth_stats(self):
        """
        Initializes the goalie_youth_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_youth_stats \
                (id INT, year INT, team_name VARCHAR(255), league_name VARCHAR(255), game_type_id INT, sequence INT, games_played INT,\
                save_percent FLOAT, goals_against_average FLOAT, goals_against INT, wins INT, losses INT, time_on_ice VARCHAR(100),\
                ties INT,\
                FOREIGN KEY (id) REFERENCES players(id),\
                FOREIGN KEY (year) REFERENCES seasons(year), PRIMARY KEY (id, year, team_name, league_name, game_type_id, sequence));" 

    def __delete_goalie_youth_stats(self):
        return "DROP TABLE IF EXISTS goalie_youth_stats"

    def __initialize_goalie_advanced_stats_days_rest(self):
        """
        Initializes the goalie_advanced_stats_days_rest table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_days_rest \
                (id INT, year INT, team_id INT, games_played INT, games_played_days_rest_0 INT, games_played_days_rest_1 INT,\
                games_played_days_rest_2 INT, games_played_days_rest_3 INT, games_played_days_rest_4 INT, games_played_days_rest_4_plus INT,\
                games_started INT, losses INT, ot_losses INT, save_percent FLOAT, save_percent_days_rest_0 FLOAT, save_percent_days_rest_1 FLOAT,\
                save_percent_days_rest_2 FLOAT, save_percent_days_rest_3 FLOAT, save_percent_days_rest_4 FLOAT, save_percent_days_rest_4_plus FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats_days_rest(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_days_rest"

    def __initialize_goalie_advanced_stats_penalty_shots(self):
        """
        Initializes the goalie_advanced_stats_penalty_shots table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_penalty_shots \
                (id INT, year INT, team_id INT, penalty_shot_save_percent FLOAT, penalty_shot_against INT, penalty_shot_goals_against INT,\
                penalty_shot_saves INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats_penalty_shots(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_penalty_shots"
    
    def __initialize_goalie_advanced_stats_saves_by_strength(self):
        """
        Initializes the goalie_advanced_stats_saves_by_strength table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_saves_by_strength \
                (id INT, year INT, team_id INT, ev_goals_against INT, ev_save_percent FLOAT, ev_saves INT, ev_shots_against INT,\
                pp_goals_against INT, pp_save_percent FLOAT, pp_saves INT, pp_shots_against INT, pk_goals_against INT,\
                pk_save_percent FLOAT, pk_saves INT, pk_shots_against INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats_saves_by_strength(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_saves_by_strength"

    def __initialize_goalie_advanced_stats_shootout(self):
        """
        Initializes the goalie_advanced_stats_shootout table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_shootout \
                (id INT, year INT, team_id INT, career_shootout_games_played INT, career_shootout_goals_allowed INT, career_shootout_losses INT,\
                career_shootout_save_percent FLOAT, career_shootout_saves INT, career_shootout_shots_against INT, career_shootout_wins INT,\
                shootout_goals_against INT, shootout_losses INT, shootout_save_percent FLOAT, shootout_saves INT, shootout_shots_against INT,\
                shootout_wins INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats_shootout(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_shootout"

    def __initialize_goalie_advanced_stats_start_relieved(self):
        """
        Initializes the goalie_advanced_stats_start_relieve table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_start_relieved \
                (id INT, year INT, team_id INT, games_played INT, games_relieved INT, games_relieved_goals_against INT, games_relieved_losses INT,\
                games_relieved_ot_losses INT, games_relieved_save_percent FLOAT, games_relieved_saves INT, games_relieved_shots_against INT,\
                games_relieved_ties INT, games_relieved_wins INT, games_started INT, games_started_goals_against INT, games_started_losses INT,\
                games_started_ot_losses INT, games_started_save_percent FLOAT, games_started_saves INT, games_started_shots_against INT,\
                games_started_ties INT, games_started_wins INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id));"

    def __delete_goalie_advanced_stats_start_relieved(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_start_relieved"

# TEAM TABLES
    def __initialize_teams(self):
        """
        Initializes the teams table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS teams\
                (team_id INT, year INT, conference_name VARCHAR(25), division_name VARCHAR(25), place_name VARCHAR(255), team_name VARCHAR(50),\
                team_abbreviation VARCHAR(5), team_logo VARCHAR(255), team_color_1 VARCHAR(255), team_color_2 VARCHAR(255),\
                FOREIGN KEY (year) REFERENCES seasons(year), PRIMARY KEY (team_id, year));"

    def __delete_teams(self):
        return "DROP TABLE IF EXISTS teams"
    
    def __initialize_team_stats(self):
        """
        Initializes the team_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS team_stats\
                (team_id INT, year INT, game_type_id INT, games_played INT, goals_against INT, goals_for INT, losses INT, ot_losses INT,\
                points INT, shootout_losses INT, shootout_wins INT, streak_code VARCHAR(5), streak_count INT, ties INT, waiver_sequence INT,\
                regulation_wins INT, regulation_plus_ot_wins INT, home_games_played INT, home_goals_against INT, home_goals_for INT, home_losses INT,\
                home_ot_losses INT, home_points INT, home_regulation_wins INT, home_regulation_plus_ot_wins INT, home_ties INT, home_wins INT,\
                last_10_games_played INT, last_10_goals_against INT, last_10_goals_for INT, last_10_losses INT, last_10_ot_losses INT,\
                last_10_points INT, last_10_regulation_wins INT, last_10_regulation_plus_ot_wins INT, last_10_ties INT, last_10_wins INT,\
                road_games_played INT, road_goals_against INT, road_goals_for INT,road_losses INT, road_ot_losses INT, road_points INT, road_regulation_wins INT,\
                road_regulation_plus_ot_wins INT, road_ties INT, road_wins INT,\
                FOREIGN KEY (team_id) REFERENCES teams(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (team_id, year, game_type_id));"
                
    def __delete_team_stats(self):
        return "DROP TABLE IF EXISTS team_stats"

    def __initialize_seasons(self):
        """
        Initializes the seasons table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS seasons\
                (year INT, conferences_in_use BOOLEAN, point_for_ot_loss BOOLEAN, regulation_wins BOOLEAN, `row` BOOLEAN,\
                standings_start_date VARCHAR(50), standings_end_date VARCHAR(50), ties_in_use BOOLEAN, wild_card_in_use BOOLEAN,\
                PRIMARY KEY (year));"

    def __delete_seasons(self):
        return "DROP TABLE IF EXISTS seasons"

    def __initialize_games(self):
        """
        Initializes the games table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS games\
                (game_id INT, year INT, game_type_id INT, venue_name VARCHAR(255), start_time_utc VARCHAR(50), eastern_utc_offset VARCHAR(50),\
                venue_utc_offset VARCHAR(50), venue_time_zone VARCHAR(50), game_state VARCHAR(50), game_schedule_state VARCHAR(50),\
                away_team_id INT, home_team_id INT, shootout_in_use BOOLEAN, regulation_periods INT, ot_in_use BOOLEAN, ties_in_use BOOLEAN,\
                video_3_min_recap_id VARCHAR(255), video_condensed_game VARCHAR(255),\
                FOREIGN KEY (year) REFERENCES seasons(year), FOREIGN KEY (away_team_id) REFERENCES teams(team_id),\
                FOREIGN KEY (home_team_id) REFERENCES teams(team_id), PRIMARY KEY (game_id, year, game_type_id));"

    def __delete_games(self):
        return "DROP TABLE IF EXISTS games"
    
    def __initialize_game_boxscore(self):
        """
        Initializes the game_boxscore table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_boxscore\
                (game_id INT, away_team_id INT, away_goals INT, away_score INT, away_shots INT, away_faceoff_percent FLOAT, away_power_play_conversion VARCHAR(25),\
                away_penalty_minutes INT, away_hits INT, away_blocked_shots INT, home_team_id INT, home_goals INT, home_score INT, home_shots INT,\
                home_faceoff_percent FLOAT, home_power_play_conversion VARCHAR(25), home_penalty_minutes INT, home_hits INT, home_blocked_shots INT,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (away_team_id) REFERENCES teams(team_id), FOREIGN KEY (home_team_id) REFERENCES teams(team_id),\
                PRIMARY KEY (game_id)\
                );"
    
    def __delete_game_boxscore(self):
        return "DROP TABLE IF EXISTS game_boxscore"

    def __initialize_game_roster(self):
        """
        Initializes the game_roster table in the database.
        """
        return """CREATE TABLE IF NOT EXISTS game_roster(
                game_id INT, 
                team_id INT, 
                player_id INT, 
                scratched BOOLEAN, 
                `starting` BOOLEAN,
                FOREIGN KEY (game_id) REFERENCES games(game_id),
                FOREIGN KEY (team_id) REFERENCES teams(team_id),
                FOREIGN KEY (player_id) REFERENCES players(id),
                PRIMARY KEY (game_id, team_id, player_id)
            );"""
    
    def __delete_game_roster(self):
        return "DROP TABLE IF EXISTS game_roster"
    
    def __initialize_game_scoreboard(self):
        """
        Initializes the game_scoreboard table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_scoreboard \
                (game_id INT, home_score INT, away_score INT, home_shots INT, away_shots INT, time_remaining VARCHAR(25), period INT,\
                seconds_remaining FLOAT, running BOOLEAN, in_intermission BOOLEAN,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), PRIMARY KEY (game_id));"

    def __delete_game_scoreboard(self):
        return "DROP TABLE IF EXISTS game_scoreboard"
    
    def __initialize_referees(self):
        """
        Initializes the referees table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS referees \
                (game_id INT, referee_1_name VARCHAR(255), referee_2_name VARCHAR(255), linesman_1_name VARCHAR(255), linesman_2_name VARCHAR(255),\
                FOREIGN KEY (game_id) REFERENCES games(game_id), PRIMARY KEY (game_id));"
    
    def __delete_referees(self):
        return "DROP TABLE IF EXISTS referees"

    def __initialize_game_skater_stats(self):
        """
        Initializes the game_skater_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_skater_stats \
                (game_id INT, player_id INT, team_id INT, goals INT, assists INT, points INT, plus_minus INT, penalty_minutes INT,\
                hits INT, blocks INT, power_play_goals INT, power_play_points INT, shorthanded_goals INT, shorthanded_points INT,\
                shots INT, faceoffs VARCHAR(25), time_on_ice VARCHAR(25), power_play_time_on_ice VARCHAR(25), shorthanded_time_on_ice VARCHAR(25),\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (player_id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id),\
                PRIMARY KEY (game_id, player_id));"
    
    def __delete_game_skater_stats(self):
        return "DROP TABLE IF EXISTS game_skater_stats"
    
    def __initialize_game_goalie_stats(self):
        """
        Initializes the game_goalie_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_goalie_stats \
                (game_id INT, player_id INT, team_id INT, even_strength_shots_against VARCHAR(25), power_play_shots_against VARCHAR(25),\
                shorthanded_shots_against VARCHAR(25), saves_shots_against VARCHAR(25), even_strength_goals_against INT, power_play_goals_against INT,\
                shorthanded_goals_against INT, penalty_minutes INT, goals_against INT, time_on_ice VARCHAR(25),\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (player_id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(team_id),\
                PRIMARY KEY (game_id, player_id));"
    
    def __delete_game_goalie_stats(self):
        return "DROP TABLE IF EXISTS game_goalie_stats"
    
    def __initialize_game_plays(self):
        """
        Initializes the game_plays table in the database.
        This table holds the common details about each play.
        """
        return """CREATE TABLE IF NOT EXISTS game_plays (
                    game_id INT, play_id INT, event_id INT, period_number INT, period_type VARCHAR(25), time_in_period VARCHAR(25),\
                    time_remaining VARCHAR(25), situation_code VARCHAR(25), home_team_defending_side VARCHAR(25), type_code VARCHAR(25),\
                    type_description_key VARCHAR(50), sort_order INT, x_coord INT, y_coord INT, zone_code VARCHAR(25), shot_type VARCHAR(50),\
                    FOREIGN KEY (game_id) REFERENCES games(game_id),\
                    PRIMARY KEY (game_id, play_id)\
                );"""
    
    def __delete_game_plays(self):
        return "DROP TABLE IF EXISTS game_plays"

    def __initialize_play_roles(self):
        """
        Initializes the play_roles table in the database.
        This table links players to plays and specifies their roles in each play.
        """
        return """CREATE TABLE IF NOT EXISTS play_roles (
                    game_id INT, play_id INT, player_id INT, role_code VARCHAR(50),\
                    FOREIGN KEY (game_id, play_id) REFERENCES game_plays(game_id, play_id),\
                    FOREIGN KEY (player_id) REFERENCES players(id),\
                    PRIMARY KEY (game_id, play_id, player_id, role_code)\
                );"""
    
    def __delete_play_roles(self):
        return "DROP TABLE IF EXISTS play_roles"

    def __initialize_play_outcomes(self):
        """
        Initializes the play_outcomes table in the database.
        This table stores the outcomes specific to certain types of plays.
        """
        return """CREATE TABLE IF NOT EXISTS play_outcomes (
                    game_id INT, play_id INT, away_score INT, home_score INT, duration INT, reason VARCHAR(255),\
                    secondary_reason VARCHAR(255),\
                    FOREIGN KEY (game_id, play_id) REFERENCES game_plays(game_id, play_id),\
                    PRIMARY KEY (game_id, play_id)\
                );"""

    def __delete_play_outcomes(self):
        return "DROP TABLE IF EXISTS play_outcomes"
    
    def __initialize_play_on_ice(self):
        """
        Initializes the play_on_ice table in the database.
        This table stores the players on the ice for each play.
        """
        return """CREATE TABLE IF NOT EXISTS play_on_ice (
                    game_id INT, play_id INT, player_id INT, team_id INT, home BOOLEAN, away BOOLEAN,\
                    FOREIGN KEY (game_id, play_id) REFERENCES game_plays(game_id, play_id),\
                    FOREIGN KEY (player_id) REFERENCES players(id),\
                    FOREIGN KEY (team_id) REFERENCES teams(team_id),\
                    PRIMARY KEY (game_id, play_id, player_id)\
                );"""
    
    def __delete_play_on_ice(self):
        return "DROP TABLE IF EXISTS play_on_ice"
    
    def __initialize_game_three_stars(self):
        """
        Initializes the game_three_stars table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_three_stars \
                (game_id INT, star_1 INT, star_2 INT, star_3 INT,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), PRIMARY KEY (game_id)\
                );"
    
    def __delete_game_three_stars(self):
        return "DROP TABLE IF EXISTS game_three_stars"
    
    def __initialize_game_goals(self):
        """
        Initializes the game_goals table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS game_goals \
                (game_id INT, situation_code VARCHAR(25), strength VARCHAR(25), player_id INT, highlight_clip_id BIGINT, goals_to_date INT,\
                away_score INT, home_score INT, leading_team_id INT, time_in_period VARCHAR(25), shot_type VARCHAR(25), goal_modifier VARCHAR(25),\
                assist_1_player_id INT, assist_2_player_id INT,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (player_id) REFERENCES players(id),\
                FOREIGN KEY (leading_team_id) REFERENCES teams(team_id), FOREIGN KEY (assist_1_player_id) REFERENCES players(id),\
                FOREIGN KEY (assist_2_player_id) REFERENCES players(id), PRIMARY KEY (game_id, home_score, away_score));"

    def __delete_game_goals(self):
        return "DROP TABLE IF EXISTS game_goals"
    
    def __initialize_shift_data(self):
        """
        Initializes the shift_data table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS shift_data \
                (shift_id INT, game_id INT, player_id INT, detail_code INT, duration VARCHAR(25), end_time VARCHAR(25), start_time VARCHAR(25),\
                event_description VARCHAR(25), event_details VARCHAR(25), event_number INT, period_number INT, shift_number INT, type_code INT,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (player_id) REFERENCES players(id), PRIMARY KEY (shift_id));"
    
    def __delete_shift_data(self):
        return "DROP TABLE IF EXISTS shift_data"

    def __initialize_schedule(self):
        """
        Initializes the schedule table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS schedule \
                (game_id INT, home_team_id INT, away_team_id INT,\
                FOREIGN KEY (game_id) REFERENCES games(game_id), FOREIGN KEY (home_team_id) REFERENCES teams(team_id),\
                FOREIGN KEY (away_team_id) REFERENCES teams(team_id), PRIMARY KEY (game_id));"
    
    def __delete_schedule(self):
        return "DROP TABLE IF EXISTS schedule"
    
# MISC

    def __initialize_draft_rankings(self):
        """
        Initializes the draft_rankings table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS draft_rankings \
                (year INT, first_name VARCHAR(255), last_name VARCHAR(255), position_code VARCHAR(5), shoots_catches VARCHAR(5), height_inches INT,\
                weight_pounds INT, last_amateur_club VARCHAR(50), last_amateur_league VARCHAR(50), birth_date DATE, birth_city VARCHAR(50),\
                birth_state_province VARCHAR(50), birth_country VARCHAR(50), midterm_rank INT, final_rank INT,\
                PRIMARY KEY (year, first_name, last_name, final_rank));"
    
    def __delete_draft_rankings(self):
        return "DROP TABLE IF EXISTS draft_rankings"
    
    def __initialize_playoff_bracket(self):
        """
        Initializes the playoff_bracket table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS playoff_bracket \
                (year INT, round INT, top_seed_rank INT, top_seed_wins INT, top_seed_team_id INT, series_title VARCHAR(50),\
                bottom_seed_rank INT, bottom_seed_wins INT, bottom_seed_team_id INT, winning_team_id INT, losing_team_id INT,\
                FOREIGN KEY (top_seed_team_id) REFERENCES teams(team_id), FOREIGN KEY (bottom_seed_team_id) REFERENCES teams(team_id),\
                FOREIGN KEY (winning_team_id) REFERENCES teams(team_id), FOREIGN KEY (losing_team_id) REFERENCES teams(team_id),\
                PRIMARY KEY (year, round, top_seed_team_id, bottom_seed_team_id)\
                );"
    
    def __delete_playoff_bracket(self):
        return "DROP TABLE IF EXISTS playoff_bracket"
    
# TODO: ADD FANTASY HOCKEY RELATED TABLES