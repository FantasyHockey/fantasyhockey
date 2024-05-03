

class SkaterAdvnacedStatsMisc:
    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.blocked_shots = None
        self.empty_net_assists = None
        self.empty_net_goals = None
        self.empty_net_points = None
        self.first_goals = None
        self.giveaways = None
        self.games_played = None
        self.hits = None
        self.missed_shot_crossbar = None
        self.missed_shot_goalpost = None
        self.missed_shot_over = None
        self.missed_shot_wide = None
        self.missed_shots = None
        self.ot_goals = None
        self.takeaways = None
        self.time_on_ice_per_game = None

    def get_player_id(self):
        return self.player_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_blocked_shots(self, blocked_shots):
        self.blocked_shots = blocked_shots

    def get_blocked_shots(self):
        return self.blocked_shots
    
    def set_empty_net_assists(self, empty_net_assists):
        self.empty_net_assists = empty_net_assists

    def get_empty_net_assists(self):
        return self.empty_net_assists
    
    def set_empty_net_goals(self, empty_net_goals):
        self.empty_net_goals = empty_net_goals

    def get_empty_net_goals(self):
        return self.empty_net_goals
    
    def set_empty_net_points(self, empty_net_points):
        self.empty_net_points = empty_net_points

    def get_empty_net_points(self):
        return self.empty_net_points
    
    def set_first_goals(self, first_goals):
        self.first_goals = first_goals

    def get_first_goals(self):
        return self.first_goals
    
    def set_giveaways(self, giveaways):
        self.giveaways = giveaways

    def get_giveaways(self):
        return self.giveaways
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_hits(self, hits):
        self.hits = hits

    def get_hits(self):
        return self.hits
    
    def set_missed_shot_crossbar(self, missed_shot_crossbar):
        self.missed_shot_crossbar = missed_shot_crossbar

    def get_missed_shot_crossbar(self):
        return self.missed_shot_crossbar
    
    def set_missed_shot_goalpost(self, missed_shot_goalpost):
        self.missed_shot_goalpost = missed_shot_goalpost

    def get_missed_shot_goalpost(self):
        return self.missed_shot_goalpost
    
    def set_missed_shot_over(self, missed_shot_over):
        self.missed_shot_over = missed_shot_over

    def get_missed_shot_over(self):
        return self.missed_shot_over
    
    def set_missed_shot_wide(self, missed_shot_wide):
        self.missed_shot_wide = missed_shot_wide

    def get_missed_shot_wide(self):
        return self.missed_shot_wide
    
    def set_missed_shots(self, missed_shots):
        self.missed_shots = missed_shots

    def get_missed_shots(self):
        return self.missed_shots
    
    def set_ot_goals(self, ot_goals):
        self.ot_goals = ot_goals

    def get_ot_goals(self):
        return self.ot_goals
    
    def set_takeaways(self, takeaways):
        self.takeaways = takeaways

    def get_takeaways(self):
        return self.takeaways
    
    def set_time_on_ice_per_game(self, time_on_ice_per_game):
        self.time_on_ice_per_game = time_on_ice_per_game

    def get_time_on_ice_per_game(self):
        return self.time_on_ice_per_game
    