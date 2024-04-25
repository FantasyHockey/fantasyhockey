from fantasyhockey.database.database_init import DatabaseInitializer


def run():
    db_initializer = DatabaseInitializer()
    db_initializer.run()