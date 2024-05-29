from fantasyhockey.data_fetching.teams.models.team_data import TeamData
from fantasyhockey.data_fetching.teams.models.team_stats import TeamStats
from fantasyhockey.data_fetching.teams.models.team_advanced_stats_days_rest import TeamAdvancedStatsDaysRest


class Team:
    def __init__(self, team_id):
        self.team_id = team_id
        self.team_data: TeamData = None
        self.team_stats: TeamStats = None
        self.team_advanced_stats_days_rest: TeamAdvancedStatsDaysRest = None
        self.team_advanced_stats_corsi_fenwick = None
        self.team_advanced_stats_faceoff_percent = None
        self.team_advanced_stats_goals_by_period = None
        self.team_advanced_stats_goals_by_strength = None
        self.team_advanced_stats_leading_trailing = None
        self.team_advanced_stats_misc = None
        self.team_advanced_stats_outshoot_outshot = None
        self.team_advanced_stats_penalties = None
        self.team_advanced_stats_powerplay_penalty_kill = None
        self.team_advanced_stats_scoring_first = None
        self.team_advanced_stats_shot_type = None
        self.team_advanced_stats_team_goal_games = None

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

    def set_team_advanced_stats_days_rest(self, team_advanced_stats_days_rest: TeamAdvancedStatsDaysRest):
        self.team_advanced_stats_days_rest = team_advanced_stats_days_rest

    def get_team_advanced_stats_days_rest(self):
        return self.team_advanced_stats_days_rest
    
    def set_team_advanced_stats_corsi_fenwick(self, team_advanced_stats_corsi_fenwick):
        self.team_advanced_stats_corsi_fenwick = team_advanced_stats_corsi_fenwick

    def get_team_advanced_stats_corsi_fenwick(self):
        return self.team_advanced_stats_corsi_fenwick
    
    def set_team_advanced_stats_faceoff_percent(self, team_advanced_stats_faceoff_percent):
        self.team_advanced_stats_faceoff_percent = team_advanced_stats_faceoff_percent

    def get_team_advanced_stats_faceoff_percent(self):
        return self.team_advanced_stats_faceoff_percent
    
    def set_team_advanced_stats_goals_by_period(self, team_advanced_stats_goals_by_period):
        self.team_advanced_stats_goals_by_period = team_advanced_stats_goals_by_period

    def get_team_advanced_stats_goals_by_period(self):
        return self.team_advanced_stats_goals_by_period
    
    def set_team_advanced_stats_goals_by_strength(self, team_advanced_stats_goals_by_strength):
        self.team_advanced_stats_goals_by_strength = team_advanced_stats_goals_by_strength

    def get_team_advanced_stats_goals_by_strength(self):
        return self.team_advanced_stats_goals_by_strength
    
    def set_team_advanced_stats_leading_trailing(self, team_advanced_stats_goals_by_strength):
        self.team_advanced_stats_leading_trailing = team_advanced_stats_goals_by_strength

    def get_team_advanced_stats_leading_trailing(self):
        return self.team_advanced_stats_goals_by_strength

    def set_team_advanced_stats_misc(self, team_advanced_stats_misc):
        self.team_advanced_stats_misc = team_advanced_stats_misc

    def get_team_advanced_stats_misc(self):
        return self.team_advanced_stats_misc
    
    def set_team_advanced_stats_outshoot_outshot(self, team_advanced_stats_outshoot_outshot):
        self.team_advanced_stats_outshoot_outshot = team_advanced_stats_outshoot_outshot

    def get_team_advanced_stats_outshoot_outshot(self):
        return self.team_advanced_stats_outshoot_outshot
    
    def set_team_advanced_stats_penalties(self, team_advanced_stats_penalties):
        self.team_advanced_stats_penalties = team_advanced_stats_penalties

    def get_team_advanced_stats_penalties(self):
        return self.team_advanced_stats_penalties

    def set_team_advanced_stats_powerplay_penalty_kill(self, team_advanced_stats_powerplay_penalty_kill):
        self.team_advanced_stats_powerplay_penalty_kill = team_advanced_stats_powerplay_penalty_kill

    def get_team_advanced_stats_powerplay_penalty_kill(self):
        return self.team_advanced_stats_powerplay_penalty_kill
    
    def set_team_advanced_stats_scoring_first(self, team_advanced_stats_scoring_first):
        self.team_advanced_stats_scoring_first = team_advanced_stats_scoring_first

    def get_team_advanced_stats_scoring_first(self):
        return self.team_advanced_stats_scoring_first

    def set_team_advanced_stats_shot_type(self, team_advanced_stats_shot_type):
        self.team_advanced_stats_shot_type = team_advanced_stats_shot_type

    def get_team_advanced_stats_shot_type(self):
        return self.team_advanced_stats_shot_type

    def set_team_advanced_stats_team_goal_games(self, team_advanced_stats_team_goal_games):
        self.team_advanced_stats_team_goal_games = team_advanced_stats_team_goal_games

    def get_team_advanced_stats_team_goal_games(self):
        return self.team_advanced_stats_team_goal_games