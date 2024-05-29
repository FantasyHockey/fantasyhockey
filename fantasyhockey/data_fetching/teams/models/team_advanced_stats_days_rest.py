

class TeamAdvancedStatsDaysRest:

    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.days_rest = None
        self.games_played = None
        self.faceoff_percent = None
        self.goals_against_per_game = None
        self.goals_for_per_game = None
        self.losses = None
        self.net_goals_per_game = None
        self.ot_losses = None
        self.penalty_kill_percent = None
        self.point_percent = None
        self.points = None
        self.power_play_percent = None
        self.power_play_opportunities_per_game = None
        self.shot_differential_per_game = None
        self.shots_against_per_game = None
        self.shots_for_per_game = None
        self.ties = None
        self.times_shorthanded_per_game = None
        self.wins = None

    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_days_rest(self):
        return self.days_rest
    
    def set_days_rest(self, days_rest):
        self.days_rest = days_rest

    def get_games_played(self):
        return self.games_played
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_faceoff_percent(self):
        return self.faceoff_percent
    
    def set_faceoff_percent(self, faceoff_percent):
        self.faceoff_percent = faceoff_percent

    def get_goals_against_per_game(self):
        return self.goals_against_per_game
    
    def set_goals_against_per_game(self, goals_against_per_game):
        self.goals_against_per_game = goals_against_per_game

    def get_goals_for_per_game(self):
        return self.goals_for_per_game
    
    def set_goals_for_per_game(self, goals_for_per_game):
        self.goals_for_per_game = goals_for_per_game

    def get_losses(self):
        return self.losses
    
    def set_losses(self, losses):
        self.losses = losses

    def get_net_goals_per_game(self):
        return self.net_goals_per_game
    
    def set_net_goals_per_game(self, net_goals_per_game):
        self.net_goals_per_game = net_goals_per_game

    def get_ot_losses(self):
        return self.ot_losses
    
    def set_ot_losses(self, ot_losses):
        self.ot_losses = ot_losses

    def get_penalty_kill_percent(self):
        return self.penalty_kill_percent
    
    def set_penalty_kill_percent(self, penalty_kill_percent):
        self.penalty_kill_percent = penalty_kill_percent

    def get_point_percent(self):
        return self.point_percent
    
    def set_point_percent(self, point_percent):
        self.point_percent = point_percent

    def get_points(self):
        return self.points
    
    def set_points(self, points):
        self.points = points

    def get_power_play_percent(self):
        return self.power_play_percent
    
    def set_power_play_percent(self, power_play_percent):
        self.power_play_percent = power_play_percent

    def get_power_play_opportunities_per_game(self):
        return self.power_play_opportunities_per_game
    
    def set_power_play_opportunities_per_game(self, power_play_opportunities_per_game):
        self.power_play_opportunities_per_game = power_play_opportunities_per_game

    def get_shot_differential_per_game(self):
        return self.shot_differential_per_game
    
    def set_shot_differential_per_game(self, shot_differential_per_game):
        self.shot_differential_per_game = shot_differential_per_game

    def get_shots_against_per_game(self):
        return self.shots_against_per_game
    
    def set_shots_against_per_game(self, shots_against_per_game):
        self.shots_against_per_game = shots_against_per_game

    def get_shots_for_per_game(self):
        return self.shots_for_per_game
    
    def set_shots_for_per_game(self, shots_for_per_game):
        self.shots_for_per_game = shots_for_per_game

    def get_ties(self):
        return self.ties
    
    def set_ties(self, ties):
        self.ties = ties

    def get_times_shorthanded_per_game(self):
        return self.times_shorthanded_per_game
    
    def set_times_shorthanded_per_game(self, times_shorthanded_per_game):
        self.times_shorthanded_per_game = times_shorthanded_per_game

    def get_wins(self):
        return self.wins
    
    def set_wins(self, wins):
        self.wins = wins

        