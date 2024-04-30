from fantasyhockey.api.api_connector import APIConnector

class Player:
    def __init__(self):
        pass

    def get_player(self):
        APIConnector.get("https://api-web.nhle.com")
