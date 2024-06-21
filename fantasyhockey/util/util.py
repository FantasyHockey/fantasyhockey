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
        if "," in team_abbrev:
            team_abbrev = team_abbrev.split(",")[0] 
        query = "SELECT team_id FROM teams WHERE team_abbreviation = %s"
        params = (team_abbrev,)
        res = self.db_operator.read(query, params)
        return res[0][0] if res else None
    
    def get_team_id_from_name(self, team_name):
        if team_name is None:
            return None
        query = "SELECT team_id FROM teams WHERE team_name = %s"
        params = (team_name,)
        res = self.db_operator.read(query, params)
        return res[0][0] if res else None
    
import warnings
import functools

def obsolete(func):
    """This is a decorator to mark functions as obsolete."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        warnings.warn(
            f"{func.__name__} is obsolete and will be removed in future versions.",
            category=DeprecationWarning,
            stacklevel=2
        )
        return func(*args, **kwargs)
    return wrapped_func
