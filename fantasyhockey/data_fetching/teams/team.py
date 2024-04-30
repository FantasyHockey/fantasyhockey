

class Team:
    def __init__(self, team_id):
        self.team_id = team_id
        self.team_data = None
        self.team_stats = None

    def get_team_id(self):
        return self.team_id

    def set_team_data(self, team_data):
        self.team_data = team_data

    def get_team_data(self):
        return self.team_data
    
    def set_team_stats(self, team_stats):
        self.team_stats = team_stats

    def get_team_stats(self):
        return self.team_stats
