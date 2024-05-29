

class TeamAdvancedStatsGoalsByPeriod:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.ev_goals_for = None
        self.period_1_goals_against = None
        self.period_1_goals_for = None
        self.period_2_goals_against = None
        self.period_2_goals_for = None
        self.period_3_goals_against = None
        self.period_3_goals_for = None
        self.period_ot_goals_against = None
        self.period_ot_goals_for = None
        self.pp_goals_for = None
        self.pk_goals_for = None

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_ev_goals_for(self):
        return self.ev_goals_for
    
    def set_ev_goals_for(self, ev_goals_for):
        self.ev_goals_for = ev_goals_for

    def get_period_1_goals_against(self):
        return self.period_1_goals_against
    
    def set_period_1_goals_against(self, period_1_goals_against):
        self.period_1_goals_against = period_1_goals_against

    def get_period_1_goals_for(self):
        return self.period_1_goals_for
    
    def set_period_1_goals_for(self, period_1_goals_for):
        self.period_1_goals_for = period_1_goals_for

    def get_period_2_goals_against(self):
        return self.period_2_goals_against
    
    def set_period_2_goals_against(self, period_2_goals_against):
        self.period_2_goals_against = period_2_goals_against

    def get_period_2_goals_for(self):
        return self.period_2_goals_for
    
    def set_period_2_goals_for(self, period_2_goals_for):
        self.period_2_goals_for = period_2_goals_for

    def get_period_3_goals_against(self):
        return self.period_3_goals_against
    
    def set_period_3_goals_against(self, period_3_goals_against):
        self.period_3_goals_against = period_3_goals_against

    def get_period_3_goals_for(self):
        return self.period_3_goals_for
    
    def set_period_3_goals_for(self, period_3_goals_for):
        self.period_3_goals_for = period_3_goals_for

    def get_period_ot_goals_against(self):
        return self.period_ot_goals_against
    
    def set_period_ot_goals_against(self, period_ot_goals_against):
        self.period_ot_goals_against = period_ot_goals_against

    def get_period_ot_goals_for(self):
        return self.period_ot_goals_for
    
    def set_period_ot_goals_for(self, period_ot_goals_for):
        self.period_ot_goals_for = period_ot_goals_for

    def get_pp_goals_for(self):
        return self.pp_goals_for
    
    def set_pp_goals_for(self, pp_goals_for):
        self.pp_goals_for = pp_goals_for

    def get_pk_goals_for(self):
        return self.pk_goals_for
    
    def set_pk_goals_for(self, pk_goals_for):
        self.pk_goals_for = pk_goals_for

        