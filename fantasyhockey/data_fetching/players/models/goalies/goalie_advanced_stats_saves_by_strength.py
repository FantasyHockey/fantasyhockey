

class GoalieAdvancedStatsSavesByStrength():
    
    def __init__(self, player_id, year, team_id):
        self.player_id = player_id
        self.year = year
        self.team_id = team_id
        self.ev_goals_against = None
        self.ev_save_percent = None
        self.ev_saves = None
        self.ev_shots_against = None
        self.pp_goals_against = None
        self.pp_save_percent = None
        self.pp_saves = None
        self.pp_shots_against = None
        self.pk_goals_against = None
        self.pk_save_percent = None
        self.pk_saves = None
        self.pk_shots_against = None

    def get_player_id(self):
        return self.player_id
    
    def set_ev_goals_against(self, ev_goals_against):
        self.ev_goals_against = ev_goals_against

    def get_ev_goals_against(self):
        return self.ev_goals_against
    
    def set_ev_save_percent(self, ev_save_percent):
        self.ev_save_percent = ev_save_percent

    def get_ev_save_percent(self):
        return self.ev_save_percent
    
    def set_ev_saves(self, ev_saves):
        self.ev_saves = ev_saves

    def get_ev_saves(self):
        return self.ev_saves
    
    def set_ev_shots_against(self, ev_shots_against):
        self.ev_shots_against = ev_shots_against

    def get_ev_shots_against(self):
        return self.ev_shots_against
    
    def set_pp_goals_against(self, pp_goals_against):
        self.pp_goals_against = pp_goals_against

    def get_pp_goals_against(self):
        return self.pp_goals_against
    
    def set_pp_save_percent(self, pp_save_percent):
        self.pp_save_percent = pp_save_percent

    def get_pp_save_percent(self):
        return self.pp_save_percent
    
    def set_pp_saves(self, pp_saves):
        self.pp_saves = pp_saves

    def get_pp_saves(self):
        return self.pp_saves
    
    def set_pp_shots_against(self, pp_shots_against):
        self.pp_shots_against = pp_shots_against

    def get_pp_shots_against(self):
        return self.pp_shots_against
    
    def set_pk_goals_against(self, pk_goals_against):
        self.pk_goals_against = pk_goals_against

    def get_pk_goals_against(self):
        return self.pk_goals_against
    
    def set_pk_save_percent(self, pk_save_percent):
        self.pk_save_percent = pk_save_percent

    def get_pk_save_percent(self):
        return self.pk_save_percent
    
    def set_pk_saves(self, pk_saves):
        self.pk_saves = pk_saves

    def get_pk_saves(self):
        return self.pk_saves
    
    def set_pk_shots_against(self, pk_shots_against):
        self.pk_shots_against = pk_shots_against

    def get_pk_shots_against(self):
        return self.pk_shots_against
    
    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    