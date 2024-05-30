class SerializeDraftRanking:
    def __init__(self, player_data):
        self.__player_data = player_data
        
    def __serialize(self):
        final_rank = 0
        ranking = SerializeDraftRanking(year, self.__player_data["firstName"], self.__player_data["lastName"], final_rank)
        ranking.set_position_code(self.data_parser.parse(self.__player_data, "positionCode", 'none'))
        ranking.set_shoots_catches(self.data_parser.parse(self.__player_data, "shootsCatches", 'none'))
        ranking.set_height_inches(self.data_parser.parse(self.__player_data, "heightInInches", 'none'))
        ranking.set_weight_pounds(self.data_parser.parse(self.__player_data, "weightInPounds", 'none'))
        ranking.set_last_amateur_club(self.data_parser.parse(self.__player_data, "lastAmateurClub", 'none'))
        ranking.set_last_amateur_league(self.data_parser.parse(self.__player_data, "lastAmateurLeague", 'none'))
        ranking.set_birth_date(self.data_parser.parse(self.__player_data, "birthDate", 'none'))
        ranking.set_birth_city(self.data_parser.parse(self.__player_data, "birthCity", 'none'))
        ranking.set_birth_state_province(self.data_parser.parse(self.__player_data, "birthStateProvince", 'none'))
        ranking.set_birth_country(self.data_parser.parse(self.__player_data, "birthCountry", 'none'))
        ranking.set_midterm_rank(self.data_parser.parse(self.__player_data, "midtermRank", 'none'))
        return ranking