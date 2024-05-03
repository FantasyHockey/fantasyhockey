

class DraftRanking:

    def __init__(self, year, first_name, last_name, final_rank):
        self.year = year
        self.first_name = first_name
        self.last_name = last_name
        self.final_rank = final_rank
        self.position_code = None
        self.shoots_catches = None
        self.height_inches = None
        self.weight_pounds = None
        self.last_amateur_club = None
        self.last_amateur_league = None
        self.birth_date = None
        self.birth_city = None
        self.birth_state_province = None
        self.birth_country = None
        self.midterm_rank = None

    def get_year(self):
        return self.year
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_final_rank(self):
        return self.final_rank
    
    def set_position_code(self, position_code):
        self.position_code = position_code

    def get_position_code(self):
        return self.position_code
    
    def set_shoots_catches(self, shoots_catches):
        self.shoots_catches = shoots_catches

    def get_shoots_catches(self):
        return self.shoots_catches
    
    def set_height_inches(self, height_inches):
        self.height_inches = height_inches

    def get_height_inches(self):
        return self.height_inches
    
    def set_weight_pounds(self, weight_pounds):
        self.weight_pounds = weight_pounds

    def get_weight_pounds(self):
        return self.weight_pounds
    
    def set_last_amateur_club(self, last_amateur_club):
        self.last_amateur_club = last_amateur_club

    def get_last_amateur_club(self):
        return self.last_amateur_club
    
    def set_last_amateur_league(self, last_amateur_league):
        self.last_amateur_league = last_amateur_league

    def get_last_amateur_league(self):
        return self.last_amateur_league
    
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
    
    def set_midterm_rank(self, midterm_rank):
        self.midterm_rank = midterm_rank

    def get_midterm_rank(self):
        return self.midterm_rank