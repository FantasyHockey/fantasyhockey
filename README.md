# FantasyHockey

To run from the main entry point of app.py:
- source env/bin/activate
- python3 -m fantasyhockey


** Weird thing in the nhl api where for draft details 
    the team id isn't shown. Only the team abbreviation so we need to perform a lookup to convert abbrev to id first before populating this db.

    Also for the stats db there is only league abbrev, need to do lookup for league Id first