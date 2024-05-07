from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.seasons.update_seasons import UpdateSeasons
from fantasyhockey.data_fetching.teams.update_teams import UpdateTeams
from fantasyhockey.data_fetching.players.update_players import UpdatePlayers
from fantasyhockey.data_fetching.draft_rankings.update_draft_ranking import UpdateDraftRankings

def run():
    db_initializer = DatabaseInitializer()
    db_initializer.run()
    #update_seasons = UpdateSeasons()
    #update_seasons.update_in_db()
    #update_teams = UpdateTeams()
    #update_teams.update_in_db()
    #update_players = UpdatePlayers()
    #update_players.update_in_db()
    update_draft_rankings = UpdateDraftRankings()
    update_draft_rankings.update_in_db()

    pass