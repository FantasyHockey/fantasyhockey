import time
from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.teams.update_teams import UpdateTeams
from fantasyhockey.data_fetching.players.update_players import UpdatePlayers
from fantasyhockey.data_fetching.players.update_skaters import UpdateSkaters
from fantasyhockey.data_fetching.players.update_goalies import UpdateGoalies
<<<<<<< HEAD
from fantasyhockey.data_fetching.games.fetch_games import FetchGames
from fantasyhockey.data_fetching.draft_rankings.update_draft_ranking import UpdateDraftRankings
=======
from fantasyhockey.database.database_operator import DatabaseOperator
from fantasyhockey.data_fetching.fetch import FetchSeasons, FetchDraftRankings
from fantasyhockey.data_fetching.update import CentralUpdater, UpdateSeasons, UpdateDraftRankings

>>>>>>> a39f72b (Start of refactor)
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
    update_draft_rankings = UpdateDraftRankings()
    update_draft_rankings.update_in_db()

    database_operator = DatabaseOperator()
    fetch_seasons = FetchSeasons()
    fetch_draft_rankings = FetchDraftRankings()

    update_seasons = UpdateSeasons(database_operator, fetch_seasons)
    update_draft_rankings = UpdateDraftRankings(database_operator, fetch_draft_rankings)
    updater = CentralUpdater([update_seasons, update_draft_rankings])
    updater.update_all()


    


    print("Execution time: ", (time.time() - start_time) / 60, " minutes.")
    pass