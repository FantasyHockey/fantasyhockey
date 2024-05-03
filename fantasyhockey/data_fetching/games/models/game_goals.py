

class GameGoals:

    def __init__(self, game_id, away_score, home_score):
        self.game_id = game_id
        self.away_score = away_score
        self.home_score = home_score
        self.situation_code = None
        self.strength = None
        self.player_id = None
        self.highlight_clip_id = None
        self.goals_to_date = None
        self.leading_team_id = None
        self.time_in_period = None
        self.shot_type = None
        self.goal_modifier = None
        self.assist_1_player_id = None
        self.assist_2_player_id = None

    def get_game_id(self):
        return self.game_id
    
    def get_away_score(self):
        return self.away_score
    
    def get_home_score(self):
        return self.home_score
    
    def set_situation_code(self, situation_code):
        self.situation_code = situation_code

    def get_situation_code(self):
        return self.situation_code
    
    def set_strength(self, strength):
        self.strength = strength

    def get_strength(self):
        return self.strength
    
    def set_player_id(self, player_id):
        self.player_id = player_id

    def get_player_id(self):
        return self.player_id
    
    def set_highlight_clip_id(self, highlight_clip_id):
        self.highlight_clip_id = highlight_clip_id

    def get_highlight_clip_id(self):
        return self.highlight_clip_id
    
    def set_goals_to_date(self, goals_to_date):
        self.goals_to_date = goals_to_date

    def get_goals_to_date(self):
        return self.goals_to_date
    
    def set_leading_team_id(self, leading_team_id):
        self.leading_team_id = leading_team_id

    def get_leading_team_id(self):
        return self.leading_team_id
    
    def set_time_in_period(self, time_in_period):
        self.time_in_period = time_in_period

    def get_time_in_period(self):
        return self.time_in_period
    
    def set_shot_type(self, shot_type):
        self.shot_type = shot_type

    def get_shot_type(self):
        return self.shot_type
    
    def set_goal_modifier(self, goal_modifier):
        self.goal_modifier = goal_modifier

    def get_goal_modifier(self):
        return self.goal_modifier
    
    def set_assist_1_player_id(self, assist_1_player_id):
        self.assist_1_player_id = assist_1_player_id

    def get_assist_1_player_id(self):
        return self.assist_1_player_id
    
    def set_assist_2_player_id(self, assist_2_player_id):
        self.assist_2_player_id = assist_2_player_id

    def get_assist_2_player_id(self):
        return self.assist_2_player_id
    
    