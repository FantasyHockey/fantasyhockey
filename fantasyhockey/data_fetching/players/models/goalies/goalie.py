

class Goalie:
    def __init__(self, id):
        self.id = id
        self.goalie_stats = []
        self.goalie_youth_stats = []
        self.goalie_advanced_stats = []
        self.goalie_advanced_stats_start_relieved = []
        self.goalie_advanced_stats_shootout = []
        self.goalie_advanced_stats_saves_by_strength = []
        self.goalie_advanced_stats_penalty_shots = []
        self.goalie_advanced_stats_days_rest = []

    def get_id(self):
        return self.id
    
    def set_goalie_stats(self, goalie_stats):
        self.goalie_stats = goalie_stats

    def get_goalie_stats(self):
        return self.goalie_stats
    
    def set_goalie_youth_stats(self, goalie_youth_stats):
        self.goalie_youth_stats = goalie_youth_stats

    def get_goalie_youth_stats(self):
        return self.goalie_youth_stats
    
    def set_goalie_advanced_stats(self, goalie_advanced_stats):
        self.goalie_advanced_stats = goalie_advanced_stats

    def get_goalie_advanced_stats(self):
        return self.goalie_advanced_stats
    
    def set_goalie_advanced_stats_start_relieved(self, goalie_advanced_stats_start_relieved):
        self.goalie_advanced_stats_start_relieved = goalie_advanced_stats_start_relieved

    def get_goalie_advanced_stats_start_relieved(self):
        return self.goalie_advanced_stats_start_relieved
    
    def set_goalie_advanced_stats_shootout(self, goalie_advanced_stats_shootout):
        self.goalie_advanced_stats_shootout = goalie_advanced_stats_shootout

    def get_goalie_advanced_stats_shootout(self):
        return self.goalie_advanced_stats_shootout
    
    def set_goalie_advanced_stats_saves_by_strength(self, goalie_advanced_stats_saves_by_strength):
        self.goalie_advanced_stats_saves_by_strength = goalie_advanced_stats_saves_by_strength

    def get_goalie_advanced_stats_saves_by_strength(self):
        return self.goalie_advanced_stats_saves_by_strength
    
    def set_goalie_advanced_stats_penalty_shots(self, goalie_advanced_stats_penalty_shots):
        self.goalie_advanced_stats_penalty_shots = goalie_advanced_stats_penalty_shots

    def get_goalie_advanced_stats_penalty_shots(self):
        return self.goalie_advanced_stats_penalty_shots
    
    def set_goalie_advanced_stats_days_rest(self, goalie_advanced_stats_days_rest):
        self.goalie_advanced_stats_days_rest = goalie_advanced_stats_days_rest

    def get_goalie_advanced_stats_days_rest(self):
        return self.goalie_advanced_stats_days_rest
    


