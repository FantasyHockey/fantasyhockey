

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.team_id = None
        self.is_active = None

    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_is_active(self, is_active):
        self.is_active = is_active

    def get_is_active(self):
        return self.is_active
    



