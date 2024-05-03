

class GameSkaterStats:

    def __init__(self, game_id, player_id):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = None
        self.goals = None
        self.assists = None
        self.points = None
        self.plus_minus = None
        self.peanlty_minutes = None
        self.hits = None
        self.blocks = None
        self.power_play_goals = None
        self.power_play_points = None
        self.short_handed_goals = None
        self.short_handed_points = None
        self.shots = None
        self.faceoffs = None
        self.time_on_ice = None
        self.power_play_time_on_ice = None
        self.shorthanded_time_on_ice = None

    def get_game_id(self):
        return self.game_id
    
    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_goals(self, goals):
        self.goals = goals

    def get_goals(self):
        return self.goals
    
    def set_assists(self, assists):
        self.assists = assists

    def get_assists(self):
        return self.assists
    
    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points
    
    def set_plus_minus(self, plus_minus):
        self.plus_minus = plus_minus

    def get_plus_minus(self):
        return self.plus_minus
    
    def set_penalty_minutes(self, penalty_minutes):
        self.penalty_minutes = penalty_minutes

    def get_penalty_minutes(self):
        return self.penalty_minutes
    
    def set_hits(self, hits):
        self.hits = hits

    def get_hits(self):
        return self.hits
    
    def set_blocks(self, blocks):
        self.blocks = blocks

    def get_blocks(self):
        return self.blocks
    
    def set_power_play_goals(self, power_play_goals):
        self.power_play_goals = power_play_goals

    def get_power_play_goals(self):
        return self.power_play_goals
    
    def set_power_play_points(self, power_play_points):
        self.power_play_points = power_play_points

    def get_power_play_points(self):
        return self.power_play_points
    
    def set_short_handed_goals(self, short_handed_goals):
        self.short_handed_goals = short_handed_goals

    def get_short_handed_goals(self):
        return self.short_handed_goals
    
    def set_short_handed_points(self, short_handed_points):
        self.short_handed_points = short_handed_points

    def get_short_handed_points(self):
        return self.short_handed_points
    
    def set_shots(self, shots):
        self.shots = shots

    def get_shots(self):
        return self.shots
    
    def set_faceoffs(self, faceoffs):
        self.faceoffs = faceoffs

    def get_faceoffs(self):
        return self.faceoffs
    
    def set_time_on_ice(self, time_on_ice):
        self.time_on_ice = time_on_ice

    def get_time_on_ice(self):
        return self.time_on_ice
    
    def set_power_play_time_on_ice(self, power_play_time_on_ice):
        self.power_play_time_on_ice = power_play_time_on_ice

    def get_power_play_time_on_ice(self):
        return self.power_play_time_on_ice
    
    def set_shorthanded_time_on_ice(self, shorthanded_time_on_ice):
        self.shorthanded_time_on_ice = shorthanded_time_on_ice

    def get_shorthanded_time_on_ice(self):
        return self.shorthanded_time_on_ice
    
    
