

class SkaterAdvancedStatsTOI:
    def __init__(self, player_id):
        self.player_id = player_id
        self.team_id = None
        self.year = None
        self.ev_time_on_ice = None
        self.games_played = None
        self.ot_time_on_ice = None
        self.ot_time_on_ice_per_ot_game = None
        self.pp_time_on_ice = None
        self.sh_time_on_ice = None
        self.shifts = None
        self.time_on_ice = None

    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_ev_time_on_ice(self, ev_time_on_ice):
        self.ev_time_on_ice = ev_time_on_ice

    def get_ev_time_on_ice(self):
        return self.ev_time_on_ice
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_ot_time_on_ice(self, ot_time_on_ice):
        self.ot_time_on_ice = ot_time_on_ice

    def get_ot_time_on_ice(self):
        return self.ot_time_on_ice
    
    def set_ot_time_on_ice_per_ot_game(self, ot_time_on_ice_per_ot_game):
        self.ot_time_on_ice_per_ot_game = ot_time_on_ice_per_ot_game

    def get_ot_time_on_ice_per_ot_game(self):
        return self.ot_time_on_ice_per_ot_game
    
    def set_pp_time_on_ice(self, pp_time_on_ice):
        self.pp_time_on_ice = pp_time_on_ice

    def get_pp_time_on_ice(self):
        return self.pp_time_on_ice
    
    def set_sh_time_on_ice(self, sh_time_on_ice):
        self.sh_time_on_ice = sh_time_on_ice

    def get_sh_time_on_ice(self):
        return self.sh_time_on_ice
    
    def set_shifts(self, shifts):
        self.shifts = shifts

    def get_shifts(self):
        return self.shifts
    
    def set_time_on_ice(self, time_on_ice):
        self.time_on_ice = time_on_ice

    def get_time_on_ice(self):
        return self.time_on_ice