<<<<<<< HEAD
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
=======



class Season:
    def __init__(self, season_id=None):
        self._season_id = season_id
        self._conference_in_use = None
        self._division_in_use = None
        self._point_for_ot_loss_in_use = None
        self._regulation_wins_in_use = None
        self._row_in_use = None
        self._standings_end = None
        self._standings_start = None
        self._ties_in_use = None
        self._wild_card_in_use = None

    @property
    def season_id(self):
        return self._season_id

    @season_id.setter
    def season_id(self, value):
        self._season_id = value

    @property
    def conference_in_use(self):
        return self._conference_in_use

    @conference_in_use.setter
    def conference_in_use(self, value):
        self._conference_in_use = value

    @property
    def division_in_use(self):
        return self._division_in_use

    @division_in_use.setter
    def division_in_use(self, value):
        self._division_in_use = value

    @property
    def point_for_ot_loss_in_use(self):
        return self._point_for_ot_loss_in_use

    @point_for_ot_loss_in_use.setter
    def point_for_ot_loss_in_use(self, value):
        self._point_for_ot_loss_in_use = value

    @property
    def regulation_wins_in_use(self):
        return self._regulation_wins_in_use

    @regulation_wins_in_use.setter
    def regulation_wins_in_use(self, value):
        self._regulation_wins_in_use = value

    @property
    def row_in_use(self):
        return self._row_in_use

    @row_in_use.setter
    def row_in_use(self, value):
        self._row_in_use = value

    @property
    def standings_end(self):
        return self._standings_end

    @standings_end.setter
    def standings_end(self, value):
        self._standings_end = value

    @property
    def standings_start(self):
        return self._standings_start

    @standings_start.setter
    def standings_start(self, value):
        self._standings_start = value

    @property
    def ties_in_use(self):
        return self._ties_in_use

    @ties_in_use.setter
    def ties_in_use(self, value):
        self._ties_in_use = value

    @property
    def wild_card_in_use(self):
        return self._wild_card_in_use

    @wild_card_in_use.setter
    def wild_card_in_use(self, value):
        self._wild_card_in_use = value

class DraftRanking:
    def __init__(self, year=None, first_name=None, last_name=None, position_code=None):
        self._year = year
        self._first_name = first_name
        self._last_name = last_name
        self._final_rank = None
        self._position_code = position_code
        self._shoots_catches = None
        self._height_inches = None
        self._weight_pounds = None
        self._last_amateur_club = None
        self._last_amateur_league = None
        self._birth_date = None
        self._birth_city = None
        self._birth_state_province = None
        self._birth_country = None
        self._midterm_rank = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def final_rank(self):
        return self._final_rank

    @final_rank.setter
    def final_rank(self, value):
        self._final_rank = value

    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value

    @property
    def shoots_catches(self):
        return self._shoots_catches

    @shoots_catches.setter
    def shoots_catches(self, value):
        self._shoots_catches = value

    @property
    def height_inches(self):
        return self._height_inches

    @height_inches.setter
    def height_inches(self, value):
        self._height_inches = value

    @property
    def weight_pounds(self):
        return self._weight_pounds

    @weight_pounds.setter
    def weight_pounds(self, value):
        self._weight_pounds = value

    @property
    def last_amateur_club(self):
        return self._last_amateur_club

    @last_amateur_club.setter
    def last_amateur_club(self, value):
        self._last_amateur_club = value

    @property
    def last_amateur_league(self):
        return self._last_amateur_league

    @last_amateur_league.setter
    def last_amateur_league(self, value):
        self._last_amateur_league = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def birth_city(self):
        return self._birth_city

    @birth_city.setter
    def birth_city(self, value):
        self._birth_city = value

    @property
    def birth_state_province(self):
        return self._birth_state_province

    @birth_state_province.setter
    def birth_state_province(self, value):
        self._birth_state_province = value

    @property
    def birth_country(self):
        return self._birth_country

    @birth_country.setter
    def birth_country(self, value):
        self._birth_country = value

    @property
    def midterm_rank(self):
        return self._midterm_rank

    @midterm_rank.setter
    def midterm_rank(self, value):
        self._midterm_rank = value

#pass
>>>>>>> a39f72b (Start of refactor)
