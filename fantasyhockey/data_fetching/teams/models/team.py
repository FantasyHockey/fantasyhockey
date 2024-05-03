from fantasyhockey.data_fetching.teams.models.team_data import TeamData
from fantasyhockey.data_fetching.teams.models.team_stats import TeamStats

class Team:
    def __init__(self, team_id):
        self.team_id = team_id
        self.team_data: TeamData = None
        self.team_stats: TeamStats = None

    def get_team_id(self):
        return self.team_id

    def set_team_data(self, team_data: TeamData):
        self.team_data = team_data

    def get_team_data(self):
        return self.team_data
    
    def set_team_stats(self, team_stats: TeamStats):
        self.team_stats = team_stats

    def get_team_stats(self):
        return self.team_stats