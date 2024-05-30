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
            query, params = self.__update_query(player_data)
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
    
    def __update_query(self, player_data) -> tuple:
        query = "UPDATE draft_rankings SET year = %s, first_name = %s, last_name = %s, position_code = %s, shoots_catches = %s, height_inches = %s, weight_pounds = %s, last_amateur_club = %s, last_amateur_league = %s, birth_date = %s, \
              birth_city = %s, birth_state_province = %s, birth_country = %s, midterm_rank = %s, final_rank = %s WHERE year = %s AND first_name = %s AND last_name = %s "
        
        params = (player_data.get_year(), player_data.get_first_name(),player_data.get_last_name(), player_data.get_position_code(),\
                    player_data.get_shoots_catches(), player_data.get_height_inches(), player_data.get_weight_pounds(), player_data.get_last_amateur_club(), player_data.get_last_amateur_league(),\
                    player_data.get_birth_date(), player_data.get_birth_city(), player_data.get_birth_state_province(), player_data.get_birth_country(), player_data.get_midterm_rank(), player_data.get_final_rank(),player_data.get_year(),player_data.get_first_name(),player_data.get_last_name())
        return query, params
    


<<<<<<< HEAD
    

    
=======
    def __update_player_awards_query(self, award: PlayerAwards) -> tuple:
        query = "UPDATE player_awards SET award_name = %s, year = %s WHERE id = %s AND award_name = %s AND year = %s"
        params = (award.get_award(), award.get_year(), award.get_player_id(), award.get_award(), award.get_year())
        return query, params
>>>>>>> 2083f4ce141888766d3a5f39055d006a28b9a306
