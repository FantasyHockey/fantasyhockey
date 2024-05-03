

class SkaterAdvancedStatsGoals:

    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.even_strength_goal_difference = None
        self.even_strength_goals_against = None
        self.even_strength_goals_for = None
        self.even_strength_time_on_ice_per_game = None
        self.games_played = None
        self.pp_goals_for = None
        self.pp_goals_against = None
        self.pk_goals_for = None
        self.pk_goals_against = None

    def get_player_id(self):
        return self.player_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_even_strength_goal_difference(self, even_strength_goal_difference):
        self.even_strength_goal_difference = even_strength_goal_difference

    def get_even_strength_goal_difference(self):
        return self.even_strength_goal_difference
    
    def set_even_strength_goals_against(self, even_strength_goals_against):
        self.even_strength_goals_against = even_strength_goals_against

    def get_even_strength_goals_against(self):
        return self.even_strength_goals_against
    
    def set_even_strength_goals_for(self, even_strength_goals_for):
        self.even_strength_goals_for = even_strength_goals_for

    def get_even_strength_goals_for(self):
        return self.even_strength_goals_for
    
    def set_even_strength_time_on_ice_per_game(self, even_strength_time_on_ice_per_game):
        self.even_strength_time_on_ice_per_game = even_strength_time_on_ice_per_game

    def get_even_strength_time_on_ice_per_game(self):
        return self.even_strength_time_on_ice_per_game
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_pp_goals_for(self, pp_goals_for):
        self.pp_goals_for = pp_goals_for

    def get_pp_goals_for(self):
        return self.pp_goals_for
    
    def set_pp_goals_against(self, pp_goals_against):
        self.pp_goals_against = pp_goals_against

    def get_pp_goals_against(self):
        return self.pp_goals_against
    
    def set_pk_goals_for(self, pk_goals_for):
        self.pk_goals_for = pk_goals_for

    def get_pk_goals_for(self):
        return self.pk_goals_for
    
    def set_pk_goals_against(self, pk_goals_against):
        self.pk_goals_against = pk_goals_against

    def get_pk_goals_against(self):
        return self.pk_goals_against
    
