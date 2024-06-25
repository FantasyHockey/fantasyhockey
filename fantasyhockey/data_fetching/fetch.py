from abc import ABC, abstractmethod
from fantasyhockey.api.api_connector import APIConnector
from fantasyhockey.util.data_parser import DataParser
from fantasyhockey.util.util import Util
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.serializers import SerializerFactory
from fantasyhockey.data_fetching.models import *
import concurrent.futures
import time
from requests.exceptions import HTTPError
import random

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

    def __init__(self, max_workers=10, max_retries=3, backoff_factor=0.5):
        self._data = []
        self._items = []
        self._data_parser = DataParser()
        self._util = Util()
        self._database_operator = DatabaseOperator()
        self._api_connector = APIConnector()
        self._serializer = SerializerFactory.get_serializer("json")
        self.max_workers = max_workers
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

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

    def _fetch_with_retry(self, fetch_function, *args):
        retries = 0
        while retries < self.max_retries:
            try:
                return fetch_function(*args)
            except HTTPError as e:
                if e.response.status_code == 502:
                    retries += 1
                    sleep_time = self.backoff_factor * (2 ** retries) + random.uniform(0, 1)
                    time.sleep(sleep_time)
                else:
                    raise
        return None

    def _fetch_parallel(self, fetch_function, items):
        count = 0 
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_item = {executor.submit(self._fetch_with_retry, fetch_function, item): item for item in items}
            for future in concurrent.futures.as_completed(future_to_item):
                count += 1
                print(f"Processed {count} of {len(items)} items")
                item = future_to_item[future]
                result = future.result()
                if result:
                    self._data.append(result)
                else:
                    print(f"Failed to fetch data for item: {item}")

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
        self._fetch_parallel(self._fetch_season_data, self._items)

    def _fetch_season_data(self, season):
        try:
            season_obj = self._serializer.deserialize(season, Season)
            return season_obj
        except ValueError as e:
            print(f"Error occurred while fetching season data (id: {season['id']}): {e}")
            return None

    def _process_data(self, data):
        pass

class FetchDraftRankings(DataFetcher):
    """
    A class to fetch the draft ranking data from the NHL API.
    """

    def __init__(self):
        super().__init__()

    def _get_items(self):
        """
        Fetches the draft ranking data from the NHL API and returns a list of draft ranking objects.
        """
        data = self._api_connector.get_json("https://api-web.nhle.com/v1/draft/rankings/now")
        self._items = data["rankings"]
        for item in self._items:
            item["year"] = data["draftYear"]

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_draft_ranking_data, self._items)

    def _fetch_draft_ranking_data(self, item):
        try:
            draft_ranking = self._serializer.deserialize(item, DraftRanking)
            return draft_ranking
        except ValueError as e:
            print(f"Error occurred while fetching draft ranking data (ranking: {item['firstName']}): {e}")
            return None

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
        
        # Use a thread pool to fetch data in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self._process_data, year) for year in years]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Ensure exceptions are raised if any

    def _get_data_by_item(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self._fetch_team_data, team) for team in self._items]
            for future in concurrent.futures.as_completed(futures):
                team_obj = future.result()
                if team_obj is not None:
                    self._data.append(team_obj)

        # Add a null team object
        null_team_obj = Team(0)
        null_team_obj.team_data = TeamData(0)
        null_team_obj.team_data.year = 20232024
        self._data.append(null_team_obj)

        # Add temporary utah team
        utah_team_obj = Team(59)
        utah_team_obj.team_data = TeamData(59)
        utah_team_obj.team_data.team_name = "Utah"
        utah_team_obj.team_data.team_abbreviation = "UTA"
        utah_team_obj.team_data.year = 20232024
        self._data.append(utah_team_obj)

    def _fetch_team_data(self, team):
        try:
            team_abbrev = self._data_parser.double_parse(team, "teamAbbrev", "default", "none")
            team_id = self.__find_team_id(team_abbrev)
            if team_id is None:
                print(f"Team ID not found for team abbreviation: {team_abbrev}")
                return None
            team["teamId"] = team_id

            team_obj = Team(team_id)
            team_obj.team_data = self._serializer.deserialize(team, TeamData)
            team_obj.team_stats = self._serializer.deserialize(team, TeamStats)

            return team_obj
        except ValueError as e:
            print(f"Error: {e}")
            return None

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
        ids = [row[0] for row in res]
        self._items = list(set(ids))

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_team_advanced_stats_data, self._items)

    def _fetch_team_advanced_stats_data(self, team_id):
        try:
            team_obj = TeamAdvancedStats(team_id)
            
            team_obj.team_advanced_stats_days_rest = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/daysbetweengames?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsDaysRest)

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
            team_obj.team_advanced_stats_shot_type = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/shottype?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsShotType)
            team_obj.team_advanced_stats_outshoot_outshot = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/outshootoutshotby?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsOutshootOutshot)
            team_obj.team_advanced_stats_faceoff_percent = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/faceoffpercentages?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsFaceoffPercent)
            team_obj.team_advanced_stats_goals_by_period = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalsbyperiod?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsGoalsByPeriod)
            team_obj.team_advanced_stats_goals_by_strength = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalsforbystrength?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsGoalsByStrength)
            team_obj.team_advanced_stats_leading_trailing = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/leadingtrailing?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsLeadingTrailing)
            team_obj.team_advanced_stats_misc = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/realtime?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsMisc)
            team_obj.team_advanced_stats_penalties = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/penalties?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsPenalties)
            
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
            team_obj.team_advanced_stats_scoring_first = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/scoretrailfirst?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsScoringFirst)
            team_obj.team_advanced_stats_team_goal_games = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/goalgames?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsTeamGoalGames)

            return team_obj
        except Exception as e:
            print(f"Error occurred while fetching team advanced stats data (team_id: {team_id}): {e}")
            return None

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


