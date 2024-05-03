
class PlayerDetails:
    def __init__(self, player_id):
        self.player_id = player_id 
        self.first_name = None
        self.last_name = None
        self.jersey_number = None
        self.position = None
        self.headshot = None
        self.hero_image = None
        self.height_inches = None
        self.weight_pounds = None
        self.birth_date = None
        self.birth_city = None
        self.birth_state_province = None
        self.birth_country = None
        self.shoots_catches = None
        self.in_top_100_all_time = None
        self.in_hhof = None

    def get_player_id(self):
        return self.player_id
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name
    
    def set_jersey_number(self, jersey_number):
        self.jersey_number = jersey_number

    def get_jersey_number(self):
        return self.jersey_number
    
    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position
    
    def set_headshot(self, headshot):
        self.headshot = headshot

    def get_headshot(self):
        return self.headshot
    
    def set_hero_image(self, hero_image):
        self.hero_image = hero_image

    def get_hero_image(self):
        return self.hero_image
    
    def set_height_inches(self, height_inches):
        self.height_inches = height_inches

    def get_height_inches(self):
        return self.height_inches
    
    def set_weight_pounds(self, weight_pounds):
        self.weight_pounds = weight_pounds

    def get_weight_pounds(self):
        return self.weight_pounds
    
    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_birth_date(self):
        return self.birth_date
    
    def set_birth_city(self, birth_city):
        self.birth_city = birth_city

    def get_birth_city(self):
        return self.birth_city
    
    def set_birth_state_province(self, birth_state_province):
        self.birth_state_province = birth_state_province

    def get_birth_state_province(self):
        return self.birth_state_province
    
    def set_birth_country(self, birth_country):
        self.birth_country = birth_country

    def get_birth_country(self):
        return self.birth_country
    
    def set_shoots_catches(self, shoots_catches):
        self.shoots_catches = shoots_catches

    def get_shoots_catches(self):
        return self.shoots_catches
    
    def set_in_top_100_all_time(self, in_top_100_all_time):
        self.in_top_100_all_time = in_top_100_all_time

    def get_in_top_100_all_time(self):
        return self.in_top_100_all_time
    
    def set_in_hhof(self, in_hhof):
        self.in_hhof = in_hhof

    def get_in_hhof(self):
        return self.in_hhof
    
    