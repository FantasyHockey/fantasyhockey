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
                if team_id is None:
                    print(f"Team ID not found for team abbreviation: {team_abbrev}")
                    continue
                team["teamId"] = team_id

                team_obj = Team(team_id)
                team_obj.team_data = self._serializer.deserialize(team, TeamData)
                team_obj.team_stats = self._serializer.deserialize(team, TeamStats)

                self._data.append(team_obj)
        
            except ValueError as e:
                print(f"Error: ", e)

        # Add a null team object
        null_team_obj = Team(0)
        null_team_obj.team_data = TeamData(0)
        null_team_obj.team_data.year = 20232024
        self._data.append(null_team_obj)

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
            
            days_rest_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/team/daysbetweengames?cayenneExp=teamId={team_id}", team_id, TeamAdvancedStatsDaysRest)
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
            team_obj.team_advanced_stats_penalties = penalties_list

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
            ids = []
            for row in res:
                ids.append(row[0])

            self._items = ids
        else:
            for team in self._fetch_team_ids():
                self.__fetch_players_for_team(team[0], team[1])

    def _get_data_by_item(self):
        count = 0
        player_ids = list(self.__player_ids)  # Convert set to list
        for player_id in player_ids:
            count += 1
            print(f"Fetching player {player_id} - {count} of {len(player_ids)}")
            json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{player_id}/landing")
            player = Player(player_id)
            if "currentTeamId" not in json:
                team_id = None
            else:
                team_id = self._data_parser.parse(json, "currentTeamId", "error")
            player.team_id = team_id
            is_active = self._data_parser.parse(json, "isActive", "error")
            player.is_active = is_active

            player_details = self._serializer.deserialize(json, PlayerDetails)
            player.player_details = player_details

            player_draft_json = self._data_parser.parse(json, "draftDetails", "empty_dict")
            player_draft_json["playerId"] = player_id
            player_draft = self._serializer.deserialize(player_draft_json, PlayerDraft)
            player.player_draft = player_draft

            player_awards = self._data_parser.parse(json, "awards", "empty_list")
            player_awards_list = self._parse_awards(player_awards, player_id)
            player_awards_list = [self._serializer.deserialize(award, PlayerAwards) for award in player_awards_list]
            player.player_awards = player_awards_list

            self._data.append(player)
            
        default_player = Player(0)
        default_player.team_id = 0
        default_player.is_active = 0

        self._data.append(default_player)


    def _parse_awards(self, player_awards, player_id):
        player_awards_list = []

        for award in player_awards:
            for season in self._data_parser.parse(award, "seasons", "empty_list"):
                award_json = {}
                award_json["playerId"] = player_id
                award_json["trophy"] = self._data_parser.double_parse(award, "trophy", "default")
                award_json["seasonId"] = self._data_parser.parse(season, "seasonId")
                player_awards_list.append(award_json)

        return player_awards_list
    
    def _process_data(self, data):
        pass

    def _fetch_team_ids(self):
        query = "SELECT team_abbreviation, year FROM teams;"
        res = self._database_operator.read(query)
        teams = []
        for row in res:
            teams.append([row[0], row[1]])
        
        return teams
    
    def __fetch_players_for_team(self, team_abbrev, year):
        """Fetch players for a given team."""
        players = self._api_connector.get_json(f"https://api-web.nhle.com/v1/roster/{team_abbrev}/{year}")

        try:
            forwards = self._data_parser.parse(players, "forwards", "empty_list")
            for player in forwards:
                try:
                    self.__player_ids.add(self._data_parser.parse(player, "id", "error"))
                except KeyError:
                    print("Error parsing a player id from the forwards from team id: ", team_abbrev, " year: ", year)
                    continue

            defensemen = self._data_parser.parse(players, "defensemen", "empty_list")
            for player in defensemen:
                try:
                    self.__player_ids.add(self._data_parser.parse(player, "id", "error"))
                except KeyError:
                    print("Error parsing a player id from the defensemen from team id: ", team_abbrev, " year: ", year)
                    continue

            goalies = self._data_parser.parse(players, "goalies", "empty_list")
            for player in goalies:
                try:
                    self.__player_ids.add(self._data_parser.parse(player, "id", "error"))
                except KeyError:
                    print("Error parsing a player id from the goalies from team id: ", team_abbrev, " year: ", year)
                    continue
        except KeyError:
            print("Error parsing players from team id: ", team_abbrev, " year: ", year)
            return
        
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
        ids = []
        for row in res:
            ids.append(row[0])

        self._items = ids
            

    def _get_data_by_item(self):
        count = 0
        for skater_id in self._items:
            count += 1
            print(f"Fetching skater {skater_id} - {count} of {len(self._items)}")
            skater = Skater(skater_id)
            skater_stats = self._data_parser.parse(self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{skater_id}/landing"), "seasonTotals", "empty_list")
            nhl_seasons, youth_seasons = self._parse_skater_stats(skater_stats, skater_id)
            skater.skater_stats = nhl_seasons
            skater.youth_stats = youth_seasons

            faceoff_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/faceoffwins?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsFaceoffs)
            skater.advanced_stats_faceoffs = faceoff_list

            goals_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/goalsForAgainst?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsGoals)
            skater.advanced_stats_goals = goals_list

            misc_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/realtime?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsMisc)
            skater.advanced_stats_misc = misc_list

            penalties_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/penalties?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPenalties)
            skater.advanced_stats_penalties = penalties_list

            penalty_kill_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/penaltykill?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPenaltyKill)
            skater.advanced_stats_penalty_kill = penalty_kill_list

            powerplay_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/powerplay?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsPowerplay)
            skater.advanced_stats_powerplay = powerplay_list

            scoring_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/shottype?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsScoring)
            skater.advanced_stats_scoring = scoring_list

            shootout_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/shootout?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsShootout)
            skater.advanced_stats_shootout = shootout_list

            toi_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/skater/timeonice?cayenneExp=playerId={skater_id}", SkaterAdvancedStatsTOI)
            skater.advanced_stats_toi = toi_list

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

            self._data.append(skater)

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
        ids = []
        for row in res:
            ids.append(row[0])

        self._items = ids

    def _get_data_by_item(self):
        count = 0
        for goalie_id in self._items:
            count += 1
            print(f"Fetching goalie {goalie_id} - {count} of {len(self._items)}")
            goalie = Goalie(goalie_id)
            goalie_stats = self._data_parser.parse(self._api_connector.get_json(f"https://api-web.nhle.com/v1/player/{goalie_id}/landing"), "seasonTotals", "empty_list")
            nhl_seasons, youth_seasons = self._parse_goalie_stats(goalie_stats, goalie_id)
            goalie.goalie_stats = nhl_seasons
            goalie.goalie_youth_stats = youth_seasons

            days_rest_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/daysrest?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsDaysRest)
            goalie.goalie_advanced_stats_days_rest = days_rest_list

            advanced_stats_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/advanced?cayenneExp=playerId={goalie_id}", GoalieAdvancedStats)
            goalie.goalie_advanced_stats = advanced_stats_list

            start_relieved_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/startedVsRelieved?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsStartRelieved)
            goalie.goalie_advanced_stats_start_relieved = start_relieved_list

            shootout_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/shootout?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsShootout)
            goalie.goalie_advanced_stats_shootout = shootout_list

            saves_by_strength = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/savesByStrength?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsSavesByStrength)
            goalie.goalie_advanced_stats_saves_by_strength = saves_by_strength

            penalty_shots_list = self._process_advanced_stats_obj(f"https://api.nhle.com/stats/rest/en/goalie/penaltyShots?cayenneExp=playerId={goalie_id}", GoalieAdvancedStatsPenaltyShots)
            goalie.goalie_advanced_stats_penalty_shots = penalty_shots_list

            self._data.append(goalie)


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

    def _get_items(self, year=None):
        abbrevs = self._get_team_abbrevs()
        game_ids = []

        for team_abbrev, year in abbrevs[:1]:
            url = f"https://api-web.nhle.com/v1/club-schedule-season/{team_abbrev}/{year}"
            print(url)
            data = self._api_connector.get_json(url)
            if "currentSeason" not in data:
                continue

            for game in data["games"]:
                game_ids.append(game["id"])

        self._items = list(set(game_ids))


    def _get_data_by_item(self):
        count = 0
        for game_id in self._items:
            count += 1
            print(f"Fetching game {game_id} - {count} of {len(self._items)}")
            game_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/landing")
            game = self._serializer.deserialize(game_json, Games)

            star_obj = self._serializer.deserialize(game_json, GameThreeStars)
            game.game_three_stars = star_obj

            boxscore_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/boxscore")
            skater_stats_list, goalie_stats_list = self._process_player_stats(boxscore_json)

            game.game_skater_stats = skater_stats_list
            game.game_goalie_stats = goalie_stats_list


            play_by_play_json = self._api_connector.get_json(f"https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play")
            game_roster_obj = self._process_roster(play_by_play_json)
            game.game_roster = game_roster_obj

            refs_obj = self._process_refs(play_by_play_json)
            game.game_referees = refs_obj

            scoreboard_obj = self._process_scoreboard(play_by_play_json)
            game.game_scoreboard = scoreboard_obj

            boxscore_obj = self._serializer.deserialize(boxscore_json, GameBoxscore)
            game.game_boxscore = boxscore_obj

            self._data.append(game)

    def _process_player_stats(self, boxscore_json):
        teams = self._data_parser.parse(boxscore_json, "playerByGameStats", "empty_list")
        game_id = self._data_parser.parse(boxscore_json, "id")
        home_id = self._data_parser.double_parse(boxscore_json, "homeTeam", "id")
        away_id = self._data_parser.double_parse(boxscore_json, "awayTeam", "id")

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
            game_id = self._data_parser.parse(play_by_play_json, "id")
            roster_spot["gameId"] = game_id
            roster_obj = self._serializer.deserialize(roster_spot, GameRoster)
            roster.append(roster_obj)
        
        return roster

    def _process_refs(self, play_by_play_json):
        refs = {}
        game_info = self._data_parser.double_parse(play_by_play_json, "summary", "gameInfo", "empty_dict")
        referees = self._data_parser.parse(game_info, "referees", "empty_list")
        linesmen = self._data_parser.parse(game_info, "linesmen", "empty_list")
        game_id = self._data_parser.parse(play_by_play_json, "id")
        refs["gameId"] = game_id
        if len(referees) != 2:
            refs["referee1Name"] = referees[0]["default"]
            refs["referee2Name"] = None
        else:
            refs["referee1Name"] = referees[0]["default"]
            refs["referee2Name"] = referees[1]["default"]

        if len(linesmen) != 2:
            refs["linesman1Name"] = linesmen[0]["default"]
            refs["linesman2Name"] = None
        else:
            refs["linesman1Name"] = linesmen[0]["default"]
            refs["linesman2Name"] = linesmen[1]["default"]

        refs_obj = self._serializer.deserialize(refs, Referees)
        return refs_obj

    def _process_scoreboard(self, play_by_play_json):
        scoreboard_json = {}
        game_id = self._data_parser.parse(play_by_play_json, "id")
        clock = self._data_parser.parse(play_by_play_json, "clock", "empty_dict")
        home_team = self._data_parser.parse(play_by_play_json, "homeTeam", "empty_dict")
        away_team = self._data_parser.parse(play_by_play_json, "awayTeam", "empty_dict")
        period = self._data_parser.double_parse(play_by_play_json, "periodDescriptor", "number")
        scoreboard_json['timeRemaining'] = self._data_parser.parse(clock, "timeRemaining")
        scoreboard_json['secondsRemaining'] = self._data_parser.parse(clock, "secondsRemaining")
        scoreboard_json['running'] = self._data_parser.parse(clock, "running")
        scoreboard_json['inIntermission'] = self._data_parser.parse(clock, "inIntermission")
        scoreboard_json['gameId'] = game_id
        scoreboard_json['homeScore'] = self._data_parser.parse(home_team, "score")
        scoreboard_json['awayScore'] = self._data_parser.parse(away_team, "score")
        scoreboard_json['homeShots'] = self._data_parser.parse(home_team, "sog")
        scoreboard_json['awayShots'] = self._data_parser.parse(away_team, "sog")
        scoreboard_json['period'] = period

        scoreboard_obj = self._serializer.deserialize(scoreboard_json, GameScoreboard)
        return scoreboard_obj

    def _process_boxscore(self, boxscore_json):
        game_id = self._data_parser.parse(boxscore_json, "id")
        home_team_id = self._data_parser.double_parse(boxscore_json, "homeTeam", "id")
        home_score = self._data_parser.double_parse(boxscore_json, "homeTeam", "score")
        away_team_id = self._data_parser.double_parse(boxscore_json, "awayTeam", "id")
        away_score = self._data_parser.double_parse(boxscore_json, "awayTeam", "score")
        boxscore_json = {}
        boxscore_json["gameId"] = game_id
        boxscore_json["homeTeamId"] = home_team_id
        boxscore_json["homeScore"] = home_score
        boxscore_json["awayTeamId"] = away_team_id
        boxscore_json["awayScore"] = away_score


        for stat in self._data_parser.parse(boxscore_json, "teamGameStats", "empty_list"):
            dict_key = stat["category"]
            boxscore_json["home" + dict_key] = stat["homeValue"]
            boxscore_json["away" + dict_key] = stat["awayValue"]

        boxscore_obj = self._serializer.deserialize(boxscore_json, GameBoxscore)
        return boxscore_obj
    




            
    def _process_data(self, data):
        pass

    def _get_team_abbrevs(self):
        query = """SELECT team_abbreviation, year FROM teams;"""
        res = self._database_operator.read(query)
        abbrevs = []
        for row in res:
            abbrev = row[0]
            year = row[1]
            if abbrev == None:
                continue
            abbrevs.append((row[0], row[1]))

        return abbrevs

class FetchShiftData(DataFetcher):
    def __init__(self):
        super().__init__()

    def _get_items(self):
        pass

    def _get_data_by_item(self):
        pass

    def _process_data(self, data):
        pass

class FetchPlayoffBracket(DataFetcher):
    def __init__(self):
        super().__init__()

    def _get_items(self):
        pass

    def _get_data_by_item(self):
        pass

    def _process_data(self, data):
        pass