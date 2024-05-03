

class PlayerDraft:
    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.round = None
        self.pick_in_round = None
        self.overall_pick = None

    def get_player_id(self):
        return self.player_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_round(self, round):
        self.round = round

    def get_round(self):
        return self.round
    
    def set_pick_in_round(self, pick_in_round):
        self.pick_in_round = pick_in_round

    def get_pick_in_round(self):
        return self.pick_in_round
    
    def set_overall_pick(self, overall_pick):
        self.overall_pick = overall_pick

    def get_overall_pick(self):
        return self.overall_pick
    
    