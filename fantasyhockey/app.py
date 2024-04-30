from fantasyhockey.database.database_init import DatabaseInitializer
from fantasyhockey.data_fetching.seasons.update_seasons import UpdateSeasons


def run():
    db_initializer = DatabaseInitializer()
    db_initializer.run()
    #update_seasons = UpdateSeasons()
    #update_seasons.update_in_db()
    pass