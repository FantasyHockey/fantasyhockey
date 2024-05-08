from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.draft_rankings.models.draft_ranking import DraftRanking
from fantasyhockey.util.data_parser import DataParser

class FetchDraftRankings:
    """
    A class to fetch the draft ranking data from the NHL API.

    Methods
    -------
    get_draft_ranking()
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects.
    """
    

    def __init__(self):
        self.api_connector = APIConnector()
        self.data_parser = DataParser()
        self.draft_rankings = []

    def get_draft_rankings(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects.
        """
        if not self.draft_rankings:
            self.__fetch()
        return self.draft_rankings

    def __fetch(self):
        data = self.api_connector.get_json("https://api-web.nhle.com/v1/draft/rankings/now")
        year = data["draftYear"]
        for player_data in data["rankings"]:
            try:
               final_rank = 0
               if "finalRank" in player_data:
                   final_rank = player_data["finalRank"]
            

               ranking = DraftRanking(year, player_data["firstName"], player_data["lastName"], final_rank)
               ranking.set_position_code(self.data_parser.parse(player_data, "positionCode", 'none'))
               ranking.set_shoots_catches(self.data_parser.parse(player_data, "shootsCatches", 'none'))
               ranking.set_height_inches(self.data_parser.parse(player_data, "heightInInches", 'none'))
               ranking.set_weight_pounds(self.data_parser.parse(player_data, "weightInPounds", 'none'))
               ranking.set_last_amateur_club(self.data_parser.parse(player_data, "lastAmateurClub", 'none'))
               ranking.set_last_amateur_league(self.data_parser.parse(player_data, "lastAmateurLeague", 'none'))
               ranking.set_birth_date(self.data_parser.parse(player_data, "birthDate", 'none'))
               ranking.set_birth_city(self.data_parser.parse(player_data, "birthCity", 'none'))
               ranking.set_birth_state_province(self.data_parser.parse(player_data, "birthStateProvince", 'none'))
               ranking.set_birth_country(self.data_parser.parse(player_data, "birthCountry", 'none'))
               ranking.set_midterm_rank(self.data_parser.parse(player_data, "midtermRank", 'none'))
               self.draft_rankings.append(ranking)

            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {player_data['firstName']}): {e}")

    