from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.players.fetch_goalies import FetchGoalies
from fantasyhockey.data_fetching.players.models.goalies.goalie_stats import GoalieStats
from fantasyhockey.data_fetching.players.models.goalies.goalie import Goalie
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats import GoalieAdvancedStats
from fantasyhockey.data_fetching.players.models.goalies.goalie_youth_stats import GoalieYouthStats
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_days_rest import GoalieAdvancedStatsDaysRest
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_penalty_shots import GoalieAdvancedStatsPenaltyShots
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_saves_by_strength import GoalieAdvancedStatsSavesByStrength
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_shootout import GoalieAdvancedStatsShootout
from fantasyhockey.data_fetching.players.models.goalies.goalie_advanced_stats_start_relieved import GoalieAdvancedStatsStartRelieved


class UpdateGoalies:
    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_goalies = FetchGoalies()


    def write_in_db(self):
        """Write player data to the database."""
        goalies = self.fetch_goalies.get_goalies()
        count = 0
        for goalie in goalies:
            count += 1
            print(f"Writing goalie {count} / {len(goalies)} to database.")
            try:
                goalie_stats = goalie.get_goalie_stats()
                for stats in goalie_stats:
                    query, params = self.__create_goalie_stats_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} stats to database.")
                print(e)

            try:
                goalie_youth_stats = goalie.get_goalie_youth_stats()
                for stats in goalie_youth_stats:
                    query, params = self.__create_goalie_youth_stats_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} youth stats to database.")
                print(e)

            try:
                goalie_advanced_stats = goalie.get_goalie_advanced_stats()
                for stats in goalie_advanced_stats:
                    query, params = self.__create_goalie_advanced_stats_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats to database.")
                print(e)

            try:
                goalie_advanced_stats_days_rest = goalie.get_goalie_advanced_stats_days_rest()
                for stats in goalie_advanced_stats_days_rest:
                    query, params = self.__create_goalie_advanced_stats_days_rest_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats days rest to database.")
                print(e)

            try:
                goalie_advanced_stats_penalty_shots = goalie.get_goalie_advanced_stats_penalty_shots()
                for stats in goalie_advanced_stats_penalty_shots:
                    query, params = self.__create_goalie_advanced_stats_penalty_shots_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats penalty shots to database.")
                print(e)

            try:
                goalie_advanced_stats_saves_by_strength = goalie.get_goalie_advanced_stats_saves_by_strength()
                for stats in goalie_advanced_stats_saves_by_strength:
                    query, params = self.__create_goalie_advanced_stats_saves_by_strength_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats saves by strength to database.")
                print(e)

            try:
                goalie_advanced_stats_shootout = goalie.get_goalie_advanced_stats_shootout()
                for stats in goalie_advanced_stats_shootout:
                    query, params = self.__create_goalie_advanced_stats_shootout_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats shootout to database.")
                print(e)

            try:
                goalie_advanced_stats_start_relieved = goalie.get_goalie_advanced_stats_start_relieved()
                for stats in goalie_advanced_stats_start_relieved:
                    query, params = self.__create_goalie_advanced_stats_start_relieved_query(stats)
                    self.database_operator.write(query, params)
            except Exception as e:
                print(f"Error writing skater {goalie.get_id()} advanced stats start relieved to database.")
                print(e)

    def update_in_db(self):
        """Update player data in the database."""
        pass

    def __create_goalie_stats_query(self, goalie_stats: GoalieStats) -> tuple:

        query = "INSERT INTO goalie_stats (id, team_id, year, game_type_id, sequence, games_played, goals, assists, games_started,\
                wins, losses, ot_losses, shots_against, goals_against, save_percent, shutouts, time_on_ice, goals_against_average,\
                penalty_minutes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_stats.get_player_id(), goalie_stats.get_team_id(), goalie_stats.get_year(), goalie_stats.get_game_type_id(),\
                    goalie_stats.get_sequence(), goalie_stats.get_games_played(), goalie_stats.get_goals(), goalie_stats.get_assists(),\
                    goalie_stats.get_games_started(), goalie_stats.get_wins(), goalie_stats.get_losses(), goalie_stats.get_ot_losses(),\
                    goalie_stats.get_shots_against(), goalie_stats.get_goals_against(), goalie_stats.get_save_percent(), goalie_stats.get_shutouts(),\
                    goalie_stats.get_time_on_ice(), goalie_stats.get_goals_against_average(), goalie_stats.get_penalty_minutes())
        
        return query, params
        
    def __create_goalie_youth_stats_query(self, goalie_youth_stats: GoalieYouthStats) -> tuple:

        query = "INSERT INTO goalie_youth_stats (id, year, team_name, league_name, game_type_id, sequence, games_played, save_percent,\
                goals_against_average, goals_against, wins, losses, time_on_ice, ties) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_youth_stats.get_player_id(), goalie_youth_stats.get_year(), goalie_youth_stats.get_team_name(), goalie_youth_stats.get_league_name(),\
                    goalie_youth_stats.get_game_type_id(), goalie_youth_stats.get_sequence(), goalie_youth_stats.get_games_played(), goalie_youth_stats.get_save_percentage(),\
                    goalie_youth_stats.get_goals_against_average(), goalie_youth_stats.get_goals_against(), goalie_youth_stats.get_wins(), goalie_youth_stats.get_losses(),\
                    goalie_youth_stats.get_time_on_ice(), goalie_youth_stats.get_ties())
        
        return query, params
    
    def __create_goalie_advanced_stats_query(self, goalie_advanced_stats: GoalieAdvancedStats) -> tuple:
            
        query = "INSERT INTO goalie_advanced_stats (id, year, team_id, complete_game_percent, complete_games, games_played,\
                games_started, goals_against, goals_against_average, goals_for, goals_for_average, incomplete_games, quality_start,\
                quality_starts_percent, regulation_losses, regulation_wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (goalie_advanced_stats.get_player_id(), goalie_advanced_stats.get_year(), goalie_advanced_stats.get_team_id(), goalie_advanced_stats.get_complete_game_percentage(),\
                    goalie_advanced_stats.get_complete_games(), goalie_advanced_stats.get_games_played(), goalie_advanced_stats.get_games_started(), goalie_advanced_stats.get_goals_against(),\
                    goalie_advanced_stats.get_goals_against_average(), goalie_advanced_stats.get_goals_for(), goalie_advanced_stats.get_goals_for_average(), goalie_advanced_stats.get_incomplete_games(),\
                    goalie_advanced_stats.get_quality_starts(), goalie_advanced_stats.get_quality_starts_percentage(), goalie_advanced_stats.get_regulation_losses(), goalie_advanced_stats.get_regulation_wins())
        
        return query, params
    
    def __create_goalie_advanced_stats_days_rest_query(self, goalie_advanced_stats_days_rest: GoalieAdvancedStatsDaysRest) -> tuple:
                
        query = "INSERT INTO goalie_advanced_stats_days_rest (id, year, team_id, games_played, games_played_days_rest_0, games_played_days_rest_1,\
                games_played_days_rest_2, games_played_days_rest_3, games_played_days_rest_4, games_played_days_rest_4_plus, games_started, losses,\
                ot_losses, save_percent, save_percent_days_rest_0, save_percent_days_rest_1, save_percent_days_rest_2, save_percent_days_rest_3,\
                save_percent_days_rest_4, save_percent_days_rest_4_plus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_advanced_stats_days_rest.get_player_id(), goalie_advanced_stats_days_rest.get_year(), goalie_advanced_stats_days_rest.get_team_id(), goalie_advanced_stats_days_rest.get_games_played(),\
                    goalie_advanced_stats_days_rest.get_games_played_days_rest_0(), goalie_advanced_stats_days_rest.get_games_played_days_rest_1(), goalie_advanced_stats_days_rest.get_games_played_days_rest_2(), goalie_advanced_stats_days_rest.get_games_played_days_rest_3(),\
                    goalie_advanced_stats_days_rest.get_games_played_days_rest_4(), goalie_advanced_stats_days_rest.get_games_played_days_rest_4_plus(), goalie_advanced_stats_days_rest.get_games_started(), goalie_advanced_stats_days_rest.get_losses(),\
                    goalie_advanced_stats_days_rest.get_ot_losses(), goalie_advanced_stats_days_rest.get_save_percent(), goalie_advanced_stats_days_rest.get_save_percent_days_rest_0(), goalie_advanced_stats_days_rest.get_save_percent_days_rest_1(),\
                    goalie_advanced_stats_days_rest.get_save_percent_days_rest_2(), goalie_advanced_stats_days_rest.get_save_percent_days_rest_3(), goalie_advanced_stats_days_rest.get_save_percent_days_rest_4(), goalie_advanced_stats_days_rest.get_save_percent_days_rest_4_plus())
        
        return query, params
    
    def __create_goalie_advanced_stats_penalty_shots_query(self, goalie_advanced_stats_penalty_shots: GoalieAdvancedStatsPenaltyShots) -> tuple:
        
        query = "INSERT INTO goalie_advanced_stats_penalty_shots (id, year, team_id, penalty_shot_save_percent, penalty_shot_against,\
                penalty_shot_goals_against, penalty_shot_saves) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_advanced_stats_penalty_shots.get_player_id(), goalie_advanced_stats_penalty_shots.get_year(), goalie_advanced_stats_penalty_shots.get_team_id(), goalie_advanced_stats_penalty_shots.get_penalty_shot_save_percent(),\
                    goalie_advanced_stats_penalty_shots.get_penalty_shot_against(), goalie_advanced_stats_penalty_shots.get_penalty_shot_goals_against(), goalie_advanced_stats_penalty_shots.get_penalty_shot_saves())
        
        return query, params
    
    def __create_goalie_advanced_stats_saves_by_strength_query(self, goalie_advanced_stats_saves_by_strength: GoalieAdvancedStatsSavesByStrength) -> tuple:
            
        query = "INSERT INTO goalie_advanced_stats_saves_by_strength (id, year, team_id, ev_goals_against, ev_save_percent,\
                ev_saves, ev_shots_against, pp_goals_against, pp_save_percent, pp_saves, pp_shots_against, pk_goals_against,\
                pk_save_percent, pk_saves, pk_shots_against) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_advanced_stats_saves_by_strength.get_player_id(), goalie_advanced_stats_saves_by_strength.get_year(), goalie_advanced_stats_saves_by_strength.get_team_id(), goalie_advanced_stats_saves_by_strength.get_ev_goals_against(),\
                    goalie_advanced_stats_saves_by_strength.get_ev_save_percent(), goalie_advanced_stats_saves_by_strength.get_ev_saves(), goalie_advanced_stats_saves_by_strength.get_ev_shots_against(), goalie_advanced_stats_saves_by_strength.get_pp_goals_against(),\
                    goalie_advanced_stats_saves_by_strength.get_pp_save_percent(), goalie_advanced_stats_saves_by_strength.get_pp_saves(), goalie_advanced_stats_saves_by_strength.get_pp_shots_against(), goalie_advanced_stats_saves_by_strength.get_pk_goals_against(),\
                    goalie_advanced_stats_saves_by_strength.get_pk_save_percent(), goalie_advanced_stats_saves_by_strength.get_pk_saves(), goalie_advanced_stats_saves_by_strength.get_pk_shots_against())
        
        return query, params
    
    def __create_goalie_advanced_stats_shootout_query(self, goalie_advanced_stats_shootout: GoalieAdvancedStatsShootout) -> tuple:
            
        query = "INSERT INTO goalie_advanced_stats_shootout (id, year, team_id, career_shootout_games_played, career_shootout_goals_allowed,\
                career_shootout_losses, career_shootout_save_percent, career_shootout_saves, career_shootout_shots_against, career_shootout_wins,\
                shootout_goals_against, shootout_losses, shootout_save_percent, shootout_saves, shootout_shots_against, shootout_wins)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_advanced_stats_shootout.get_player_id(), goalie_advanced_stats_shootout.get_year(), goalie_advanced_stats_shootout.get_team_id(), goalie_advanced_stats_shootout.get_career_shootout_games_played(),\
                    goalie_advanced_stats_shootout.get_career_shootout_goals_allowed(), goalie_advanced_stats_shootout.get_career_shootout_losses(), goalie_advanced_stats_shootout.get_career_shootout_save_percentage(), goalie_advanced_stats_shootout.get_career_shooutout_saves(),\
                    goalie_advanced_stats_shootout.get_career_shootout_shots_against(), goalie_advanced_stats_shootout.get_career_shootout_wins(), goalie_advanced_stats_shootout.get_shootout_goals_against(), goalie_advanced_stats_shootout.get_shootout_losses(),\
                    goalie_advanced_stats_shootout.get_shootout_save_percent(), goalie_advanced_stats_shootout.get_shootout_saves(), goalie_advanced_stats_shootout.get_shootout_shots_against(), goalie_advanced_stats_shootout.get_shootout_wins())
        
        return query, params
    
    def __create_goalie_advanced_stats_start_relieved_query(self, goalie_advanced_stats_start_relieved: GoalieAdvancedStatsStartRelieved) -> tuple:
                
        query = "INSERT INTO goalie_advanced_stats_start_relieved (id, year, team_id, games_played, games_relieved, games_relieved_goals_against,\
                games_relieved_losses, games_relieved_ot_losses, games_relieved_save_percent,\
                games_relieved_saves, games_relieved_shots_against, games_relieved_ties, games_relieved_wins, games_started, games_started_goals_against,\
                games_started_losses, games_started_ot_losses, games_started_save_percent, games_started_saves, games_started_shots_against,\
                games_started_ties, games_started_wins) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (goalie_advanced_stats_start_relieved.get_player_id(), goalie_advanced_stats_start_relieved.get_year(), goalie_advanced_stats_start_relieved.get_team_id(), goalie_advanced_stats_start_relieved.get_games_played(),\
                    goalie_advanced_stats_start_relieved.get_games_relieved(), goalie_advanced_stats_start_relieved.get_games_relieved_goals_against(), goalie_advanced_stats_start_relieved.get_games_relieved_losses(),\
                    goalie_advanced_stats_start_relieved.get_games_relieved_ot_losses(), goalie_advanced_stats_start_relieved.get_games_relieved_save_percent(), goalie_advanced_stats_start_relieved.get_games_relieved_saves(),\
                    goalie_advanced_stats_start_relieved.get_games_relieved_shots_against(), goalie_advanced_stats_start_relieved.get_games_relieved_ties(), goalie_advanced_stats_start_relieved.get_games_relieved_wins(), goalie_advanced_stats_start_relieved.get_games_started(),\
                    goalie_advanced_stats_start_relieved.get_games_started_goals_against(), goalie_advanced_stats_start_relieved.get_games_started_losses(), goalie_advanced_stats_start_relieved.get_games_started_ot_losses(), goalie_advanced_stats_start_relieved.get_games_started_save_percent(),\
                    goalie_advanced_stats_start_relieved.get_games_started_saves(), goalie_advanced_stats_start_relieved.get_games_started_shots_against(), goalie_advanced_stats_start_relieved.get_games_started_ties(), goalie_advanced_stats_start_relieved.get_games_started_wins())
        
        return query, params