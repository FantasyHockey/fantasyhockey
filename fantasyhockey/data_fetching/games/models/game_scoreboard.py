

class GameScoreboard:

    def __init__(self, game_id):
        self.game_id = game_id
        self.home_score = None
        self.away_score = None
        self.home_shots = None
        self.away_shots = None
        self.time_remaining = None
        self.period = None
        self.seconds_remaining = None
        self.running = None
        self.in_intermission = None

    def get_game_id(self):
        return self.game_id
    
    def set_home_score(self, home_score):
        self.home_score = home_score

    def get_home_score(self):
        return self.home_score
    
    def set_away_score(self, away_score):
        self.away_score = away_score

    def get_away_score(self):
        return self.away_score
    
    def set_home_shots(self, home_shots):
        self.home_shots = home_shots

    def get_home_shots(self):
        return self.home_shots
    
    def set_away_shots(self, away_shots):
        self.away_shots = away_shots

    def get_away_shots(self):
        return self.away_shots
    
    def set_time_remaining(self, time_remaining):
        self.time_remaining = time_remaining

    def get_time_remaining(self):
        return self.time_remaining
    
    def set_period(self, period):
        self.period = period

    def get_period(self):
        return self.period
    
    def set_seconds_remaining(self, seconds_remaining):
        self.seconds_remaining = seconds_remaining

    def get_seconds_remaining(self):
        return self.seconds_remaining
    
    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running
    
    def set_in_intermission(self, in_intermission):
        self.in_intermission = in_intermission

    def get_in_intermission(self):
        return self.in_intermission
    
    