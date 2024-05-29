

class TeamAdvancedStatsCorsiFenwick:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
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
        self.fenwick_relative = None
        self.fenwick_tied = None
        self.fenwick_total = None
        self.corsi_percent = None
        self.corsi_ahead_percent = None
        self.corsi_behind_percent = None
        self.corsi_close_percent = None
        self.corsi_tied_percent = None
        self.corsi_relative = None
        self.shooting_percent_5on5 = None
        self.save_percent_5on5 = None
        self.shooting_plus_save_percent_5on5 = None
        self.fenwick_tied_percent = None
        self.fenwick_ahead_percent = None
        self.fenwick_behind_percent = None
        self.fenwick_close_percent = None
        self.fenwick_tied_percent = None
        self.zone_start_5on5_percent = None
        self.fenwick_percent = None
    
    def get_team_id(self):
        return self.team_id
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_games_played(self):
        return self.games_played
    
    def set_games_played(self, games_played):
        self.games_played = games_played

    def get_corsi_against(self):
        return self.corsi_against
    
    def set_corsi_against(self, corsi_against):
        self.corsi_against = corsi_against

    def get_corsi_ahead(self):
        return self.corsi_ahead
    
    def set_corsi_ahead(self, corsi_ahead):
        self.corsi_ahead = corsi_ahead

    def get_corsi_behind(self):
        return self.corsi_behind
    
    def set_corsi_behind(self, corsi_behind):
        self.corsi_behind = corsi_behind

    def get_corsi_close(self):
        return self.corsi_close
    
    def set_corsi_close(self, corsi_close):
        self.corsi_close = corsi_close

    def get_corsi_for(self):
        return self.corsi_for
    
    def set_corsi_for(self, corsi_for):
        self.corsi_for = corsi_for

    def get_corsi_tied(self):
        return self.corsi_tied
    
    def set_corsi_tied(self, corsi_tied):
        self.corsi_tied = corsi_tied

    def get_corsi_total(self):
        return self.corsi_total
    
    def set_corsi_total(self, corsi_total):
        self.corsi_total = corsi_total

    def get_fenwick_against(self):
        return self.fenwick_against
    
    def set_fenwick_against(self, fenwick_against):
        self.fenwick_against = fenwick_against

    def get_fenwick_ahead(self):
        return self.fenwick_ahead
    
    def set_fenwick_ahead(self, fenwick_ahead):
        self.fenwick_ahead = fenwick_ahead

    def get_fenwick_behind(self):
        return self.fenwick_behind
    
    def set_fenwick_behind(self, fenwick_behind):
        self.fenwick_behind = fenwick_behind

    def get_fenwick_close(self):
        return self.fenwick_close
    
    def set_fenwick_close(self, fenwick_close):
        self.fenwick_close = fenwick_close

    def get_fenwick_for(self):
        return self.fenwick_for
    
    def set_fenwick_for(self, fenwick_for):
        self.fenwick_for = fenwick_for

    def get_fenwick_relative(self):
        return self.fenwick_relative
    
    def set_fenwick_relative(self, fenwick_relative):
        self.fenwick_relative = fenwick_relative

    def get_fenwick_tied(self):
        return self.fenwick_tied
    
    def set_fenwick_tied(self, fenwick_tied):
        self.fenwick_tied = fenwick_tied

    def get_fenwick_total(self):
        return self.fenwick_total
    
    def set_fenwick_total(self, fenwick_total):
        self.fenwick_total = fenwick_total

    def get_corsi_percent(self):
        return self.corsi_percent
    
    def set_corsi_percent(self, corsi_percent):
        self.corsi_percent = corsi_percent

    def get_corsi_ahead_percent(self):
        return self.corsi_ahead_percent
    
    def set_corsi_ahead_percent(self, corsi_ahead_percent):
        self.corsi_ahead_percent = corsi_ahead_percent

    def get_corsi_behind_percent(self):
        return self.corsi_behind_percent
    
    def set_corsi_behind_percent(self, corsi_behind_percent):
        self.corsi_behind_percent = corsi_behind_percent

    def get_corsi_close_percent(self):
        return self.corsi_close_percent
    
    def set_corsi_close_percent(self, corsi_close_percent):
        self.corsi_close_percent = corsi_close_percent

    def get_corsi_tied_percent(self):
        return self.corsi_tied_percent
    
    def set_corsi_tied_percent(self, corsi_tied_percent):
        self.corsi_tied_percent = corsi_tied_percent

    def get_corsi_relative(self):
        return self.corsi_relative
    
    def set_corsi_relative(self, corsi_relative):
        self.corsi_relative = corsi_relative

    def get_shooting_percent_5on5(self):
        return self.shooting_percent_5on5
    
    def set_shooting_percent_5on5(self, shooting_percent_5on5):
        self.shooting_percent_5on5 = shooting_percent_5on5

    def get_save_percent_5on5(self):
        return self.save_percent_5on5
    
    def set_save_percent_5on5(self, save_percent_5on5):
        self.save_percent_5on5 = save_percent_5on5

    def get_shooting_plus_save_percent_5on5(self):
        return self.shooting_plus_save_percent_5on5
    
    def set_shooting_plus_save_percent_5on5(self, shooting_plus_save_percent_5on5):
        self.shooting_plus_save_percent_5on5 = shooting_plus_save_percent_5on5

    def get_fenwick_tied_percent(self):
        return self.fenwick_tied_percent
    
    def set_fenwick_tied_percent(self, fenwick_tied_percent):
        self.fenwick_tied_percent = fenwick_tied_percent

    def get_fenwick_ahead_percent(self):
        return self.fenwick_ahead_percent
    
    def set_fenwick_ahead_percent(self, fenwick_ahead_percent):
        self.fenwick_ahead_percent = fenwick_ahead_percent

    def get_fenwick_behind_percent(self):
        return self.fenwick_behind_percent
    
    def set_fenwick_behind_percent(self, fenwick_behind_percent):
        self.fenwick_behind_percent = fenwick_behind_percent

    def get_fenwick_close_percent(self):
        return self.fenwick_clost_percent
    
    def set_fenwick_close_percent(self, fenwick_clost_percent):
        self.fenwick_clost_percent = fenwick_clost_percent

    def get_fenwick_tied_percent(self):
        return self.fenwick_tied_percent
    
    def set_fenwick_tied_percent(self, fenwick_tied_percent):
        self.fenwick_tied_percent = fenwick_tied_percent

    def get_zone_start_5on5_percent(self):
        return self.zone_start_5on5_percent
    
    def set_zone_start_5on5_percent(self, zone_start_5on5_percent):
        self.zone_start_5on5_percent = zone_start_5on5_percent

    def get_fenwick_percent(self):
        return self.fenwick_percent
    
    def set_fenwick_percent(self, fenwick_percent):
        self.fenwick_percent = fenwick_percent