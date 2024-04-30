

class TeamStats:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.game_type_id = None
        self.games_played = None
        self.goals_against = None
        self.goals_for = None
        self.losses = None
        self.ot_losses = None
        self.points = None
        self.shootout_losses = None
        self.shootout_wins = None
        self.streak_code = None
        self.streak_count = None
        self.ties = None
        self.waiver_sequence = None
        self.regulation_wins = None
        self.regulation_plus_ot_wins = None
        self.home_games_played = None
        self.home_goals_against = None
        self.home_goals_for = None
        self.home_losses = None
        self.home_ot_losses = None
        self.home_points = None
        self.home_regulation_wins = None
        self.home_regulation_plus_ot_wins = None
        self.home_ties = None
        self.home_wins = None
        self.last_10_games_played = None
        self.last_10_goals_against = None
        self.last_10_goals_for = None
        self.last_10_losses = None
        self.last_10_ot_losses = None
        self.last_10_points = None
        self.last_10_regulation_wins = None
        self.last_10_regulation_plus_ot_wins = None
        self.last_10_ties = None
        self.last_10_wins = None
        self.road_games_played = None
        self.road_goals_against = None
        self.road_goals_for = None  
        self.road_losses = None
        self.road_ot_losses = None
        self.road_points = None
        self.road_regulation_wins = None
        self.road_regulation_plus_ot_wins = None
        self.road_ties = None
        self.road_wins = None

    def get_team_id(self):
        return self.team_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_game_type_id(self, game_type_id):
        self.game_type_id = game_type_id

    def get_game_type_id(self):
        return self.game_type_id
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_goals_against(self, goals_against):
        self.goals_against = goals_against

    def get_goals_against(self):
        return self.goals_against
    
    def set_goals_for(self, goals_for):
        self.goals_for = goals_for

    def get_goals_for(self):
        return self.goals_for
    
    def set_losses(self, losses):
        self.losses = losses

    def get_losses(self):
        return self.losses
    
    def set_ot_losses(self, ot_losses):
        self.ot_losses = ot_losses

    def get_ot_losses(self):
        return self.ot_losses
    
    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points
    
    def set_shootout_losses(self, shootout_losses):
        self.shootout_losses = shootout_losses

    def get_shootout_losses(self):
        return self.shootout_losses
    
    def set_shootout_wins(self, shootout_wins):
        self.shootout_wins = shootout_wins

    def get_shootout_wins(self):
        return self.shootout_wins
    
    def set_streak_code(self, streak_code):
        self.streak_code = streak_code

    def get_streak_code(self):
        return self.streak_code
    
    def set_streak_count(self, streak_count):
        self.streak_count = streak_count

    def get_streak_count(self):
        return self.streak_count
    
    def set_ties(self, ties):
        self.ties = ties

    def get_ties(self):
        return self.ties
    
    def set_waiver_sequence(self, waiver_sequence):
        self.waiver_sequence = waiver_sequence

    def get_waiver_sequence(self):
        return self.waiver_sequence
    
    def set_regulation_wins(self, regulation_wins):
        self.regulation_wins = regulation_wins

    def get_regulation_wins(self):
        return self.regulation_wins
    
    def set_regulation_plus_ot_wins(self, regulation_plus_ot_wins):
        self.regulation_plus_ot_wins = regulation_plus_ot_wins

    def get_regulation_plus_ot_wins(self):
        return self.regulation_plus_ot_wins
    
    def set_home_games_played(self, home_games_played):
        self.home_games_played = home_games_played

    def get_home_games_played(self):
        return self.home_games_played
    
    def set_home_goals_against(self, home_goals_against):
        self.home_goals_against = home_goals_against

    def get_home_goals_against(self):
        return self.home_goals_against
    
    def set_home_goals_for(self, home_goals_for):
        self.home_goals_for = home_goals_for

    def get_home_goals_for(self):
        return self.home_goals_for
    
    def set_home_losses(self, home_losses):
        self.home_losses = home_losses

    def get_home_losses(self):
        return self.home_losses
    
    def set_home_ot_losses(self, home_ot_losses):
        self.home_ot_losses = home_ot_losses

    def get_home_ot_losses(self):
        return self.home_ot_losses
    
    def set_home_points(self, home_points):
        self.home_points = home_points

    def get_home_points(self):
        return self.home_points
    
    def set_home_regulation_wins(self, home_regulation_wins):
        self.home_regulation_wins = home_regulation_wins

    def get_home_regulation_wins(self):
        return self.home_regulation_wins
    
    def set_home_regulation_plus_ot_wins(self, home_regulation_plus_ot_wins):
        self.home_regulation_plus_ot_wins = home_regulation_plus_ot_wins

    def get_home_regulation_plus_ot_wins(self):
        return self.home_regulation_plus_ot_wins
    
    def set_home_ties(self, home_ties):
        self.home_ties = home_ties

    def get_home_ties(self):
        return self.home_ties
    
    def set_home_wins(self, home_wins):
        self.home_wins = home_wins

    def get_home_wins(self):
        return self.home_wins
    
    def set_last_10_games_played(self, last_10_games_played):
        self.last_10_games_played = last_10_games_played

    def get_last_10_games_played(self):
        return self.last_10_games_played
    
    def set_last_10_goals_against(self, last_10_goals_against):
        self.last_10_goals_against = last_10_goals_against

    def get_last_10_goals_against(self):
        return self.last_10_goals_against
    
    def set_last_10_goals_for(self, last_10_goals_for):
        self.last_10_goals_for = last_10_goals_for

    def get_last_10_goals_for(self):
        return self.last_10_goals_for
    
    def set_last_10_losses(self, last_10_losses):
        self.last_10_losses = last_10_losses

    def get_last_10_losses(self):
        return self.last_10_losses
    
    def set_last_10_ot_losses(self, last_10_ot_losses):
        self.last_10_ot_losses = last_10_ot_losses

    def get_last_10_ot_losses(self):
        return self.last_10_ot_losses
    
    def set_last_10_points(self, last_10_points):
        self.last_10_points = last_10_points

    def get_last_10_points(self):
        return self.last_10_points
    
    def set_last_10_regulation_wins(self, last_10_regulation_wins):
        self.last_10_regulation_wins = last_10_regulation_wins

    def get_last_10_regulation_wins(self):
        return self.last_10_regulation_wins
    
    def set_last_10_regulation_plus_ot_wins(self, last_10_regulation_plus_ot_wins):
        self.last_10_regulation_plus_ot_wins = last_10_regulation_plus_ot_wins

    def get_last_10_regulation_plus_ot_wins(self):
        return self.last_10_regulation_plus_ot_wins
    
    def set_last_10_ties(self, last_10_ties):
        self.last_10_ties = last_10_ties

    def get_last_10_ties(self):
        return self.last_10_ties

    def set_last_10_wins(self, last_10_wins):
        self.last_10_wins = last_10_wins

    def get_last_10_wins(self):
        return self.last_10_wins
    
    def set_road_games_played(self, road_games_played):
        self.road_games_played = road_games_played

    def get_road_games_played(self):
        return self.road_games_played
    
    def set_road_goals_against(self, road_goals_against):
        self.road_goals_against = road_goals_against

    def get_road_goals_against(self):
        return self.road_goals_against
    
    def set_road_goals_for(self, road_goals_for):
        self.road_goals_for = road_goals_for

    def get_road_goals_for(self):
        return self.road_goals_for
    
    def set_road_losses(self, road_losses):
        self.road_losses = road_losses

    def get_road_losses(self):
        return self.road_losses
    
    def set_road_ot_losses(self, road_ot_losses):
        self.road_ot_losses = road_ot_losses

    def get_road_ot_losses(self):
        return self.road_ot_losses
    
    def set_road_points(self, road_points):
        self.road_points = road_points

    def get_road_points(self):
        return self.road_points
    
    def set_road_regulation_wins(self, road_regulation_wins):
        self.road_regulation_wins = road_regulation_wins

    def get_road_regulation_wins(self):
        return self.road_regulation_wins
    
    def set_road_regulation_plus_ot_wins(self, road_regulation_plus_ot_wins):
        self.road_regulation_plus_ot_wins = road_regulation_plus_ot_wins

    def get_road_regulation_plus_ot_wins(self):
        return self.road_regulation_plus_ot_wins
    
    def set_road_ties(self, road_ties):
        self.road_ties = road_ties

    def get_road_ties(self):
        return self.road_ties
    
    def set_road_wins(self, road_wins):
        self.road_wins = road_wins

    def get_road_wins(self):
        return self.road_wins
    






