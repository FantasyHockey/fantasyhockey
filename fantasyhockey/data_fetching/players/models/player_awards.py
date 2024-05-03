

class PlayerAwards:

    def __init__(self, player_id):
        self.player_id = player_id
        self.award = None
        self.year = None

    def get_player_id(self):
        return self.player_id
    
    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
        