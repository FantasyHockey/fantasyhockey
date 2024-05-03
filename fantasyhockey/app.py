from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.seasons.update_seasons import UpdateSeasons
from fantasyhockey.data_fetching.teams.update_teams import UpdateTeams
from fantasyhockey.data_fetching.draft_rankings.fetch_draft_ranking import FetchDraftRankings

def run():
    db_initializer = DatabaseInitializer()
    db_initializer.run()


    pass