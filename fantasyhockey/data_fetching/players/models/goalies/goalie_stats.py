

class GoalieStats:

    def __init__(self, player_id):
        self.player_id = player_id
        self.team_id = None
        self.year = None
        self.game_type_id = None
        self.sequence = None
        self.games_played = None
        self.goals = None
        self.assists = None
        self.games_started = None
        self.wins = None
        self.losses = None
        self.ot_losses = None
        self.shots_against = None
        self.goals_against = None
        self.save_percent = None
        self.shutouts = None
        self.time_on_ice = None
        self.penalty_minutes = None
        self.goals_against_average = None

    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def set_year(self, year):
        self.year = year

    def set_game_type_id(self, game_type_id):
        self.game_type_id = game_type_id

    def set_sequence(self, sequence):
        self.sequence = sequence
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_goals(self, goals):
        self.goals = goals

    def get_goals(self):
        return self.goals
    
    def set_assists(self, assists):
        self.assists = assists

    def get_assists(self):
        return self.assists
    
    def set_games_started(self, games_started):
        self.games_started = games_started

    def get_games_started(self):
        return self.games_started
    
    def set_wins(self, wins):
        self.wins = wins

    def get_wins(self):
        return self.wins
    
    def set_losses(self, losses):
        self.losses = losses

    def get_losses(self):
        return self.losses
    
    def set_ot_losses(self, ot_losses):
        self.ot_losses = ot_losses

    def get_ot_losses(self):
        return self.ot_losses
    
    def set_shots_against(self, shots_against):
        self.shots_against = shots_against

    def get_shots_against(self):
        return self.shots_against
    
    def set_goals_against(self, goals_against):
        self.goals_against = goals_against

    def get_goals_against(self):
        return self.goals_against
    
    def set_save_percent(self, save_percent):
        self.save_percent = save_percent

    def get_save_percent(self):
        return self.save_percent
    
    def set_shutouts(self, shutouts):
        self.shutouts = shutouts

    def get_shutouts(self):
        return self.shutouts
    
    def set_time_on_ice(self, time_on_ice):
        self.time_on_ice = time_on_ice

    def get_time_on_ice(self):
        return self.time_on_ice
    
    def set_penalty_minutes(self, penalty_minutes):
        self.penalty_minutes = penalty_minutes

    def get_penalty_minutes(self):
        return self.penalty_minutes
    
    def set_goals_against_average(self, goals_against_average):
        self.goals_against_average = goals_against_average

    def get_goals_against_average(self):
        return self.goals_against_average

    def get_team_id(self):
        return self.team_id

    def get_year(self):
        return self.year

    def get_game_type_id(self):
        return self.game_type_id

    def get_sequence(self):
        return self.sequence
