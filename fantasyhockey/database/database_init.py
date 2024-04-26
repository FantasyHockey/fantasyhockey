from fantasyhockey.database.database_operator import DatabaseOperator


class DatabaseInitializer:
    def __init__(self):
        pass

    def run(self):
        db_operator = DatabaseOperator()

        db_operator.write(self.__initialize_database())
        db_operator.write(self.__initialize_players())
        

        # db_operator.write(self.__delete_players())

        return False

    def __initialize_database(self):
        return "CREATE DATABASE IF NOT EXISTS fantasyhockey"

    def __initialize_players(self):
        return "CREATE TABLE IF NOT EXISTS players  \
                (id INT PRIMARY KEY, team_id INT, is_active BOOLEAN)"

    def __delete_players(self):
        return "DROP TABLE IF EXISTS players"

    def __initialize_player_details(self):
        return "CREATE TABLE IF NOT EXISTS player_details \
                (id INT PRIMARY KEY, is_active BOOLEAN, team_id INT, first_name VARCHAR(255), last_name VARCHAR(255),\
                jersey_number VARCHAR(255), position VARCHAR(15), headshot VARCHAR(255), hero_image VARCHAR(255),\
                height_inches INT, weight_pounds INT, birth_date VARCHAR(50),\
                birth_city VARCHAR(255), birth_state_province VARCHAR(255), birth_country VARCHAR(255), shoots_catches VARCHAR(5),\
                in_top_100_all_time BOOLEAN, in_hhof BOOLEAN),\
                Foreign Key (id) References players(id), \
                Foreign Key (team_id) References players(team_id)"

    def __delete_player_details(self):
        return "DROP TABLE IF EXISTS player_details"

    def __initialize_player_draft(self):
        return "CREATE TABLE IF NOT EXISTS player_draft \
                (id INT PRIMARY KEY, year VARCHAR(255), team_id INT, round INT, pick_in_round INT, overall_pick INT  \
                Foreign Key (id) References players(id), \
                Foreign Key (team_id) References players(team_id)"

    def __delete_player_draft(self):
        return "DROP TABLE IF EXISTS player_draft"

    def __initialize_player_awards(self):
        return "CREATE TABLE IF NOT EXISTS player_awards \
                (id INT, award_name VARCHAR(255), year VARCHAR(255) \
                Foreign Key (id) References players(id), Primary Key (id, award_name, year)"

    def __delete_player_awards(self):
        return "DROP TABLE IF EXISTS player_awards"

