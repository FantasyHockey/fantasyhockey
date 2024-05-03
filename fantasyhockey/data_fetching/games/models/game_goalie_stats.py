

class GameGoalieStats:

    def __init__(self, game_id, player_id):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = None
        self.even_strength_shots_against = None
        self.power_play_shots_against = None
        self.short_handed_shots_against = None
        self.saves_shots_against = None
        self.even_strength_goals_against = None
        self.power_play_goals_against = None
        self.shorthanded_goals_against = None
        self.penalty_minutes = None
        self.goals_against = None
        self.time_on_ice = None

    def get_game_id(self):
        return self.game_id
    
    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_even_strength_shots_against(self, even_strength_shots_against):
        self.even_strength_shots_against = even_strength_shots_against

    def get_even_strength_shots_against(self):
        return self.even_strength_shots_against
    
    def set_power_play_shots_against(self, power_play_shots_against):
        self.power_play_shots_against = power_play_shots_against

    def get_power_play_shots_against(self):
        return self.power_play_shots_against
    
    def set_short_handed_shots_against(self, short_handed_shots_against):
        self.short_handed_shots_against = short_handed_shots_against

    def get_short_handed_shots_against(self):
        return self.short_handed_shots_against
    
    def set_saves_shots_against(self, saves_shots_against):
        self.saves_shots_against = saves_shots_against

    def get_saves_shots_against(self):
        return self.saves_shots_against
    
    def set_even_strength_goals_against(self, even_strength_goals_against):
        self.even_strength_goals_against = even_strength_goals_against

    def get_even_strength_goals_against(self):
        return self.even_strength_goals_against
    
    def set_power_play_goals_against(self, power_play_goals_against):
        self.power_play_goals_against = power_play_goals_against

    def get_power_play_goals_against(self):
        return self.power_play_goals_against
    
    def set_shorthanded_goals_against(self, shorthanded_goals_against):
        self.shorthanded_goals_against = shorthanded_goals_against

    def get_shorthanded_goals_against(self):
        return self.shorthanded_goals_against
    
    def set_penalty_minutes(self, penalty_minutes):
        self.penalty_minutes = penalty_minutes

    def get_penalty_minutes(self):
        return self.penalty_minutes
    
    def set_goals_against(self, goals_against):
        self.goals_against = goals_against

    def get_goals_against(self):
        return self.goals_against
    
    def set_time_on_ice(self, time_on_ice):
        self.time_on_ice = time_on_ice

    def get_time_on_ice(self):
        return self.time_on_ice