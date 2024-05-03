

class SkaterAdvancedStatsPenaltyKill:

    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.pk_assists = None
        self.pk_goals = None
        self.pk_individual_corsi_against = None
        self.pk_primary_assists = None
        self.pk_secondary_assists = None
        self.pk_shooting_percentage = None
        self.pk_shots = None
        self.pk_time_on_ice = None
        self.pk_time_on_ice_per_game = None
        self.pk_time_on_ice_percentage = None

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
    
    def set_pk_assists(self, pk_assists):
        self.pk_assists = pk_assists

    def get_pk_assists(self):
        return self.pk_assists
    
    def set_pk_goals(self, pk_goals):
        self.pk_goals = pk_goals

    def get_pk_goals(self):
        return self.pk_goals
    
    def set_pk_individual_corsi_against(self, pk_individual_corsi_against):
        self.pk_individual_corsi_against = pk_individual_corsi_against

    def get_pk_individual_corsi_against(self):
        return self.pk_individual_corsi_against
    
    def set_pk_primary_assists(self, pk_primary_assists):
        self.pk_primary_assists = pk_primary_assists

    def get_pk_primary_assists(self):
        return self.pk_primary_assists
    
    def set_pk_secondary_assists(self, pk_secondary_assists):
        self.pk_secondary_assists = pk_secondary_assists

    def get_pk_secondary_assists(self):
        return self.pk_secondary_assists
    
    def set_pk_shooting_percentage(self, pk_shooting_percentage):
        self.pk_shooting_percentage = pk_shooting_percentage

    def get_pk_shooting_percentage(self):
        return self.pk_shooting_percentage
    
    def set_pk_shots(self, pk_shots):
        self.pk_shots = pk_shots

    def get_pk_shots(self):
        return self.pk_shots
    
    def set_pk_time_on_ice(self, pk_time_on_ice):
        self.pk_time_on_ice = pk_time_on_ice

    def get_pk_time_on_ice(self):
        return self.pk_time_on_ice
    
    def set_pk_time_on_ice_per_game(self, pk_time_on_ice_per_game):
        self.pk_time_on_ice_per_game = pk_time_on_ice_per_game

    def get_pk_time_on_ice_per_game(self):
        return self.pk_time_on_ice_per_game
    
    def set_pk_time_on_ice_percentage(self, pk_time_on_ice_percentage):
        self.pk_time_on_ice_percentage = pk_time_on_ice_percentage

    def get_pk_time_on_ice_percentage(self):
        return self.pk_time_on_ice_percentage
