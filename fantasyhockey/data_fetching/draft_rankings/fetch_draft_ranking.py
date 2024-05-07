from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.draft_rankings.models.draft_ranking import DraftRanking

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
               ranking.set_position_code(self.__parse_data(player_data, "positionCode"))
               ranking.set_shoots_catches(self.__parse_data(player_data, "shootsCatches"))
               ranking.set_height_inches(self.__parse_data(player_data, "heightInInches"))
               ranking.set_weight_pounds(self.__parse_data(player_data, "weightInPounds"))
               ranking.set_last_amateur_club(self.__parse_data(player_data, "lastAmateurClub"))
               ranking.set_last_amateur_league(self.__parse_data(player_data, "lastAmateurLeague"))
               ranking.set_birth_date(self.__parse_data(player_data, "birthDate"))
               ranking.set_birth_city(self.__parse_data(player_data, "birthCity"))
               ranking.set_birth_state_province(self.__parse_data(player_data, "birthStateProvince"))
               ranking.set_birth_country(self.__parse_data(player_data, "birthCountry"))
               ranking.set_midterm_rank(self.__parse_data(player_data, "midtermRank"))
               self.draft_rankings.append(ranking)

            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {player_data['firstName']}): {e}")

    def __parse_data(self, json, key):
        if key in json:
            return json[key]
        return None