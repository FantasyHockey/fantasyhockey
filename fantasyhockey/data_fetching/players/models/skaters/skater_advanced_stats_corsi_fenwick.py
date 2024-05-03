

class SkaterAdvancedStatsCorsiFenwick:

    def __init__(self, player_id):
        self.player_id = player_id
        self.year = None
        self.team_id = None
        self.games_played = None
        self.corsi_against = None
        self.corsi_ahead = None
        self.corsi_behind = None
        self.corsi_close = None
        self.corsi_for = None
        self.corsi_tied = None
        self.corsi_total = None
        self.fenwick_against = None
        self.fenwick_ahead = None
        self.fenwick_behind = None
        self.fenwick_close = None
        self.fenwick_for = None
        self.fenwick_tied = None
        self.fenwick_relative = None
        self.fenwick_total = None
        self.corsi_percentage = None
        self.corsi_ahead_percentage = None
        self.corsi_behind_percentage = None
        self.corsi_close_percentage = None
        self.corsi_tied_percentage = None
        self.corsi_relative = None
        self.shooting_percent_5on5 = None
        self.skater_save_percent_5on5 = None
        self.skater_shooting_plus_save_percent_5on5 = None
        self.time_on_ice_5on5_per_game = None
        self.fenwick_percentage = None
        self.fenwick_ahead_percentage = None
        self.fenwick_behind_percentage = None
        self.fenwick_close_percentage = None
        self.fenwick_tied_percentage = None
        self.zone_start_5on5_percentage = None

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
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_games_played(self):
        return self.games_played
    
    def set_corsi_against(self, corsi_against):
        self.corsi_against = corsi_against

    def get_corsi_against(self):
        return self.corsi_against
    
    def set_corsi_ahead(self, corsi_ahead):
        self.corsi_ahead = corsi_ahead

    def get_corsi_ahead(self):
        return self.corsi_ahead
    
    def set_corsi_behind(self, corsi_behind):
        self.corsi_behind = corsi_behind

    def get_corsi_behind(self):
        return self.corsi_behind
    
    def set_corsi_close(self, corsi_close):
        self.corsi_close = corsi_close

    def get_corsi_close(self):
        return self.corsi_close
    
    def set_corsi_for(self, corsi_for):
        self.corsi_for = corsi_for

    def get_corsi_for(self):
        return self.corsi_for
    
    def set_corsi_tied(self, corsi_tied):
        self.corsi_tied = corsi_tied

    def get_corsi_tied(self):
        return self.corsi_tied
    
    def set_corsi_total(self, corsi_total):
        self.corsi_total = corsi_total

    def get_corsi_total(self):
        return self.corsi_total
    
    def set_fenwick_against(self, fenwick_against):
        self.fenwick_against = fenwick_against

    def get_fenwick_against(self):
        return self.fenwick_against
    
    def set_fenwick_ahead(self, fenwick_ahead):
        self.fenwick_ahead = fenwick_ahead

    def get_fenwick_ahead(self):
        return self.fenwick_ahead
    
    def set_fenwick_behind(self, fenwick_behind):
        self.fenwick_behind = fenwick_behind

    def get_fenwick_behind(self):
        return self.fenwick_behind
    
    def set_fenwick_close(self, fenwick_close):
        self.fenwick_close = fenwick_close

    def get_fenwick_close(self):
        return self.fenwick_close
    
    def set_fenwick_for(self, fenwick_for):
        self.fenwick_for = fenwick_for

    def get_fenwick_for(self):
        return self.fenwick_for
    
    def set_fenwick_tied(self, fenwick_tied):
        self.fenwick_tied = fenwick_tied

    def get_fenwick_tied(self):
        return self.fenwick_tied
    
    def set_fenwick_relative(self, fenwick_relative):
        self.fenwick_relative = fenwick_relative

    def get_fenwick_relative(self):
        return self.fenwick_relative
    
    def set_fenwick_total(self, fenwick_total):
        self.fenwick_total = fenwick_total

    def get_fenwick_total(self):
        return self.fenwick_total
    
    def set_corsi_percentage(self, corsi_percentage):
        self.corsi_percentage = corsi_percentage

    def get_corsi_percentage(self):
        return self.corsi_percentage
    
    def set_corsi_ahead_percentage(self, corsi_ahead_percentage):
        self.corsi_ahead_percentage = corsi_ahead_percentage

    def get_corsi_ahead_percentage(self):
        return self.corsi_ahead_percentage
    
    def set_corsi_behind_percentage(self, corsi_behind_percentage):
        self.corsi_behind_percentage = corsi_behind_percentage

    def get_corsi_behind_percentage(self):
        return self.corsi_behind_percentage
    
    def set_corsi_close_percentage(self, corsi_close_percentage):
        self.corsi_close_percentage = corsi_close_percentage

    def get_corsi_close_percentage(self):
        return self.corsi_close_percentage
    
    def set_corsi_tied_percentage(self, corsi_tied_percentage):
        self.corsi_tied_percentage = corsi_tied_percentage

    def get_corsi_tied_percentage(self):
        return self.corsi_tied_percentage
    
    def set_corsi_relative(self, corsi_relative):
        self.corsi_relative = corsi_relative

    def get_corsi_relative(self):
        return self.corsi_relative
    
    def set_shooting_percent_5on5(self, shooting_percent_5on5):
        self.shooting_percent_5on5 = shooting_percent_5on5

    def get_shooting_percent_5on5(self):
        return self.shooting_percent_5on5
    
    def set_skater_save_percent_5on5(self, skater_save_percent_5on5):
        self.skater_save_percent_5on5 = skater_save_percent_5on5

    def get_skater_save_percent_5on5(self):
        return self.skater_save_percent_5on5
    
    def set_skater_shooting_plus_save_percent_5on5(self, skater_shooting_plus_save_percent_5on5):
        self.skater_shooting_plus_save_percent_5on5 = skater_shooting_plus_save_percent_5on5

    def get_skater_shooting_plus_save_percent_5on5(self):
        return self.skater_shooting_plus_save_percent_5on5
    
    def set_time_on_ice_5on5_per_game(self, time_on_ice_5on5_per_game):
        self.time_on_ice_5on5_per_game = time_on_ice_5on5_per_game

    def get_time_on_ice_5on5_per_game(self):
        return self.time_on_ice_5on5_per_game
    
    def set_fenwick_percentage(self, fenwick_percentage):
        self.fenwick_percentage = fenwick_percentage

    def get_fenwick_percentage(self):
        return self.fenwick_percentage
    
    def set_fenwick_ahead_percentage(self, fenwick_ahead_percentage):
        self.fenwick_ahead_percentage = fenwick_ahead_percentage

    def get_fenwick_ahead_percentage(self):
        return self.fenwick_ahead_percentage
    
    def set_fenwick_behind_percentage(self, fenwick_behind_percentage):
        self.fenwick_behind_percentage = fenwick_behind_percentage

    def get_fenwick_behind_percentage(self):
        return self.fenwick_behind_percentage
    
    def set_fenwick_close_percentage(self, fenwick_close_percentage):
        self.fenwick_close_percentage = fenwick_close_percentage

    def get_fenwick_close_percentage(self):
        return self.fenwick_close_percentage
    
    def set_fenwick_tied_percentage(self, fenwick_tied_percentage):
        self.fenwick_tied_percentage = fenwick_tied_percentage

    def get_fenwick_tied_percentage(self):
        return self.fenwick_tied_percentage
    
    def set_zone_start_5on5_percentage(self, zone_start_5on5_percentage):
        self.zone_start_5on5_percentage = zone_start_5on5_percentage

    def get_zone_start_5on5_percentage(self):
        return self.zone_start_5on5_percentage
