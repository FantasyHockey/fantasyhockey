

class TeamAdvancedStatsMisc:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.blocked_shots = None
        self.empty_net_goals = None
        self.giveaways = None 
        self.hits = None
        self.missed_shots = None
        self.takeaways = None
        self.time_on_ice_per_game_5on5 = None
        

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_blocked_shots(self):
        return self.blocked_shots
    
    def set_blocked_shots(self, blocked_shots):
        self.blocked_shots = blocked_shots

    def get_empty_net_goals(self):
        return self.empty_net_goals
    
    def set_empty_net_goals(self, empty_net_goals):
        self.empty_net_goals = empty_net_goals

    def get_giveaways(self):
        return self.giveaways
    
    def set_giveaways(self, giveaways):
        self.giveaways = giveaways

    def get_hits(self):
        return self.hits
    
    def set_hits(self, hits):
        self.hits = hits

    def get_missed_shots(self):
        return self.missed_shots
    
    def set_missed_shots(self, missed_shots):
        self.missed_shots = missed_shots

    def get_takeaways(self):
        return self.takeaways
    
    def set_takeaways(self, takeaways):
        self.takeaways = takeaways

    def get_time_on_ice_per_game_5on5(self):
        return self.time_on_ice_per_game
    
    def set_time_on_ice_per_game_5on5(self, time_on_ice_per_game):
        self.time_on_ice_per_game = time_on_ice_per_game

        