

class Season:
    """
    Represents a season in the NHL.
    """
    def __init__(self, year, conference_in_use = None, division_in_use = None, point_for_ot_loss_in_use = None,
                 regulation_wins_in_use = None, row_in_use = None, standings_end = None, standings_start = None,
                 ties_in_use = None, wild_card_in_use = None):
        self.year = year
        self.conference_in_use = conference_in_use
        self.division_in_use = division_in_use
        self.point_for_ot_loss_in_use = point_for_ot_loss_in_use
        self.regulation_wins_in_use = regulation_wins_in_use
        self.row_in_use = row_in_use
        self.standings_end = standings_end
        self.standings_start = standings_start
        self.ties_in_use = ties_in_use
        self.wild_card_in_use = wild_card_in_use

    def get_year(self):
        return self.year
    
    def get_conference_in_use(self):
        return self.conference_in_use
    
    def set_conference_in_use(self, conference_in_use):
        if type(conference_in_use) != bool:
            raise ValueError("Conference must be either True or False.")
        self.conference_in_use = conference_in_use

    def get_division_in_use(self):
        return self.division_in_use
    
    def set_division_in_use(self, division_in_use):
        if type(division_in_use) != bool:
            raise ValueError("Division must be either True or False.")
        self.division_in_use = division_in_use

    def get_point_for_ot_loss_in_use(self):
        return self.point_for_ot_loss_in_use
    
    def set_point_for_ot_loss_in_use(self, point_for_ot_loss_in_use):
        if type(point_for_ot_loss_in_use) != bool:
            raise ValueError("Point for OT Loss must be either True or False.")
        self.point_for_ot_loss_in_use = point_for_ot_loss_in_use

    def get_regulation_wins_in_use(self):
        return self.regulation_wins_in_use
    
    def set_regulation_wins_in_use(self, regulation_wins_in_use):
        if type(regulation_wins_in_use) != bool:
            raise ValueError("Regulation Wins must be either True or False.")
        self.regulation_wins_in_use = regulation_wins_in_use

    def get_row_in_use(self):
        return self.row_in_use
    
    def set_row_in_use(self, row_in_use):
        if type(row_in_use) != bool:
            raise ValueError("Row must be either True or False.")
        self.row_in_use = row_in_use

    def get_standings_end(self):
        return self.standings_end
    
    def set_standings_end(self, standings_end):
        if type(standings_end) != str:
            raise ValueError("Standings End must be str")
        self.standings_end = standings_end

    def get_standings_start(self):
        return self.standings_start
    
    def set_standings_start(self, standings_start):
        if type(standings_start) != str:
            raise ValueError("Standings Start must be str")
        self.standings_start = standings_start

    def get_ties_in_use(self):
        return self.ties_in_use
    
    def set_ties_in_use(self, ties_in_use):
        if type(ties_in_use) != bool:
            raise ValueError("Ties must be either True or False.")
        self.ties_in_use = ties_in_use

    def get_wild_card_in_use(self):
        return self.wild_card_in_use
    
    def set_wild_card_in_use(self, wild_card_in_use):
        if type(wild_card_in_use) != bool:
            raise ValueError("Wild Card must be either True or False.")
        self.wild_card_in_use = wild_card_in_use

    def __str__(self):
        return f"Season(year={self.year}, conference_in_use={self.conference_in_use}, division_in_use={self.division_in_use}, point_for_ot_loss_in_use={self.point_for_ot_loss_in_use}, regulation_wins_in_use={self.regulation_wins_in_use}, row_in_use={self.row_in_use}, standings_end={self.standings_end}, standings_start={self.standings_start}, ties_in_use={self.ties_in_use}, wild_card_in_use={self.wild_card_in_use})"
    
    def __repr__(self):
        return f"Season(year={self.year}, conference_in_use={self.conference_in_use}, division_in_use={self.division_in_use}, point_for_ot_loss_in_use={self.point_for_ot_loss_in_use}, regulation_wins_in_use={self.regulation_wins_in_use}, row_in_use={self.row_in_use}, standings_end={self.standings_end}, standings_start={self.standings_start}, ties_in_use={self.ties_in_use}, wild_card_in_use={self.wild_card_in_use})"
    

