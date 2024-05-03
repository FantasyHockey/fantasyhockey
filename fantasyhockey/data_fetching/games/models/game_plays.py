

class GamePlays:

    def __init__(self, game_id, play_id):
        self.game_id = game_id
        self.play_id = play_id
        self.event_id = None
        self.period_number = None
        self.period_type = None
        self.time_in_period = None
        self.time_remaining = None
        self.situation_code = None
        self.home_team_defending_side = None
        self.type_code = None
        self.type_description_key = None
        self.sort_order = None
        self.x_coord = None
        self.y_coord = None
        self.zone_code = None
        self.shot_type = None

    def get_game_id(self):
        return self.game_id
    
    def get_play_id(self):
        return self.play_id
    
    def set_event_id(self, event_id):
        self.event_id = event_id

    def get_event_id(self):
        return self.event_id
    
    def set_period_number(self, period_number):
        self.period_number = period_number

    def get_period_number(self):
        return self.period_number
    
    def set_period_type(self, period_type):
        self.period_type = period_type

    def get_period_type(self):
        return self.period_type
    
    def set_time_in_period(self, time_in_period):
        self.time_in_period = time_in_period

    def get_time_in_period(self):
        return self.time_in_period
    
    def set_time_remaining(self, time_remaining):
        self.time_remaining = time_remaining

    def get_time_remaining(self):
        return self.time_remaining
    
    def set_situation_code(self, situation_code):
        self.situation_code = situation_code

    def get_situation_code(self):
        return self.situation_code
    
    def set_home_team_defending_side(self, home_team_defending_side):
        self.home_team_defending_side = home_team_defending_side

    def get_home_team_defending_side(self):
        return self.home_team_defending_side
    
    def set_type_code(self, type_code):
        self.type_code = type_code

    def get_type_code(self):
        return self.type_code
    
    def set_type_description_key(self, type_description_key):
        self.type_description_key = type_description_key

    def get_type_description_key(self):
        return self.type_description_key
    
    def set_sort_order(self, sort_order):
        self.sort_order = sort_order

    def get_sort_order(self):
        return self.sort_order
    
    def set_x_coord(self, x_coord):
        self.x_coord = x_coord

    def get_x_coord(self):
        return self.x_coord
    
    def set_y_coord(self, y_coord):
        self.y_coord = y_coord

    def get_y_coord(self):
        return self.y_coord
    
    def set_zone_code(self, zone_code):
        self.zone_code = zone_code

    def get_zone_code(self):
        return self.zone_code
    
    def set_shot_type(self, shot_type):
        self.shot_type = shot_type

    def get_shot_type(self):
        return self.shot_type
    
    