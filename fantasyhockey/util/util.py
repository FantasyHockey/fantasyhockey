from fantasyhockey.database.database_operator import DatabaseOperator

class Util:
    def __init__(self):
        self.db_operator = DatabaseOperator()

    def remove_duplicates(self, data):
        """Remove duplicate player ids."""
        return list(set(data))
    
    def get_team_id_from_abbrev(self, team_abbrev):
        if team_abbrev is None:
            return None
        query = "SELECT team_id FROM teams WHERE team_abbreviation = %s"
        params = (team_abbrev,)
        res = self.db_operator.read(query, params)
        return res[0][0] if res else None
