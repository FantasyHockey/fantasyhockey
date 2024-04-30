

class TeamData:
    def __init__(self, team_id):
        self.team_id = team_id
        self.year = None
        self.conference_name = None
        self.division_name = None
        self.location_name = None
        self.team_name = None
        self.team_abbreviation = None
        self.team_logo = None
        self.team_color_1 = None
        self.team_color_2 = None

    def get_team_id(self):
        return self.team_id
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_conference_name(self, conference_name):
        self.conference_name = conference_name

    def get_conference_name(self):
        return self.conference_name
    
    def set_division_name(self, division_name):
        self.division_name = division_name

    def get_division_name(self):
        return self.division_name
    
    def set_location_name(self, location_name):
        self.location_name = location_name

    def get_location_name(self):
        return self.location_name
    
    def set_team_name(self, team_name):
        self.team_name = team_name

    def get_team_name(self):
        return self.team_name
    
    def set_team_abbreviation(self, team_abbreviation):
        self.team_abbreviation = team_abbreviation

    def get_team_abbreviation(self):
        return self.team_abbreviation
    
    def set_team_logo(self, team_logo):
        self.team_logo = team_logo

    def get_team_logo(self):
        return self.team_logo
    
    def set_team_color_1(self, team_color_1):
        self.team_color_1 = team_color_1

    def get_team_color_1(self):
        return self.team_color_1
    
    def set_team_color_2(self, team_color_2):
        self.team_color_2 = team_color_2

    def get_team_color_2(self):
        return self.team_color_2