class FetchPlayers(DataFetcher):
    def __init__(self, active_only=False):
        super().__init__()
        self.__player_ids = set()
        self._active_only = active_only

    def _get_items(self):
        if self._active_only:
            query = "SELECT p.id FROM players p JOIN player_details pd ON p.id = pd.id\
                     WHERE pd.position != 'G' AND p.is_active = 1;"
            res = self._database_operator.read(query)
            ids = [row[0] for row in res]
            self._items = ids
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                teams = self._fetch_team_ids()
                futures = [executor.submit(self.__fetch_players_for_team, team[0], team[1]) for team in teams]
                for future in concurrent.futures.as_completed(futures):
                    future.result()  # Ensure exceptions are raised if any

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_player_data, self.__player_ids)

    def _fetch_player_data(self, player_id):
        try:
            json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{player_id}/landing")
            player = Player(player_id)
            team_id = self._data_parser.parse(json, "currentTeamId", "none")
            player.team_id = team_id if team_id != "none" else None
            player.is_active = self._data_parser.parse(json, "isActive", "none")

            player.player_details = self._serializer.deserialize(json, PlayerDetails)
            player_draft_json = self._data_parser.parse(json, "draftDetails", "empty_dict")
            player_draft_json["playerId"] = player_id
            player.player_draft = self._serializer.deserialize(player_draft_json, PlayerDraft)

            player_awards = self._data_parser.parse(json, "awards", "empty_list")
            player.player_awards = [self._serializer.deserialize(award, PlayerAwards) for award in self._parse_awards(player_awards, player_id)]

            return player
        except Exception as e:
            print(f"Error occurred while fetching player data (id: {player_id}): {e}")
            return None

    def _parse_awards(self, player_awards, player_id):
        player_awards_list = []

        for award in player_awards:
            for season in self._data_parser.parse(award, "seasons", "empty_list"):
                award_json = {
                    "playerId": player_id,
                    "trophy": self._data_parser.double_parse(award, "trophy", "default"),
                    "seasonId": self._data_parser.parse(season, "seasonId")
                }
                player_awards_list.append(award_json)

        return player_awards_list

    def _process_data(self, data):
        pass

    def _fetch_team_ids(self):
        query = "SELECT team_abbreviation, year FROM teams;"
        res = self._database_operator.read(query)
        return [[row[0], row[1]] for row in res]
    
    def __fetch_players_for_team(self, team_abbrev, year):
        """Fetch players for a given team."""
        players = self._api_connector.get_json(f"https://api-web.nhle.com/v1/roster/{team_abbrev}/{year}")

        try:
            forwards = self._data_parser.parse(players, "forwards", "empty_list")
            defensemen = self._data_parser.parse(players, "defensemen", "empty_list")
            goalies = self._data_parser.parse(players, "goalies", "empty_list")
            
            for player in forwards + defensemen + goalies:
                try:
                    self.__player_ids.add(self._data_parser.parse(player, "id", "error"))
                except KeyError:
                    print(f"Error parsing a player id from team {team_abbrev}, year {year}")
        except KeyError:
            print(f"Error parsing players from team {team_abbrev}, year {year}")

