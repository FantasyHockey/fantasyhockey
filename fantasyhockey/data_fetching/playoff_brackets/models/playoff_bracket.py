

class PlayoffBracket:
    def __init__(self, year, round, top_seed_team_id, bottom_seed_team_id):
        self.year = year
        self.round = round
        self.top_seed_team_id = top_seed_team_id
        self.bottom_seed_team_id = bottom_seed_team_id
        self.top_seed_rank = None
        self.top_seed_wins = None
        self.series_title = None
        self.bottom_seed_rank = None
        self.bottom_seed_wins = None
        self.winning_team_id = None
        self.losing_team_id = None

    def get_year(self):
        return self.year
    
    def get_round(self):
        return self.round
    
    def get_top_seed_team_id(self):
        return self.top_seed_team_id
    
    def get_bottom_seed_team_id(self):
        return self.bottom_seed_team_id
    
    def set_top_seed_rank(self, top_seed_rank):
        self.top_seed_rank = top_seed_rank

    def get_top_seed_rank(self):
        return self.top_seed_rank
    
    def set_top_seed_wins(self, top_seed_wins):
        self.top_seed_wins = top_seed_wins

    def get_top_seed_wins(self):
        return self.top_seed_wins
    
    def set_series_title(self, series_title):
        self.series_title = series_title

    def get_series_title(self):
        return self.series_title
    
    def set_bottom_seed_rank(self, bottom_seed_rank):
        self.bottom_seed_rank = bottom_seed_rank

    def get_bottom_seed_rank(self):
        return self.bottom_seed_rank
    
    def set_bottom_seed_wins(self, bottom_seed_wins):
        self.bottom_seed_wins = bottom_seed_wins

    def get_bottom_seed_wins(self):
        return self.bottom_seed_wins
    
    def set_winning_team_id(self, winning_team_id):
        self.winning_team_id = winning_team_id

    def get_winning_team_id(self):
        return self.winning_team_id
    
    def set_losing_team_id(self, losing_team_id):
        self.losing_team_id = losing_team_id

    def get_losing_team_id(self):
        return self.losing_team_id
    
    
