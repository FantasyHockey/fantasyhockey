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
    #update_seasons = UpdateSeasons()
    #update_seasons.update_in_db()
    #update_teams = UpdateTeams()
    #update_teams.write_in_db()
    #update_players = UpdatePlayers()
    #update_players.write_in_db_update()
    #update_skaters = UpdateSkaters()
    #update_skaters.write_in_db()
    #update_goalies = UpdateGoalies()
    #update_goalies.write_in_db()
    #fetch_games = FetchGames()
    #fetch_games.get_games()

    database_operator = DatabaseOperator()
    #fetch_seasons = FetchSeasons()
    fetch_team_advanced_stats = FetchTeamAdvancedStats()
    #fetch_team_advanced_stats._get_items()

    #update_seasons = UpdateSeasons(database_operator, fetch_seasons)
    #update_draft_rankings = UpdateDraftRankings(database_operator, fetch_draft_rankings)
    #fetch_teams = FetchTeams()
    #update_teams = UpdateTeams(database_operator, fetch_teams)
    #update_team_stats = UpdateTeamStats(database_operator, fetch_teams)
    #update_team_advanced_stats = UpdateTeamAdvancedStats(database_operator, fetch_team_advanced_stats)
    updater = CentralUpdater([update_team_advanced_stats])
    updater.update_all()


    print("Execution time: ", (time.time() - start_time) / 60, " minutes.")
    pass