class FetchSkaters(DataFetcher):
    def __init__(self, active_only=False):
        super().__init__()
        self._active_only = active_only

    def _get_items(self):
        if self._active_only:
            query = "SELECT p.id FROM players p JOIN player_details pd ON p.id = pd.id\
                     WHERE pd.position != 'G' AND p.is_active = 1;"
        else:
            query = "SELECT id FROM player_details WHERE position != 'G';"
        res = self._database_operator.read(query)
        ids = [row[0] for row in res]
        self._items = ids

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_skater_data, self._items)

    def fetch_single_skater(self, skater_id):
        try:
            skater = self._fetch_skater_data(skater_id)
            return skater
        except Exception as e:
            print(f"Error occurred while fetching skater data (id: {skater_id}): {e}")
            return None

    def _fetch_skater_data(self, skater_id):
        try:
            skater = Skater(skater_id)
            skater_stats = self._data_parser.parse(self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{skater_id}/landing"), "seasonTotals", "empty_list")
            nhl_seasons, youth_seasons = self._parse_skater_stats(skater_stats, skater_id)
            skater.skater_stats = nhl_seasons
            skater.youth_stats = youth_seasons

            skater.advanced_stats_faceoffs = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/faceoffwins?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsFaceoffs)
            skater.advanced_stats_goals = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/goalsForAgainst?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsGoals)
            skater.advanced_stats_misc = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/realtime?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsMisc)
            skater.advanced_stats_penalties = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/penalties?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPenalties)
            skater.advanced_stats_penalty_kill = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/penaltykill?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPenaltyKill)
            skater.advanced_stats_powerplay = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/powerplay?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPowerplay)
            skater.advanced_stats_scoring = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/shottype?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsScoring)
            skater.advanced_stats_shootout = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/shootout?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsShootout)
            skater.advanced_stats_toi = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/timeonice?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsTOI)

            corsi_fenwick_counts = self._fetch_paginated_data(f"https://api.nhle.com/stats/rest/en/skater/summaryshooting?cayenneExp=playerId={skater_id}")
            corsi_fenwick_percents = self._fetch_paginated_data(f"https://api.nhle.com/stats/rest/en/skater/percentages?cayenneExp=playerId={skater_id}")

            if len(corsi_fenwick_counts) != len(corsi_fenwick_percents):
                raise ValueError("The lengths of corsi_fenwick_counts and corsi_fenwick_percents do not match.")
            corsi_fenwick_data = zip(corsi_fenwick_counts, corsi_fenwick_percents)
            corsi_fenwick_list = []

            for counts, percents in corsi_fenwick_data:
                merged_data = {**counts, **percents}
                corsi_fenwick_obj = self._serializer.deserialize(merged_data, SkaterAdvancedStatsCorsiFenwick)
                corsi_fenwick_list.append(corsi_fenwick_obj)

            skater.advanced_stats_corsi_fenwick = corsi_fenwick_list

            return skater
        except Exception as e:
            print(f"Error occurred while fetching skater data (id: {skater_id}): {e}")
            return None

    def _process_data(self, data):
        pass

    def _process_advanced_stats_obj(self, url, obj):
        advanced_stats_list = []
        data = self._fetch_paginated_data(url)
        for advanced_stats in data:
            advanced_stats_obj = self._serializer.deserialize(advanced_stats, obj)
            advanced_stats_list.append(advanced_stats_obj)
        return advanced_stats_list
        
    def _parse_skater_stats(self, skater_stats, player_id):
        stat_seasons = []
        youth_seasons = []

        for season in skater_stats:
            season["playerId"] = player_id
            if season["leagueAbbrev"] != "NHL":
                youth_season = self._serializer.deserialize(season, YouthSkaterStats)
                youth_seasons.append(youth_season)
            else:
                nhl_season = self._serializer.deserialize(season, SkaterStats)
                stat_seasons.append(nhl_season)

        return stat_seasons, youth_seasons
    
