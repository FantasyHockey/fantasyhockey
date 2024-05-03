

class Referees:

    def __init__(self, game_id):
        self.game_id = game_id
        self.referee_1_name = None
        self.referee_2_name = None
        self.linesman_1_name = None
        self.linesman_2_name = None

    def get_game_id(self):
        return self.game_id
    
    def set_referee_1_name(self, referee_1_name):
        self.referee_1_name = referee_1_name

    def get_referee_1_name(self):
        return self.referee_1_name
    
    def set_referee_2_name(self, referee_2_name):
        self.referee_2_name = referee_2_name

    def get_referee_2_name(self):
        return self.referee_2_name
    
    def set_linesman_1_name(self, linesman_1_name):
        self.linesman_1_name = linesman_1_name

    def get_linesman_1_name(self):
        return self.linesman_1_name
    
    def set_linesman_2_name(self, linesman_2_name):
        self.linesman_2_name = linesman_2_name

    def get_linesman_2_name(self):
        return self.linesman_2_name
    
    