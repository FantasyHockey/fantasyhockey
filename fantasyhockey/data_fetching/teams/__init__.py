from fantasyhockey.api.api_connector import APIConnector

class Team:
    def __init__(self):
        pass

    def get_team(self):
        APIConnector.get("https://api-web.nhle.com")

    def __get_seasons(self):
        data = APIConnector.get("https://api-web.nhle.com/v1/season")