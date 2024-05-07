

class DataParser:
    """
    A class that provides methods for parsing JSON data based on different versions.

    Args:
        data (dict): The JSON data to be parsed.

    Methods:
        parse(json, key, version=None):
            Parses the JSON data based on the specified version.
            'empty_list': Returns an empty list if the key is not found in the JSON data.
            'none': Returns None if the key is not found in the JSON data.
            'empty_dict': Returns an empty dictionary if the key is not found in the JSON data.
            'empty_string': Returns an empty string if the key is not found in the JSON data.
            'checker': Checks if the specified key is present in the JSON data.
            default: Raises a ValueError if the specified version is not found.
        
        double_parse(json, key, sub_key, version=None):
            Parses the JSON data based on the specified version.
            'empty_list': Returns an empty list if the key is not found in the JSON data.
            'none': Returns None if the key is not found in the JSON data.
            'empty_dict': Returns an empty dictionary if the key is not found in the JSON data.
            'empty_string': Returns an empty string if the key is not found in the JSON data.
            'checker': Checks if the specified key is present in the JSON data.
            default: Raises a ValueError if the specified version is not found.
    """

    def __init__(self, data):
        self.data = data

    def parse(self, json, key, version=None):
        """
        Parses the JSON data based on the specified version.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.
            version (str, optional): The version of parsing to be applied. Defaults to None.

        Returns:
            The parsed value based on the specified version.

        Raises:
            ValueError: If the specified version is not found.
        """
        if version is None:
            return self.__parse_error(json, key)
        elif version == "empty_list":
            return self.__parse_empty_list(json, key)
        elif version == "none":
            return self.__parse_none(json, key)
        elif version == "empty_dict":
            return self.__parse_empty_dict(json, key)
        elif version == "empty_string":
            return self.__parse_empty_string(json, key)
        elif version == "checker":
            return self.__parse_checker(json, key)
        else:
            raise ValueError(f"Version {version} not found.")

    def double_parse(self, json, key, sub_key, version=None):
        """
        Parses the JSON data based on the specified version.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.
            sub_key (str): The sub-key to be parsed from the JSON data.
            version (str, optional): The version of parsing to be applied. Defaults to None.

        Returns:
            The parsed value based on the specified version.

        Raises:
            ValueError: If the specified version is not found.
        """
        if version is None:
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_error(sub_json, sub_key)
        elif version == "empty_list":
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_empty_list(sub_json, sub_key)
        elif version == "none":
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_none(sub_json, sub_key)
        elif version == "empty_dict":
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_empty_dict(sub_json, sub_key)
        elif version == "empty_string":
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_empty_string(sub_json, sub_key)
        elif version == "checker":
            sub_json = self.__parse_empty_dict(json, key)
            return self.__parse_checker(sub_json, sub_key)
        else:
            raise ValueError(f"Version {version} not found.")

    def __parse_error(self, json, key):
        """
        Parses the JSON data and returns the value associated with the specified key.
        Raises a KeyError if the key is not found in the JSON data.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.

        Returns:
            The parsed value associated with the specified key.

        Raises:
            KeyError: If the specified key is not found in the JSON data.
        """
        if key in json:
            return json[key]
        raise KeyError(f"Key {key} not found in json data.")

    def __parse_empty_list(self, json, key):
        """
        Parses the JSON data and returns the value associated with the specified key.
        Returns an empty list if the key is not found in the JSON data.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.

        Returns:
            The parsed value associated with the specified key, or an empty list if the key is not found.
        """
        if key in json:
            return json[key]
        return []

    def __parse_none(self, json, key):
        """
        Parses the JSON data and returns the value associated with the specified key.
        Returns None if the key is not found in the JSON data.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.

        Returns:
            The parsed value associated with the specified key, or None if the key is not found.
        """
        if key in json:
            return json[key]
        return None

    def __parse_empty_dict(self, json, key):
        """
        Parses the JSON data and returns the value associated with the specified key.
        Returns an empty dictionary if the key is not found in the JSON data.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.

        Returns:
            The parsed value associated with the specified key, or an empty dictionary if the key is not found.
        """
        if key in json:
            return json[key]
        return {}

    def __parse_empty_string(self, json, key):
        """
        Parses the JSON data and returns the value associated with the specified key.
        Returns an empty string if the key is not found in the JSON data.

        Args:
            json (dict): The JSON data to be parsed.
            key (str): The key to be parsed from the JSON data.

        Returns:
            The parsed value associated with the specified key, or an empty string if the key is not found.
        """
        if key in json:
            return json[key]
        return ""

    def __parse_checker(self, json, key):
        """
        Checks if the specified key is present in the JSON data.

        Args:
            json (dict): The JSON data to be checked.
            key (str): The key to be checked in the JSON data.

        Returns:
            True if the key is found in the JSON data, False otherwise.
        """
        return key in json
    

