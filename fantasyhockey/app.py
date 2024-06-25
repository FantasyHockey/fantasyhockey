import time
from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.fetch import *
from fantasyhockey.data_fetching.update import *
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.update import CentralUpdater

def run():
    start_time = time.time()
    db_initializer = DatabaseInitializer()
    db_initializer.run()

    database_operator = DatabaseOperator()
    fetch_seasons = FetchSeasons()
    update_seasons = UpdateSeasons(database_operator, fetch_seasons)

    fetch_team_advanced_stats = FetchTeamAdvancedStats()
    update_team_advanced_stats = UpdateTeamAdvancedStats(database_operator, fetch_team_advanced_stats)

    fetch_draft_rankings = FetchDraftRankings()
    update_draft_rankings = UpdateDraftRankings(database_operator, fetch_draft_rankings)

    fetch_teams = FetchTeams()
    update_teams = UpdateTeams(database_operator, fetch_teams)
    
    fetch_players = FetchPlayers()
    update_players = UpdatePlayers(database_operator, fetch_players)

    fetch_skaters = FetchSkaters()
    update_skaters = UpdateSkaters(database_operator, fetch_skaters)

    fetch_goalies = FetchGoalies()
    update_goalies = UpdateGoalies(database_operator, fetch_goalies)

    fetch_games = FetchGames()
    update_games = UpdateGames(database_operator, fetch_games)

    updater = CentralUpdater([update_games])
    updater.update_all()


    print("Execution time: ", (time.time() - start_time) / 60, " minutes.")
    pass