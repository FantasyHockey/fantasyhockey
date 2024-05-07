from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.draft_rankings.fetch_draft_ranking import FetchDraftRankings

class UpdateDraftRankings:
    """
    A class to update the draft rankings table in the database.

    This class provides methods to fetch the seasons data from the NHL API and update the seasons table in the database.

    Methods
    -------
    update_in_db()
        Fetches the draft rankings data from the NHL API and updates the draft rankings table in the database.
    """

    def __init__(self):
        """
        Initializes the UpdateDraftRankings instance.
        
        Parameters
        ----------
        database_operator : DatabaseOperator
            An instance of the DatabaseOperator class to interact
            with the database.
            
        fetch_draft_ranking : FetchDraftRankings
            An instance of the FetchDraftRankings class to fetch the
            draft rankings data from the NHL API.
            
        """
        self.database_operator = DatabaseOperator()
        self.fetch_draft_ranking = FetchDraftRankings()

    def update_in_db(self):
        """
        Fetches the seasons data from the NHL API and updates the seasons table in the database.
        """
        draft_rankings = self.fetch_draft_ranking.get_draft_rankings()
        for player_data in draft_rankings:    
            query, params = self.__create_query(player_data)
            self.database_operator.write(query, params)

    def __create_query(self, player_data):
        """
        Creates a query to insert a ranking into the draft_rankings table.  
        """
        query = "INSERT INTO draft_rankings (year, first_name, last_name, position_code,\
                    shoots_catches, height_inches, weight_pounds, last_amateur_club, last_amateur_league, birth_date, birth_city, birth_state_province, birth_country, midterm_rank, final_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        params = (player_data.get_year(), player_data.get_first_name(), player_data.get_last_name(), player_data.get_position_code(),\
                    player_data.get_shoots_catches(), player_data.get_height_inches(), player_data.get_weight_pounds(), player_data.get_last_amateur_club(), player_data.get_last_amateur_league(),\
                    player_data.get_birth_date(), player_data.get_birth_city(), player_data.get_birth_state_province(), player_data.get_birth_country(), player_data.get_midterm_rank(), player_data.get_final_rank())
        return query, params
    

    def __update_query(self):
        '''
        Updates the draft_rankings table
        '''
        sql = "UPDATE draft_rankings SET first_name = 'get_first_name()', last_name = 'get_last_name()', position_code = 'get_position_code()', shoots_catches = 'get_shoots_catches()', height_inches = 'get_height_inches()'\
            weight_pounds = 'get_weight_pounds()'WHERE address = 'get_first_name()'"

