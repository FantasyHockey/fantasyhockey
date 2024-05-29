
class TeamAdvancedStatsPowerplayPenaltyKill:

    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.pk_net_percent = None
        self.pk_percent = None
        self.pk_net_goals = None
        self.pk_net_goals_for_per_game = None
        self.pk_time_on_ice_per_game = None
        self.pk_goals_against = None
        self.pk_goals_against_per_game = None
        self.pk_goals_for = None
        self.pk_goals_for_per_game = None
        self.times_shorthanded = None
        self.times_shorthanded_per_game = None
        self.overall_penalty_kill_percent = None
        self.penalty_kill_percent_3on4 = None
        self.penalty_kill_percent_3on5 = None
        self.penalty_kill_percent_4on5 = None
        self.time_on_ice_3on4 = None
        self.time_on_ice_3on5 = None
        self.time_on_ice_4on5 = None
        self.time_on_ice_shorthanded = None
        self.time_shorthanded_3v4 = None
        self.time_shorthanded_3v5 = None
        self.time_shorthanded_4v5 = None
        self.pp_goals_for = None
        self.pp_net_percent = None
        self.pp_percent = None
        self.pp_goals_per_game = None
        self.pp_net_goals = None
        self.pp_net_goals_for_per_game = None
        self.pp_opportunites = None
        self.pp_opportunities_per_game = None
        self.pp_time_on_ice_per_game = None
        self.pp_goals_against = None
        self.pp_goals_against_per_game = None
        self.opportunities_4on3 = None
        self.opportunities_5on3 = None
        self.opportunities_5on4 = None
        self.pp_percent_4on3 = None
        self.pp_percent_5on3 = None
        self.pp_percent_5on4 = None
        self.time_on_ice_4on3 = None
        self.time_on_ice_5on3 = None
        self.time_on_ice_5on4 = None
        self.pp_time_on_ice = None
        self.goals_against_3on4 = None
        self.goals_against_3on5 = None
        self.goals_against_4on5 = None
        self.goals_4on3 = None
        self.goals_5on3 = None
        self.goals_5on4 = None
        
    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_pk_net_percent(self):
        return self.pk_net_percent
    
    def set_pk_net_percent(self, pk_net_percent):
        self.pk_net_percent = pk_net_percent

    def get_pk_percent(self):
        return self.pk_percent
    
    def set_pk_percent(self, pk_percent):
        self.pk_percent = pk_percent

    def get_pk_net_goals(self):
        return self.pk_net_goals
    
    def set_pk_net_goals(self, pk_net_goals):
        self.pk_net_goals = pk_net_goals

    def get_pk_net_goals_for_per_game(self):
        return self.pk_net_goals_for_per_game
    
    def set_pk_net_goals_for_per_game(self, pk_net_goals_for_per_game):
        self.pk_net_goals_for_per_game = pk_net_goals_for_per_game

    def get_pk_time_on_ice_per_game(self):
        return self.pk_time_on_ice_per_game
    
    def set_pk_time_on_ice_per_game(self, pk_time_on_ice_per_game):
        self.pk_time_on_ice_per_game = pk_time_on_ice_per_game

    def get_pk_goals_against(self):
        return self.pk_goals_against
    
    def set_pk_goals_against(self, pk_goals_against):
        self.pk_goals_against = pk_goals_against

    def get_pk_goals_against_per_game(self):
        return self.pk_goals_against_per_game
    
    def set_pk_goals_against_per_game(self, pk_goals_against_per_game):
        self.pk_goals_against_per_game = pk_goals_against_per_game

    def get_pk_goals_for(self):
        return self.pk_goals_for
    
    def set_pk_goals_for(self, pk_goals_for):
        self.pk_goals_for = pk_goals_for

    def get_pk_goals_for_per_game(self):
        return self.pk_goals_for_per_game
    
    def set_pk_goals_for_per_game(self, pk_goals_for_per_game):
        self.pk_goals_for_per_game = pk_goals_for_per_game

    def get_times_shorthanded(self):
        return self.times_shorthanded
    
    def set_times_shorthanded(self, times_shorthanded):
        self.times_shorthanded = times_shorthanded

    def get_times_shorthanded_per_game(self):
        return self.times_shorthanded_per_game
    
    def set_times_shorthanded_per_game(self, times_shorthanded_per_game):
        self.times_shorthanded_per_game = times_shorthanded_per_game

    def get_overall_penalty_kill_percent(self):
        return self.overall_penalty_kill_percent
    
    def set_overall_penalty_kill_percent(self, overall_penalty_kill_percent):
        self.overall_penalty_kill_percent = overall_penalty_kill_percent

    def get_penalty_kill_percent_3on4(self):
        return self.penalty_kill_percent_3on4
    
    def set_penalty_kill_percent_3on4(self, penalty_kill_percent_3on4):
        self.penalty_kill_percent_3on4 = penalty_kill_percent_3on4

    def get_penalty_kill_percent_3on5(self):
        return self.penalty_kill_percent_3on5
    
    def set_penalty_kill_percent_3on5(self, penalty_kill_percent_3on5):
        self.penalty_kill_percent_3on5 = penalty_kill_percent_3on5

    def get_penalty_kill_percent_4on5(self):
        return self.penalty_kill_percent_4on5
    
    def set_penalty_kill_percent_4on5(self, penalty_kill_percent_4on5):
        self.penalty_kill_percent_4on5 = penalty_kill_percent_4on5

    def get_time_on_ice_3on4(self):
        return self.time_on_ice_3on4
    
    def set_time_on_ice_3on4(self, time_on_ice_3on4):
        self.time_on_ice_3on4 = time_on_ice_3on4

    def get_time_on_ice_3on5(self):
        return self.time_on_ice_3on5
    
    def set_time_on_ice_3on5(self, time_on_ice_3on5):
        self.time_on_ice_3on5 = time_on_ice_3on5

    def get_time_on_ice_4on5(self):
        return self.time_on_ice_4on5
    
    def set_time_on_ice_4on5(self, time_on_ice_4on5):
        self.time_on_ice_4on5 = time_on_ice_4on5

    def get_time_on_ice_shorthanded(self):
        return self.time_on_ice_shorthanded
    
    def set_time_on_ice_shorthanded(self, time_on_ice_shorthanded):
        self.time_on_ice_shorthanded = time_on_ice_shorthanded

    def get_time_shorthanded_3v4(self):
        return self.time_shorthanded_3v4
    
    def set_time_shorthanded_3v4(self, time_shorthanded_3v4):
        self.time_shorthanded_3v4 = time_shorthanded_3v4

    def get_time_shorthanded_3v5(self):
        return self.time_shorthanded_3v5
    
    def set_time_shorthanded_3v5(self, time_shorthanded_3v5):
        self.time_shorthanded_3v5 = time_shorthanded_3v5

    def get_time_shorthanded_4v5(self):
        return self.time_shorthanded_4v5
    
    def set_time_shorthanded_4v5(self, time_shorthanded_4v5):
        self.time_shorthanded_4v5 = time_shorthanded_4v5

    def get_pp_goals_for(self):
        return self.pp_goals_for
    
    def set_pp_goals_for(self, pp_goals_for):
        self.pp_goals_for = pp_goals_for

    def get_pp_net_percent(self):
        return self.pp_net_percent
    
    def set_pp_net_percent(self, pp_net_percent):
        self.pp_net_percent = pp_net_percent

    def get_pp_percent(self):
        return self.pp_percent
    
    def set_pp_percent(self, pp_percent):
        self.pp_percent = pp_percent

    def get_pp_goals_per_game(self):
        return self.pp_goals_per_game
    
    def set_pp_goals_per_game(self, pp_goals_per_game):
        self.pp_goals_per_game = pp_goals_per_game

    def get_pp_net_goals(self):
        return self.pp_net_goals
    
    def set_pp_net_goals(self, pp_net_goals):
        self.pp_net_goals = pp_net_goals

    def get_pp_net_goals_for_per_game(self):
        return self.pp_net_goals_for_per_game
    
    def set_pp_net_goals_for_per_game(self, pp_net_goals_for_per_game):
        self.pp_net_goals_for_per_game = pp_net_goals_for_per_game

    def get_pp_opportunites(self):
        return self.pp_opportunites
    
    def set_pp_opportunites(self, pp_opportunites):
        self.pp_opportunites = pp_opportunites

    def get_pp_opportunities_per_game(self):
        return self.pp_opportunities_per_game
    
    def set_pp_opportunities_per_game(self, pp_opportunities_per_game):
        self.pp_opportunities_per_game = pp_opportunities_per_game

    def get_pp_time_on_ice_per_game(self):
        return self.pp_time_on_ice_per_game
    
    def set_pp_time_on_ice_per_game(self, pp_time_on_ice_per_game):
        self.pp_time_on_ice_per_game = pp_time_on_ice_per_game

    def get_pp_goals_against(self):
        return self.pp_goals_against
    
    def set_pp_goals_against(self, pp_goals_against):
        self.pp_goals_against = pp_goals_against

    def get_pp_goals_against_per_game(self):
        return self.pp_goals_against_per_game
    
    def set_pp_goals_against_per_game(self, pp_goals_against_per_game):
        self.pp_goals_against_per_game = pp_goals_against_per_game

    def get_opportunities_4on3(self):
        return self.opportunities_4on3
    
    def set_opportunities_4on3(self, opportunities_4on3):
        self.opportunities_4on3 = opportunities_4on3

    def get_opportunities_5on3(self):
        return self.opportunities_5on3
    
    def set_opportunities_5on3(self, opportunities_5on3):
        self.opportunities_5on3 = opportunities_5on3

    def get_opportunities_5on4(self):
        return self.opportunities_5on4
    
    def set_opportunities_5on4(self, opportunities_5on4):
        self.opportunities_5on4 = opportunities_5on4

    def get_pp_percent_4on3(self):
        return self.pp_percent_4on3
    
    def set_pp_percent_4on3(self, pp_percent_4on3):
        self.pp_percent_4on3 = pp_percent_4on3

    def get_pp_percent_5on3(self):
        return self.pp_percent_5on3
    
    def set_pp_percent_5on3(self, pp_percent_5on3):
        self.pp_percent_5on3 = pp_percent_5on3

    def get_pp_percent_5on4(self):
        return self.pp_percent_5on4
    
    def set_pp_percent_5on4(self, pp_percent_5on4):
        self.pp_percent_5on4 = pp_percent_5on4

    def get_time_on_ice_4on3(self):
        return self.time_on_ice_4on3
    
    def set_time_on_ice_4on3(self, time_on_ice_4on3):
        self.time_on_ice_4on3 = time_on_ice_4on3

    def get_time_on_ice_5on3(self):
        return self.time_on_ice_5on3
    
    def set_time_on_ice_5on3(self, time_on_ice_5on3):
        self.time_on_ice_5on3 = time_on_ice_5on3

    def get_time_on_ice_5on4(self):
        return self.time_on_ice_5on4
    
    def set_time_on_ice_5on4(self, time_on_ice_5on4):
        self.time_on_ice_5on4 = time_on_ice_5on4

    def get_pp_time_on_ice(self):
        return self.pp_time_on_ice
    
    def set_pp_time_on_ice(self, pp_time_on_ice):
        self.pp_time_on_ice = pp_time_on_ice

    def get_goals_against_3on4(self):
        return self.goals_against_3on4
    
    def set_goals_against_3on4(self, goals_against_3on4):
        self.goals_against_3on4 = goals_against_3on4

    def get_goals_against_3on5(self):
        return self.goals_against_3on5
    
    def set_goals_against_3on5(self, goals_against_3on5):
        self.goals_against_3on5 = goals_against_3on5

    def get_goals_against_4on5(self):
        return self.goals_against_4on5
    
    def set_goals_against_4on5(self, goals_against_4on5):
        self.goals_against_4on5 = goals_against_4on5

    def get_goals_4on3(self):
        return self.goals_4on3
    
    def set_goals_4on3(self, goals_4on3):
        self.goals_4on3 = goals_4on3

    def get_goals_5on3(self):
        return self.goals_5on3
    
    def set_goals_5on3(self, goals_5on3):
        self.goals_5on3 = goals_5on3

    def get_goals_5on4(self):
        return self.goals_5on4
    
    def set_goals_5on4(self, goals_5on4):
        self.goals_5on4 = goals_5on4