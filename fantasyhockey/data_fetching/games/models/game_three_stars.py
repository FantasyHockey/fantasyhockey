

class GameThreeStars:
    def __init__(self, game_id):
        self.game_id = game_id
        self.first_star = None
        self.second_star = None
        self.third_star = None

    def get_game_id(self):
        return self.game_id
    
    def set_first_star(self, first_star):
        self.first_star = first_star

    def get_first_star(self):
        return self.first_star
    
    def set_second_star(self, second_star):
        self.second_star = second_star

    def get_second_star(self):
        return self.second_star
    
    def set_third_star(self, third_star):
        self.third_star = third_star

    def get_third_star(self):
        return self.third_star
    
    