<<<<<<< HEAD
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
=======
from abc import ABC, abstractmethod
from fantasyhockey.data_fetching.maps import ApiMapperFactory
import json

class Serializer(ABC):
    """Abstract base class for serializers."""

    @abstractmethod
    def serialize(self, obj) -> str:
        """Serialize the given object into a string representation.

        Args:
            obj: The object to be serialized.

        Returns:
            str: The serialized string representation of the object.
        """
        pass

    @abstractmethod
    def deserialize(self, data: str, cls):
        """Deserialize the given string representation into an object.

        Args:
            data (str): The string representation of the object.
            cls: The class of the object to be deserialized.

        Returns:
            The deserialized object.
        """
        pass

class JsonSerializer(Serializer):
    """A serializer that converts objects to JSON strings and vice versa."""

    def serialize(self, obj) -> str:
        """Serialize the given object to a JSON string.

        Args:
            obj: The object to be serialized.

        Returns:
            str: The JSON string representation of the object.
        """
        mapper = ApiMapperFactory.get_mapper(obj)
        data_dict = mapper.reverse_map(obj)
        return json.dumps(data_dict)

    def deserialize(self, data: dict, cls):
        """Deserialize the given JSON string to an object of the specified class.

        Args:
            data (str): The JSON string to be deserialized.
            cls: The class of the object to be deserialized.

        Returns:
            The deserialized object.
        """
        if isinstance(data, dict):
            data_dict = data
        else:
            data_dict = json.loads(data)

        mapper = ApiMapperFactory.get_mapper(cls)
        return mapper.map(data_dict)
    
class SerializerFactory:
    """
    Factory class for creating serializers based on the specified format.
    """

    @staticmethod
    def get_serializer(format: str) -> Serializer:
        """
        Returns a serializer instance based on the specified format.

        Args:
            format (str): The format of the serializer.

        Returns:
            Serializer: An instance of the serializer.

        Raises:
            ValueError: If the specified format is unknown.
        """
        if format == 'json':
            return JsonSerializer()
        else:
            raise ValueError(f"Unknown format: {format}")
>>>>>>> a39f72b (Start of refactor)
