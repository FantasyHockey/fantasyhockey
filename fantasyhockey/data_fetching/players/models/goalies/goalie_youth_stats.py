
class GoalieYouthStats:

    def __init__(self, player_id, year, team_name, league_name, game_type_id, sequence):
        self.player_id = player_id
        self.year = year
        self.team_name = team_name
        self.league_name = league_name
        self.game_type_id = game_type_id
        self.sequence = sequence
        self.games_played = None
        self.save_percentage = None
        self.goals_against_average = None
        self.goals_against = None
        self.wins = None
        self.losses = None
        self.time_on_ice = None
        self.ties = None

    def get_player_id(self):
        return self.player_id
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_save_percentage(self, save_percentage):
        self.save_percentage = save_percentage

    def get_save_percentage(self):
        return self.save_percentage
    
    def set_goals_against_average(self, goals_against_average):
        self.goals_against_average = goals_against_average

    def get_goals_against_average(self):
        return self.goals_against_average
    
    def set_goals_against(self, goals_against):
        self.goals_against = goals_against

    def get_goals_against(self):
        return self.goals_against
    
    def set_wins(self, wins):
        self.wins = wins

    def get_wins(self):
        return self.wins
    
    def set_losses(self, losses):
        self.losses = losses

    def get_losses(self):
        return self.losses
    
    def set_time_on_ice(self, time_on_ice):
        self.time_on_ice = time_on_ice

    def get_time_on_ice(self):
        return self.time_on_ice
    
    def set_ties(self, ties):
        self.ties = ties

    def get_ties(self):
        return self.ties

    def get_team_name(self):
        return self.team_name

    def get_league_name(self):
        return self.league_name

    def get_game_type_id(self):
        return self.game_type_id

    def get_sequence(self):
        return self.sequence

    def get_year(self):
        return self.year