from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.data_fetching.teams.models.team import Team
from fantasyhockey.data_fetching.teams.models.team_data import TeamData
from fantasyhockey.data_fetching.teams.models.team_stats import TeamStats

class FetchTeams:
    """
    A class that fetches and stores NHL team data.
    
    Attributes:
        api_connector (APIConnector): An instance of the APIConnector class for making API requests.
        teams (list): A list to store the fetched Team objects.
        __TEAM_URL (str): The URL for fetching team standings data.
        __ROSTER_SEASON_URL (str): The URL for fetching roster season data.
        __TEAM_ID_URL (str): The URL for fetching team ID data.
        team_id_lookup (dict): A dictionary to store the team ID lookup data.
    """
    
    def __init__(self):
        self.api_connector = APIConnector()
        self.teams = []
        self.__TEAM_URL = "https://api-web.nhle.com/v1/standings/"
        self.__ROSTER_SEASON_URL = "https://api-web.nhle.com/v1/roster-season/mtl"
        self.__TEAM_ID_URL = "https://api.nhle.com/stats/rest/en/team"

        self.team_id_lookup = None    

    def get_teams(self):
        """
        Fetches and returns the list of Team objects.
        
        If the teams list is empty, it calls the __fetch() method to fetch the data.
        
        Returns:
            list: A list of Team objects.
        """
        if not self.teams:
            self.__fetch()
        return self.teams
    
    def __get_team_id_lookup(self):
        """
        Fetches and stores the team ID lookup data.
        """
        data = self.api_connector.get_json(self.__TEAM_ID_URL)
        self.team_id_lookup = data["data"]

    def __fetch(self):
        """
        Fetches team data for each year and creates Team objects.
        """
        self.__get_team_id_lookup()
        year_data = self.api_connector.get_json(self.__ROSTER_SEASON_URL)
        for year in year_data:
            self.__fetch_year_data(year)

    def __fetch_year_data(self, year):
        """
        Fetches team data for a specific year and creates a Team object for each team.
        
        Args:
            year (int): The year for which to fetch the team data.
        """
        data = self.api_connector.get_json(self.__TEAM_URL + str(year)[4:] + "-04-18")
        for team_json in data["standings"]:
            team_abbrev = self.__parse_data(self.__parse_data(team_json, "teamAbbrev"), "default")
            
            team_id = self.__find_team_id(team_abbrev)
            team = Team(team_id)
            team.set_team_data(self.__parse_team_details(team_id, year, team_abbrev, team_json))
            team.set_team_stats(self.__parse_team_stats(team_json, team_id, year))

            self.teams.append(team)

    def __parse_team_details(self, team_id, year, team_abbrev, team_json) -> TeamData:
        """
        Parses and returns the team details from the team JSON data.
        
        Args:
            team_id (int): The ID of the team.
            year (int): The year for which the team data is being parsed.
            team_abbrev (str): The team abbreviation.
            team_json (dict): The JSON data for the team.
        
        Returns:
            TeamData: An instance of the TeamData class containing the parsed team details.
        """
        team_data = TeamData(team_id)
        team_data.set_year(year)
        team_data.set_conference_name(self.__parse_data(team_json, "conferenceName"))
        team_data.set_division_name(self.__parse_data(team_json, "divisionName"))
        team_data.set_location_name(self.__parse_data(self.__parse_data(team_json, "placeName"), "default"))
        team_data.set_team_name(self.__parse_data(self.__parse_data(team_json, "teamName"), "default"))
        team_data.set_team_abbreviation(team_abbrev)
        team_data.set_team_logo(self.__parse_data(team_json, "teamLogo"))
        team_data.set_team_color_1(self.__get_team_colors(team_abbrev)["primary_color"])
        team_data.set_team_color_2(self.__get_team_colors(team_abbrev)["secondary_color"])
        return team_data

    def __parse_team_stats(self, team_json, team_id, year) -> TeamStats:
        """
        Parses and returns the team stats from the team JSON data.
        
        Args:
            team_json (dict): The JSON data for the team.
            team_id (int): The ID of the team.
            year (int): The year for which the team data is being parsed.
        
        Returns:
            TeamStats: An instance of the TeamStats class containing the parsed team stats.
        """
        team_stats = TeamStats(team_id)
        team_stats.set_year(year)
        team_stats.set_game_type_id(self.__parse_data(team_json, "gameTypeId"))
        team_stats.set_games_played(self.__parse_data(team_json, "gamesPlayed"))
        team_stats.set_goals_against(self.__parse_data(team_json, "goalAgainst"))
        team_stats.set_goals_for(self.__parse_data(team_json, "goalFor"))
        team_stats.set_losses(self.__parse_data(team_json, "losses"))
        team_stats.set_ot_losses(self.__parse_data(team_json, "otLosses"))
        team_stats.set_points(self.__parse_data(team_json, "points"))
        team_stats.set_shootout_losses(self.__parse_data(team_json, "shootoutLosses"))
        team_stats.set_shootout_wins(self.__parse_data(team_json, "shootoutWins"))
        team_stats.set_streak_code(self.__parse_data(team_json, "streakCode"))
        team_stats.set_streak_count(self.__parse_data(team_json, "streakCount"))
        team_stats.set_ties(self.__parse_data(team_json, "ties"))
        team_stats.set_waiver_sequence(self.__parse_data(team_json, "waiversSequence"))
        team_stats.set_regulation_wins(self.__parse_data(team_json, "regulationWins"))
        team_stats.set_regulation_plus_ot_wins(self.__parse_data(team_json, "regulationPlusOtWins"))
        team_stats.set_home_games_played(self.__parse_data(team_json, "homeGamesPlayed"))
        team_stats.set_home_goals_against(self.__parse_data(team_json, "homeGoalsAgainst"))
        team_stats.set_home_goals_for(self.__parse_data(team_json, "homeGoalsFor"))
        team_stats.set_home_losses(self.__parse_data(team_json, "homeLosses"))
        team_stats.set_home_ot_losses(self.__parse_data(team_json, "homeOtLosses"))
        team_stats.set_home_points(self.__parse_data(team_json, "homePoints"))
        team_stats.set_home_regulation_wins(self.__parse_data(team_json, "homeRegulationWins"))
        team_stats.set_home_regulation_plus_ot_wins(self.__parse_data(team_json, "homeRegulationPlusOtWins"))
        team_stats.set_home_ties(self.__parse_data(team_json, "homeTies"))
        team_stats.set_home_wins(self.__parse_data(team_json, "homeWins"))
        team_stats.set_last_10_games_played(self.__parse_data(team_json, "l10GamesPlayed"))
        team_stats.set_last_10_goals_against(self.__parse_data(team_json, "l10GoalsAgainst"))
        team_stats.set_last_10_goals_for(self.__parse_data(team_json, "l10GoalsFor"))
        team_stats.set_last_10_losses(self.__parse_data(team_json, "l10Losses"))
        team_stats.set_last_10_ot_losses(self.__parse_data(team_json, "l10OtLosses"))
        team_stats.set_last_10_points(self.__parse_data(team_json, "l10Points"))
        team_stats.set_last_10_regulation_wins(self.__parse_data(team_json, "l10RegulationWins"))
        team_stats.set_last_10_regulation_plus_ot_wins(self.__parse_data(team_json, "l10RegulationPlusOtWins"))
        team_stats.set_last_10_ties(self.__parse_data(team_json, "l10Ties"))
        team_stats.set_last_10_wins(self.__parse_data(team_json, "l10Wins"))
        team_stats.set_road_games_played(self.__parse_data(team_json, "roadGamesPlayed"))
        team_stats.set_road_goals_against(self.__parse_data(team_json, "roadGoalsAgainst"))
        team_stats.set_road_goals_for(self.__parse_data(team_json, "roadGoalsFor"))
        team_stats.set_road_losses(self.__parse_data(team_json, "roadLosses"))
        team_stats.set_road_ot_losses(self.__parse_data(team_json, "roadOtLosses"))
        team_stats.set_road_points(self.__parse_data(team_json, "roadPoints"))
        team_stats.set_road_regulation_wins(self.__parse_data(team_json, "roadRegulationWins"))
        team_stats.set_road_regulation_plus_ot_wins(self.__parse_data(team_json, "roadRegulationPlusOtWins"))
        team_stats.set_road_ties(self.__parse_data(team_json, "roadTies"))
        team_stats.set_road_wins(self.__parse_data(team_json, "roadWins"))
        return team_stats

    def __find_team_id(self, team_abbrev):
        """
        Finds and returns the team ID for a given team abbreviation.
        
        Args:
            team_abbrev (str): The abbreviation of the team.
        
        Returns:
            int: The ID of the team, or None if not found.
        """
        for team in self.team_id_lookup:
            if team["triCode"] == team_abbrev:
                return team["id"]
        return None
    
    def __parse_data(self, json, key):
        """
        Parses and returns the value of a key from a JSON object.
        
        Args:
            json (dict): The JSON object.
            key (str): The key to retrieve the value for.
        
        Returns:
            Any: The value of the key, or None if not found.
        """
        if key in json:
            return json[key]
        return None
    
    def __get_team_colors(self, team_id):
        """
        Returns the primary and secondary colors for a given team ID.
        
        Args:
            team_id (str): The ID of the team.
        
        Returns:
            dict: A dictionary containing the primary and secondary colors of the team.
        """
        team_colors = {
            "NYR": {"primary_color": "Blue", "secondary_color": "Red"},
            "DAL": {"primary_color": "Green", "secondary_color": "Black"},
            "CAR": {"primary_color": "Red", "secondary_color": "Black"},
            "WPG": {"primary_color": "Blue", "secondary_color": "Silver"},
            "FLA": {"primary_color": "Red", "secondary_color": "Blue"},
            "VAN": {"primary_color": "Blue", "secondary_color": "Green"},
            "BOS": {"primary_color": "Black", "secondary_color": "Gold"},
            "COL": {"primary_color": "Burgundy", "secondary_color": "Blue"},
            "EDM": {"primary_color": "Blue", "secondary_color": "Orange"},
            "TOR": {"primary_color": "Blue", "secondary_color": "White"},
            "NSH": {"primary_color": "Yellow", "secondary_color": "Blue"},
            "LAK": {"primary_color": "Black", "secondary_color": "Silver"},
            "TBL": {"primary_color": "Blue", "secondary_color": "White"},
            "VGK": {"primary_color": "Gold", "secondary_color": "Black"},
            "NYI": {"primary_color": "Blue", "secondary_color": "Orange"},
            "STL": {"primary_color": "Blue", "secondary_color": "Gold"},
            "WSH": {"primary_color": "Red", "secondary_color": "Blue"},
            "DET": {"primary_color": "Red", "secondary_color": "White"},
            "PIT": {"primary_color": "Black", "secondary_color": "Gold"},
            "MIN": {"primary_color": "Green", "secondary_color": "Red"},
            "PHI": {"primary_color": "Orange", "secondary_color": "Black"},
            "BUF": {"primary_color": "Blue", "secondary_color": "Gold"},
            "NJD": {"primary_color": "Red", "secondary_color": "Black"},
            "ARI": {"primary_color": "Red", "secondary_color": "Green"},
            "MTL": {"primary_color": "Red", "secondary_color": "Blue"},
            "CBJ": {"primary_color": "Blue", "secondary_color": "Red"},
            "ANA": {"primary_color": "Black", "secondary_color": "Gold"},
            "CHI": {"primary_color": "Red", "secondary_color": "Black"},
            "SJS": {"primary_color": "Teal", "secondary_color": "Black"}
        }
        
        return team_colors.get(team_id, {"primary_color": "Unknown", "secondary_color": "Unknown"})