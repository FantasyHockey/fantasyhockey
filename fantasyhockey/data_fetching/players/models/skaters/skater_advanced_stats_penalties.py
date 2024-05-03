
class SkaterAdvancedStatsPenalties:

    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.game_misconduct_penalties = None
        self.games_played = None
        self.major_penalties = None
        self.match_penalties = None
        self.minor_penalties = None
        self.misconduct_penalties = None
        self.net_penalties = None
        self.penalties = None
        self.penalties_drawn = None
        self.penalty_minutes = None
        self.time_on_ice_per_game = None

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
    
    def set_game_misconduct_penalties(self, game_misconduct_penalties):
        self.game_misconduct_penalties = game_misconduct_penalties

    def get_game_misconduct_penalties(self):
        return self.game_misconduct_penalties
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_major_penalties(self, major_penalties):
        self.major_penalties = major_penalties

    def get_major_penalties(self):
        return self.major_penalties
    
    def set_match_penalties(self, match_penalties):
        self.match_penalties = match_penalties

    def get_match_penalties(self):
        return self.match_penalties
    
    def set_minor_penalties(self, minor_penalties):
        self.minor_penalties = minor_penalties

    def get_minor_penalties(self):
        return self.minor_penalties
    
    def set_misconduct_penalties(self, misconduct_penalties):
        self.misconduct_penalties = misconduct_penalties

    def get_misconduct_penalties(self):
        return self.misconduct_penalties
    
    def set_net_penalties(self, net_penalties):
        self.net_penalties = net_penalties

    def get_net_penalties(self):
        return self.net_penalties
    
    def set_penalties(self, penalties):
        self.penalties = penalties

    def get_penalties(self):
        return self.penalties
    
    def set_penalties_drawn(self, penalties_drawn):
        self.penalties_drawn = penalties_drawn

    def get_penalties_drawn(self):
        return self.penalties_drawn
    
    def set_penalty_minutes(self, penalty_minutes):
        self.penalty_minutes = penalty_minutes

    def get_penalty_minutes(self):
        return self.penalty_minutes
    
    def set_time_on_ice_per_game(self, time_on_ice_per_game):
        self.time_on_ice_per_game = time_on_ice_per_game

    def get_time_on_ice_per_game(self):
        return self.time_on_ice_per_game
    
    