

class TeamAdvancedStatsFaceoffPercent:

    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.defensive_zone_faceoff_percent = None
        self.defensive_zone_faceoffs = None
        self.ev_faceoff_percent = None
        self.ev_faceoffs = None
        self.faceoff_win_percent = None
        self.neutral_zone_faceoff_percent = None
        self.neutral_zone_faceoffs = None
        self.offensive_zone_faceoff_percent = None
        self.offensive_zone_faceoffs = None
        self.pp_faceoff_percent = None
        self.pp_faceoffs = None
        self.pk_faceoff_percent = None
        self.pk_faceoffs = None
        self.total_faceoffs = None

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_defensive_zone_faceoff_percent(self):
        return self.defensive_zone_faceoff_percent
    
    def set_defensive_zone_faceoff_percent(self, defensive_zone_faceoff_percent):
        self.defensive_zone_faceoff_percent = defensive_zone_faceoff_percent

    def get_defensive_zone_faceoffs(self):
        return self.defensive_zone_faceoffs
    
    def set_defensive_zone_faceoffs(self, defensive_zone_faceoffs):
        self.defensive_zone_faceoffs = defensive_zone_faceoffs

    def get_ev_faceoff_percent(self):
        return self.ev_faceoff_percent
    
    def set_ev_faceoff_percent(self, ev_faceoff_percent):
        self.ev_faceoff_percent = ev_faceoff_percent

    def get_ev_faceoffs(self):
        return self.ev_faceoffs
    
    def set_ev_faceoffs(self, ev_faceoffs):
        self.ev_faceoffs = ev_faceoffs

    def get_faceoff_win_percent(self):
        return self.faceoff_win_percent
    
    def set_faceoff_win_percent(self, faceoff_win_percent):
        self.faceoff_win_percent = faceoff_win_percent

    def get_neutral_zone_faceoff_percent(self):
        return self.neutral_zone_faceoff_percent
    
    def set_neutral_zone_faceoff_percent(self, neutral_zone_faceoff_percent):
        self.neutral_zone_faceoff_percent = neutral_zone_faceoff_percent

    def get_neutral_zone_faceoffs(self):
        return self.neutral_zone_faceoffs
    
    def set_neutral_zone_faceoffs(self, neutral_zone_faceoffs):
        self.neutral_zone_faceoffs = neutral_zone_faceoffs

    def get_offensive_zone_faceoff_percent(self):
        return self.offensive_zone_faceoff_percent
    
    def set_offensive_zone_faceoff_percent(self, offensive_zone_faceoff_percent):
        self.offensive_zone_faceoff_percent = offensive_zone_faceoff_percent

    def get_offensive_zone_faceoffs(self):
        return self.offensive_zone_faceoffs
    
    def set_offensive_zone_faceoffs(self, offensive_zone_faceoffs):
        self.offensive_zone_faceoffs = offensive_zone_faceoffs

    def get_pp_faceoff_percent(self):
        return self.pp_faceoff_percent
    
    def set_pp_faceoff_percent(self, pp_faceoff_percent):
        self.pp_faceoff_percent = pp_faceoff_percent

    def get_pp_faceoffs(self):
        return self.pp_faceoffs
    
    def set_pp_faceoffs(self, pp_faceoffs):
        self.pp_faceoffs = pp_faceoffs

    def get_pk_faceoff_percent(self):
        return self.pk_faceoff_percent
    
    def set_pk_faceoff_percent(self, pk_faceoff_percent):
        self.pk_faceoff_percent = pk_faceoff_percent

    def get_pk_faceoffs(self):
        return self.pk_faceoffs
    
    def set_pk_faceoffs(self, pk_faceoffs):
        self.pk_faceoffs = pk_faceoffs

    def get_total_faceoffs(self):
        return self.total_faceoffs
    
    def set_total_faceoffs(self, total_faceoffs):
        self.total_faceoffs = total_faceoffs
