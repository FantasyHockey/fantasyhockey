import time
from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.seasons.update_seasons import UpdateSeasons
from fantasyhockey.data_fetching.teams.update_teams import UpdateTeams
from fantasyhockey.data_fetching.players.update_players import UpdatePlayers
from fantasyhockey.data_fetching.players.update_skaters import UpdateSkaters
from fantasyhockey.data_fetching.players.update_goalies import UpdateGoalies
from fantasyhockey.data_fetching.games.fetch_games import FetchGames

def run():
    start_time = time.time()
    db_initializer = DatabaseInitializer()
    db_initializer.run()
    #update_seasons = UpdateSeasons()
    #update_seasons.update_in_db()
    update_teams = UpdateTeams()
    update_teams.write_in_db()
    #update_players = UpdatePlayers()
    #update_players.write_in_db_update()
    #update_skaters = UpdateSkaters()
    #update_skaters.write_in_db()
    #update_goalies = UpdateGoalies()
    #update_goalies.write_in_db()
    #fetch_games = FetchGames()
    #fetch_games.get_games()

    


    print("Execution time: ", (time.time() - start_time) / 60, " minutes.")
    pass