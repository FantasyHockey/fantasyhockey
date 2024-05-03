

class GameRoster:

    def __init__(self, game_id, team_id, player_id):
        self.game_id = game_id
        self.team_id = team_id
        self.player_id = player_id
        self.scratched = None
        self.starting = None

    def get_game_id(self):
        return self.game_id
    
    def get_team_id(self):
        return self.team_id
    
    def get_player_id(self):
        return self.player_id
    
    def set_scratched(self, scratched):
        self.scratched = scratched

    def get_scratched(self):
        return self.scratched
    
    def set_starting(self, starting):
        self.starting = starting

    def get_starting(self):
        return self.starting
    
    