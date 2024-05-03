
class PlayRoles:
    def __init__(self, game_id, play_id, player_id, role_code):
        self.game_id = game_id
        self.play_id = play_id
        self.player_id = player_id
        self.role_code = role_code

    def get_game_id(self):
        return self.game_id

    def get_play_id(self):
        return self.play_id

    def get_player_id(self):
        return self.player_id

    def get_role_code(self):
        return self.role_code
    