# SKATER EXCLUSIVE TABLES   
    def __initialize_skater_current_stats(self):
        """
        Initializes the current_skater_stats table in the database.

        Primary Key - id, year, sequence, game_type_id

        Need blocks, hits, primary and secondary assists from other source
        """
        return "CREATE TABLE IF NOT EXISTS current_skater_stats \
                (id INT, team_id INT, games_played INT, goals INT, assists INT, points INT, plus_minus INT, penalty_minutes INT,\
                game_winning_goals INT, ot_goals INT, power_play_goals INT, power_play_points INT, shooting_percent FLOAT,\
                shorthanded_goals INT, shorthanded_points INT, shots INT, time_on_ice VARCHAR(255), game_type_id INT, year INT,\
                sequence INT, faceoff_percent FLOAT, league_id INT, blocks INT, hits INT, primary_assists INT, secondary_assists INT),\
                FOREIGN KEY (id) References players(id), FOREIGN KEY (team_id) References players(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, sequence, game_type_id)"

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
                sequence INT, faceoff_percent FLOAT, league_id INT, blocks INT, hits INT, primary_assists INT, secondary_assists INT),\
                FOREIGN KEY (id) References players(id), FOREIGN KEY (team_id) References players(team_id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, sequence, game_type_id)"

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
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id)"

    def __delete_skater_advanced_stats_toi(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats"

    def __initialize_skater_advanced_stats_scoring(self):
        """
        Initializes the skater_advanced_stats_scoring table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_scoring \
                (id INT, year INT, team_id INT, goals_backhand INT, goals_bat INT, goals_between_legs INT,\
                    goals_cradle INT, goals_deflected INT, goals_poke INT, goals_slap INT, goals_snap INT, goals_tip INT, goals_wrap_around INT, goals_wrist INT,\
                    shots_backhand INT, shots_bat INT, shots_between_legs INT, shots_cradle INT, shots_deflected INT, shots_poke INT, shots_slap INT, shots_snap INT,\
                    shots_tip INT, shots_wrap_around INT, shots_wrist INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id)"

    def __delete_skater_advanced_stats_scoring(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_scoring"
                    
    def __initialize_skate_advanced_stats_shootout(self):
        """
        Initializes the skater_advanced_stats_shootout table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_shootout \
                (id INT, year INT, team_id INT, career_shootout_game_deciding_goals INT, career_shootout_games_played INT, career_shootout_goals INT,\
                    career_shootout_percentage FLOAT, career_shootout_shots INT, shootout_game_deciding_goals INT, shootout_games_played INT,\
                    shootout_goals INT, shootout_percentage FLOAT, shootout_shots INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id)"

    def __delete_skater_advanced_stats_shootout(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_shootout"

    def __initialize_skater_advanced_stats_corsi_fenwick(self):
        """
        Initializes the skater_advanced_stats_corsi_fenwick table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_corsi_fenwick \
                (id INT, year INT, team_id INT, games_played INT, corsi_against INT, corsi_ahead INT, corsi_behind INT,\
                corsi_close INT, corsi_for INT, corsi_relative FLOAT, corsi_tied INT, corsi_total INT, fenwick_against INT,\
                fenwick_ahead INT, fenwick_behind INT, fenwick_close INT, fenwick_for INT, fenwick_relative FLOAT,\
                fenwick_tied INT, fenwick_total INT, corsi_percent FLOAT, corsi_ahead_percent FLOAT, corsi_behind_percent FLOAT,\
                corsi_close_percent FLOAT, corsi_tied_percent FLOAT, corsi_relative FLOAT, shooting_percent_5on5 FLOAT,\
                skater_save_percent_5on5 FLOAT, skater_shooting_plus_save_percent_5on5 FLOAT, time_on_ice_5on5_per_game FLOAT,\
                fenwick_percent FLOAT, fenwick_ahead_percent FLOAT, fenwick_behind_percent FLOAT, fenwick_close_percent FLOAT,\
                fenwick_tied_percent FLOAT, zone_start_5on5_percent FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"
    
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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

    def __delete_skater_advanced_stats_misc(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_misc"

    def __initialize_skater_advanced_stats_goals(self):
        """
        Initializes the skater_advanced_stats_goals table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_advanced_stats_goals \
                (id INT, year INT, team_id INT, even_strength_goal_difference INT, even_strength_goals_against INT, even_strength_goals_for INT,\
                even_strength_time_on_ice_per_Game FLOAT, games_played INT, pp_goals_for INT, pp_goals_against INT, pk_goals_for INT,\
                pk_goals_against INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

    def __delete_skater_advanced_stats_faceoffs(self):
        return "DROP TABLE IF EXISTS skater_advanced_stats_faceoffs"

    def __initialize_skater_youth_stats(self):
        """
        Initializes the skater_youth_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS skater_youth_stats \
                (id INT, year INT, team_name VARCHAR(255), league_name VARCHAR(255), game_type_id INT, sequence INT, games_played INT,\
                goals INT, assists INT, points INT, pim INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_name) REFERENCES teams(team_name), FOREIGN KEY (league_name) REFERENCES leagues(league_name),\
                FOREIGN KEY (year) REFERENCES seasons(year), PRIMARY KEY (id, year, team_name, league_name, game_type_id, sequence)"

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
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id, game_type_id, sequence)"

    def __delete_goalie_current_stats(self):
        return "DROP TABLE IF EXISTS goalie_current_stats"

    def __initialize_goalie_stats(self):
        """
        Initializes the goalie_stats table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_stats \
                (id INT, team_id INT, year INT, game_type_id INT, league_id INT, sequence INT, games_played INT, goals INT, assists INT,\
                    games_started INT, wins INT, losses INT, ot_losses INT, shots_against INT, goals_against INT, save_percent FLOAT,\
                    shutouts INT, time_on_ice VARCHAR (100), goals_against_average FLOAT, pim INT,\
                    FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                    PRIMARY KEY (id, year, team_id, game_type_id, sequence)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_name) REFERENCES teams(team_name), FOREIGN KEY (league_name) REFERENCES leagues(league_name),\
                FOREIGN KEY (year) REFERENCES seasons(year), PRIMARY KEY (id, year, team_name, league_name, game_type_id, sequence)" 

    def __delete_goalie_youth_stats(self):
        return "DROP TABLE IF EXISTS goalie_youth_stats"

# TEAM TABLES
    def __initialize_goalie_advanced_stats_days_rest(self):
        """
        Initializes the goalie_advanced_stats_days_rest table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_days_rest \
                (id INT, year INT, team_id INT, games_played INT, games_played_days_rest_0 INT, games_played_days_rest_1 INT,\
                games_played_days_rest_2 INT, games_played_days_rest_3 INT, games_played_days_rest_4 INT, games_played_days_rest_4_plus INT,\
                games_started INT, losses INT, ot_losses INT, save_percent FLOAT, save_percent_days_rest_0 FLOAT, save_percent_days_rest_1 FLOAT,\
                save_percent_days_rest_2 FLOAT, save_percent_days_rest_3 FLOAT, save_percent_days_rest_4 FLOAT, save_percent_days_rest_4_plus FLOAT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

    def __delete_goalie_advanced_stats_days_rest(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_days_rest"

    def __initialize_goalie_advanced_stats_penalty_shots(self):
        """
        Initializes the goalie_advanced_stats_penalty_shots table in the database.
        """
        return "CREATE TABLE IF NOT EXISTS goalie_advanced_stats_penalty_shots \
                (id INT, year INT, team_id INT, penalty_shot_save_percent FLOAT, penalty_shot_against INT, penalty_shot_goals_against INT,\
                penalty_shot_saves INT,\
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

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
                FOREIGN KEY (id) REFERENCES players(id), FOREIGN KEY (team_id) REFERENCES teams(id), FOREIGN KEY (year) REFERENCES seasons(year),\
                PRIMARY KEY (id, year, team_id)"

    def __delete_goalie_advanced_stats_start_relieved(self):
        return "DROP TABLE IF EXISTS goalie_advanced_stats_start_relieved"

    def __initialize_teams(self):
        pass

    def __delete_teams(self):
        pass

    def __initialize_leagues(self):
        pass

    def __delete_leagues(self):
        pass

    def __initialize_seasons(self):
        pass

    def __delete_seasons(self):
        pass

    def __initialize_team_stats(self):
        pass

    def __delete_team_stats(self):
        pass

    def __initialize_team_advanced_stats(self):
        pass

    def __delete_team_advanced_stats(self):
        pass

    def __initialize_games(self):
        pass

    def __delete_games(self):
        pass

    def __initialize_game__team_stats(self):
        pass

    def __delete_game_team_stats(self):
        pass

    def __initialize_team_schedule(self):
        pass

    def __delete_team_schedule(self):
        pass

    def __initialize_game_skater_stats(self):
        pass

    def __delete_game_skater_stats(self):
        pass

    def __initialize_game_skater_advanced_stats(self):
        pass

    def __delete_game_skater_advanced_stats(self):
        pass

    def __initialize_game_goalie_stats(self):
        pass

    def __delete_game_goalie_stats(self):
        pass

    def __initialize_game_goalie_advanced_stats(self):
        pass

    def __delete_game_goalie_advanced_stats(self):
        pass

    def __initialize_game_events(self):
        pass

    def __delete_game_events(self):
        pass

    def __initialize_shift_data(self):
        pass

    def __delete_shift_data(self):
        pass