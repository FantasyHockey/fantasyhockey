from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.seasons.fetch_seasons import FetchSeasons

class UpdateSeasons:
    """
    A class to update the seasons table in the database.

    This class provides methods to fetch the seasons data from the NHL API and update the seasons table in the database.

    Methods
    -------
    update_in_db()
        Fetches the seasons data from the NHL API and updates the seasons table in the database.
    """

    def __init__(self):
        """
        Initializes the UpdateSeasons instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact
            with the database.
            
        fetch_seasons : FetchSeasons
            An instance of the FetchSeasons class to fetch the
            seasons data from the NHL API.
            
        """
        self.database_operator = DatabaseOperator()
        self.fetch_seasons = FetchSeasons()

    def update_in_db(self):
        """
        Fetches the seasons data from the NHL API and updates the seasons table in the database.
        """
        seasons = self.fetch_seasons.get_seasons()
        for season in seasons:
            query, params = self.__create_query(season)
            self.database_operator.write(query, params)

    def __create_query(self, season):
        """
        Creates a query to insert a season into the seasons table.
        """
        query = "INSERT INTO seasons (year, conferences_in_use, point_for_ot_loss, regulation_wins, `row`,\
                    standings_start_date, standings_end_date, ties_in_use, wild_card_in_use) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (season.get_year(), season.get_conference_in_use(), season.get_point_for_ot_loss_in_use(), season.get_regulation_wins_in_use(),\
                    season.get_row_in_use(), season.get_standings_start(), season.get_standings_end(), season.get_ties_in_use(), season.get_wild_card_in_use())
        return query, params