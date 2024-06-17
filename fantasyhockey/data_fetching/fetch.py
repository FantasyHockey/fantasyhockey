from abc import ABC, abstractmethod
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.serializers import SerializerFactory
from fantasyhockey.data_fetching.models import *

class DataFetcher(ABC):
    """
    Abstract base class for fetching data.

    Attributes:
        _data (list): A list to store the fetched data.
        _items (list): A list to store the items to fetch data for.
        _database_operator (DatabaseOperator): An instance of the DatabaseOperator class.
        _api_connector (APIConnector): An instance of the APIConnector class.
        _data_parser (DataParser): An instance of the DataParser class.
        _util (Util): An instance of the Util class.
        _serializer (Serializer): An instance of the Serializer class.

    Methods:
        get_data(): Returns the fetched data.
        _fetch(): Fetches the data by calling _get_items() and _get_data_by_item() methods.
        _get_items(): Abstract method to be implemented by subclasses to get the items to fetch data for.
        _get_data_by_item(): Abstract method to be implemented by subclasses to fetch data for each item.
        _process_data(data): Abstract method to be implemented by subclasses to process the fetched data.
    """

    def __init__(self):
        self._data = []
        self._items = []
        self._data_parser = DataParser()
        self._database_operator = DatabaseOperator()
        self._api_connector = APIConnector()
        self._serializer = SerializerFactory.get_serializer("json")

    def get_data(self):
        """
        Returns the fetched data.

        Returns:
            list: The fetched data.
        """
        if not self._data:
            self._fetch()
        return self._data

    def _fetch(self):
        """
        Fetches the data by calling _get_items() and _get_data_by_item() methods.
        """
        self._get_items()
        self._get_data_by_item()

    def _fetch_paginated_data(self, url, start=0, accumulated_data=None):
        """
        Recursively fetches paginated data from the given URL.

        Args:
            url (str): The URL to fetch data from.
            start (int): The starting point for fetching data.
            accumulated_data (list): The accumulated data from previous pages.

        Returns:
            list: The accumulated data from all pages.
        """
        if accumulated_data is None:
            accumulated_data = []

        paginated_url = f"{url}&start={start}"
        try:
            data = self._api_connector.get_json(paginated_url)
            
            if "total" not in data or "data" not in data:
                print(f"Unexpected response format: {data}")
                return []

        except Exception as e:
            print(f"Error occurred while fetching paginated data from {paginated_url}: {e}")
            return []
        
        total_count = data["total"]
        accumulated_data.extend(data["data"])

        if start + len(data["data"]) < total_count:
            return self._fetch_paginated_data(url, start + len(data["data"]), accumulated_data)
        else:
            return accumulated_data

    @abstractmethod
    def _get_items(self):
        """
        Abstract method to be implemented by subclasses to get the items to fetch data for.
        """
        pass

    @abstractmethod
    def _get_data_by_item(self):
        """
        Abstract method to be implemented by subclasses to fetch data for each item.
        """
        pass

    @abstractmethod
    def _process_data(self, data):
        """
        Abstract method to be implemented by subclasses to process the fetched data.

        Args:
            data (list): The fetched data.
        """
        pass

class FetchSeasons(DataFetcher):
    def __init__(self):
        super().__init__()

    def _get_items(self):
        self._items = self._api_connector.get_json("https://api-web.nhle.com/v1/standings-season/")["seasons"]

    def _get_data_by_item(self):
        for season in self._items:
            try:
                season_obj = self._serializer.deserialize(season, Season)
                self._data.append(season_obj)
            except ValueError as e:
                print(f"Error occurred while fetching season data (id: {season['id']}): {e}")
            
            
    def _process_data(self, data):
        pass

