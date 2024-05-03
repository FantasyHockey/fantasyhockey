

class YouthSkaterStats:
    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_name = None
        self.league_name = None
        self.game_type_id = None
        self.sequence = None
        self.games_played = None
        self.goals = None
        self.assists = None
        self.points = None
        self.pim = None

    def get_player_id(self):
        return self.player_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_team_name(self, team_name):
        self.team_name = team_name

    def get_team_name(self):
        return self.team_name
    
    def set_league_name(self, league_name):
        self.league_name = league_name

    def get_league_name(self):
        return self.league_name
    
    def set_game_type_id(self, game_type_id):
        self.game_type_id = game_type_id

    def get_game_type_id(self):
        return self.game_type_id
    
    def set_sequence(self, sequence):
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence
    
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
    
    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points
    
    def set_pim(self, pim):
        self.pim = pim

    def get_pim(self):
        return self.pim

