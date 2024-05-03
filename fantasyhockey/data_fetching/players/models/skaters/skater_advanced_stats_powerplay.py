

class SkaterAdvancedStatsPowerplay():

    def __init__(self, player_id):
        self.player_id = player_id
        self.team_id = None
        self.year = None
        self.pp_assists = None
        self.pp_goals = None
        self.pp_individual_corsi_for = None
        self.pp_primary_assists = None
        self.pp_secondary_assists = None
        self.pp_shooting_percentage = None
        self.pp_shots = None
        self.pp_time_on_ice = None
        self.pp_time_on_ice_per_game = None
        self.pp_time_on_ice_percentage = None

    def get_player_id(self):
        return self.player_id
    
    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return self.team_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_pp_assists(self, pp_assists):
        self.pp_assists = pp_assists

    def get_pp_assists(self):
        return self.pp_assists
    
    def set_pp_goals(self, pp_goals):
        self.pp_goals = pp_goals

    def get_pp_goals(self):
        return self.pp_goals
    
    def set_pp_individual_corsi_for(self, pp_individual_corsi_for):
        self.pp_individual_corsi_for = pp_individual_corsi_for

    def get_pp_individual_corsi_for(self):
        return self.pp_individual_corsi_for
    
    def set_pp_primary_assists(self, pp_primary_assists):
        self.pp_primary_assists = pp_primary_assists

    def get_pp_primary_assists(self):
        return self.pp_primary_assists
    
    def set_pp_secondary_assists(self, pp_secondary_assists):
        self.pp_secondary_assists = pp_secondary_assists

    def get_pp_secondary_assists(self):
        return self.pp_secondary_assists
    
    def set_pp_shooting_percentage(self, pp_shooting_percentage):
        self.pp_shooting_percentage = pp_shooting_percentage

    def get_pp_shooting_percentage(self):
        return self.pp_shooting_percentage
    
    def set_pp_shots(self, pp_shots):
        self.pp_shots = pp_shots

    def get_pp_shots(self):
        return self.pp_shots
    
    def set_pp_time_on_ice(self, pp_time_on_ice):
        self.pp_time_on_ice = pp_time_on_ice

    def get_pp_time_on_ice(self):
        return self.pp_time_on_ice
    
    def set_pp_time_on_ice_per_game(self, pp_time_on_ice_per_game):
        self.pp_time_on_ice_per_game = pp_time_on_ice_per_game

    def get_pp_time_on_ice_per_game(self):
        return self.pp_time_on_ice_per_game
    
    def set_pp_time_on_ice_percentage(self, pp_time_on_ice_percentage):
        self.pp_time_on_ice_percentage = pp_time_on_ice_percentage

    def get_pp_time_on_ice_percentage(self):
        return self.pp_time_on_ice_percentage
    
    