class FetchGoalies(DataFetcher):
    def __init__(self, active_only=False):
        super().__init__()
        self._active_only = active_only

    def _get_items(self):
        if self._active_only:
            query = "SELECT p.id FROM players p JOIN player_details pd ON p.id = pd.id\
                     WHERE pd.position = 'G' AND p.is_active = 1;"
        else:
            query = "SELECT id FROM player_details WHERE position = 'G';"
        res = self._database_operator.read(query)
        ids = [row[0] for row in res]
        self._items = ids

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_goalie_data, self._items)

    def _fetch_goalie_data(self, goalie_id):
        try:
            goalie = Goalie(goalie_id)
            goalie_stats = self._data_parser.parse(self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{goalie_id}/landing"), "seasonTotals", "empty_list")
            nhl_seasons, youth_seasons = self._parse_goalie_stats(goalie_stats, goalie_id)
            goalie.goalie_stats = nhl_seasons
            goalie.goalie_youth_stats = youth_seasons

            goalie.goalie_advanced_stats_days_rest = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/daysrest?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsDaysRest)
            goalie.goalie_advanced_stats = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/advanced?cayenneExp=playerId={goalie_id}", GoalieAdvancedStats)
            goalie.goalie_advanced_stats_start_relieved = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/startedVsRelieved?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsStartRelieved)
            goalie.goalie_advanced_stats_shootout = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/shootout?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsShootout)
            goalie.goalie_advanced_stats_saves_by_strength = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/savesByStrength?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsSavesByStrength)
            goalie.goalie_advanced_stats_penalty_shots = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/penaltyShots?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsPenaltyShots)

            return goalie
        except Exception as e:
            print(f"Error occurred while fetching goalie data (id: {goalie_id}): {e}")
            return None

    def _process_data(self, data):
        pass

    def _parse_goalie_stats(self, goalie_stats, player_id):
        stat_seasons = []
        youth_seasons = []

        for season in goalie_stats:
            season["playerId"] = player_id
            if season["leagueAbbrev"] != "NHL":
                youth_season = self._serializer.deserialize(season, GoalieYouthStats)
                youth_seasons.append(youth_season)
            else:
                nhl_season = self._serializer.deserialize(season, GoalieStats)
                stat_seasons.append(nhl_season)

        return stat_seasons, youth_seasons

    def _process_advanced_stats_obj(self, url, obj):
        advanced_stats_list = []
        data = self._fetch_paginated_data(url)
        for advanced_stats in data:
            advanced_stats_obj = self._serializer.deserialize(advanced_stats, obj)
            advanced_stats_list.append(advanced_stats_obj)
        return advanced_stats_list
    
    
