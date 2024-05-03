

class Game:

    def __init(self, game_id):
        self.game_id = game_id
        self.year = None
        self.game_type_id = None
        self.venue_name = None
        self.start_time_utc = None
        self.eastern_utc_offset = None
        self.venue_utc_offset = None
        self.venue_time_zone = None
        self.game_state = None
        self.game_schedule_state = None
        self.away_team_id = None
        self.home_team_id = None
        self.shootout_in_use = None
        self.regulation_periods = None
        self.ot_in_use = None
        self.ties_in_use = None
        self.video_3_min_recap_id = None
        self.video_condensed_game = None


    def get_game_id(self):
        return self.game_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_game_type_id(self, game_type_id):
        self.game_type_id = game_type_id

    def get_game_type_id(self):
        return self.game_type_id
    
    def set_venue_name(self, venue_name):
        self.venue_name = venue_name

    def get_venue_name(self):
        return self.venue_name
    
    def set_start_time_utc(self, start_time_utc):
        self.start_time_utc = start_time_utc

    def get_start_time_utc(self):
        return self.start_time_utc
    
    def set_eastern_utc_offset(self, eastern_utc_offset):
        self.eastern_utc_offset = eastern_utc_offset

    def get_eastern_utc_offset(self):
        return self.eastern_utc_offset
    
    def set_venue_utc_offset(self, venue_utc_offset):
        self.venue_utc_offset = venue_utc_offset

    def get_venue_utc_offset(self):
        return self.venue_utc_offset
    
    def set_venue_time_zone(self, venue_time_zone):
        self.venue_time_zone = venue_time_zone

    def get_venue_time_zone(self):
        return self.venue_time_zone
    
    def set_game_state(self, game_state):
        self.game_state = game_state

    def get_game_state(self):
        return self.game_state
    
    def set_game_schedule_state(self, game_schedule_state):
        self.game_schedule_state = game_schedule_state

    def get_game_schedule_state(self):
        return self.game_schedule_state
    
    def set_away_team_id(self, away_team_id):
        self.away_team_id = away_team_id

    def get_away_team_id(self):
        return self.away_team_id
    
    def set_home_team_id(self, home_team_id):
        self.home_team_id = home_team_id

    def get_home_team_id(self):
        return self.home_team_id
    
    def set_shootout_in_use(self, shootout_in_use):
        self.shootout_in_use = shootout_in_use

    def get_shootout_in_use(self):
        return self.shootout_in_use
    
    def set_regulation_periods(self, regulation_periods):
        self.regulation_periods = regulation_periods

    def get_regulation_periods(self):
        return self.regulation_periods
    
    def set_ot_in_use(self, ot_in_use):
        self.ot_in_use = ot_in_use

    def get_ot_in_use(self):
        return self.ot_in_use
    
    def set_ties_in_use(self, ties_in_use):
        self.ties_in_use = ties_in_use

    def get_ties_in_use(self):
        return self.ties_in_use
    
    def set_video_3_min_recap_id(self, video_3_min_recap_id):
        self.video_3_min_recap_id = video_3_min_recap_id

    def get_video_3_min_recap_id(self):
        return self.video_3_min_recap_id
    
    def set_video_condensed_game(self, video_condensed_game):
        self.video_condensed_game = video_condensed_game

    def get_video_condensed_game(self):
        return self.video_condensed_game
    
