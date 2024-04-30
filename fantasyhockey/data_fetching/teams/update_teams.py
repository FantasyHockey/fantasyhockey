from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.teams.fetch_teams import FetchTeams

class UpdateTeams:
    def __init__(self):
        self.database_operator = DatabaseOperator()
        self.fetch_teams = FetchTeams()

    def update_in_db(self):
        teams = self.fetch_teams.get_teams()
        for team in teams:
            teams_query, teams_params = self.__create_teams_query(team)
            team_stats_query, team_stats_params = self.__create_team_stats_query(team)
            self.database_operator.write(teams_query, teams_params)
            self.database_operator.write(team_stats_query, team_stats_params)

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

                
                
                