

class ShiftData:

    def __init__(self, shift_id):
        self.shift_id = shift_id
        self.game_id = None
        self.player_id = None
        self.detail_code = None
        self.duration = None
        self.end_time = None
        self.start_time = None
        self.event_description = None
        self.event_details = None
        self.event_number = None
        self.period_number = None
        self.shift_number = None
        self.type_code = None

    def get_shift_id(self):
        return self.shift_id
    
    def set_game_id(self, game_id):
        self.game_id = game_id

    def get_game_id(self):
        return self.game_id
    
    def set_player_id(self, player_id):
        self.player_id = player_id

    def get_player_id(self):
        return self.player_id
    
    def set_detail_code(self, detail_code):
        self.detail_code = detail_code

    def get_detail_code(self):
        return self.detail_code
    
    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration
    
    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time
    
    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_start_time(self):
        return self.start_time
    
    def set_event_description(self, event_description):
        self.event_description = event_description

    def get_event_description(self):
        return self.event_description
    
    def set_event_details(self, event_details):
        self.event_details = event_details

    def get_event_details(self):
        return self.event_details
    
    def set_event_number(self, event_number):
        self.event_number = event_number

    def get_event_number(self):
        return self.event_number
    
    def set_period_number(self, period_number):
        self.period_number = period_number

    def get_period_number(self):
        return self.period_number
    
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def get_shift_number(self):
        return self.shift_number
    
    def set_type_code(self, type_code):
        self.type_code = type_code

    def get_type_code(self):
        return self.type_code