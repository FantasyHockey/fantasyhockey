
class TeamAdvancedStatsLeadingTrailing:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.loss_lead_period_1 = None
        self.loss_lead_period_2 = None
        self.loss_trail_period_1 = None
        self.loss_trail_period_2 = None
        self.ot_loss_lead_period_1 = None
        self.ot_loss_lead_period_2 = None
        self.ot_loss_trail_period_1 = None
        self.ot_loss_trail_period_2 = None
        self.period_1_goals_against = None
        self.period_1_goals_for = None
        self.period_2_goals_against = None
        self.period_2_goals_for = None
        self.ties_lead_period_1 = None
        self.ties_lead_period_2 = None
        self.ties_trail_period_1 = None
        self.ties_trail_period_2 = None
        self.win_percent_lead_period_1 = None
        self.win_percent_lead_period_2 = None
        self.win_percent_trail_period_1 = None
        self.win_percent_trail_period_2 = None
        self.wins_lead_period_1 = None
        self.wins_lead_period_2 = None
        self.wins_trail_period_1 = None
        self.wins_trail_period_2 = None

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_loss_lead_period_1(self):
        return self.loss_lead_period_1
    
    def set_loss_lead_period_1(self, loss_lead_period_1):
        self.loss_lead_period_1 = loss_lead_period_1

    def get_loss_lead_period_2(self):
        return self.loss_lead_period_2
    
    def set_loss_lead_period_2(self, loss_lead_period_2):
        self.loss_lead_period_2 = loss_lead_period_2

    def get_loss_trail_period_1(self):
        return self.loss_trail_period_1
    
    def set_loss_trail_period_1(self, loss_trail_period_1):
        self.loss_trail_period_1 = loss_trail_period_1

    def get_loss_trail_period_2(self):
        return self.loss_trail_period_2
    
    def set_loss_trail_period_2(self, loss_trail_period_2):
        self.loss_trail_period_2 = loss_trail_period_2

    def get_ot_loss_lead_period_1(self):
        return self.ot_loss_lead_period_1
    
    def set_ot_loss_lead_period_1(self, ot_loss_lead_period_1):
        self.ot_loss_lead_period_1 = ot_loss_lead_period_1

    def get_ot_loss_lead_period_2(self):
        return self.ot_loss_lead_period_2
    
    def set_ot_loss_lead_period_2(self, ot_loss_lead_period_2):
        self.ot_loss_lead_period_2 = ot_loss_lead_period_2

    def get_ot_loss_trail_period_1(self):
        return self.ot_loss_trail_period_1
    
    def set_ot_loss_trail_period_1(self, ot_loss_trail_period_1):
        self.ot_loss_trail_period_1 = ot_loss_trail_period_1

    def get_ot_loss_trail_period_2(self):
        return self.ot_loss_trail_period_2
    
    def set_ot_loss_trail_period_2(self, ot_loss_trail_period_2):
        self.ot_loss_trail_period_2 = ot_loss_trail_period_2

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

    def get_ties_lead_period_1(self):
        return self.ties_lead_period_1
    
    def set_ties_lead_period_1(self, ties_lead_period_1):
        self.ties_lead_period_1 = ties_lead_period_1

    def get_ties_lead_period_2(self):
        return self.ties_lead_period_2
    
    def set_ties_lead_period_2(self, ties_lead_period_2):
        self.ties_lead_period_2 = ties_lead_period_2

    def get_ties_trail_period_1(self):
        return self.ties_trail_period_1
    
    def set_ties_trail_period_1(self, ties_trail_period_1):
        self.ties_trail_period_1 = ties_trail_period_1

    def get_ties_trail_period_2(self):
        return self.ties_trail_period_2
    
    def set_ties_trail_period_2(self, ties_trail_period_2):
        self.ties_trail_period_2 = ties_trail_period_2

    def get_win_percent_lead_period_1(self):
        return self.win_percent_lead_period_1
    
    def set_win_percent_lead_period_1(self, win_percent_lead_period_1):
        self.win_percent_lead_period_1 = win_percent_lead_period_1

    def get_win_percent_lead_period_2(self):
        return self.win_percent_lead_period_2
    
    def set_win_percent_lead_period_2(self, win_percent_lead_period_2):
        self.win_percent_lead_period_2 = win_percent_lead_period_2

    def get_win_percent_trail_period_1(self):
        return self.win_percent_trail_period_1
    
    def set_win_percent_trail_period_1(self, win_percent_trail_period_1):
        self.win_percent_trail_period_1 = win_percent_trail_period_1

    def get_win_percent_trail_period_2(self):
        return self.win_percent_trail_period_2
    
    def set_win_percent_trail_period_2(self, win_percent_trail_period_2):
        self.win_percent_trail_period_2 = win_percent_trail_period_2

    def get_wins_lead_period_1(self):
        return self.wins_lead_period_1
    
    def set_wins_lead_period_1(self, wins_lead_period_1):
        self.wins_lead_period_1 = wins_lead_period_1

    def get_wins_lead_period_2(self):
        return self.wins_lead_period_2
    
    def set_wins_lead_period_2(self, wins_lead_period_2):
        self.wins_lead_period_2 = wins_lead_period_2

    def get_wins_trail_period_1(self):
        return self.wins_trail_period_1
    
    def set_wins_trail_period_1(self, wins_trail_period_1):
        self.wins_trail_period_1 = wins_trail_period_1

    def get_wins_trail_period_2(self):
        return self.wins_trail_period_2
    
    def set_wins_trail_period_2(self, wins_trail_period_2):
        self.wins_trail_period_2 = wins_trail_period_2

