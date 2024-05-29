

class TeamAdvancedStatsScoringFirst:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.losses_scoring_first = None
        self.losses_trailing_first = None
        self.ot_losses_scoring_first = None
        self.ot_losses_trailing_first = None
        self.scoring_first_games_played = None
        self.ties_scoring_first = None
        self.ties_trailing_first = None
        self.trailing_first_games_played = None
        self.win_percent_scoring_first = None
        self.win_percent_trailing_first = None
        self.wins_scoring_first = None
        self.wins_trailing_first = None

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_losses_scoring_first(self):
        return self.losses_scoring_first
    
    def set_losses_scoring_first(self, losses_scoring_first):
        self.losses_scoring_first = losses_scoring_first

    def get_losses_trailing_first(self):
        return self.losses_trailing_first
    
    def set_losses_trailing_first(self, losses_trailing_first):
        self.losses_trailing_first = losses_trailing_first

    def get_ot_losses_scoring_first(self):
        return self.ot_losses_scoring_first
    
    def set_ot_losses_scoring_first(self, ot_losses_scoring_first):
        self.ot_losses_scoring_first = ot_losses_scoring_first

    def get_ot_losses_trailing_first(self):
        return self.ot_losses_trailing_first
    
    def set_ot_losses_trailing_first(self, ot_losses_trailing_first):
        self.ot_losses_trailing_first = ot_losses_trailing_first

    def get_scoring_first_games_played(self):
        return self.scoring_first_games_played
    
    def set_scoring_first_games_played(self, scoring_first_games_played):
        self.scoring_first_games_played = scoring_first_games_played

    def get_ties_scoring_first(self):
        return self.ties_scoring_first
    
    def set_ties_scoring_first(self, ties_scoring_first):
        self.ties_scoring_first = ties_scoring_first

    def get_ties_trailing_first(self):
        return self.ties_trailing_first
    
    def set_ties_trailing_first(self, ties_trailing_first):
        self.ties_trailing_first = ties_trailing_first

    def get_trailing_first_games_played(self):
        return self.trailing_first_games_played
    
    def set_trailing_first_games_played(self, trailing_first_games_played):
        self.trailing_first_games_played = trailing_first_games_played

    def get_win_percent_scoring_first(self):
        return self.win_percent_scoring_first
    
    def set_win_percent_scoring_first(self, win_percent_scoring_first):
        self.win_percent_scoring_first = win_percent_scoring_first

    def get_win_percent_trailing_first(self):
        return self.win_percent_trailing_first
    
    def set_win_percent_trailing_first(self, win_percent_trailing_first):
        self.win_percent_trailing_first = win_percent_trailing_first

    def get_wins_scoring_first(self):
        return self.wins_scoring_first
    
    def set_wins_scoring_first(self, wins_scoring_first):
        self.wins_scoring_first = wins_scoring_first

    def get_wins_trailing_first(self):
        return self.wins_trailing_first
    
    def set_wins_trailing_first(self, wins_trailing_first):
        self.wins_trailing_first = wins_trailing_first

            