class FetchGames(DataFetcher):
    def __init__(self):
        super().__init__()
        self._items = []

    def _get_items(self):
        abbrevs = self._get_team_abbrevs()
        game_ids = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {executor.submit(self._fetch_game_ids, team_abbrev, year): (team_abbrev, year) for team_abbrev, year in abbrevs}
            for future in concurrent.futures.as_completed(future_to_url):
                data = future.result()
                if data:
                    game_ids.extend(data)

        self._items = list(set(game_ids))

    def _fetch_game_ids(self, team_abbrev, year):
        url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_abbrev}/{year}"
        data = self._api_connector.get_json(url)
        if "currentSeason" not in data:
            return []
        return [game["id"] for game in data["games"]]

    def _get_data_by_item(self):
        self._fetch_parallel(self._fetch_game_data, self._items)
        return self._items

    def _fetch_game_data(self, game_id):
        play_by_play_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play")
        landing_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/landing")
        
        game = self._serializer.deserialize(play_by_play_json, Games)
        game.game_three_stars = self._serializer.deserialize(play_by_play_json, GameThreeStars)
        game.game_skater_stats, game.game_goalie_stats = self._process_player_stats(play_by_play_json)
        game.game_roster = self._process_roster(play_by_play_json)
        game.game_referees = self._process_refs(play_by_play_json)
        game.game_scoreboard = self._process_scoreboard(play_by_play_json)
        game.game_boxscore = self._process_boxscore(play_by_play_json)
        game.game_goals = self._process_goals(landing_json)
        game.game_plays = self._process_plays(play_by_play_json)
        game.game_shifts = self._process_shifts(self._api_connector.get_json(f"https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={game_id}"), game_id)

        return game
    
    def _process_player_stats(self, boxscore_json):
        teams = self._data_parser.parse(boxscore_json, "playerByGameStats", "empty_list")
        game_id = self._data_parser.parse(boxscore_json, "id", "none")
        home_id = self._data_parser.double_parse(boxscore_json, "homeTeam", "id", "none")
        away_id = self._data_parser.double_parse(boxscore_json, "awayTeam", "id", "none")

        skater_stats = []
        goalie_stats = []
        away_forwards = self._data_parser.double_parse(teams, "awayTeam", "forwards", "empty_list")
        away_defense = self._data_parser.double_parse(teams, "awayTeam", "defense", "empty_list")
        away_goalies = self._data_parser.double_parse(teams, "awayTeam", "goalies", "empty_list")
        home_forwards = self._data_parser.double_parse(teams, "homeTeam", "forwards", "empty_list")
        home_defensemen = self._data_parser.double_parse(teams, "homeTeam", "defense", "empty_list")
        home_goalies = self._data_parser.double_parse(teams, "homeTeam", "goalies", "empty_list")
        
        for away_forward in away_forwards:
            away_forward["gameId"] = game_id
            away_forward["teamId"] = away_id
            skater_stats.append(self._serializer.deserialize(away_forward, GameSkaterStats))

        for away_defenseman in away_defense:
            away_defenseman["gameId"] = game_id
            away_defenseman["teamId"] = away_id
            skater_stats.append(self._serializer.deserialize(away_defenseman, GameSkaterStats))

        for away_goalie in away_goalies:
            away_goalie["gameId"] = game_id
            away_goalie["teamId"] = away_id
            goalie_stats.append(self._serializer.deserialize(away_goalie, GameGoalieStats))

        for home_forward in home_forwards:
            home_forward["gameId"] = game_id
            home_forward["teamId"] = home_id
            skater_stats.append(self._serializer.deserialize(home_forward, GameSkaterStats))

        for home_defenseman in home_defensemen:
            home_defenseman["gameId"] = game_id
            home_defenseman["teamId"] = home_id
            skater_stats.append(self._serializer.deserialize(home_defenseman, GameSkaterStats))

        for home_goalie in home_goalies:
            home_goalie["gameId"] = game_id
            home_goalie["teamId"] = home_id
            goalie_stats.append(self._serializer.deserialize(home_goalie, GameGoalieStats))

        return skater_stats, goalie_stats

    def _process_roster(self, play_by_play_json):
        roster = []
        for roster_spot in self._data_parser.parse(play_by_play_json, "rosterSpots", "empty_list"):
            game_id = self._data_parser.parse(play_by_play_json, "id", "none")
            roster_spot["gameId"] = game_id
            roster_obj = self._serializer.deserialize(roster_spot, GameRoster)
            roster.append(roster_obj)
        
        return roster

    def _process_refs(self, play_by_play_json):
        refs = {}
        game_info = self._data_parser.double_parse(play_by_play_json, "summary", "gameInfo", "empty_dict")
        referees = self._data_parser.parse(game_info, "referees", "empty_list")
        linesmen = self._data_parser.parse(game_info, "linesmen", "empty_list")
        game_id = self._data_parser.parse(play_by_play_json, "id", "none")
        refs["gameId"] = game_id
        try:
            if len(referees) == 1:
                refs["referee1Name"] = referees[0]["default"]
                refs["referee2Name"] = None
            elif len(referees) == 2:
                refs["referee1Name"] = referees[0]["default"]
                refs["referee2Name"] = referees[1]["default"]

            if len(linesmen) == 1:
                refs["linesman1Name"] = linesmen[0]["default"]
                refs["linesman2Name"] = None
            elif len(referees) == 2:
                refs["linesman1Name"] = linesmen[0]["default"]
                refs["linesman2Name"] = linesmen[1]["default"]
        except IndexError: 
            refs["referee1Name"] = None
            refs["referee2Name"] = None
            refs["linesman1Name"] = None
            refs["linesman2Name"] = None

        refs_obj = self._serializer.deserialize(refs, Referees)
        return refs_obj

    def _process_scoreboard(self, play_by_play_json):
        scoreboard_json = {}
        game_id = self._data_parser.parse(play_by_play_json, "id")
        clock = self._data_parser.parse(play_by_play_json, "clock", "empty_dict")
        home_team = self._data_parser.parse(play_by_play_json, "homeTeam", "empty_dict")
        away_team = self._data_parser.parse(play_by_play_json, "awayTeam", "empty_dict")
        period = self._data_parser.double_parse(play_by_play_json, "periodDescriptor", "number", "none")
        scoreboard_json['timeRemaining'] = self._data_parser.parse(clock, "timeRemaining", "none")
        scoreboard_json['secondsRemaining'] = self._data_parser.parse(clock, "secondsRemaining", "none")
        scoreboard_json['running'] = self._data_parser.parse(clock, "running", "none")
        scoreboard_json['inIntermission'] = self._data_parser.parse(clock, "inIntermission", "none")
        scoreboard_json['gameId'] = game_id
        scoreboard_json['homeScore'] = self._data_parser.parse(home_team, "score", "none")
        scoreboard_json['awayScore'] = self._data_parser.parse(away_team, "score", "none")
        scoreboard_json['homeShots'] = self._data_parser.parse(home_team, "sog", "none")
        scoreboard_json['awayShots'] = self._data_parser.parse(away_team, "sog", "none")
        scoreboard_json['period'] = period

        scoreboard_obj = self._serializer.deserialize(scoreboard_json, GameScoreboard)
        return scoreboard_obj

    def _process_boxscore(self, data):
        game_id = self._data_parser.parse(data, "id")
        home_team_id = self._data_parser.double_parse(data, "homeTeam", "id", "none")
        home_score = self._data_parser.double_parse(data, "homeTeam", "score", "none")
        away_team_id = self._data_parser.double_parse(data, "awayTeam", "id", "none")
        away_score = self._data_parser.double_parse(data, "awayTeam", "score", "none")
        boxscore_json = {}
        boxscore_json["gameId"] = game_id
        boxscore_json["homeTeamId"] = home_team_id
        boxscore_json["homeGoals"] = home_score
        boxscore_json["awayTeamId"] = away_team_id
        boxscore_json["awayGoals"] = away_score

        for stat in self._data_parser.double_parse(data, "summary", "teamGameStats", "empty_list"):
            dict_key = stat["category"]
            boxscore_json["home" + dict_key] = stat["homeValue"]
            boxscore_json["away" + dict_key] = stat["awayValue"]

        boxscore_obj = self._serializer.deserialize(boxscore_json, GameBoxscore)
        return boxscore_obj
    
    def _process_plays(self, play_by_play_json):
        plays = []
        game_id = self._data_parser.parse(play_by_play_json, "id")
        for play in self._data_parser.parse(play_by_play_json, "plays", "empty_list"):
            play["gameId"] = game_id
            play["periodNumber"] = self._data_parser.double_parse(play, "periodDescriptor", "number", "none")
            play["periodType"] = self._data_parser.double_parse(play, "periodDescriptor", "periodType", "none")
            play["xCoord"] = self._data_parser.double_parse(play, "details", "xCoord", "none")
            play["yCoord"] = self._data_parser.double_parse(play, "details", "yCoord", "none")
            play["zoneCode"] = self._data_parser.double_parse(play, "details", "zoneCode", "none")
            play["shotType"] = self._data_parser.double_parse(play, "details", "shotType", "none")
            play["reason"] = self._data_parser.double_parse(play, "details", "reason", "none")
            play["teamId"] = self._data_parser.double_parse(play, "details", "eventOwnerTeamId", "none")
            play["descKey"] = self._data_parser.double_parse(play, "details", "descKey", "none")
            play["duration"] = self._data_parser.double_parse(play, "details", "duration", "none")

            play_key = play["typeDescKey"]
            owner_player_id = None
            receiving_player_id = None
            assist_1_player_id = None
            assist_2_player_id = None
            if play_key == "faceoff":
                owner_player_id = self._data_parser.double_parse(play, "details", "winningPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "losingPlayerId", "none")
            elif play_key == "hit":
                owner_player_id = self._data_parser.double_parse(play, "details", "hittingPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "hitteePlayerId", "none")
            elif play_key == "blocked-shot":
                owner_player_id = self._data_parser.double_parse(play, "details", "blockingPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "shootingPlayerId", "none")
            elif play_key == "takeaway":
                owner_player_id = self._data_parser.double_parse(play, "details", "playerId", "none")
                receiving_player_id = None
            elif play_key == "giveaway":
                owner_player_id = self._data_parser.double_parse(play, "details", "playerId", "none")
                receiving_player_id = None
            elif play_key == "shot-on-goal" or play_key == "missed-shot":
                owner_player_id = self._data_parser.double_parse(play, "details", "shootingPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "goalieInNetId", "none")
            elif play_key == "penalty":
                owner_player_id = self._data_parser.double_parse(play, "details", "committedByPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "drawnByPlayerId", "none")
            elif play_key == "goal":
                owner_player_id = self._data_parser.double_parse(play, "details", "scoringPlayerId", "none")
                receiving_player_id = self._data_parser.double_parse(play, "details", "goalieInNetId", "none")
                assist_1_player_id = self._data_parser.double_parse(play, "details", "assist1PlayerId", "none")
                assist_2_player_id = self._data_parser.double_parse(play, "details", "assist2PlayerId", "none")

            play["ownerPlayerId"] = owner_player_id
            play["receivingPlayerId"] = receiving_player_id
            play["assist1PlayerId"] = assist_1_player_id
            play["assist2PlayerId"] = assist_2_player_id

            play_obj = self._serializer.deserialize(play, GamePlays)

            plays.append(play_obj)

        return plays
    
    def _process_shifts(self, shift_json, game_id):
        shifts = []
        for shift in shift_json['data']:
            shift["gameId"] = game_id
            shift_obj = self._serializer.deserialize(shift, ShiftData)
            shifts.append(shift_obj)

        return shifts
            
    def _process_data(self, data):
        pass

    def _process_goals(self, data):
        goals = []
        game_id = self._data_parser.parse(data, "id")
        goals_json = self._data_parser.double_parse(data, "summary", "scoring", "empty_list")
        for period_num in range(len(self._data_parser.double_parse(data, "summary", "scoring", "empty_list"))):
            period = goals_json[period_num]["periodDescriptor"]["number"]
            period_goals = goals_json[period_num]
            for goal in period_goals["goals"]:
                goal["gameId"] = game_id
                goal["period"] = period
                team_abbrev = self._data_parser.double_parse(goal, "teamAbbrev", "default", "none")
                leading_team_abbrev = self._data_parser.double_parse(goal, "leadingTeamAbbrev", "default", "none")
                goal["teamId"] = self._util.get_team_id_from_abbrev(team_abbrev)
                goal["leadingTeamId"] = self._util.get_team_id_from_abbrev(leading_team_abbrev)
                assist1 = None
                assist2 = None
                if len(goal["assists"]) == 2:
                    assist1 = goal["assists"][0]["playerId"]
                    assist2 = goal["assists"][1]["playerId"]
                elif len(goal["assists"]) == 1:
                    assist1 = goal["assists"][0]["playerId"]

                goal["assist1PlayerId"] = assist1
                goal["assist2PlayerId"] = assist2

                goal_obj = self._serializer.deserialize(goal, GameGoals)    

                goals.append(goal_obj)

        return goals

    def _get_team_abbrevs(self):
        query = """SELECT team_abbreviation, year FROM teams ;"""
        res = self._database_operator.read(query)
        abbrevs = []
        print(len(res))
        for row in res:
            abbrev = row[0]
            year = row[1]
            if abbrev == None:
                continue
            if 0 < year <= 19301931:
                abbrevs.append((row[0], row[1]))

        return abbrevs

    def _fetch_single_game(self, game_id):
        play_by_play_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play")
        landing_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/landing")
        
        game = self._serializer.deserialize(play_by_play_json, Games)
        game.game_three_stars = self._serializer.deserialize(play_by_play_json, GameThreeStars)
        game.game_skater_stats, game.game_goalie_stats = self._process_player_stats(play_by_play_json)
        game.game_roster = self._process_roster(play_by_play_json)
        game.game_referees = self._process_refs(play_by_play_json)
        game.game_scoreboard = self._process_scoreboard(play_by_play_json)
        game.game_boxscore = self._process_boxscore(play_by_play_json)
        game.game_goals = self._process_goals(landing_json)
        game.game_plays = self._process_plays(play_by_play_json)
        game.game_shifts = self._process_shifts(self._api_connector.get_json(f"https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={game_id}"), game_id)

        return game