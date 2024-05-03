

class Schedule:
    def __init__(self, game_id):
        self.game_id = game_id
        self.home_team_id = None
        self.away_team_id = None

    def get_game_id(self):
        return self.game_id
    
    def set_home_team_id(self, home_team_id):
        self.home_team_id = home_team_id

    def get_home_team_id(self):
        return self.home_team_id
    
    def set_away_team_id(self, away_team_id):
        self.away_team_id = away_team_id

    def get_away_team_id(self):
        return self.away_team_id
    
    