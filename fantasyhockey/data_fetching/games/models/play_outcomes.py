

class PlayOutcomes:
    def __init__(self, game_id, play_id):
        self.game_id = game_id
        self.play_id = play_id
        self.away_score = None
        self.home_score = None
        self.duration = None
        self.reason = None
        self.secondary_reason = None

    def get_game_id(self):
        return self.game_id
    
    def get_play_id(self):
        return self.play_id
    
    def set_away_score(self, away_score):
        self.away_score = away_score

    def get_away_score(self):
        return self.away_score
    
    def set_home_score(self, home_score):
        self.home_score = home_score

    def get_home_score(self):
        return self.home_score
    
    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration
    
    def set_reason(self, reason):
        self.reason = reason

    def get_reason(self):
        return self.reason
    
    def set_secondary_reason(self, secondary_reason):
        self.secondary_reason = secondary_reason

    def get_secondary_reason(self):
        return self.secondary_reason
    
    
        
