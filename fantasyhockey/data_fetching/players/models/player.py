from fantasyhockey.data_fetching.players.models.player_draft import PlayerDraft
from fantasyhockey.data_fetching.players.models.player_awards import PlayerAwards
from fantasyhockey.data_fetching.players.models.player_details import PlayerDetails

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.team_id = None
        self.is_active = None
        self.player_draft = None
        self.player_awards = []
        self.player_details = None

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
    
    def set_player_draft(self, player_draft: PlayerDraft):
        self.player_draft = player_draft

    def get_player_draft(self):
        return self.player_draft
    
    def add_player_award(self, player_award: PlayerAwards):
        self.player_awards.append(player_award)

    def get_player_awards(self):
        return self.player_awards
    
    def set_player_details(self, player_details: PlayerDetails):
        self.player_details = player_details

    def get_player_details(self):
        return self.player_details
    
