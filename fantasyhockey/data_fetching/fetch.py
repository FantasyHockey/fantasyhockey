from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.draft_rankings.models.draft_ranking import DraftRanking
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.data_fetching.serializers import SerializeDraftRanking

class FetchDraftRankings:
    """
    A class to fetch the draft ranking data from the NHL API.

    Methods
    -------
    get_draft_ranking()
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
    """
    

    def __init__(self):
        self.api_connector = APIConnector()
        self.data_parser = DataParser()
        self.draft_rankings = []

    def get_draft_rankings(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
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
                    
                ranking = SerializeDraftRanking(player_data).__serialize()
               
            

            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {player_data['firstName']}): {e}")

    