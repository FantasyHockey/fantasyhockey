

class GoalieAdvancedStats:

    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.complete_game_percentage = None
        self.complete_games = None
        self.games_played = None
        self.games_started = None
        self.goals_against = None
        self.goals_against_average = None
        self.goals_for = None
        self.goals_for_average = None
        self.incomplete_games = None
        self.quality_starts = None
        self.quality_starts_percentage = None
        self.regulation_losses = None
        self.regulation_wins = None

    def get_player_id(self):
        return self.player_id
    
    def set_year(self, year):
        self.year = year

    def set_team_id(self, team_id):
        self.team_id = team_id
    
    def set_complete_game_percentage(self, complete_game_percentage):
        self.complete_game_percentage = complete_game_percentage

    def get_complete_game_percentage(self):
        return self.complete_game_percentage
    
    def set_complete_games(self, complete_games):
        self.complete_games = complete_games

    def get_complete_games(self):
        return self.complete_games
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_games_started(self, games_started):
        self.games_started = games_started

    def get_games_started(self):
        return self.games_started
    
    def set_goals_against(self, goals_against):
        self.goals_against = goals_against

    def get_goals_against(self):
        return self.goals_against
    
    def set_goals_against_average(self, goals_against_average):
        self.goals_against_average = goals_against_average

    def get_goals_against_average(self):
        return self.goals_against_average
    
    def set_goals_for(self, goals_for):
        self.goals_for = goals_for

    def get_goals_for(self):
        return self.goals_for
    
    def set_goals_for_average(self, goals_for_average):
        self.goals_for_average = goals_for_average

    def get_goals_for_average(self):
        return self.goals_for_average
    
    def set_incomplete_games(self, incomplete_games):
        self.incomplete_games = incomplete_games

    def get_incomplete_games(self):
        return self.incomplete_games
    
    def set_quality_starts(self, quality_starts):
        self.quality_starts = quality_starts

    def get_quality_starts(self):
        return self.quality_starts
    
    def set_quality_starts_percentage(self, quality_starts_percentage):
        self.quality_starts_percentage = quality_starts_percentage

    def get_quality_starts_percentage(self):
        return self.quality_starts_percentage
    
    def set_regulation_losses(self, regulation_losses):
        self.regulation_losses = regulation_losses

    def get_regulation_losses(self):
        return self.regulation_losses
    
    def set_regulation_wins(self, regulation_wins):
        self.regulation_wins = regulation_wins

    def get_regulation_wins(self):
        return self.regulation_wins
    
    def get_year(self):
        return self.year
    
    def get_team_id(self):
        return self.team_id