class FetchDraftRankings(DataFetcher):
    """
    A class to fetch the draft ranking data from the NHL API.

    Methods
    -------
    get_draft_ranking()
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
    """

    def __init__(self):
        super().__init__()

    def _get_items(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects
        """
        data = self._api_connector.get_json("https://api-web.nhle.com/v1/draft/rankings/now")
        self.items = data["rankings"]
        for item in self.items:
            item["year"] = data["draftYear"]

    def _get_data_by_item(self):
        for item in self.items:
            try:
                draft_ranking = self._serializer.deserialize(item, DraftRanking)
                self._data.append(draft_ranking)
            except ValueError as e:
                print(f"Error occurred while fetching draft ranking data (ranking: {item['firstName']}): {e}")

    def _process_data(self, data):
        pass

class FetchTeams(DataFetcher):
    """
    A class to fetch the team data from the NHL API.

    Methods
    -------
    get_teams()
        Fetches the team data from the NHL API and returns a list of team objects

    Notes
    -------
    The NHL API does not provide a direct endpoint to fetch team data. The team data is fetched from the standings data.
    But I will add all of the stat data into one team data for each team.
    """

    def __init__(self):
        super().__init__()
        self.__TEAM_ID_URL = "https://api.nhle.com/stats/rest/en/team"
        self.__ROSTER_SEASON_URL = "https://api-web.nhle.com/v1/roster-season/mtl"
        self.__TEAM_URL = "https://api-web.nhle.com/v1/standings/"
        self.__SEASON_STANDINGS_URL = "https://api-web.nhle.com/v1/standings-season/"
        self.team_id_lookup = None
        self.season_end_lookup = None

    def _get_items(self):
        """
        Fetches the team data from the NHL API and returns a list of team objects
        """
        self._get_team_id_lookup()
        self._get_season_standings()
        years = self._api_connector.get_json(self.__ROSTER_SEASON_URL)
        for year in years:
            self._process_data(year)
        

    def _get_data_by_item(self):
        for team in self._items:
            # Each season combination of every team
            try:
                team_abbrev = self._data_parser.double_parse(team, "teamAbbrev", "default", "none")
                team_id = self.__find_team_id(team_abbrev)
                team["teamId"] = team_id

                team_obj = Team(team_id)
                team_obj.team_data = self._serializer.deserialize(team, TeamData)
                team_obj.team_stats = self._serializer.deserialize(team, TeamStats)

                self._data.append(team_obj)
        
            except ValueError as e:
                print(f"Error: ", e)

    def _process_data(self, year):
        season_end = self._find_season_end(year)
        data = self._api_connector.get_json(self.__TEAM_URL + season_end)
        for team_json in data["standings"]:
            self._items.append(team_json)

    def _get_team_id_lookup(self):
        """
        Fetches and stores the team ID lookup data.
        """
        data = self._api_connector.get_json(self.__TEAM_ID_URL)
        self.team_id_lookup = data["data"]

    def _get_season_standings(self):
        data = self._api_connector.get_json(self.__SEASON_STANDINGS_URL)
        self.season_end_lookup = data["seasons"]

    def _find_season_end(self, year):
        for season in self.season_end_lookup:
            if season["id"] == year:
                return season["standingsEnd"]
        return None


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
    
class FetchTeamAdvancedStats(DataFetcher):
    def __init__(self):
        super().__init__()  
        self._team_ids = []

    def _get_items(self):
        """
        Fetches the team data from the NHL API and returns a list of team objects
        """
        query = "SELECT team_id FROM teams;"
        res = self._database_operator.read(query)
        ids = []
        for row in res:
            ids.append(row[0])
        self._items = list(set(ids))
        

    def _get_data_by_item(self):
        for team_id in self._items:
            team_obj = TeamAdvancedStats(team_id)
            
            '''days_rest_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/daysbetweengames?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsDaysRest)
            team_obj.team_advanced_stats_days_rest = days_rest_list

            corsi_fenwick_counts = self._fetch_paginated_data(f"https://api.nhle.com/stats/rest/en/team/summaryshooting?cayenneExp=teamId={team_id}")
            corsi_fenwick_percents = self._fetch_paginated_data(f"https://api.nhle.com/stats/rest/en/team/percentages?cayenneExp=teamId={team_id}")

            if len(corsi_fenwick_counts) != len(corsi_fenwick_percents):
                raise ValueError("The lengths of corsi_fenwick_counts and corsi_fenwick_percents do not match.")
            corsi_fenwick_data = zip(corsi_fenwick_counts, corsi_fenwick_percents)
            corsi_fenwick_list = []

            for counts, percents in corsi_fenwick_data:
                merged_data = {**counts, **percents}
                merged_data["teamId"] = team_id
                corsi_fenwick_obj = self._serializer.deserialize(merged_data, TeamAdvancedStatsCorsiFenwick)
                corsi_fenwick_list.append(corsi_fenwick_obj)

            team_obj.team_advanced_stats_corsi_fenwick = corsi_fenwick_list
            

            shot_type_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/shottype?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsShotType)
            team_obj.team_advanced_stats_shot_type = shot_type_list

            outshoot_outshot_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/outshootoutshotby?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsOutshootOutshot)
            team_obj.team_advanced_stats_outshoot_outshot = outshoot_outshot_list

            faceoff_percent_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/faceoffpercentages?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsFaceoffPercent)
            team_obj.team_advanced_stats_faceoff_percent = faceoff_percent_list
            count += len(shot_type_list)

            goals_by_period_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalsbyperiod?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsGoalsByPeriod)
            team_obj.team_advanced_stats_goals_by_period = goals_by_period_list

            goals_by_strength_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalsforbystrength?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsGoalsByStrength)
            team_obj.team_advanced_stats_goals_by_strength = goals_by_strength_list

            leading_trailing_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/leadingtrailing?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsLeadingTrailing)
            team_obj.team_advanced_stats_leading_trailing = leading_trailing_list

            misc_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/realtime?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsMisc)
            team_obj.team_advanced_stats_misc = misc_list

            penalties_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/penalties?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsPenalties)
            team_obj.team_advanced_stats_penalties = penalties_list'''

            url_pk = f"https://api.nhle.com/stats/rest/en/team/penaltykill?cayenneExp=teamId={team_id}"
            url_pk_time = f"https://api.nhle.com/stats/rest/en/team/penaltykilltime?cayenneExp=teamId={team_id}"
            url_pp = f"https://api.nhle.com/stats/rest/en/team/powerplay?cayenneExp=teamId={team_id}"
            url_pp_time = f"https://api.nhle.com/stats/rest/en/team/powerplaytime?cayenneExp=teamId={team_id}"

            pk_data = self._fetch_paginated_data(url_pk)
            pk_time_data = self._fetch_paginated_data(url_pk_time)
            pp_data = self._fetch_paginated_data(url_pp)
            pp_time_data = self._fetch_paginated_data(url_pp_time)

            pk_merged_data = [{**pk, **pk_time} for pk, pk_time in zip(pk_data, pk_time_data)]
            pp_merged_data = [{**pp, **pp_time} for pp, pp_time in zip(pp_data, pp_time_data)]
            pp_pk_data = zip(pk_merged_data, pp_merged_data)

            pp_pk_list = []
            for pk_data, pp_data in pp_pk_data:
                merged_data = {**pk_data, **pp_data}
                merged_data["teamId"] = team_id
                pp_pk_obj = self._serializer.deserialize(merged_data, TeamAdvancedStatsPowerplayPenaltyKill)
                pp_pk_list.append(pp_pk_obj)

            team_obj.team_advanced_stats_powerplay_penalty_kill = pp_pk_list

            scoring_first_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/scoretrailfirst?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsScoringFirst)
            
            team_obj.team_advanced_stats_scoring_first = scoring_first_list

            team_goal_games = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalgames?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsTeamGoalGames)
            team_obj.team_advanced_stats_team_goal_games = team_goal_games

            self._data.append(team_obj)

    def _process_advanced_stats_obj(self, url, team_id, obj):
        advanced_stats_list = []
        data = self._fetch_paginated_data(url)
        for advanced_stats in data:
            advanced_stats["teamId"] = team_id
            advanced_stats_obj = self._serializer.deserialize(advanced_stats, obj)
            advanced_stats_list.append(advanced_stats_obj)
  
        return advanced_stats_list
    
    def _process_data(self, data):
        pass
    