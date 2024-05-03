

class GoalieAdvancedStatsPenaltyShots:

    def __init__(self, player_id, year, team_id):
        self.player_id = player_id
        self.year = year
        self.team_id = team_id
        self.penalty_shot_save_percent = None
        self.penalty_shot_against = None
        self.penalty_shot_goals_against = None
        self.penalty_shot_saves = None

    def get_player_id(self):
        return self.player_id
    
    def set_penalty_shot_save_percent(self, penalty_shot_save_percent):
        self.penalty_shot_save_percent = penalty_shot_save_percent

    def get_penalty_shot_save_percent(self):
        return self.penalty_shot_save_percent
    
    def set_penalty_shot_against(self, penalty_shot_against):
        self.penalty_shot_against = penalty_shot_against

    def get_penalty_shot_against(self):
        return self.penalty_shot_against
    
    def set_penalty_shot_goals_against(self, penalty_shot_goals_against):
        self.penalty_shot_goals_against = penalty_shot_goals_against

    def get_penalty_shot_goals_against(self):
        return self.penalty_shot_goals_against
    
    def set_penalty_shot_saves(self, penalty_shot_saves):
        self.penalty_shot_saves = penalty_shot_saves

    def get_penalty_shot_saves(self):
        return self.penalty_shot_saves
    
    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
