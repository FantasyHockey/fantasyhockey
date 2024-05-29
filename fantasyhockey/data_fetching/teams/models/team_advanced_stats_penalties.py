

class TeamAdvancedStatsPenalties:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.bench_minor_penalties = None
        self.game_misconducts = None
        self.majors = None
        self.match_penalties = None
        self.minors = None
        self.misconducts = None
        self.net_penalties = None
        self.penalties = None
        self.penalty_minutes = None
        self.penalty_seconds_per_game = None
        self.total_penalties_drawn = None
        
    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_bench_minor_penalties(self):
        return self.bench_minor_penalties
    
    def set_bench_minor_penalties(self, bench_minor_penalties):
        self.bench_minor_penalties = bench_minor_penalties

    def get_game_misconducts(self):
        return self.game_misconducts
    
    def set_game_misconducts(self, game_misconducts):
        self.game_misconducts = game_misconducts

    def get_majors(self):
        return self.majors
    
    def set_majors(self, majors):
        self.majors = majors

    def get_match_penalties(self):
        return self.match_penalties
    
    def set_match_penalties(self, match_penalties):
        self.match_penalties = match_penalties

    def get_minors(self):
        return self.minors
    
    def set_minors(self, minors):
        self.minors = minors

    def get_misconducts(self):
        return self.misconducts
    
    def set_misconducts(self, misconducts):
        self.misconducts = misconducts

    def get_net_penalties(self):
        return self.net_penalties
    
    def set_net_penalties(self, net_penalties):
        self.net_penalties = net_penalties

    def get_penalties(self):
        return self.penalties
    
    def set_penalties(self, penalties):
        self.penalties = penalties

    def get_penalty_minutes(self):
        return self.penalty_minutes
    
    def set_penalty_minutes(self, penalty_minutes):
        self.penalty_minutes = penalty_minutes

    def get_penalty_seconds_per_game(self):
        return self.penalty_seconds_per_game
    
    def set_penalty_seconds_per_game(self, penalty_seconds_per_game):
        self.penalty_seconds_per_game = penalty_seconds_per_game

    def get_total_penalties_drawn(self):
        return self.total_penalties_drawn
    
    def set_total_penalties_drawn(self, total_penalties_drawn):
        self.total_penalties_drawn = total_penalties_drawn
