

class PlayOnIce:

    def __init__(self, game_id, play_id, player_id):
        self.game_id = game_id
        self.play_id = play_id
        self.player_id = player_id
        self.team_id = None
        self.home = None
        self.away = None

    def get_game_id(self):
        return self.game_id
    
    def get_play_id(self):
        return self.play_id
    
    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_home(self, home):
        self.home = home

    def get_home(self):
        return self.home
    
    def set_away(self, away):
        self.away = away

    def get_away(self):
        return self.away