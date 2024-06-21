
class Season:
    def __init__(self, season_id=None):
        self._year = season_id
        self._conference_in_use = None
        self._division_in_use = None
        self._point_for_ot_loss_in_use = None
        self._regulation_wins_in_use = None
        self._row_in_use = None
        self._standings_end = None
        self._standings_start = None
        self._ties_in_use = None
        self._wild_card_in_use = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def conference_in_use(self):
        return self._conference_in_use

    @conference_in_use.setter
    def conference_in_use(self, value):
        self._conference_in_use = value

    @property
    def division_in_use(self):
        return self._division_in_use

    @division_in_use.setter
    def division_in_use(self, value):
        self._division_in_use = value

    @property
    def point_for_ot_loss_in_use(self):
        return self._point_for_ot_loss_in_use

    @point_for_ot_loss_in_use.setter
    def point_for_ot_loss_in_use(self, value):
        self._point_for_ot_loss_in_use = value

    @property
    def regulation_wins_in_use(self):
        return self._regulation_wins_in_use

    @regulation_wins_in_use.setter
    def regulation_wins_in_use(self, value):
        self._regulation_wins_in_use = value

    @property
    def row_in_use(self):
        return self._row_in_use

    @row_in_use.setter
    def row_in_use(self, value):
        self._row_in_use = value

    @property
    def standings_end(self):
        return self._standings_end

    @standings_end.setter
    def standings_end(self, value):
        self._standings_end = value

    @property
    def standings_start(self):
        return self._standings_start

    @standings_start.setter
    def standings_start(self, value):
        self._standings_start = value

    @property
    def ties_in_use(self):
        return self._ties_in_use

    @ties_in_use.setter
    def ties_in_use(self, value):
        self._ties_in_use = value

    @property
    def wild_card_in_use(self):
        return self._wild_card_in_use

    @wild_card_in_use.setter
    def wild_card_in_use(self, value):
        self._wild_card_in_use = value

class DraftRanking:
    def __init__(self, year=None, first_name=None, last_name=None, position_code=None):
        self._year = year
        self._first_name = first_name
        self._last_name = last_name
        self._final_rank = None
        self._position_code = position_code
        self._shoots_catches = None
        self._height_inches = None
        self._weight_pounds = None
        self._last_amateur_club = None
        self._last_amateur_league = None
        self._birth_date = None
        self._birth_city = None
        self._birth_state_province = None
        self._birth_country = None
        self._midterm_rank = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def final_rank(self):
        return self._final_rank

    @final_rank.setter
    def final_rank(self, value):
        self._final_rank = value

    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value

    @property
    def shoots_catches(self):
        return self._shoots_catches

    @shoots_catches.setter
    def shoots_catches(self, value):
        self._shoots_catches = value

    @property
    def height_inches(self):
        return self._height_inches

    @height_inches.setter
    def height_inches(self, value):
        self._height_inches = value

    @property
    def weight_pounds(self):
        return self._weight_pounds

    @weight_pounds.setter
    def weight_pounds(self, value):
        self._weight_pounds = value

    @property
    def last_amateur_club(self):
        return self._last_amateur_club

    @last_amateur_club.setter
    def last_amateur_club(self, value):
        self._last_amateur_club = value

    @property
    def last_amateur_league(self):
        return self._last_amateur_league

    @last_amateur_league.setter
    def last_amateur_league(self, value):
        self._last_amateur_league = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def birth_city(self):
        return self._birth_city

    @birth_city.setter
    def birth_city(self, value):
        self._birth_city = value

    @property
    def birth_state_province(self):
        return self._birth_state_province

    @birth_state_province.setter
    def birth_state_province(self, value):
        self._birth_state_province = value

    @property
    def birth_country(self):
        return self._birth_country

    @birth_country.setter
    def birth_country(self, value):
        self._birth_country = value

    @property
    def midterm_rank(self):
        return self._midterm_rank

    @midterm_rank.setter
    def midterm_rank(self, value):
        self._midterm_rank = value


class SkaterAdvancedStatsCorsiFenwick:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._games_played = None
        self._corsi_against = None
        self._corsi_ahead = None
        self._corsi_behind = None
        self._corsi_close = None
        self._corsi_for = None
        self._corsi_tied = None
        self._corsi_total = None
        self._fenwick_against = None
        self._fenwick_ahead = None
        self._fenwick_behind = None
        self._fenwick_close = None
        self._fenwick_for = None
        self._fenwick_tied = None
        self._fenwick_relative = None
        self._fenwick_total = None
        self._corsi_percentage = None
        self._corsi_ahead_percentage = None
        self._corsi_behind_percentage = None
        self._corsi_close_percentage = None
        self._corsi_tied_percentage = None
        self._corsi_relative = None
        self._shooting_percent_5on5 = None
        self._skater_save_percent_5on5 = None
        self._skater_shooting_plus_save_percent_5on5 = None
        self._time_on_ice_5on5_per_game = None
        self._fenwick_percentage = None
        self._fenwick_ahead_percentage = None
        self._fenwick_behind_percentage = None
        self._fenwick_close_percentage = None
        self._fenwick_tied_percentage = None
        self._zone_start_5on5_percentage = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def games_played(self):
        return self._games_played

    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def corsi_against(self):
        return self._corsi_against

    @corsi_against.setter
    def corsi_against(self, value):
        self._corsi_against = value

    @property
    def corsi_ahead(self):
        return self._corsi_ahead

    @corsi_ahead.setter
    def corsi_ahead(self, value):
        self._corsi_ahead = value

    @property
    def corsi_behind(self):
        return self._corsi_behind

    @corsi_behind.setter
    def corsi_behind(self, value):
        self._corsi_behind = value

    @property
    def corsi_close(self):
        return self._corsi_close

    @corsi_close.setter
    def corsi_close(self, value):
        self._corsi_close = value

    @property
    def corsi_for(self):
        return self._corsi_for

    @corsi_for.setter
    def corsi_for(self, value):
        self._corsi_for = value

    @property
    def corsi_tied(self):
        return self._corsi_tied

    @corsi_tied.setter
    def corsi_tied(self, value):
        self._corsi_tied = value

    @property
    def corsi_total(self):
        return self._corsi_total

    @corsi_total.setter
    def corsi_total(self, value):
        self._corsi_total = value

    @property
    def fenwick_against(self):
        return self._fenwick_against

    @fenwick_against.setter
    def fenwick_against(self, value):
        self._fenwick_against = value

    @property
    def fenwick_ahead(self):
        return self._fenwick_ahead

    @fenwick_ahead.setter
    def fenwick_ahead(self, value):
        self._fenwick_ahead = value

    @property
    def fenwick_behind(self):
        return self._fenwick_behind

    @fenwick_behind.setter
    def fenwick_behind(self, value):
        self._fenwick_behind = value

    @property
    def fenwick_close(self):
        return self._fenwick_close

    @fenwick_close.setter
    def fenwick_close(self, value):
        self._fenwick_close = value

    @property
    def fenwick_for(self):
        return self._fenwick_for

    @fenwick_for.setter
    def fenwick_for(self, value):
        self._fenwick_for = value

    @property
    def fenwick_tied(self):
        return self._fenwick_tied

    @fenwick_tied.setter
    def fenwick_tied(self, value):
        self._fenwick_tied = value

    @property
    def fenwick_relative(self):
        return self._fenwick_relative

    @fenwick_relative.setter
    def fenwick_relative(self, value):
        self._fenwick_relative = value

    @property
    def fenwick_total(self):
        return self._fenwick_total

    @fenwick_total.setter
    def fenwick_total(self, value):
        self._fenwick_total = value

    @property
    def corsi_percentage(self):
        return self._corsi_percentage

    @corsi_percentage.setter
    def corsi_percentage(self, value):
        self._corsi_percentage = value

    @property
    def corsi_ahead_percentage(self):
        return self._corsi_ahead_percentage

    @corsi_ahead_percentage.setter
    def corsi_ahead_percentage(self, value):
        self._corsi_ahead_percentage = value

    @property
    def corsi_behind_percentage(self):
        return self._corsi_behind_percentage

    @corsi_behind_percentage.setter
    def corsi_behind_percentage(self, value):
        self._corsi_behind_percentage = value

    @property
    def corsi_close_percentage(self):
        return self._corsi_close_percentage

    @corsi_close_percentage.setter
    def corsi_close_percentage(self, value):
        self._corsi_close_percentage = value

    @property
    def corsi_tied_percentage(self):
        return self._corsi_tied_percentage

    @corsi_tied_percentage.setter
    def corsi_tied_percentage(self, value):
        self._corsi_tied_percentage = value

    @property
    def corsi_relative(self):
        return self._corsi_relative

    @corsi_relative.setter
    def corsi_relative(self, value):
        self._corsi_relative = value

    @property
    def shooting_percent_5on5(self):
        return self._shooting_percent_5on5

    @shooting_percent_5on5.setter
    def shooting_percent_5on5(self, value):
        self._shooting_percent_5on5 = value

    @property
    def skater_save_percent_5on5(self):
        return self._skater_save_percent_5on5

    @skater_save_percent_5on5.setter
    def skater_save_percent_5on5(self, value):
        self._skater_save_percent_5on5 = value

    @property
    def skater_shooting_plus_save_percent_5on5(self):
        return self._skater_shooting_plus_save_percent_5on5

    @skater_shooting_plus_save_percent_5on5.setter
    def skater_shooting_plus_save_percent_5on5(self, value):
        self._skater_shooting_plus_save_percent_5on5 = value

    @property
    def time_on_ice_5on5_per_game(self):
        return self._time_on_ice_5on5_per_game

    @time_on_ice_5on5_per_game.setter
    def time_on_ice_5on5_per_game(self, value):
        self._time_on_ice_5on5_per_game = value

    @property
    def fenwick_percentage(self):
        return self._fenwick_percentage

    @fenwick_percentage.setter
    def fenwick_percentage(self, value):
        self._fenwick_percentage = value

    @property
    def fenwick_ahead_percentage(self):
        return self._fenwick_ahead_percentage

    @fenwick_ahead_percentage.setter
    def fenwick_ahead_percentage(self, value):
        self._fenwick_ahead_percentage = value

    @property
    def fenwick_behind_percentage(self):
        return self._fenwick_behind_percentage

    @fenwick_behind_percentage.setter
    def fenwick_behind_percentage(self, value):
        self._fenwick_behind_percentage = value

    @property
    def fenwick_close_percentage(self):
        return self._fenwick_close_percentage
    
    @fenwick_close_percentage.setter
    def fenwick_close_percentage(self, value):
        self._fenwick_close_percentage = value

    @property
    def fenwick_tied_percentage(self):
        return self._fenwick_tied_percentage
    
    @fenwick_tied_percentage.setter
    def fenwick_tied_percentage(self, value):
        self._fenwick_tied_percentage = value

    @property
    def zone_start_5on5_percentage(self):
        return self._zone_start_5on5_percentage
    
    @zone_start_5on5_percentage.setter
    def zone_start_5on5_percentage(self, value):
        self._zone_start_5on5_percentage = value

class SkaterAdvancedStatsFaceoffs:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._defensive_zone_faceoffs = None
        self._defensive_zone_faceoffs_won = None
        self._defensive_zone_faceoffs_lost = None
        self._ev_faceoffs = None
        self._ev_faceoffs_won = None
        self._ev_faceoffs_lost = None
        self._faceoff_percentage = None
        self._neutral_zone_faceoffs = None
        self._neutral_zone_faceoffs_won = None
        self._neutral_zone_faceoffs_lost = None
        self._offensive_zone_faceoffs = None
        self._offensive_zone_faceoffs_won = None
        self._offensive_zone_faceoffs_lost = None
        self._pp_faceoffs = None
        self._pp_faceoffs_won = None
        self._pp_faceoffs_lost = None
        self._pk_faceoffs = None
        self._pk_faceoffs_won = None
        self._pk_faceoffs_lost = None
        self._total_faceoffs = None
        self._total_faceoffs_won = None
        self._total_faceoffs_lost = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def defensive_zone_faceoffs(self):
        return self._defensive_zone_faceoffs
    
    @defensive_zone_faceoffs.setter
    def defensive_zone_faceoffs(self, value):
        self._defensive_zone_faceoffs = value

    @property
    def defensive_zone_faceoffs_won(self):
        return self._defensive_zone_faceoffs_won
    
    @defensive_zone_faceoffs_won.setter
    def defensive_zone_faceoffs_won(self, value):
        self._defensive_zone_faceoffs_won = value

    @property
    def defensive_zone_faceoffs_lost(self):
        return self._defensive_zone_faceoffs_lost
    
    @defensive_zone_faceoffs_lost.setter
    def defensive_zone_faceoffs_lost(self, value):
        self._defensive_zone_faceoffs_lost = value

    @property
    def ev_faceoffs(self):
        return self._ev_faceoffs
    
    @ev_faceoffs.setter
    def ev_faceoffs(self, value):
        self._ev_faceoffs = value

    @property
    def ev_faceoffs_won(self):
        return self._ev_faceoffs_won
    
    @ev_faceoffs_won.setter
    def ev_faceoffs_won(self, value):
        self._ev_faceoffs_won = value

    @property
    def ev_faceoffs_lost(self):
        return self._ev_faceoffs_lost
    
    @ev_faceoffs_lost.setter
    def ev_faceoffs_lost(self, value):
        self._ev_faceoffs_lost = value

    @property
    def faceoff_percentage(self):
        return self._faceoff_percentage
    
    @faceoff_percentage.setter
    def faceoff_percentage(self, value):
        self._faceoff_percentage = value

    @property
    def neutral_zone_faceoffs(self):
        return self._neutral_zone_faceoffs
    
    @neutral_zone_faceoffs.setter
    def neutral_zone_faceoffs(self, value):
        self._neutral_zone_faceoffs = value

    @property
    def neutral_zone_faceoffs_won(self):
        return self._neutral_zone_faceoffs_won
    
    @neutral_zone_faceoffs_won.setter
    def neutral_zone_faceoffs_won(self, value):
        self._neutral_zone_faceoffs_won = value

    @property
    def neutral_zone_faceoffs_lost(self):
        return self._neutral_zone_faceoffs_lost
    
    @neutral_zone_faceoffs_lost.setter
    def neutral_zone_faceoffs_lost(self, value):
        self._neutral_zone_faceoffs_lost = value

    @property
    def offensive_zone_faceoffs(self):
        return self._offensive_zone_faceoffs
    
    @offensive_zone_faceoffs.setter
    def offensive_zone_faceoffs(self, value):
        self._offensive_zone_faceoffs = value

    @property
    def offensive_zone_faceoffs_won(self):
        return self._offensive_zone_faceoffs_won
    
    @offensive_zone_faceoffs_won.setter
    def offensive_zone_faceoffs_won(self, value):
        self._offensive_zone_faceoffs_won = value

    @property
    def offensive_zone_faceoffs_lost(self):
        return self._offensive_zone_faceoffs_lost
    
    @offensive_zone_faceoffs_lost.setter
    def offensive_zone_faceoffs_lost(self, value):
        self._offensive_zone_faceoffs_lost = value

    @property
    def pp_faceoffs(self):
        return self._pp_faceoffs
    
    @pp_faceoffs.setter
    def pp_faceoffs(self, value):
        self._pp_faceoffs = value

    @property
    def pp_faceoffs_won(self):
        return self._pp_faceoffs_won
    
    @pp_faceoffs_won.setter
    def pp_faceoffs_won(self, value):
        self._pp_faceoffs_won = value

    @property
    def pp_faceoffs_lost(self):
        return self._pp_faceoffs_lost
    
    @pp_faceoffs_lost.setter
    def pp_faceoffs_lost(self, value):
        self._pp_faceoffs_lost = value

    @property
    def pk_faceoffs(self):
        return self._pk_faceoffs
    
    @pk_faceoffs.setter
    def pk_faceoffs(self, value):
        self._pk_faceoffs = value

    @property
    def pk_faceoffs_won(self):
        return self._pk_faceoffs_won
    
    @pk_faceoffs_won.setter
    def pk_faceoffs_won(self, value):
        self._pk_faceoffs_won = value

    @property
    def pk_faceoffs_lost(self):
        return self._pk_faceoffs_lost
    
    @pk_faceoffs_lost.setter
    def pk_faceoffs_lost(self, value):
        self._pk_faceoffs_lost = value

    @property
    def total_faceoffs(self):
        return self._total_faceoffs
    
    @total_faceoffs.setter
    def total_faceoffs(self, value):
        self._total_faceoffs = value

    @property
    def total_faceoffs_won(self):
        return self._total_faceoffs_won
    
    @total_faceoffs_won.setter
    def total_faceoffs_won(self, value):
        self._total_faceoffs_won = value

    @property
    def total_faceoffs_lost(self):
        return self._total_faceoffs_lost
    
    @total_faceoffs_lost.setter
    def total_faceoffs_lost(self, value):
        self._total_faceoffs_lost = value

class SkaterAdvancedStatsGoals:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._even_strength_goal_difference = None
        self._even_strength_goals_against = None
        self._even_strength_goals_for = None
        self._even_strength_time_on_ice_per_game = None
        self._games_played = None
        self._pp_goals_for = None
        self._pp_goals_against = None
        self._pk_goals_for = None
        self._pk_goals_against = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def even_strength_goal_difference(self):
        return self._even_strength_goal_difference
    
    @even_strength_goal_difference.setter
    def even_strength_goal_difference(self, value):
        self._even_strength_goal_difference = value

    @property
    def even_strength_goals_against(self):
        return self._even_strength_goals_against
    
    @even_strength_goals_against.setter
    def even_strength_goals_against(self, value):
        self._even_strength_goals_against = value

    @property
    def even_strength_goals_for(self):
        return self._even_strength_goals_for
    
    @even_strength_goals_for.setter
    def even_strength_goals_for(self, value):
        self._even_strength_goals_for = value

    @property
    def even_strength_time_on_ice_per_game(self):
        return self._even_strength_time_on_ice_per_game
    
    @even_strength_time_on_ice_per_game.setter
    def even_strength_time_on_ice_per_game(self, value):
        self._even_strength_time_on_ice_per_game = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def pp_goals_for(self):
        return self._pp_goals_for
    
    @pp_goals_for.setter
    def pp_goals_for(self, value):
        self._pp_goals_for = value

    @property
    def pp_goals_against(self):
        return self._pp_goals_against
    
    @pp_goals_against.setter
    def pp_goals_against(self, value):
        self._pp_goals_against = value

    @property
    def pk_goals_for(self):
        return self._pk_goals_for
    
    @pk_goals_for.setter
    def pk_goals_for(self, value):
        self._pk_goals_for = value

    @property
    def pk_goals_against(self):
        return self._pk_goals_against
    
    @pk_goals_against.setter
    def pk_goals_against(self, value):
        self._pk_goals_against = value

class SkaterAdvancedStatsMisc:
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._blocked_shots = None
        self._empty_net_assists = None
        self._empty_net_goals = None
        self._empty_net_points = None
        self._first_goals = None
        self._giveaways = None
        self._games_played = None
        self._hits = None
        self._missed_shot_crossbar = None
        self._missed_shot_goalpost = None
        self._missed_shot_over = None
        self._missed_shot_wide = None
        self._missed_shots = None
        self._ot_goals = None
        self._takeaways = None
        self._time_on_ice_per_game = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def blocked_shots(self):
        return self._blocked_shots
    
    @blocked_shots.setter
    def blocked_shots(self, value):
        self._blocked_shots = value

    @property
    def empty_net_assists(self):
        return self._empty_net_assists
    
    @empty_net_assists.setter
    def empty_net_assists(self, value):
        self._empty_net_assists = value

    @property
    def empty_net_goals(self):
        return self._empty_net_goals
    
    @empty_net_goals.setter
    def empty_net_goals(self, value):
        self._empty_net_goals = value

    @property
    def empty_net_points(self):
        return self._empty_net_points
    
    @empty_net_points.setter
    def empty_net_points(self, value):
        self._empty_net_points = value

    @property
    def first_goals(self):
        return self._first_goals
    
    @first_goals.setter
    def first_goals(self, value):
        self._first_goals = value

    @property
    def giveaways(self):
        return self._giveaways
    
    @giveaways.setter
    def giveaways(self, value):
        self._giveaways = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def hits(self):
        return self._hits
    
    @hits.setter
    def hits(self, value):
        self._hits = value

    @property
    def missed_shot_crossbar(self):
        return self._missed_shot_crossbar
    
    @missed_shot_crossbar.setter
    def missed_shot_crossbar(self, value):
        self._missed_shot_crossbar = value

    @property
    def missed_shot_goalpost(self):
        return self._missed_shot_goalpost
    
    @missed_shot_goalpost.setter
    def missed_shot_goalpost(self, value):
        self._missed_shot_goalpost = value

    @property
    def missed_shot_over(self):
        return self._missed_shot_over
    
    @missed_shot_over.setter
    def missed_shot_over(self, value):
        self._missed_shot_over = value

    @property
    def missed_shot_wide(self):
        return self._missed_shot_wide
    
    @missed_shot_wide.setter
    def missed_shot_wide(self, value):
        self._missed_shot_wide = value

    @property
    def missed_shots(self):
        return self._missed_shots
    
    @missed_shots.setter
    def missed_shots(self, value):
        self._missed_shots = value

    @property
    def ot_goals(self):
        return self._ot_goals
    
    @ot_goals.setter
    def ot_goals(self, value):
        self._ot_goals = value

    @property
    def takeaways(self):
        return self._takeaways
    
    @takeaways.setter
    def takeaways(self, value):
        self._takeaways = value

    @property
    def time_on_ice_per_game(self):
        return self._time_on_ice_per_game
    
    @time_on_ice_per_game.setter
    def time_on_ice_per_game(self, value):
        self._time_on_ice_per_game = value

class SkaterAdvancedStatsPenalties:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._game_misconduct_penalties = None
        self._games_played = None
        self._major_penalties = None
        self._match_penalties = None
        self._minor_penalties = None
        self._misconduct_penalties = None
        self._net_penalties = None
        self._penalties = None
        self._penalties_drawn = None
        self._penalty_minutes = None
        self._time_on_ice_per_game = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self.__penaltieslayer_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def game_misconduct_penalties(self):
        return self._game_misconduct_penalties
    
    @game_misconduct_penalties.setter
    def game_misconduct_penalties(self, value):
        self._game_misconduct_penalties = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def major_penalties(self):
        return self._major_penalties
    
    @major_penalties.setter
    def major_penalties(self, value):
        self._major_penalties = value

    @property
    def match_penalties(self):
        return self._match_penalties
    
    @match_penalties.setter 
    def match_penalties(self, value):
        self._match_penalties = value

    @property
    def minor_penalties(self):
        return self._minor_penalties
    
    @minor_penalties.setter
    def minor_penalties(self, value):
        self._minor_penalties = value

    @property
    def misconduct_penalties(self):
        return self._misconduct_penalties
    
    @misconduct_penalties.setter    
    def misconduct_penalties(self, value):
        self._misconduct_penalties = value

    @property
    def net_penalties(self):
        return self._net_penalties
    
    @net_penalties.setter
    def net_penalties(self, value):
        self._net_penalties = value

    @property
    def penalties(self):
        return self._penalties
    
    @penalties.setter
    def penalties(self, value):
        self._penalties = value

    @property
    def penalties_drawn(self):
        return self._penalties_drawn
    
    @penalties_drawn.setter
    def penalties_drawn(self, value):
        self._penalties_drawn = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def time_on_ice_per_game(self):
        return self._time_on_ice_per_game
    
    @time_on_ice_per_game.setter
    def time_on_ice_per_game(self, value):
        self._time_on_ice_per_game = value

class SkaterAdvancedStatsPenaltyKill:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._pk_assists = None
        self._pk_goals = None
        self._pk_individual_corsi_for = None
        self._pk_primary_assists = None
        self._pk_secondary_assists = None
        self._pk_shooting_percentage = None
        self._pk_shots = None
        self._pk_time_on_ice = None
        self._pk_time_on_ice_per_game = None
        self._pk_time_on_ice_percentage = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def pk_assists(self):
        return self._pk_assists
    
    @pk_assists.setter
    def pk_assists(self, value):
        self._pk_assists = value

    @property
    def pk_goals(self):
        return self._pk_goals
    
    @pk_goals.setter
    def pk_goals(self, value):
        self._pk_goals = value

    @property
    def pk_individual_corsi_for(self):
        return self._pk_individual_corsi_for
    
    @pk_individual_corsi_for.setter
    def pk_individual_corsi_for(self, value):
        self._pk_individual_corsi_for = value

    @property
    def pk_primary_assists(self):
        return self._pk_primary_assists
    
    @pk_primary_assists.setter
    def pk_primary_assists(self, value):
        self._pk_primary_assists = value

    @property
    def pk_secondary_assists(self):
        return self._pk_secondary_assists
    
    @pk_secondary_assists.setter
    def pk_secondary_assists(self, value):
        self._pk_secondary_assists = value

    @property
    def pk_shooting_percentage(self):
        return self._pk_shooting_percentage
    
    @pk_shooting_percentage.setter
    def pk_shooting_percentage(self, value):
        self._pk_shooting_percentage = value

    @property
    def pk_shots(self):
        return self._pk_shots
    
    @pk_shots.setter
    def pk_shots(self, value):
        self._pk_shots = value

    @property
    def pk_time_on_ice(self):
        return self._pk_time_on_ice
    
    @pk_time_on_ice.setter
    def pk_time_on_ice(self, value):
        self._pk_time_on_ice = value

    @property
    def pk_time_on_ice_per_game(self):
        return self._pk_time_on_ice_per_game
    
    @pk_time_on_ice_per_game.setter
    def pk_time_on_ice_per_game(self, value):
        self._pk_time_on_ice_per_game = value

    @property
    def pk_time_on_ice_percentage(self):
        return self._pk_time_on_ice_percentage
    
    @pk_time_on_ice_percentage.setter
    def pk_time_on_ice_percentage(self, value):
        self._pk_time_on_ice_percentage = value

class SkaterAdvancedStatsPowerplay:

    def __init__(self, player_id):
        self._player_id = player_id
        self._team_id = None
        self._year = None
        self._pp_assists = None
        self._pp_goals = None
        self._pp_individual_corsi_for = None
        self._pp_primary_assists = None
        self._pp_secondary_assists = None
        self._pp_shooting_percentage = None
        self._pp_shots = None
        self._pp_time_on_ice = None
        self._pp_time_on_ice_per_game = None
        self._pp_time_on_ice_percentage = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def pp_assists(self):
        return self._pp_assists
    
    @pp_assists.setter
    def pp_assists(self, value):
        self._pp_assists = value

    @property
    def pp_goals(self):
        return self._pp_goals
    
    @pp_goals.setter
    def pp_goals(self, value):
        self._pp_goals = value

    @property
    def pp_individual_corsi_for(self):
        return self._pp_individual_corsi_for
    
    @pp_individual_corsi_for.setter
    def pp_individual_corsi_for(self, value):
        self._pp_individual_corsi_for = value

    @property
    def pp_primary_assists(self):
        return self._pp_primary_assists
    
    @pp_primary_assists.setter
    def pp_primary_assists(self, value):
        self._pp_primary_assists = value

    @property
    def pp_secondary_assists(self):
        return self._pp_secondary_assists
    
    @pp_secondary_assists.setter
    def pp_secondary_assists(self, value):
        self._pp_secondary_assists = value

    @property
    def pp_shooting_percentage(self):
        return self._pp_shooting_percentage
    
    @pp_shooting_percentage.setter
    def pp_shooting_percentage(self, value):
        self._pp_shooting_percentage = value

    @property
    def pp_shots(self):
        return self._pp_shots
    
    @pp_shots.setter
    def pp_shots(self, value):
        self._pp_shots = value

    @property
    def pp_time_on_ice(self):
        return self._pp_time_on_ice
    
    @pp_time_on_ice.setter
    def pp_time_on_ice(self, value):
        self._pp_time_on_ice = value

    @property
    def pp_time_on_ice_per_game(self):
        return self._pp_time_on_ice_per_game
    
    @pp_time_on_ice_per_game.setter
    def pp_time_on_ice_per_game(self, value):
        self._pp_time_on_ice_per_game = value

    @property
    def pp_time_on_ice_percentage(self):
        return self._pp_time_on_ice_percentage
    
    @pp_time_on_ice_percentage.setter
    def pp_time_on_ice_percentage(self, value):
        self._pp_time_on_ice_percentage = value

class SkaterAdvancedStatsScoring:
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._goals_backhand = None
        self._goals_bat = None
        self._goals_between_legs = None
        self._goals_cradle = None
        self._goals_deflected = None
        self._goals_poke = None
        self._goals_slap = None
        self._goals_snap = None
        self._goals_tip = None
        self._goals_wrap_around = None
        self._goals_wrist = None
        self._shots_backhand = None
        self._shots_bat = None
        self._shots_between_legs = None
        self._shots_cradle = None
        self._shots_deflected = None
        self._shots_poke = None
        self._shots_slap = None
        self._shots_snap = None
        self._shots_tip = None
        self._shots_wrap_around = None
        self._shots_wrist = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property   
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def goals_backhand(self):
        return self._goals_backhand
    
    @goals_backhand.setter
    def goals_backhand(self, value):
        self._goals_backhand = value

    @property
    def goals_bat(self):
        return self._goals_bat
    
    @goals_bat.setter
    def goals_bat(self, value):
        self._goals_bat = value

    @property
    def goals_between_legs(self):
        return self._goals_between_legs
    
    @goals_between_legs.setter
    def goals_between_legs(self, value):
        self._goals_between_legs = value

    @property
    def goals_cradle(self):
        return self._goals_cradle
    
    @goals_cradle.setter
    def goals_cradle(self, value):
        self._goals_cradle = value

    @property
    def goals_deflected(self):
        return self._goals_deflected
    
    @goals_deflected.setter
    def goals_deflected(self, value):
        self._goals_deflected = value

    @property
    def goals_poke(self):
        return self._goals_poke
    
    @goals_poke.setter
    def goals_poke(self, value):
        self._goals_poke = value

    @property
    def goals_slap(self):
        return self._goals_slap
    
    @goals_slap.setter
    def goals_slap(self, value):
        self._goals_slap = value

    @property
    def goals_snap(self):
        return self._goals_snap
    
    @goals_snap.setter
    def goals_snap(self, value):
        self._goals_snap = value

    @property
    def goals_tip(self):
        return self._goals_tip
    
    @goals_tip.setter
    def goals_tip(self, value):
        self._goals_tip = value

    @property
    def goals_wrap_around(self):
        return self._goals_wrap_around
    
    @goals_wrap_around.setter
    def goals_wrap_around(self, value):
        self._goals_wrap_around = value

    @property
    def goals_wrist(self):
        return self._goals_wrist
    
    @goals_wrist.setter
    def goals_wrist(self, value):
        self._goals_wrist = value

    @property
    def shots_backhand(self):
        return self._shots_backhand
    
    @shots_backhand.setter
    def shots_backhand(self, value):
        self._shots_backhand = value

    @property
    def shots_bat(self):
        return self._shots_bat
    
    @shots_bat.setter
    def shots_bat(self, value):
        self._shots_bat = value

    @property
    def shots_between_legs(self):
        return self._shots_between_legs
    
    @shots_between_legs.setter
    def shots_between_legs(self, value):
        self._shots_between_legs = value

    @property
    def shots_cradle(self):
        return self._shots_cradle
    
    @shots_cradle.setter
    def shots_cradle(self, value):
        self._shots_cradle = value

    @property
    def shots_deflected(self):
        return self._shots_deflected
    
    @shots_deflected.setter
    def shots_deflected(self, value):
        self._shots_deflected = value

    @property
    def shots_poke(self):
        return self._shots_poke
    
    @shots_poke.setter
    def shots_poke(self, value):
        self._shots_poke = value

    @property
    def shots_slap(self):
        return self._shots_slap
    
    @shots_slap.setter
    def shots_slap(self, value):
        self._shots_slap = value

    @property
    def shots_snap(self):
        return self._shots_snap
    
    @shots_snap.setter
    def shots_snap(self, value):
        self._shots_snap = value

    @property
    def shots_tip(self):
        return self._shots_tip
    
    @shots_tip.setter
    def shots_tip(self, value):
        self._shots_tip = value

    @property
    def shots_wrap_around(self):
        return self._shots_wrap_around
    
    @shots_wrap_around.setter
    def shots_wrap_around(self, value):
        self._shots_wrap_around = value

    @property
    def shots_wrist(self):
        return self._shots_wrist
    
    @shots_wrist.setter
    def shots_wrist(self, value):
        self._shots_wrist = value

class SkaterAdvancedStatsShootout:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._career_shootout_game_deciding_goals = None
        self._career_shootout_games_played = None
        self._career_shootout_goals = None
        self._career_shootout_percentage = None
        self._career_shootout_shots = None
        self._shootout_game_deciding_goals = None
        self._shootout_games_played = None
        self._shootout_goals = None
        self._shootout_percentage = None
        self._shootout_shots = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def career_shootout_game_deciding_goals(self):
        return self._career_shootout_game_deciding_goals
    
    @career_shootout_game_deciding_goals.setter
    def career_shootout_game_deciding_goals(self, value):
        self._career_shootout_game_deciding_goals = value

    @property
    def career_shootout_games_played(self):
        return self._career_shootout_games_played
    
    @career_shootout_games_played.setter
    def career_shootout_games_played(self, value):
        self._career_shootout_games_played = value

    @property
    def career_shootout_goals(self):
        return self._career_shootout_goals
    
    @career_shootout_goals.setter
    def career_shootout_goals(self, value):
        self._career_shootout_goals = value

    @property
    def career_shootout_percentage(self):
        return self._career_shootout_percentage
    
    @career_shootout_percentage.setter
    def career_shootout_percentage(self, value):
        self._career_shootout_percentage = value

    @property
    def career_shootout_shots(self):
        return self._career_shootout_shots
    
    @career_shootout_shots.setter
    def career_shootout_shots(self, value):
        self._career_shootout_shots = value

    @property
    def shootout_game_deciding_goals(self):
        return self._shootout_game_deciding_goals
    
    @shootout_game_deciding_goals.setter
    def shootout_game_deciding_goals(self, value):
        self._shootout_game_deciding_goals = value

    @property
    def shootout_games_played(self):
        return self._shootout_games_played
    
    @shootout_games_played.setter
    def shootout_games_played(self, value):
        self._shootout_games_played = value

    @property
    def shootout_goals(self):
        return self._shootout_goals
    
    @shootout_goals.setter
    def shootout_goals(self, value):
        self._shootout_goals = value

    @property
    def shootout_percentage(self):
        return self._shootout_percentage
    
    @shootout_percentage.setter
    def shootout_percentage(self, value):
        self._shootout_percentage = value

    @property
    def shootout_shots(self):
        return self._shootout_shots
    
    @shootout_shots.setter
    def shootout_shots(self, value):
        self._shootout_shots = value

class SkaterAdvancedStatsTOI:
    def __init__(self, player_id):
        self._player_id = player_id
        self._team_id = None
        self._year = None
        self._ev_time_on_ice = None
        self._games_played = None
        self._ot_time_on_ice = None
        self._ot_time_on_ice_per_ot_game = None
        self._pp_time_on_ice = None
        self._sh_time_on_ice = None
        self._shifts = None
        self._time_on_ice = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def ev_time_on_ice(self):
        return self._ev_time_on_ice
    
    @ev_time_on_ice.setter
    def ev_time_on_ice(self, value):
        self._ev_time_on_ice = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def ot_time_on_ice(self):
        return self._ot_time_on_ice
    
    @ot_time_on_ice.setter
    def ot_time_on_ice(self, value):
        self._ot_time_on_ice = value

    @property
    def ot_time_on_ice_per_ot_game(self):
        return self._ot_time_on_ice_per_ot_game
    
    @ot_time_on_ice_per_ot_game.setter
    def ot_time_on_ice_per_ot_game(self, value):
        self._ot_time_on_ice_per_ot_game = value

    @property
    def pp_time_on_ice(self):
        return self._pp_time_on_ice
    
    @pp_time_on_ice.setter
    def pp_time_on_ice(self, value):
        self._pp_time_on_ice = value

    @property
    def sh_time_on_ice(self):
        return self._sh_time_on_ice
    
    @sh_time_on_ice.setter
    def sh_time_on_ice(self, value):
        self._sh_time_on_ice = value

    @property
    def shifts(self):
        return self._shifts
    
    @shifts.setter
    def shifts(self, value):
        self._shifts = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

class SkaterStats:
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._games_played = None
        self._goals = None
        self._assists = None
        self._points = None
        self._plus_minus = None
        self._penalty_minutes = None
        self._game_winning_goals = None
        self._ot_goals = None
        self._power_play_goals = None
        self._power_play_points = None
        self._shooting_percent = None
        self._shorthanded_goals = None
        self._shorthanded_points = None
        self._shots = None
        self._time_on_ice = None
        self._game_type_id = None
        self._year = None
        self._sequence = None
        self._faceoff_percent = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, value):
        self._goals = value

    @property
    def assists(self):
        return self._assists
    
    @assists.setter
    def assists(self, value):
        self._assists = value

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        self._points = value

    @property
    def plus_minus(self):
        return self._plus_minus
    
    @plus_minus.setter
    def plus_minus(self, value):
        self._plus_minus = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def game_winning_goals(self):
        return self._game_winning_goals
    
    @game_winning_goals.setter
    def game_winning_goals(self, value):
        self._game_winning_goals = value

    @property
    def ot_goals(self):
        return self._ot_goals
    
    @ot_goals.setter
    def ot_goals(self, value):
        self._ot_goals = value

    @property
    def power_play_goals(self):
        return self._power_play_goals
    
    @power_play_goals.setter
    def power_play_goals(self, value):
        self._power_play_goals = value

    @property
    def power_play_points(self):
        return self._power_play_points
    
    @power_play_points.setter
    def power_play_points(self, value):
        self._power_play_points = value

    @property
    def shooting_percent(self):
        return self._shooting_percent
    
    @shooting_percent.setter
    def shooting_percent(self, value):
        self._shooting_percent = value

    @property
    def shorthanded_goals(self):
        return self._shorthanded_goals
    
    @shorthanded_goals.setter
    def shorthanded_goals(self, value):
        self._shorthanded_goals = value

    @property
    def shorthanded_points(self):
        return self._shorthanded_points
    
    @shorthanded_points.setter
    def shorthanded_points(self, value):
        self._shorthanded_points = value

    @property
    def shots(self):
        return self._shots
    
    @shots.setter
    def shots(self, value):
        self._shots = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

    @property
    def game_type_id(self):
        return self._game_type_id
    
    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def faceoff_percent(self):
        return self._faceoff_percent
    
    @faceoff_percent.setter
    def faceoff_percent(self, value):
        self._faceoff_percent = value

class Skater:
    def __init__(self, id):
        self._player_id = id
        self._skater_stats = []
        self._youth_stats = []
        self._advanced_stats_toi = []
        self._advanced_stats_shootout = []
        self._advanced_stats_scoring = []
        self._advanced_stats_powerplay = []
        self._advanced_stats_penalty_kill = []
        self._advanced_stats_penalties = []
        self._advanced_stats_misc = []
        self._advanced_stats_goals = []
        self._advanced_stats_faceoffs = []
        self._advanced_stats_corsi_fenwick = []

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def skater_stats(self):
        return self._skater_stats
    
    @skater_stats.setter
    def skater_stats(self, value):
        self._skater_stats = value

    @property
    def youth_stats(self):
        return self._youth_stats
    
    @youth_stats.setter
    def youth_stats(self, value):
        self._youth_stats = value

    @property
    def advanced_stats_toi(self):
        return self._advanced_stats_toi
    
    @advanced_stats_toi.setter
    def advanced_stats_toi(self, value):
        self._advanced_stats_toi = value

    @property
    def advanced_stats_shootout(self):
        return self._advanced_stats_shootout
    
    @advanced_stats_shootout.setter
    def advanced_stats_shootout(self, value):
        self._advanced_stats_shootout = value

    @property
    def advanced_stats_scoring(self):
        return self._advanced_stats_scoring
    
    @advanced_stats_scoring.setter
    def advanced_stats_scoring(self, value):
        self._advanced_stats_scoring = value

    @property
    def advanced_stats_powerplay(self):
        return self._advanced_stats_powerplay
    
    @advanced_stats_powerplay.setter
    def advanced_stats_powerplay(self, value):
        self._advanced_stats_powerplay = value

    @property
    def advanced_stats_penalty_kill(self):
        return self._advanced_stats_penalty_kill
    
    @advanced_stats_penalty_kill.setter
    def advanced_stats_penalty_kill(self, value):
        self._advanced_stats_penalty_kill = value

    @property
    def advanced_stats_penalties(self):
        return self._advanced_stats_penalties
    
    @advanced_stats_penalties.setter
    def advanced_stats_penalties(self, value):
        self._advanced_stats_penalties = value

    @property
    def advanced_stats_misc(self):
        return self._advanced_stats_misc
    
    @advanced_stats_misc.setter
    def advanced_stats_misc(self, value):
        self._advanced_stats_misc = value

    @property
    def advanced_stats_goals(self):
        return self._advanced_stats_goals
    
    @advanced_stats_goals.setter
    def advanced_stats_goals(self, value):
        self._advanced_stats_goals = value

    @property
    def advanced_stats_faceoffs(self):
        return self._advanced_stats_faceoffs
    
    @advanced_stats_faceoffs.setter
    def advanced_stats_faceoffs(self, value):
        self._advanced_stats_faceoffs = value

    @property
    def advanced_stats_corsi_fenwick(self):
        return self._advanced_stats_corsi_fenwick
    
    @advanced_stats_corsi_fenwick.setter
    def advanced_stats_corsi_fenwick(self, value):
        self._advanced_stats_corsi_fenwick = value

class YouthSkaterStats:
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_name = None
        self._league_name = None
        self._game_type_id = None
        self._sequence = None
        self._games_played = None
        self._goals = None
        self._assists = None
        self._points = None
        self._pim = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_name(self):
        return self._team_name
    
    @team_name.setter
    def team_name(self, value):
        self._team_name = value

    @property
    def league_name(self):
        return self._league_name
    
    @league_name.setter
    def league_name(self, value):
        self._league_name = value

    @property
    def game_type_id(self):
        return self._game_type_id
    
    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, value):
        self._goals = value

    @property
    def assists(self):
        return self._assists
    
    @assists.setter
    def assists(self, value):
        self._assists = value

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        self._points = value

    @property
    def pim(self):
        return self._pim
    
    @pim.setter
    def pim(self, value):
        self._pim = value

class GoalieAdvancedStatsDaysRest:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._games_played = None
        self._games_played_days_rest_0 = None
        self._games_played_days_rest_1 = None
        self._games_played_days_rest_2 = None
        self._games_played_days_rest_3 = None
        self._games_played_days_rest_4_plus = None
        self._games_started = None
        self._losses = None
        self._ot_losses = None
        self._save_percent = None
        self._save_percent_days_rest_0 = None
        self._save_percent_days_rest_1 = None
        self._save_percent_days_rest_2 = None
        self._save_percent_days_rest_3 = None
        self._save_percent_days_rest_4_plus = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def games_played_days_rest_0(self):
        return self._games_played_days_rest_0
    
    @games_played_days_rest_0.setter
    def games_played_days_rest_0(self, value):
        self._games_played_days_rest_0 = value

    @property
    def games_played_days_rest_1(self):
        return self._games_played_days_rest_1
    
    @games_played_days_rest_1.setter
    def games_played_days_rest_1(self, value):
        self._games_played_days_rest_1 = value

    @property
    def games_played_days_rest_2(self):
        return self._games_played_days_rest_2
    
    @games_played_days_rest_2.setter
    def games_played_days_rest_2(self, value):
        self._games_played_days_rest_2 = value

    @property
    def games_played_days_rest_3(self):
        return self._games_played_days_rest_3
    
    @games_played_days_rest_3.setter
    def games_played_days_rest_3(self, value):
        self._games_played_days_rest_3 = value

    @property
    def games_played_days_rest_4_plus(self):
        return self._games_played_days_rest_4_plus
    
    @games_played_days_rest_4_plus.setter
    def games_played_days_rest_4_plus(self, value):
        self._games_played_days_rest_4_plus = value

    @property
    def games_started(self):
        return self._games_started
    
    @games_started.setter
    def games_started(self, value):
        self._games_started = value

    @property
    def losses(self):
        return self._losses
    
    @losses.setter
    def losses(self, value):
        self._losses = value

    @property
    def ot_losses(self):
        return self._ot_losses
    
    @ot_losses.setter
    def ot_losses(self, value):
        self._ot_losses = value

    @property
    def save_percent(self):
        return self._save_percent
    
    @save_percent.setter
    def save_percent(self, value):
        self._save_percent = value

    @property
    def save_percent_days_rest_0(self):
        return self._save_percent_days_rest_0
    
    @save_percent_days_rest_0.setter
    def save_percent_days_rest_0(self, value):
        self._save_percent_days_rest_0 = value

    @property
    def save_percent_days_rest_1(self):
        return self._save_percent_days_rest_1
    
    @save_percent_days_rest_1.setter
    def save_percent_days_rest_1(self, value):
        self._save_percent_days_rest_1 = value

    @property
    def save_percent_days_rest_2(self):
        return self._save_percent_days_rest_2
    
    @save_percent_days_rest_2.setter
    def save_percent_days_rest_2(self, value):
        self._save_percent_days_rest_2 = value

    @property
    def save_percent_days_rest_3(self):
        return self._save_percent_days_rest_3
    
    @save_percent_days_rest_3.setter
    def save_percent_days_rest_3(self, value):
        self._save_percent_days_rest_3 = value

    @property
    def save_percent_days_rest_4_plus(self):
        return self._save_percent_days_rest_4_plus
    
    @save_percent_days_rest_4_plus.setter
    def save_percent_days_rest_4_plus(self, value):
        self._save_percent_days_rest_4_plus = value

class GoalieAdvancedStatsPenaltyShots:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._penalty_shot_save_percent = None
        self._penalty_shots_against = None
        self._penalty_shots_goals_against = None
        self._penalty_shots_saves = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def penalty_shot_save_percent(self):
        return self._penalty_shot_save_percent
    
    @penalty_shot_save_percent.setter
    def penalty_shot_save_percent(self, value):
        self._penalty_shot_save_percent = value

    @property
    def penalty_shots_against(self):
        return self._penalty_shots_against
    
    @penalty_shots_against.setter
    def penalty_shots_against(self, value):
        self._penalty_shots_against = value

    @property
    def penalty_shots_goals_against(self):
        return self._penalty_shots_goals_against
    
    @penalty_shots_goals_against.setter
    def penalty_shots_goals_against(self, value):
        self._penalty_shots_goals_against = value

    @property
    def penalty_shots_saves(self):
        return self._penalty_shots_saves
    
    @penalty_shots_saves.setter
    def penalty_shots_saves(self, value):
        self._penalty_shots_saves = value

class GoalieAdvancedStatsSavesByStrength:
    
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._ev_goals_against = None
        self._ev_save_percent = None
        self._ev_saves = None
        self._ev_shots_against = None
        self._pp_goals_against = None
        self._pp_save_percent = None
        self._pp_saves = None
        self._pp_shots_against = None
        self._pk_goals_against = None
        self._pk_save_percent = None
        self._pk_saves = None
        self._pk_shots_against = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def ev_goals_against(self):
        return self._ev_goals_against
    
    @ev_goals_against.setter
    def ev_goals_against(self, value):
        self._ev_goals_against = value

    @property
    def ev_save_percent(self):
        return self._ev_save_percent
    
    @ev_save_percent.setter
    def ev_save_percent(self, value):
        self._ev_save_percent = value

    @property
    def ev_saves(self):
        return self._ev_saves
    
    @ev_saves.setter
    def ev_saves(self, value):
        self._ev_saves = value

    @property
    def ev_shots_against(self):
        return self._ev_shots_against
    
    @ev_shots_against.setter
    def ev_shots_against(self, value):
        self._ev_shots_against = value

    @property
    def pp_goals_against(self):
        return self._pp_goals_against
    
    @pp_goals_against.setter
    def pp_goals_against(self, value):
        self._pp_goals_against = value

    @property
    def pp_save_percent(self):
        return self._pp_save_percent
    
    @pp_save_percent.setter
    def pp_save_percent(self, value):
        self._pp_save_percent = value

    @property
    def pp_saves(self):
        return self._pp_saves
    
    @pp_saves.setter
    def pp_saves(self, value):
        self._pp_saves = value

    @property
    def pp_shots_against(self):
        return self._pp_shots_against
    
    @pp_shots_against.setter
    def pp_shots_against(self, value):
        self._pp_shots_against = value

    @property
    def pk_goals_against(self):
        return self._pk_goals_against
    
    @pk_goals_against.setter
    def pk_goals_against(self, value):
        self._pk_goals_against = value

    @property
    def pk_save_percent(self):
        return self._pk_save_percent
    
    @pk_save_percent.setter
    def pk_save_percent(self, value):
        self._pk_save_percent = value

    @property
    def pk_saves(self):
        return self._pk_saves
    
    @pk_saves.setter
    def pk_saves(self, value):
        self._pk_saves = value

    @property
    def pk_shots_against(self):
        return self._pk_shots_against
    
    @pk_shots_against.setter
    def pk_shots_against(self, value):
        self._pk_shots_against = value

class GoalieAdvancedStatsShootout:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._career_shootout_games_played = None
        self._career_shootout_goals_allowed = None
        self._career_shootout_losses = None
        self._career_shootout_save_percent = None
        self._career_shootout_saves = None
        self._career_shootout_shots_against = None
        self._career_shootout_wins = None
        self._shootout_goals_against = None
        self._shootout_losses = None
        self._shootout_save_percent = None
        self._shootout_saves = None
        self._shootout_shots_against = None
        self._shootout_wins = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def career_shootout_games_played(self):
        return self._career_shootout_games_played
    
    @career_shootout_games_played.setter
    def career_shootout_games_played(self, value):
        self._career_shootout_games_played = value

    @property
    def career_shootout_goals_allowed(self):
        return self._career_shootout_goals_allowed
    
    @career_shootout_goals_allowed.setter
    def career_shootout_goals_allowed(self, value):
        self._career_shootout_goals_allowed = value

    @property
    def career_shootout_losses(self):
        return self._career_shootout_losses
    
    @career_shootout_losses.setter
    def career_shootout_losses(self, value):
        self._career_shootout_losses = value

    @property
    def career_shootout_save_percent(self):
        return self._career_shootout_save_percent
    
    @career_shootout_save_percent.setter
    def career_shootout_save_percent(self, value):
        self._career_shootout_save_percent = value

    @property
    def career_shootout_saves(self):
        return self._career_shootout_saves
    
    @career_shootout_saves.setter
    def career_shootout_saves(self, value):
        self._career_shootout_saves = value

    @property
    def career_shootout_shots_against(self):
        return self._career_shootout_shots_against
    
    @career_shootout_shots_against.setter
    def career_shootout_shots_against(self, value):
        self._career_shootout_shots_against = value

    @property
    def career_shootout_wins(self):
        return self._career_shootout_wins
    
    @career_shootout_wins.setter
    def career_shootout_wins(self, value):
        self._career_shootout_wins = value

    @property
    def shootout_goals_against(self):
        return self._shootout_goals_against
    
    @shootout_goals_against.setter
    def shootout_goals_against(self, value):
        self._shootout_goals_against = value

    @property
    def shootout_losses(self):
        return self._shootout_losses
    
    @shootout_losses.setter
    def shootout_losses(self, value):
        self._shootout_losses = value

    @property
    def shootout_save_percent(self):
        return self._shootout_save_percent
    
    @shootout_save_percent.setter
    def shootout_save_percent(self, value):
        self._shootout_save_percent = value

    @property
    def shootout_saves(self):
        return self._shootout_saves
    
    @shootout_saves.setter
    def shootout_saves(self, value):
        self._shootout_saves = value

    @property
    def shootout_shots_against(self):
        return self._shootout_shots_against
    
    @shootout_shots_against.setter
    def shootout_shots_against(self, value):
        self._shootout_shots_against = value

    @property
    def shootout_wins(self):
        return self._shootout_wins
    
    @shootout_wins.setter
    def shootout_wins(self, value):
        self._shootout_wins = value

class GoalieAdvancedStatsStartRelieved:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._games_played = None
        self._games_relieved = None
        self._games_relieved_goals_against = None
        self._games_relieved_losses = None
        self._games_relieved_ot_losses = None
        self._games_relieved_save_percent = None
        self._games_relieved_saves = None
        self._games_relieved_shots_against = None
        self._games_relieved_ties = None
        self._games_relieved_wins = None
        self._games_started = None
        self._games_started_goals_against = None
        self._games_started_losses = None
        self._games_started_ot_losses = None
        self._games_started_save_percent = None
        self._games_started_saves = None
        self._games_started_shots_against = None
        self._games_started_ties = None
        self._games_started_wins = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def games_relieved(self):
        return self._games_relieved
    
    @games_relieved.setter
    def games_relieved(self, value):
        self._games_relieved = value

    @property
    def games_relieved_goals_against(self):
        return self._games_relieved_goals_against
    
    @games_relieved_goals_against.setter
    def games_relieved_goals_against(self, value):
        self._games_relieved_goals_against = value

    @property
    def games_relieved_losses(self):
        return self._games_relieved_losses
    
    @games_relieved_losses.setter
    def games_relieved_losses(self, value):
        self._games_relieved_losses = value

    @property
    def games_relieved_ot_losses(self):
        return self._games_relieved_ot_losses
    
    @games_relieved_ot_losses.setter
    def games_relieved_ot_losses(self, value):
        self._games_relieved_ot_losses = value

    @property
    def games_relieved_save_percent(self):
        return self._games_relieved_save_percent
    
    @games_relieved_save_percent.setter
    def games_relieved_save_percent(self, value):
        self._games_relieved_save_percent = value

    @property
    def games_relieved_saves(self):
        return self._games_relieved_saves
    
    @games_relieved_saves.setter
    def games_relieved_saves(self, value):
        self._games_relieved_saves = value

    @property
    def games_relieved_shots_against(self):
        return self._games_relieved_shots_against
    
    @games_relieved_shots_against.setter
    def games_relieved_shots_against(self, value):
        self._games_relieved_shots_against = value

    @property
    def games_relieved_ties(self):
        return self._games_relieved_ties
    
    @games_relieved_ties.setter
    def games_relieved_ties(self, value):
        self._games_relieved_ties = value

    @property
    def games_relieved_wins(self):
        return self._games_relieved_wins
    
    @games_relieved_wins.setter
    def games_relieved_wins(self, value):
        self._games_relieved_wins = value

    @property
    def games_started(self):
        return self._games_started
    
    @games_started.setter
    def games_started(self, value):
        self._games_started = value

    @property
    def games_started_goals_against(self):
        return self._games_started_goals_against
    
    @games_started_goals_against.setter
    def games_started_goals_against(self, value):
        self._games_started_goals_against = value

    @property
    def games_started_losses(self):
        return self._games_started_losses
    
    @games_started_losses.setter
    def games_started_losses(self, value):
        self._games_started_losses = value

    @property
    def games_started_ot_losses(self):
        return self._games_started_ot_losses
    
    @games_started_ot_losses.setter
    def games_started_ot_losses(self, value):
        self._games_started_ot_losses = value

    @property
    def games_started_save_percent(self):
        return self._games_started_save_percent
    
    @games_started_save_percent.setter
    def games_started_save_percent(self, value):
        self._games_started_save_percent = value

    @property
    def games_started_saves(self):
        return self._games_started_saves
    
    @games_started_saves.setter
    def games_started_saves(self, value):
        self._games_started_saves = value

    @property
    def games_started_shots_against(self):
        return self._games_started_shots_against
    
    @games_started_shots_against.setter
    def games_started_shots_against(self, value):
        self._games_started_shots_against = value

    @property
    def games_started_ties(self):
        return self._games_started_ties
    
    @games_started_ties.setter
    def games_started_ties(self, value):
        self._games_started_ties = value

    @property
    def games_started_wins(self):
        return self._games_started_wins
    
    @games_started_wins.setter
    def games_started_wins(self, value):
        self._games_started_wins = value

class GoalieAdvancedStats:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._complete_game_percentage = None
        self._complete_games = None
        self._games_played = None
        self._games_started = None
        self._goals_against = None
        self._goals_against_average = None
        self._goals_for = None
        self._goals_for_average = None
        self._incomplete_games = None
        self._quality_starts = None
        self._quality_starts_percent = None
        self._regulation_losses = None
        self._regulation_wins = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter 
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def complete_game_percentage(self):
        return self._complete_game_percentage
    
    @complete_game_percentage.setter
    def complete_game_percentage(self, value):
        self._complete_game_percentage = value

    @property
    def complete_games(self):
        return self._complete_games
    
    @complete_games.setter
    def complete_games(self, value):
        self._complete_games = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def games_started(self):
        return self._games_started
    
    @games_started.setter
    def games_started(self, value):
        self._games_started = value

    @property
    def goals_against(self):
        return self._goals_against
    
    @goals_against.setter
    def goals_against(self, value):
        self._goals_against = value

    @property
    def goals_against_average(self):
        return self._goals_against_average
    
    @goals_against_average.setter
    def goals_against_average(self, value):
        self._goals_against_average = value

    @property
    def goals_for(self):
        return self._goals_for
    
    @goals_for.setter
    def goals_for(self, value):
        self._goals_for = value

    @property
    def goals_for_average(self):
        return self._goals_for_average
    
    @goals_for_average.setter
    def goals_for_average(self, value):
        self._goals_for_average = value

    @property
    def incomplete_games(self):
        return self._incomplete_games
    
    @incomplete_games.setter
    def incomplete_games(self, value):
        self._incomplete_games = value

    @property
    def quality_starts(self):
        return self._quality_starts
    
    @quality_starts.setter
    def quality_starts(self, value):
        self._quality_starts = value

    @property
    def quality_starts_percent(self):
        return self._quality_starts_percent
    
    @quality_starts_percent.setter
    def quality_starts_percent(self, value):
        self._quality_starts_percent = value

    @property
    def regulation_losses(self):
        return self._regulation_losses
    
    @regulation_losses.setter
    def regulation_losses(self, value):
        self._regulation_losses = value

    @property
    def regulation_wins(self):
        return self._regulation_wins
    
    @regulation_wins.setter
    def regulation_wins(self, value):
        self._regulation_wins = value

class GoalieStats:

    def __init__(self, player_id):
        self._player_id = player_id
        self._team_id = None
        self._year = None
        self._game_type_id = None
        self._sequence = None
        self._games_played = None
        self._goals = None
        self._assists = None
        self._games_started = None
        self._wins = None
        self._losses = None
        self._ot_losses = None
        self._shots_against = None
        self._goals_against = None
        self._save_percent = None
        self._shutouts = None
        self._time_on_ice = None
        self._penalty_minutes = None
        self._goals_against_average = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def game_type_id(self):
        return self._game_type_id
    
    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, value):
        self._goals = value

    @property
    def assists(self):
        return self._assists
    
    @assists.setter
    def assists(self, value):
        self._assists = value

    @property
    def games_started(self):
        return self._games_started
    
    @games_started.setter
    def games_started(self, value):
        self._games_started = value

    @property
    def wins(self):
        return self._wins
    
    @wins.setter
    def wins(self, value):
        self._wins = value

    @property
    def losses(self):
        return self._losses
    
    @losses.setter
    def losses(self, value):
        self._losses = value

    @property
    def ot_losses(self):
        return self._ot_losses
    
    @ot_losses.setter
    def ot_losses(self, value):
        self._ot_losses = value

    @property
    def shots_against(self):
        return self._shots_against
    
    @shots_against.setter
    def shots_against(self, value):
        self._shots_against = value

    @property
    def goals_against(self):
        return self._goals_against
    
    @goals_against.setter
    def goals_against(self, value):
        self._goals_against = value

    @property
    def save_percent(self):
        return self._save_percent
    
    @save_percent.setter
    def save_percent(self, value):
        self._save_percent = value

    @property
    def shutouts(self):
        return self._shutouts
    
    @shutouts.setter
    def shutouts(self, value):
        self._shutouts = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def goals_against_average(self):
        return self._goals_against_average
    
    @goals_against_average.setter
    def goals_against_average(self, value):
        self._goals_against_average = value

class GoalieYouthStats:

    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_name = None
        self._league_name = None
        self._game_type_id = None
        self._sequence = None
        self._games_played = None
        self._save_percent = None
        self._goals_against_average = None
        self._goals_against = None
        self._wins = None
        self._losses = None
        self._time_on_ice = None
        self._ties = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_name(self):
        return self._team_name
    
    @team_name.setter
    def team_name(self, value):
        self._team_name = value

    @property
    def league_name(self):
        return self._league_name
    
    @league_name.setter
    def league_name(self, value):
        self._league_name = value

    @property
    def game_type_id(self):
        return self._game_type_id
    
    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def sequence(self):
        return self._sequence
    
    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def save_percent(self):
        return self._save_percent
    
    @save_percent.setter
    def save_percent(self, value):
        self._save_percent = value

    @property
    def goals_against_average(self):
        return self._goals_against_average
    
    @goals_against_average.setter
    def goals_against_average(self, value):
        self._goals_against_average = value

    @property
    def goals_against(self):
        return self._goals_against
    
    @goals_against.setter
    def goals_against(self, value):
        self._goals_against = value

    @property
    def wins(self):
        return self._wins
    
    @wins.setter
    def wins(self, value):
        self._wins = value

    @property
    def losses(self):
        return self._losses
    
    @losses.setter
    def losses(self, value):
        self._losses = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

    @property
    def ties(self):
        return self._ties
    
    @ties.setter
    def ties(self, value):
        self._ties = value

class Goalie:
    def __init__(self, id):
        self._id = id
        self._goalie_stats = []
        self._goalie_youth_stats = []
        self._goalie_advanced_stats = []
        self._goalie_advanced_stats_start_relieved = []
        self._goalie_advanced_stats_shootout = []
        self._goalie_advanced_stats_saves_by_strength = []
        self._goalie_advanced_stats_penalty_shots = []
        self._goalie_advanced_stats_days_rest = []

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def goalie_stats(self):
        return self._goalie_stats
    
    @goalie_stats.setter
    def goalie_stats(self, value):
        self._goalie_stats = value

    @property
    def goalie_youth_stats(self):
        return self._goalie_youth_stats
    
    @goalie_youth_stats.setter
    def goalie_youth_stats(self, value):
        self._goalie_youth_stats = value

    @property
    def goalie_advanced_stats(self):
        return self._goalie_advanced_stats
    
    @goalie_advanced_stats.setter
    def goalie_advanced_stats(self, value):
        self._goalie_advanced_stats = value

    @property
    def goalie_advanced_stats_start_relieved(self):
        return self._goalie_advanced_stats_start_relieved
    
    @goalie_advanced_stats_start_relieved.setter
    def goalie_advanced_stats_start_relieved(self, value):
        self._goalie_advanced_stats_start_relieved = value

    @property
    def goalie_advanced_stats_shootout(self):
        return self._goalie_advanced_stats_shootout
    
    @goalie_advanced_stats_shootout.setter
    def goalie_advanced_stats_shootout(self, value):
        self._goalie_advanced_stats_shootout = value

    @property
    def goalie_advanced_stats_saves_by_strength(self):
        return self._goalie_advanced_stats_saves_by_strength
    
    @goalie_advanced_stats_saves_by_strength.setter
    def goalie_advanced_stats_saves_by_strength(self, value):
        self._goalie_advanced_stats_saves_by_strength = value

    @property
    def goalie_advanced_stats_penalty_shots(self):
        return self._goalie_advanced_stats_penalty_shots
    
    @goalie_advanced_stats_penalty_shots.setter
    def goalie_advanced_stats_penalty_shots(self, value):
        self._goalie_advanced_stats_penalty_shots = value

    @property
    def goalie_advanced_stats_days_rest(self):
        return self._goalie_advanced_stats_days_rest
    
    @goalie_advanced_stats_days_rest.setter
    def goalie_advanced_stats_days_rest(self, value):
        self._goalie_advanced_stats_days_rest = value

class PlayerAwards:

    def __init__(self, player_id):
        self._player_id = player_id
        self._award = None
        self._year = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def award(self):
        return self._award
    
    @award.setter
    def award(self, value):
        self._award = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

class PlayerDetails:
    def __init__(self, player_id):
        self._player_id = player_id 
        self._first_name = None
        self._last_name = None
        self._jersey_number = None
        self._position = None
        self._headshot = None
        self._hero_image = None
        self._height_inches = None
        self._weight_pounds = None
        self._birth_date = None
        self._birth_city = None
        self._birth_state_province = None
        self._birth_country = None
        self._shoots_catches = None
        self._in_top_100_all_time = None
        self._in_hhof = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def jersey_number(self):
        return self._jersey_number
    
    @jersey_number.setter
    def jersey_number(self, value):
        self._jersey_number = value

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def headshot(self):
        return self._headshot
    
    @headshot.setter
    def headshot(self, value):
        self._headshot = value

    @property
    def hero_image(self):
        return self._hero_image
    
    @hero_image.setter
    def hero_image(self, value):
        self._hero_image = value

    @property
    def height_inches(self):
        return self._height_inches
    
    @height_inches.setter
    def height_inches(self, value):
        self._height_inches = value

    @property
    def weight_pounds(self):
        return self._weight_pounds
    
    @weight_pounds.setter
    def weight_pounds(self, value):
        self._weight_pounds = value

    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def birth_city(self):
        return self._birth_city
    
    @birth_city.setter
    def birth_city(self, value):
        self._birth_city = value

    @property
    def birth_state_province(self):
        return self._birth_state_province
    
    @birth_state_province.setter
    def birth_state_province(self, value):
        self._birth_state_province = value

    @property
    def birth_country(self):
        return self._birth_country
    
    @birth_country.setter
    def birth_country(self, value):
        self._birth_country = value

    @property
    def shoots_catches(self):
        return self._shoots_catches
    
    @shoots_catches.setter
    def shoots_catches(self, value):
        self._shoots_catches = value

    @property
    def in_top_100_all_time(self):
        return self._in_top_100_all_time
    
    @in_top_100_all_time.setter
    def in_top_100_all_time(self, value):
        self._in_top_100_all_time = value

    @property
    def in_hhof(self):
        return self._in_hhof
    
    @in_hhof.setter
    def in_hhof(self, value):
        self._in_hhof = value

class PlayerDraft:
    def __init__(self, player_id):
        self._player_id = player_id
        self._year = None
        self._team_id = None
        self._round = None
        self._pick_in_round = None
        self._overall_pick = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def round(self):
        return self._round
    
    @round.setter
    def round(self, value):
        self._round = value

    @property
    def pick_in_round(self):
        return self._pick_in_round
    
    @pick_in_round.setter
    def pick_in_round(self, value):
        self._pick_in_round = value

    @property
    def overall_pick(self):
        return self._overall_pick
    
    @overall_pick.setter
    def overall_pick(self, value):
        self._overall_pick = value

class Player:
    def __init__(self, player_id):
        self._player_id = player_id
        self._team_id = None
        self._is_active = None
        self._player_draft = None
        self._player_awards = []
        self._player_details = None

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def is_active(self):
        return self._is_active
    
    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    @property
    def player_draft(self):
        return self._player_draft
    
    @player_draft.setter
    def player_draft(self, value):
        self._player_draft = value

    @property
    def player_awards(self):
        return self._player_awards
    
    @player_awards.setter
    def player_awards(self, value):
        self._player_awards = value

    @property
    def player_details(self):
        return self._player_details
    
    @player_details.setter
    def player_details(self, value):
        self._player_details = value

class TeamAdvancedStats:
    def __init__(self, team_id):
        self._team_id = team_id
        self._team_advanced_stats_days_rest: list[TeamAdvancedStatsDaysRest] = []
        self._team_advanced_stats_corsi_fenwick = []
        self._team_advanced_stats_faceoff_percent = []
        self._team_advanced_stats_goals_by_period = []
        self._team_advanced_stats_goals_by_strength = []
        self._team_advanced_stats_leading_trailing = []
        self._team_advanced_stats_misc = []
        self._team_advanced_stats_outshoot_outshot = []
        self._team_advanced_stats_penalties = []
        self._team_advanced_stats_powerplay_penalty_kill = []
        self._team_advanced_stats_scoring_first = []
        self._team_advanced_stats_shot_type = []
        self._team_advanced_stats_team_goal_games = []

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value
    
    @property
    def team_advanced_stats_days_rest(self):
        return self._team_advanced_stats_days_rest
    
    @team_advanced_stats_days_rest.setter
    def team_advanced_stats_days_rest(self, value):
        self._team_advanced_stats_days_rest = value

    @property
    def team_advanced_stats_corsi_fenwick(self):
        return self._team_advanced_stats_corsi_fenwick
    
    @team_advanced_stats_corsi_fenwick.setter
    def team_advanced_stats_corsi_fenwick(self, value):
        self._team_advanced_stats_corsi_fenwick = value

    @property
    def team_advanced_stats_faceoff_percent(self):
        return self._team_advanced_stats_faceoff_percent
    
    @team_advanced_stats_faceoff_percent.setter
    def team_advanced_stats_faceoff_percent(self, value):
        self._team_advanced_stats_faceoff_percent = value

    @property
    def team_advanced_stats_goals_by_period(self):
        return self._team_advanced_stats_goals_by_period
    
    @team_advanced_stats_goals_by_period.setter
    def team_advanced_stats_goals_by_period(self, value):
        self._team_advanced_stats_goals_by_period = value

    @property
    def team_advanced_stats_goals_by_strength(self):
        return self._team_advanced_stats_goals_by_strength
    
    @team_advanced_stats_goals_by_strength.setter
    def team_advanced_stats_goals_by_strength(self, value):
        self._team_advanced_stats_goals_by_strength = value

    @property
    def team_advanced_stats_leading_trailing(self):
        return self._team_advanced_stats_leading_trailing
    
    @team_advanced_stats_leading_trailing.setter
    def team_advanced_stats_leading_trailing(self, value):
        self._team_advanced_stats_leading_trailing = value

    @property
    def team_advanced_stats_misc(self):
        return self._team_advanced_stats_misc
    
    @team_advanced_stats_misc.setter
    def team_advanced_stats_misc(self, value):
        self._team_advanced_stats_misc = value

    @property
    def team_advanced_stats_outshoot_outshot(self):
        return self._team_advanced_stats_outshoot_outshot
    
    @team_advanced_stats_outshoot_outshot.setter
    def team_advanced_stats_outshoot_outshot(self, value):
        self._team_advanced_stats_outshoot_outshot = value

    @property
    def team_advanced_stats_penalties(self):
        return self._team_advanced_stats_penalties
    
    @team_advanced_stats_penalties.setter
    def team_advanced_stats_penalties(self, value):
        self._team_advanced_stats_penalties = value

    @property
    def team_advanced_stats_powerplay_penalty_kill(self):
        return self._team_advanced_stats_powerplay_penalty_kill
    
    @team_advanced_stats_powerplay_penalty_kill.setter
    def team_advanced_stats_powerplay_penalty_kill(self, value):
        self._team_advanced_stats_powerplay_penalty_kill = value

    @property
    def team_advanced_stats_scoring_first(self):
        return self._team_advanced_stats_scoring_first
    
    @team_advanced_stats_scoring_first.setter
    def team_advanced_stats_scoring_first(self, value):
        self._team_advanced_stats_scoring_first = value

    @property
    def team_advanced_stats_shot_type(self):
        return self._team_advanced_stats_shot_type
    
    @team_advanced_stats_shot_type.setter
    def team_advanced_stats_shot_type(self, value):
        self._team_advanced_stats_shot_type = value

    @property
    def team_advanced_stats_team_goal_games(self):
        return self._team_advanced_stats_team_goal_games
    
    @team_advanced_stats_team_goal_games.setter
    def team_advanced_stats_team_goal_games(self, value):
        self._team_advanced_stats_team_goal_games = value

class Team:
    def __init__(self, team_id):
        self._team_id = team_id
        self._team_data: TeamData = None
        self._team_stats: TeamStats = None
        

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def team_data(self):
        return self._team_data
    
    @team_data.setter
    def team_data(self, value):
        self._team_data = value

    @property
    def team_stats(self):
        return self._team_stats
    
    @team_stats.setter
    def team_stats(self, value):
        self._team_stats = value

class TeamStats:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._game_type_id = None
        self._games_played = None
        self._goals_against = None
        self._goals_for = None
        self._losses = None
        self._ot_losses = None
        self._points = None
        self._shootout_losses = None
        self._shootout_wins = None
        self._streak_code = None
        self._streak_count = None
        self._ties = None
        self._waiver_sequence = None
        self._regulation_wins = None
        self._regulation_plus_ot_wins = None
        self._home_games_played = None
        self._home_goals_against = None
        self._home_goals_for = None
        self._home_losses = None
        self._home_ot_losses = None
        self._home_points = None
        self._home_regulation_wins = None
        self._home_regulation_plus_ot_wins = None
        self._home_ties = None
        self._home_wins = None
        self._last_10_games_played = None
        self._last_10_goals_against = None
        self._last_10_goals_for = None
        self._last_10_losses = None
        self._last_10_ot_losses = None
        self._last_10_points = None
        self._last_10_regulation_wins = None
        self._last_10_regulation_plus_ot_wins = None
        self._last_10_ties = None
        self._last_10_wins = None
        self._road_games_played = None
        self._road_goals_against = None
        self._road_goals_for = None  
        self._road_losses = None
        self._road_ot_losses = None
        self._road_points = None
        self._road_regulation_wins = None
        self._road_regulation_plus_ot_wins = None
        self._road_ties = None
        self._road_wins = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def game_type_id(self):
        return self._game_type_id

    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def games_played(self):
        return self._games_played

    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def goals_against(self):
        return self._goals_against

    @goals_against.setter
    def goals_against(self, value):
        self._goals_against = value

    @property
    def goals_for(self):
        return self._goals_for

    @goals_for.setter
    def goals_for(self, value):
        self._goals_for = value

    @property
    def losses(self):
        return self._losses

    @losses.setter
    def losses(self, value):
        self._losses = value

    @property
    def ot_losses(self):
        return self._ot_losses

    @ot_losses.setter
    def ot_losses(self, value):
        self._ot_losses = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def shootout_losses(self):
        return self._shootout_losses

    @shootout_losses.setter
    def shootout_losses(self, value):
        self._shootout_losses = value

    @property
    def shootout_wins(self):
        return self._shootout_wins

    @shootout_wins.setter
    def shootout_wins(self, value):
        self._shootout_wins = value

    @property
    def streak_code(self):
        return self._streak_code

    @streak_code.setter
    def streak_code(self, value):
        self._streak_code = value

    @property
    def streak_count(self):
        return self._streak_count

    @streak_count.setter
    def streak_count(self, value):
        self._streak_count = value

    @property
    def ties(self):
        return self._ties

    @ties.setter
    def ties(self, value):
        self._ties = value

    @property
    def waiver_sequence(self):
        return self._waiver_sequence

    @waiver_sequence.setter
    def waiver_sequence(self, value):
        self._waiver_sequence = value

    @property
    def regulation_wins(self):
        return self._regulation_wins

    @regulation_wins.setter
    def regulation_wins(self, value):
        self._regulation_wins = value

    @property
    def regulation_plus_ot_wins(self):
        return self._regulation_plus_ot_wins

    @regulation_plus_ot_wins.setter
    def regulation_plus_ot_wins(self, value):
        self._regulation_plus_ot_wins = value

    @property
    def home_games_played(self):
        return self._home_games_played

    @home_games_played.setter
    def home_games_played(self, value):
        self._home_games_played = value

    @property
    def home_goals_against(self):
        return self._home_goals_against

    @home_goals_against.setter
    def home_goals_against(self, value):
        self._home_goals_against = value

    @property
    def home_goals_for(self):
        return self._home_goals_for

    @home_goals_for.setter
    def home_goals_for(self, value):
        self._home_goals_for = value

    @property
    def home_losses(self):
        return self._home_losses

    @home_losses.setter
    def home_losses(self, value):
        self._home_losses = value

    @property
    def home_ot_losses(self):
        return self._home_ot_losses

    @home_ot_losses.setter
    def home_ot_losses(self, value):
        self._home_ot_losses = value

    @property
    def home_points(self):
        return self._home_points

    @home_points.setter
    def home_points(self, value):
        self._home_points = value

    @property
    def home_regulation_wins(self):
        return self._home_regulation_wins

    @home_regulation_wins.setter
    def home_regulation_wins(self, value):
        self._home_regulation_wins = value

    @property
    def home_regulation_plus_ot_wins(self):
        return self._home_regulation_plus_ot_wins

    @home_regulation_plus_ot_wins.setter
    def home_regulation_plus_ot_wins(self, value):
        self._home_regulation_plus_ot_wins = value

    @property
    def home_ties(self):
        return self._home_ties

    @home_ties.setter
    def home_ties(self, value):
        self._home_ties = value

    @property
    def home_wins(self):
        return self._home_wins

    @home_wins.setter
    def home_wins(self, value):
        self._home_wins = value

    @property
    def last_10_games_played(self):
        return self._last_10_games_played

    @last_10_games_played.setter
    def last_10_games_played(self, value):
        self._last_10_games_played = value

    @property
    def last_10_goals_against(self):
        return self._last_10_goals_against

    @last_10_goals_against.setter
    def last_10_goals_against(self, value):
        self._last_10_goals_against = value

    @property
    def last_10_goals_for(self):
        return self._last_10_goals_for

    @last_10_goals_for.setter
    def last_10_goals_for(self, value):
        self._last_10_goals_for = value

    @property
    def last_10_losses(self):
        return self._last_10_losses

    @last_10_losses.setter
    def last_10_losses(self, value):
        self._last_10_losses = value

    @property
    def last_10_ot_losses(self):
        return self._last_10_ot_losses

    @last_10_ot_losses.setter
    def last_10_ot_losses(self, value):
        self._last_10_ot_losses = value

    @property
    def last_10_points(self):
        return self._last_10_points

    @last_10_points.setter
    def last_10_points(self, value):
        self._last_10_points = value

    @property
    def last_10_regulation_wins(self):
        return self._last_10_regulation_wins
    
    @last_10_regulation_wins.setter
    def last_10_regulation_wins(self, value):
        self._last_10_regulation_wins = value

    @property
    def last_10_regulation_plus_ot_wins(self):
        return self._last_10_regulation_plus_ot_wins

    @last_10_regulation_plus_ot_wins.setter
    def last_10_regulation_plus_ot_wins(self, value):
        self._last_10_regulation_plus_ot_wins = value

    @property
    def last_10_ties(self):
        return self._last_10_ties

    @last_10_ties.setter
    def last_10_ties(self, value):
        self._last_10_ties = value

    @property
    def last_10_wins(self):
        return self._last_10_wins

    @last_10_wins.setter
    def last_10_wins(self, value):
        self._last_10_wins = value

    @property
    def road_games_played(self):
        return self._road_games_played

    @road_games_played.setter
    def road_games_played(self, value):
        self._road_games_played = value

    @property
    def road_goals_against(self):
        return self._road_goals_against

    @road_goals_against.setter
    def road_goals_against(self, value):
        self._road_goals_against = value

    @property
    def road_goals_for(self):
        return self._road_goals_for

    @road_goals_for.setter
    def road_goals_for(self, value):
        self._road_goals_for = value

    @property
    def road_losses(self):
        return self._road_losses

    @road_losses.setter
    def road_losses(self, value):
        self._road_losses = value

    @property
    def road_ot_losses(self):
        return self._road_ot_losses

    @road_ot_losses.setter
    def road_ot_losses(self, value):
        self._road_ot_losses = value

    @property
    def road_points(self):
        return self._road_points

    @road_points.setter
    def road_points(self, value):
        self._road_points = value

    @property
    def road_regulation_wins(self):
        return self._road_regulation_wins

    @road_regulation_wins.setter
    def road_regulation_wins(self, value):
        self._road_regulation_wins = value

    @property
    def road_regulation_plus_ot_wins(self):
        return self._road_regulation_plus_ot_wins

    @road_regulation_plus_ot_wins.setter
    def road_regulation_plus_ot_wins(self, value):
        self._road_regulation_plus_ot_wins = value

    @property
    def road_ties(self):
        return self._road_ties

    @road_ties.setter
    def road_ties(self, value):
        self._road_ties = value

    @property
    def road_wins(self):
        return self._road_wins

    @road_wins.setter
    def road_wins(self, value):
        self._road_wins = value

class TeamData:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._conference_name = None
        self._division_name = None
        self._place_name = None
        self._team_name = None
        self._team_abbreviation = None
        self._team_logo = None
        self._team_color_1 = None
        self._team_color_2 = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def conference_name(self):
        return self._conference_name

    @conference_name.setter
    def conference_name(self, value):
        self._conference_name = value

    @property
    def division_name(self):
        return self._division_name

    @division_name.setter
    def division_name(self, value):
        self._division_name = value

    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value

    @property
    def team_name(self):
        return self._team_name

    @team_name.setter
    def team_name(self, value):
        self._team_name = value

    @property
    def team_abbreviation(self):
        return self._team_abbreviation

    @team_abbreviation.setter
    def team_abbreviation(self, value):
        self._team_abbreviation = value

    @property
    def team_logo(self):
        return self._team_logo

    @team_logo.setter
    def team_logo(self, value):
        self._team_logo = value

    @property
    def team_color_1(self):
        return self._team_color_1

    @team_color_1.setter
    def team_color_1(self, value):
        self._team_color_1 = value

    @property
    def team_color_2(self):
        return self._team_color_2

    @team_color_2.setter
    def team_color_2(self, value):
        self._team_color_2 = value    

class TeamAdvancedStatsTeamGoalGames:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._losses_one_goal_games = None
        self._losses_two_goal_games = None
        self._losses_three_goal_games = None
        self._ot_losses_one_goal_games = None
        self._win_percent_one_goal_games = None
        self._win_percent_two_goal_games = None
        self._win_percent_three_goal_games = None
        self._wins_one_goal_games = None
        self._wins_two_goal_games = None
        self._wins_three_goal_games = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def losses_one_goal_games(self):
        return self._losses_one_goal_games

    @losses_one_goal_games.setter
    def losses_one_goal_games(self, value):
        self._losses_one_goal_games = value

    @property
    def losses_two_goal_games(self):
        return self._losses_two_goal_games

    @losses_two_goal_games.setter
    def losses_two_goal_games(self, value):
        self._losses_two_goal_games = value

    @property
    def losses_three_goal_games(self):
        return self._losses_three_goal_games

    @losses_three_goal_games.setter
    def losses_three_goal_games(self, value):
        self._losses_three_goal_games = value

    @property
    def ot_losses_one_goal_games(self):
        return self._ot_losses_one_goal_games

    @ot_losses_one_goal_games.setter
    def ot_losses_one_goal_games(self, value):
        self._ot_losses_one_goal_games = value

    @property
    def win_percent_one_goal_games(self):
        return self._win_percent_one_goal_games

    @win_percent_one_goal_games.setter
    def win_percent_one_goal_games(self, value):
        self._win_percent_one_goal_games = value

    @property
    def win_percent_two_goal_games(self):
        return self._win_percent_two_goal_games

    @win_percent_two_goal_games.setter
    def win_percent_two_goal_games(self, value):
        self._win_percent_two_goal_games = value

    @property
    def win_percent_three_goal_games(self):
        return self._win_percent_three_goal_games

    @win_percent_three_goal_games.setter
    def win_percent_three_goal_games(self, value):
        self._win_percent_three_goal_games = value

    @property
    def wins_one_goal_games(self):
        return self._wins_one_goal_games

    @wins_one_goal_games.setter
    def wins_one_goal_games(self, value):
        self._wins_one_goal_games = value

    @property
    def wins_two_goal_games(self):
        return self._wins_two_goal_games

    @wins_two_goal_games.setter
    def wins_two_goal_games(self, value):
        self._wins_two_goal_games = value

    @property
    def wins_three_goal_games(self):
        return self._wins_three_goal_games

    @wins_three_goal_games.setter
    def wins_three_goal_games(self, value):
        self._wins_three_goal_games = value

class TeamAdvancedStatsShotType:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._goals_backhand = None
        self._goals_deflected = None
        self._goals_for = None
        self._goals_slap = None
        self._goals_snap = None
        self._goals_tip_in = None
        self._goals_wrap_around = None
        self._goals_wrist = None
        self._shooting_percent_backhand = None
        self._shooting_percent_deflected = None
        self._shooting_percent_slap = None
        self._shooting_percent_snap = None
        self._shooting_percent_tip_in = None
        self._shooting_percent_wrap_around = None
        self._shooting_percent_wrist = None
        self._shots_on_net_backhand = None
        self._shots_on_net_deflected = None
        self._shots_on_net_slap = None
        self._shots_on_net_snap = None
        self._shots_on_net_tip_in = None
        self._shots_on_net_wrap_around = None
        self._shots_on_net_wrist = None
        self._shots_attempted_backhand = None
        self._shots_attempted_deflected = None
        self._shots_attempted_slap = None
        self._shots_attempted_snap = None
        self._shots_attempted_tip_in = None
        self._shots_attempted_wrap_around = None
        self._shots_attempted_wrist = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def goals_backhand(self):
        return self._goals_backhand

    @goals_backhand.setter
    def goals_backhand(self, value):
        self._goals_backhand = value

    @property
    def goals_deflected(self):
        return self._goals_deflected

    @goals_deflected.setter
    def goals_deflected(self, value):
        self._goals_deflected = value

    @property
    def goals_for(self):
        return self._goals_for

    @goals_for.setter
    def goals_for(self, value):
        self._goals_for = value

    @property
    def goals_slap(self):
        return self._goals_slap

    @goals_slap.setter
    def goals_slap(self, value):
        self._goals_slap = value

    @property
    def goals_snap(self):
        return self._goals_snap

    @goals_snap.setter
    def goals_snap(self, value):
        self._goals_snap = value

    @property
    def goals_tip_in(self):
        return self._goals_tip_in

    @goals_tip_in.setter
    def goals_tip_in(self, value):
        self._goals_tip_in = value

    @property
    def goals_wrap_around(self):
        return self._goals_wrap_around

    @goals_wrap_around.setter
    def goals_wrap_around(self, value):
        self._goals_wrap_around = value

    @property
    def goals_wrist(self):
        return self._goals_wrist

    @goals_wrist.setter
    def goals_wrist(self, value):
        self._goals_wrist = value

    @property
    def shooting_percent_backhand(self):
        return self._shooting_percent_backhand

    @shooting_percent_backhand.setter
    def shooting_percent_backhand(self, value):
        self._shooting_percent_backhand = value

    @property
    def shooting_percent_deflected(self):
        return self._shooting_percent_deflected

    @shooting_percent_deflected.setter
    def shooting_percent_deflected(self, value):
        self._shooting_percent_deflected = value

    @property
    def shooting_percent_slap(self):
        return self._shooting_percent_slap

    @shooting_percent_slap.setter
    def shooting_percent_slap(self, value):
        self._shooting_percent_slap = value

    @property
    def shooting_percent_snap(self):
        return self._shooting_percent_snap

    @shooting_percent_snap.setter
    def shooting_percent_snap(self, value):
        self._shooting_percent_snap = value

    @property
    def shooting_percent_tip_in(self):
        return self._shooting_percent_tip_in

    @shooting_percent_tip_in.setter
    def shooting_percent_tip_in(self, value):
        self._shooting_percent_tip_in = value

    @property
    def shooting_percent_wrap_around(self):
        return self._shooting_percent_wrap_around

    @shooting_percent_wrap_around.setter
    def shooting_percent_wrap_around(self, value):
        self._shooting_percent_wrap_around = value

    @property
    def shooting_percent_wrist(self):
        return self._shooting_percent_wrist

    @shooting_percent_wrist.setter
    def shooting_percent_wrist(self, value):
        self._shooting_percent_wrist = value

    @property
    def shots_on_net_backhand(self):
        return self._shots_on_net_backhand

    @shots_on_net_backhand.setter
    def shots_on_net_backhand(self, value):
        self._shots_on_net_backhand = value

    @property
    def shots_on_net_deflected(self):
        return self._shots_on_net_deflected

    @shots_on_net_deflected.setter
    def shots_on_net_deflected(self, value):
        self._shots_on_net_deflected = value

    @property
    def shots_on_net_slap(self):
        return self._shots_on_net_slap

    @shots_on_net_slap.setter
    def shots_on_net_slap(self, value):
        self._shots_on_net_slap = value

    @property
    def shots_on_net_snap(self):
        return self._shots_on_net_snap

    @shots_on_net_snap.setter
    def shots_on_net_snap(self, value):
        self._shots_on_net_snap = value

    @property
    def shots_on_net_tip_in(self):
        return self._shots_on_net_tip_in

    @shots_on_net_tip_in.setter
    def shots_on_net_tip_in(self, value):
        self._shots_on_net_tip_in = value

    @property
    def shots_on_net_wrap_around(self):
        return self._shots_on_net_wrap_around

    @shots_on_net_wrap_around.setter
    def shots_on_net_wrap_around(self, value):
        self._shots_on_net_wrap_around = value

    @property
    def shots_on_net_wrist(self):
        return self._shots_on_net_wrist

    @shots_on_net_wrist.setter
    def shots_on_net_wrist(self, value):
        self._shots_on_net_wrist = value

    @property
    def shots_attempted_backhand(self):
        return self._shots_attempted_backhand

    @shots_attempted_backhand.setter
    def shots_attempted_backhand(self, value):
        self._shots_attempted_backhand = value

    @property
    def shots_attempted_deflected(self):
        return self._shots_attempted_deflected

    @shots_attempted_deflected.setter
    def shots_attempted_deflected(self, value):
        self._shots_attempted_deflected = value

    @property
    def shots_attempted_slap(self):
        return self._shots_attempted_slap

    @shots_attempted_slap.setter
    def shots_attempted_slap(self, value):
        self._shots_attempted_slap = value

    @property
    def shots_attempted_snap(self):
        return self._shots_attempted_snap

    @shots_attempted_snap.setter
    def shots_attempted_snap(self, value):
        self._shots_attempted_snap = value

    @property
    def shots_attempted_tip_in(self):
        return self._shots_attempted_tip_in

    @shots_attempted_tip_in.setter
    def shots_attempted_tip_in(self, value):
        self._shots_attempted_tip_in = value

    @property
    def shots_attempted_wrap_around(self):
        return self._shots_attempted_wrap_around

    @shots_attempted_wrap_around.setter
    def shots_attempted_wrap_around(self, value):
        self._shots_attempted_wrap_around = value

    @property
    def shots_attempted_wrist(self):
        return self._shots_attempted_wrist

    @shots_attempted_wrist.setter
    def shots_attempted_wrist(self, value):
        self._shots_attempted_wrist = value

class TeamAdvancedStatsScoringFirst:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._losses_scoring_first = None
        self._losses_trailing_first = None
        self._ot_losses_scoring_first = None
        self._ot_losses_trailing_first = None
        self._scoring_first_games_played = None
        self._ties_scoring_first = None
        self._ties_trailing_first = None
        self._trailing_first_games_played = None
        self._win_percent_scoring_first = None
        self._win_percent_trailing_first = None
        self._wins_scoring_first = None
        self._wins_trailing_first = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def losses_scoring_first(self):
        return self._losses_scoring_first

    @losses_scoring_first.setter
    def losses_scoring_first(self, value):
        self._losses_scoring_first = value

    @property
    def losses_trailing_first(self):
        return self._losses_trailing_first

    @losses_trailing_first.setter
    def losses_trailing_first(self, value):
        self._losses_trailing_first = value

    @property
    def ot_losses_scoring_first(self):
        return self._ot_losses_scoring_first

    @ot_losses_scoring_first.setter
    def ot_losses_scoring_first(self, value):
        self._ot_losses_scoring_first = value

    @property
    def ot_losses_trailing_first(self):
        return self._ot_losses_trailing_first

    @ot_losses_trailing_first.setter
    def ot_losses_trailing_first(self, value):
        self._ot_losses_trailing_first = value

    @property
    def scoring_first_games_played(self):
        return self._scoring_first_games_played

    @scoring_first_games_played.setter
    def scoring_first_games_played(self, value):
        self._scoring_first_games_played = value

    @property
    def ties_scoring_first(self):
        return self._ties_scoring_first

    @ties_scoring_first.setter
    def ties_scoring_first(self, value):
        self._ties_scoring_first = value

    @property
    def ties_trailing_first(self):
        return self._ties_trailing_first

    @ties_trailing_first.setter
    def ties_trailing_first(self, value):
        self._ties_trailing_first = value

    @property
    def trailing_first_games_played(self):
        return self._trailing_first_games_played

    @trailing_first_games_played.setter
    def trailing_first_games_played(self, value):
        self._trailing_first_games_played = value

    @property
    def win_percent_scoring_first(self):
        return self._win_percent_scoring_first

    @win_percent_scoring_first.setter
    def win_percent_scoring_first(self, value):
        self._win_percent_scoring_first = value

    @property
    def win_percent_trailing_first(self):
        return self._win_percent_trailing_first

    @win_percent_trailing_first.setter
    def win_percent_trailing_first(self, value):
        self._win_percent_trailing_first = value

    @property
    def wins_scoring_first(self):
        return self._wins_scoring_first

    @wins_scoring_first.setter
    def wins_scoring_first(self, value):
        self._wins_scoring_first = value

    @property
    def wins_trailing_first(self):
        return self._wins_trailing_first

    @wins_trailing_first.setter
    def wins_trailing_first(self, value):
        self._wins_trailing_first = value

class TeamAdvancedStatsPowerplayPenaltyKill:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._pk_net_percent = None
        self._pk_percent = None
        self._pk_net_goals = None
        self._pk_net_goals_for_per_game = None
        self._pk_time_on_ice_per_game = None
        self._pk_goals_against = None
        self._pk_goals_against_per_game = None
        self._pk_goals_for = None
        self._pk_goals_for_per_game = None
        self._times_shorthanded = None
        self._times_shorthanded_per_game = None
        self._overall_penalty_kill_percent = None
        self._penalty_kill_percent_3on4 = None
        self._penalty_kill_percent_3on5 = None
        self._penalty_kill_percent_4on5 = None
        self._time_on_ice_3on4 = None
        self._time_on_ice_3on5 = None
        self._time_on_ice_4on5 = None
        self._time_on_ice_shorthanded = None
        self._time_shorthanded_3v4 = None
        self._time_shorthanded_3v5 = None
        self._time_shorthanded_4v5 = None
        self._pp_goals_for = None
        self._pp_net_percent = None
        self._pp_percent = None
        self._pp_goals_per_game = None
        self._pp_net_goals = None
        self._pp_net_goals_for_per_game = None
        self._pp_opportunites = None
        self._pp_opportunities_per_game = None
        self._pp_time_on_ice_per_game = None
        self._pp_goals_against = None
        self._pp_goals_against_per_game = None
        self._opportunities_4on3 = None
        self._opportunities_5on3 = None
        self._opportunities_5on4 = None
        self._pp_percent_4on3 = None
        self._pp_percent_5on3 = None
        self._pp_percent_5on4 = None
        self._time_on_ice_4on3 = None
        self._time_on_ice_5on3 = None
        self._time_on_ice_5on4 = None
        self._pp_time_on_ice = None
        self._goals_against_3on4 = None
        self._goals_against_3on5 = None
        self._goals_against_4on5 = None
        self._goals_4on3 = None
        self._goals_5on3 = None
        self._goals_5on4 = None

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def pk_net_percent(self):
        return self._pk_net_percent

    @pk_net_percent.setter
    def pk_net_percent(self, value):
        self._pk_net_percent = value

    @property
    def pk_percent(self):
        return self._pk_percent

    @pk_percent.setter
    def pk_percent(self, value):
        self._pk_percent = value

    @property
    def pk_net_goals(self):
        return self._pk_net_goals

    @pk_net_goals.setter
    def pk_net_goals(self, value):
        self._pk_net_goals = value

    @property
    def pk_net_goals_for_per_game(self):
        return self._pk_net_goals_for_per_game

    @pk_net_goals_for_per_game.setter
    def pk_net_goals_for_per_game(self, value):
        self._pk_net_goals_for_per_game = value

    @property
    def pk_time_on_ice_per_game(self):
        return self._pk_time_on_ice_per_game

    @pk_time_on_ice_per_game.setter
    def pk_time_on_ice_per_game(self, value):
        self._pk_time_on_ice_per_game = value

    @property
    def pk_goals_against(self):
        return self._pk_goals_against

    @pk_goals_against.setter
    def pk_goals_against(self, value):
        self._pk_goals_against = value

    @property
    def pk_goals_against_per_game(self):
        return self._pk_goals_against_per_game

    @pk_goals_against_per_game.setter
    def pk_goals_against_per_game(self, value):
        self._pk_goals_against_per_game = value

    @property
    def pk_goals_for(self):
        return self._pk_goals_for

    @pk_goals_for.setter
    def pk_goals_for(self, value):
        self._pk_goals_for = value

    @property
    def pk_goals_for_per_game(self):
        return self._pk_goals_for_per_game

    @pk_goals_for_per_game.setter
    def pk_goals_for_per_game(self, value):
        self._pk_goals_for_per_game = value

    @property
    def times_shorthanded(self):
        return self._times_shorthanded

    @times_shorthanded.setter
    def times_shorthanded(self, value):
        self._times_shorthanded = value

    @property
    def times_shorthanded_per_game(self):
        return self._times_shorthanded_per_game

    @times_shorthanded_per_game.setter
    def times_shorthanded_per_game(self, value):
        self._times_shorthanded_per_game = value

    @property
    def overall_penalty_kill_percent(self):
        return self._overall_penalty_kill_percent

    @overall_penalty_kill_percent.setter
    def overall_penalty_kill_percent(self, value):
        self._overall_penalty_kill_percent = value

    @property
    def penalty_kill_percent_3on4(self):
        return self._penalty_kill_percent_3on4

    @penalty_kill_percent_3on4.setter
    def penalty_kill_percent_3on4(self, value):
        self._penalty_kill_percent_3on4 = value

    @property
    def penalty_kill_percent_3on5(self):
        return self._penalty_kill_percent_3on5

    @penalty_kill_percent_3on5.setter
    def penalty_kill_percent_3on5(self, value):
        self._penalty_kill_percent_3on5 = value

    @property
    def penalty_kill_percent_4on5(self):
        return self._penalty_kill_percent_4on5

    @penalty_kill_percent_4on5.setter
    def penalty_kill_percent_4on5(self, value):
        self._penalty_kill_percent_4on5 = value

    @property
    def time_on_ice_3on4(self):
        return self._time_on_ice_3on4

    @time_on_ice_3on4.setter
    def time_on_ice_3on4(self, value):
        self._time_on_ice_3on4 = value

    @property
    def time_on_ice_3on5(self):
        return self._time_on_ice_3on5

    @time_on_ice_3on5.setter
    def time_on_ice_3on5(self, value):
        self._time_on_ice_3on5 = value

    @property
    def time_on_ice_4on5(self):
        return self._time_on_ice_4on5

    @time_on_ice_4on5.setter
    def time_on_ice_4on5(self, value):
        self._time_on_ice_4on5 = value

    @property
    def time_on_ice_shorthanded(self):
        return self._time_on_ice_shorthanded

    @time_on_ice_shorthanded.setter
    def time_on_ice_shorthanded(self, value):
        self._time_on_ice_shorthanded = value

    @property
    def time_shorthanded_3v4(self):
        return self._time_shorthanded_3v4

    @time_shorthanded_3v4.setter
    def time_shorthanded_3v4(self, value):
        self._time_shorthanded_3v4 = value

    @property
    def time_shorthanded_3v5(self):
        return self._time_shorthanded_3v5

    @time_shorthanded_3v5.setter
    def time_shorthanded_3v5(self, value):
        self._time_shorthanded_3v5 = value

    @property
    def time_shorthanded_4v5(self):
        return self._time_shorthanded_4v5

    @time_shorthanded_4v5.setter
    def time_shorthanded_4v5(self, value):
        self._time_shorthanded_4v5 = value

    @property
    def pp_goals_for(self):
        return self._pp_goals_for

    @pp_goals_for.setter
    def pp_goals_for(self, value):
        self._pp_goals_for = value

    @property
    def pp_net_percent(self):
        return self._pp_net_percent

    @pp_net_percent.setter
    def pp_net_percent(self, value):
        self._pp_net_percent = value

    @property
    def pp_percent(self):
        return self._pp_percent

    @pp_percent.setter
    def pp_percent(self, value):
        self._pp_percent = value

    @property
    def pp_goals_per_game(self):
        return self._pp_goals_per_game

    @pp_goals_per_game.setter
    def pp_goals_per_game(self, value):
        self._pp_goals_per_game = value

    @property
    def pp_net_goals(self):
        return self._pp_net_goals

    @pp_net_goals.setter
    def pp_net_goals(self, value):
        self._pp_net_goals = value

    @property
    def pp_net_goals_for_per_game(self):
        return self._pp_net_goals_for_per_game

    @pp_net_goals_for_per_game.setter
    def pp_net_goals_for_per_game(self, value):
        self._pp_net_goals_for_per_game = value

    @property
    def pp_opportunites(self):
        return self._pp_opportunites

    @pp_opportunites.setter
    def pp_opportunites(self, value):
        self._pp_opportunites = value

    @property
    def pp_opportunities_per_game(self):
        return self._pp_opportunities_per_game

    @pp_opportunities_per_game.setter
    def pp_opportunities_per_game(self, value):
        self._pp_opportunities_per_game = value

    @property
    def pp_time_on_ice_per_game(self):
        return self._pp_time_on_ice_per_game

    @pp_time_on_ice_per_game.setter
    def pp_time_on_ice_per_game(self, value):
        self._pp_time_on_ice_per_game = value

    @property
    def pp_goals_against(self):
        return self._pp_goals_against

    @pp_goals_against.setter
    def pp_goals_against(self, value):
        self._pp_goals_against = value

    @property
    def pp_goals_against_per_game(self):
        return self._pp_goals_against_per_game

    @pp_goals_against_per_game.setter
    def pp_goals_against_per_game(self, value):
        self._pp_goals_against_per_game = value

    @property
    def opportunities_4on3(self):
        return self._opportunities_4on3

    @opportunities_4on3.setter
    def opportunities_4on3(self, value):
        self._opportunities_4on3 = value

    @property
    def opportunities_5on3(self):
        return self._opportunities_5on3

    @opportunities_5on3.setter
    def opportunities_5on3(self, value):
        self._opportunities_5on3 = value

    @property
    def opportunities_5on4(self):
        return self._opportunities_5on4

    @opportunities_5on4.setter
    def opportunities_5on4(self, value):
        self._opportunities_5on4 = value

    @property
    def pp_percent_4on3(self):
        return self._pp_percent_4on3

    @pp_percent_4on3.setter
    def pp_percent_4on3(self, value):
        self._pp_percent_4on3 = value

    @property
    def pp_percent_5on3(self):
        return self._pp_percent_5on3

    @pp_percent_5on3.setter
    def pp_percent_5on3(self, value):
        self._pp_percent_5on3 = value

    @property
    def pp_percent_5on4(self):
        return self._pp_percent_5on4

    @pp_percent_5on4.setter
    def pp_percent_5on4(self, value):
        self._pp_percent_5on4 = value

    @property
    def time_on_ice_4on3(self):
        return self._time_on_ice_4on3

    @time_on_ice_4on3.setter
    def time_on_ice_4on3(self, value):
        self._time_on_ice_4on3 = value

    @property
    def time_on_ice_5on3(self):
        return self._time_on_ice_5on3

    @time_on_ice_5on3.setter
    def time_on_ice_5on3(self, value):
        self._time_on_ice_5on3 = value

    @property
    def time_on_ice_5on4(self):
        return self._time_on_ice_5on4

    @time_on_ice_5on4.setter
    def time_on_ice_5on4(self, value):
        self._time_on_ice_5on4 = value

    @property
    def pp_time_on_ice(self):
        return self._pp_time_on_ice

    @pp_time_on_ice.setter
    def pp_time_on_ice(self, value):
        self._pp_time_on_ice = value

    @property
    def goals_against_3on4(self):
        return self._goals_against_3on4

    @goals_against_3on4.setter
    def goals_against_3on4(self, value):
        self._goals_against_3on4 = value

    @property
    def goals_against_3on5(self):
        return self._goals_against_3on5

    @goals_against_3on5.setter
    def goals_against_3on5(self, value):
        self._goals_against_3on5 = value

    @property
    def goals_against_4on5(self):
        return self._goals_against_4on5

    @goals_against_4on5.setter
    def goals_against_4on5(self, value):
        self._goals_against_4on5 = value

    @property
    def goals_4on3(self):
        return self._goals_4on3

    @goals_4on3.setter
    def goals_4on3(self, value):
        self._goals_4on3 = value

    @property
    def goals_5on3(self):
        return self._goals_5on3

    @goals_5on3.setter
    def goals_5on3(self, value):
        self._goals_5on3 = value

    @property
    def goals_5on4(self):
        return self._goals_5on4

    @goals_5on4.setter
    def goals_5on4(self, value):
        self._goals_5on4 = value    

class TeamAdvancedStatsPenalties:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._bench_minor_penalties = None
        self._game_misconducts = None
        self._majors = None
        self._match_penalties = None
        self._minors = None
        self._misconducts = None
        self._net_penalties = None
        self._penalties = None
        self._penalty_minutes = None
        self._penalty_seconds_per_game = None
        self._total_penalties_drawn = None
        
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def bench_minor_penalties(self):
        return self._bench_minor_penalties
    
    @bench_minor_penalties.setter
    def bench_minor_penalties(self, value):
        self._bench_minor_penalties = value

    @property
    def game_misconducts(self):
        return self._game_misconducts
    
    @game_misconducts.setter
    def game_misconducts(self, value):
        self._game_misconducts = value

    @property
    def majors(self):
        return self._majors
    
    @majors.setter
    def majors(self, value):
        self._majors = value

    @property
    def match_penalties(self):
        return self._match_penalties
    
    @match_penalties.setter
    def match_penalties(self, value):
        self._match_penalties = value

    @property
    def minors(self):
        return self._minors
    
    @minors.setter
    def minors(self, value):
        self._minors = value

    @property
    def misconducts(self):
        return self._misconducts
    
    @misconducts.setter
    def misconducts(self, value):
        self._misconducts = value

    @property
    def net_penalties(self):
        return self._net_penalties
    
    @net_penalties.setter
    def net_penalties(self, value):
        self._net_penalties = value

    @property
    def penalties(self):
        return self._penalties
    
    @penalties.setter
    def penalties(self, value):
        self._penalties = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def penalty_seconds_per_game(self):
        return self._penalty_seconds_per_game
    
    @penalty_seconds_per_game.setter
    def penalty_seconds_per_game(self, value):
        self._penalty_seconds_per_game = value

    @property
    def total_penalties_drawn(self):
        return self._total_penalties_drawn
    
    @total_penalties_drawn.setter
    def total_penalties_drawn(self, value):
        self._total_penalties_drawn = value

class TeamAdvancedStatsOutshootOutshot:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._losses_even_shots = None
        self._losses_outshoot = None
        self._losses_outshot = None
        self._net_shots_per_game = None
        self._ot_losses_even_shots = None
        self._ot_losses_outshoot = None
        self._ot_losses_outshot = None
        self._shots_against_per_game = None
        self._shots_for_per_game = None
        self._ties_even_shots = None
        self._ties_outshoot = None
        self._ties_outshot = None
        self._wins_even_shots = None
        self._wins_outshoot = None
        self._wins_outshot = None
        
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def losses_even_shots(self):
        return self._losses_even_shots
    
    @losses_even_shots.setter
    def losses_even_shots(self, value):
        self._losses_even_shots = value

    @property
    def losses_outshoot(self):
        return self._losses_outshoot
    
    @losses_outshoot.setter
    def losses_outshoot(self, value):
        self._losses_outshoot = value

    @property
    def losses_outshot(self):
        return self._losses_outshot
    
    @losses_outshot.setter
    def losses_outshot(self, value):
        self._losses_outshot = value

    @property
    def net_shots_per_game(self):
        return self._net_shots_per_game
    
    @net_shots_per_game.setter
    def net_shots_per_game(self, value):
        self._net_shots_per_game = value

    @property
    def ot_losses_even_shots(self):
        return self._ot_losses_even_shots
    
    @ot_losses_even_shots.setter
    def ot_losses_even_shots(self, value):
        self._ot_losses_even_shots = value

    @property
    def ot_losses_outshoot(self):
        return self._ot_losses_outshoot
    
    @ot_losses_outshoot.setter
    def ot_losses_outshoot(self, value):
        self._ot_losses_outshoot = value

    @property
    def ot_losses_outshot(self):
        return self._ot_losses_outshot
    
    @ot_losses_outshot.setter
    def ot_losses_outshot(self, value):
        self._ot_losses_outshot = value

    @property
    def shots_against_per_game(self):
        return self._shots_against_per_game
    
    @shots_against_per_game.setter
    def shots_against_per_game(self, value):
        self._shots_against_per_game = value

    @property
    def shots_for_per_game(self):
        return self._shots_for_per_game
    
    @shots_for_per_game.setter
    def shots_for_per_game(self, value):
        self._shots_for_per_game = value

    @property
    def ties_even_shots(self):
        return self._ties_even_shots
    
    @ties_even_shots.setter
    def ties_even_shots(self, value):
        self._ties_even_shots = value

    @property
    def ties_outshoot(self):
        return self._ties_outshoot
    
    @ties_outshoot.setter
    def ties_outshoot(self, value):
        self._ties_outshoot = value

    @property
    def ties_outshot(self):
        return self._ties_outshot
    
    @ties_outshot.setter
    def ties_outshot(self, value):
        self._ties_outshot = value

    @property
    def wins_even_shots(self):
        return self._wins_even_shots
    
    @wins_even_shots.setter
    def wins_even_shots(self, value):
        self._wins_even_shots = value

    @property
    def wins_outshoot(self):
        return self._wins_outshoot
    
    @wins_outshoot.setter
    def wins_outshoot(self, value):
        self._wins_outshoot = value

    @property
    def wins_outshot(self):
        return self._wins_outshot
    
    @wins_outshot.setter
    def wins_outshot(self, value):
        self._wins_outshot = value

class TeamAdvancedStatsMisc:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._blocked_shots = None
        self._empty_net_goals = None
        self._giveaways = None 
        self._hits = None
        self._missed_shots = None
        self._takeaways = None
        self._time_on_ice_per_game_5on5 = None
        
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def blocked_shots(self):
        return self._blocked_shots
    
    @blocked_shots.setter
    def blocked_shots(self, value):
        self._blocked_shots = value

    @property
    def empty_net_goals(self):
        return self._empty_net_goals
    
    @empty_net_goals.setter
    def empty_net_goals(self, value):
        self._empty_net_goals = value

    @property
    def giveaways(self):
        return self._giveaways
    
    @giveaways.setter
    def giveaways(self, value):
        self._giveaways = value

    @property
    def hits(self):
        return self._hits
    
    @hits.setter
    def hits(self, value):
        self._hits = value

    @property
    def missed_shots(self):
        return self._missed_shots
    
    @missed_shots.setter
    def missed_shots(self, value):
        self._missed_shots = value

    @property
    def takeaways(self):
        return self._takeaways
    
    @takeaways.setter
    def takeaways(self, value):
        self._takeaways = value

    @property
    def time_on_ice_per_game_5on5(self):
        return self._time_on_ice_per_game_5on5
    
    @time_on_ice_per_game_5on5.setter
    def time_on_ice_per_game_5on5(self, value):
        self._time_on_ice_per_game_5on5 = value

class TeamAdvancedStatsLeadingTrailing:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._loss_lead_period_1 = None
        self._loss_lead_period_2 = None
        self._loss_trail_period_1 = None
        self._loss_trail_period_2 = None
        self._ot_loss_lead_period_1 = None
        self._ot_loss_lead_period_2 = None
        self._ot_loss_trail_period_1 = None
        self._ot_loss_trail_period_2 = None
        self._period_1_goals_against = None
        self._period_1_goals_for = None
        self._period_2_goals_against = None
        self._period_2_goals_for = None
        self._ties_lead_period_1 = None
        self._ties_lead_period_2 = None
        self._ties_trail_period_1 = None
        self._ties_trail_period_2 = None
        self._win_percent_lead_period_1 = None
        self._win_percent_lead_period_2 = None
        self._win_percent_trail_period_1 = None
        self._win_percent_trail_period_2 = None
        self._wins_lead_period_1 = None
        self._wins_lead_period_2 = None
        self._wins_trail_period_1 = None
        self._wins_trail_period_2 = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def loss_lead_period_1(self):
        return self._loss_lead_period_1
    
    @loss_lead_period_1.setter
    def loss_lead_period_1(self, value):
        self._loss_lead_period_1 = value

    @property
    def loss_lead_period_2(self):
        return self._loss_lead_period_2
    
    @loss_lead_period_2.setter
    def loss_lead_period_2(self, value):
        self._loss_lead_period_2 = value

    @property
    def loss_trail_period_1(self):
        return self._loss_trail_period_1
    
    @loss_trail_period_1.setter
    def loss_trail_period_1(self, value):
        self._loss_trail_period_1 = value

    @property
    def loss_trail_period_2(self):
        return self._loss_trail_period_2
    
    @loss_trail_period_2.setter
    def loss_trail_period_2(self, value):
        self._loss_trail_period_2 = value

    @property
    def ot_loss_lead_period_1(self):
        return self._ot_loss_lead_period_1
    
    @ot_loss_lead_period_1.setter
    def ot_loss_lead_period_1(self, value):
        self._ot_loss_lead_period_1 = value

    @property
    def ot_loss_lead_period_2(self):
        return self._ot_loss_lead_period_2
    
    @ot_loss_lead_period_2.setter
    def ot_loss_lead_period_2(self, value):
        self._ot_loss_lead_period_2 = value

    @property
    def ot_loss_trail_period_1(self):
        return self._ot_loss_trail_period_1
    
    @ot_loss_trail_period_1.setter
    def ot_loss_trail_period_1(self, value):
        self._ot_loss_trail_period_1 = value

    @property
    def ot_loss_trail_period_2(self):
        return self._ot_loss_trail_period_2
    
    @ot_loss_trail_period_2.setter
    def ot_loss_trail_period_2(self, value):
        self._ot_loss_trail_period_2 = value

    @property
    def period_1_goals_against(self):
        return self._period_1_goals_against
    
    @period_1_goals_against.setter
    def period_1_goals_against(self, value):
        self._period_1_goals_against = value

    @property
    def period_1_goals_for(self):
        return self._period_1_goals_for
    
    @period_1_goals_for.setter
    def period_1_goals_for(self, value):
        self._period_1_goals_for = value

    @property
    def period_2_goals_against(self):
        return self._period_2_goals_against
    
    @period_2_goals_against.setter
    def period_2_goals_against(self, value):
        self._period_2_goals_against = value

    @property
    def period_2_goals_for(self):
        return self._period_2_goals_for
    
    @period_2_goals_for.setter
    def period_2_goals_for(self, value):
        self._period_2_goals_for = value

    @property
    def ties_lead_period_1(self):
        return self._ties_lead_period_1
    
    @ties_lead_period_1.setter
    def ties_lead_period_1(self, value):
        self._ties_lead_period_1 = value

    @property
    def ties_lead_period_2(self):
        return self._ties_lead_period_2
    
    @ties_lead_period_2.setter
    def ties_lead_period_2(self, value):
        self._ties_lead_period_2 = value

    @property
    def ties_trail_period_1(self):
        return self._ties_trail_period_1
    
    @ties_trail_period_1.setter
    def ties_trail_period_1(self, value):
        self._ties_trail_period_1 = value

    @property
    def ties_trail_period_2(self):
        return self._ties_trail_period_2
    
    @ties_trail_period_2.setter
    def ties_trail_period_2(self, value):
        self._ties_trail_period_2 = value

    @property
    def win_percent_lead_period_1(self):
        return self._win_percent_lead_period_1
    
    @win_percent_lead_period_1.setter
    def win_percent_lead_period_1(self, value):
        self._win_percent_lead_period_1 = value

    @property
    def win_percent_lead_period_2(self):
        return self._win_percent_lead_period_2
    
    @win_percent_lead_period_2.setter
    def win_percent_lead_period_2(self, value):
        self._win_percent_lead_period_2 = value

    @property
    def win_percent_trail_period_1(self):
        return self._win_percent_trail_period_1
    
    @win_percent_trail_period_1.setter
    def win_percent_trail_period_1(self, value):
        self._win_percent_trail_period_1 = value

    @property
    def win_percent_trail_period_2(self):
        return self._win_percent_trail_period_2
    
    @win_percent_trail_period_2.setter
    def win_percent_trail_period_2(self, value):
        self._win_percent_trail_period_2 = value

    @property
    def wins_lead_period_1(self):
        return self._wins_lead_period_1
    
    @wins_lead_period_1.setter
    def wins_lead_period_1(self, value):
        self._wins_lead_period_1 = value

    @property
    def wins_lead_period_2(self):
        return self._wins_lead_period_2
    
    @wins_lead_period_2.setter
    def wins_lead_period_2(self, value):
        self._wins_lead_period_2 = value

    @property
    def wins_trail_period_1(self):
        return self._wins_trail_period_1
    
    @wins_trail_period_1.setter
    def wins_trail_period_1(self, value):
        self._wins_trail_period_1 = value

    @property
    def wins_trail_period_2(self):
        return self._wins_trail_period_2
    
    @wins_trail_period_2.setter
    def wins_trail_period_2(self, value):
        self._wins_trail_period_2 = value

class TeamAdvancedStatsGoalsByStrength:

    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._goals_for_3on3 = None
        self._goals_for_3on4 = None
        self._goals_for_3on5 = None
        self._goals_for_3on6 = None
        self._goals_for_4on3 = None
        self._goals_for_4on4 = None
        self._goals_for_4on5 = None
        self._goals_for_4on6 = None
        self._goals_for_5on3 = None
        self._goals_for_5on4 = None
        self._goals_for_5on5 = None
        self._goals_for_5on6 = None
        self._goals_for_6on3 = None
        self._goals_for_6on4 = None
        self._goals_for_6on5 = None
        self._goals_for_penalty_shots = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def goals_for_3on3(self):
        return self._goals_for_3on3
    
    @goals_for_3on3.setter
    def goals_for_3on3(self, value):
        self._goals_for_3on3 = value

    @property
    def goals_for_3on4(self):
        return self._goals_for_3on4
    
    @goals_for_3on4.setter
    def goals_for_3on4(self, value):
        self._goals_for_3on4 = value

    @property
    def goals_for_3on5(self):
        return self._goals_for_3on5
    
    @goals_for_3on5.setter
    def goals_for_3on5(self, value):
        self._goals_for_3on5 = value

    @property
    def goals_for_3on6(self):
        return self._goals_for_3on6
    
    @goals_for_3on6.setter
    def goals_for_3on6(self, value):
        self._goals_for_3on6 = value

    @property
    def goals_for_4on3(self):
        return self._goals_for_4on3
    
    @goals_for_4on3.setter
    def goals_for_4on3(self, value):
        self._goals_for_4on3 = value

    @property
    def goals_for_4on4(self):
        return self._goals_for_4on4
    
    @goals_for_4on4.setter
    def goals_for_4on4(self, value):
        self._goals_for_4on4 = value

    @property
    def goals_for_4on5(self):
        return self._goals_for_4on5
    
    @goals_for_4on5.setter
    def goals_for_4on5(self, value):
        self._goals_for_4on5 = value

    @property
    def goals_for_4on6(self):
        return self._goals_for_4on6
    
    @goals_for_4on6.setter
    def goals_for_4on6(self, value):
        self._goals_for_4on6 = value

    @property
    def goals_for_5on3(self):
        return self._goals_for_5on3
    
    @goals_for_5on3.setter
    def goals_for_5on3(self, value):
        self._goals_for_5on3 = value

    @property
    def goals_for_5on4(self):
        return self._goals_for_5on4
    
    @goals_for_5on4.setter
    def goals_for_5on4(self, value):
        self._goals_for_5on4 = value

    @property
    def goals_for_5on5(self):
        return self._goals_for_5on5
    
    @goals_for_5on5.setter
    def goals_for_5on5(self, value):
        self._goals_for_5on5 = value

    @property
    def goals_for_5on6(self):
        return self._goals_for_5on6
    
    @goals_for_5on6.setter
    def goals_for_5on6(self, value):
        self._goals_for_5on6 = value

    @property
    def goals_for_6on3(self):
        return self._goals_for_6on3
    
    @goals_for_6on3.setter
    def goals_for_6on3(self, value):
        self._goals_for_6on3 = value

    @property
    def goals_for_6on4(self):
        return self._goals_for_6on4
    
    @goals_for_6on4.setter
    def goals_for_6on4(self, value):
        self._goals_for_6on4 = value

    @property
    def goals_for_6on5(self):
        return self._goals_for_6on5
    
    @goals_for_6on5.setter
    def goals_for_6on5(self, value):
        self._goals_for_6on5 = value

    @property
    def goals_for_penalty_shots(self):
        return self._goals_for_penalty_shots
    
    @goals_for_penalty_shots.setter
    def goals_for_penalty_shots(self, value):
        self._goals_for_penalty_shots = value

class TeamAdvancedStatsGoalsByPeriod:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._ev_goals_for = None
        self._period_1_goals_against = None
        self._period_1_goals_for = None
        self._period_2_goals_against = None
        self._period_2_goals_for = None
        self._period_3_goals_against = None
        self._period_3_goals_for = None
        self._period_ot_goals_against = None
        self._period_ot_goals_for = None
        self._pp_goals_for = None
        self._pk_goals_for = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def ev_goals_for(self):
        return self._ev_goals_for
    
    @ev_goals_for.setter
    def ev_goals_for(self, value):
        self._ev_goals_for = value

    @property
    def period_1_goals_against(self):
        return self._period_1_goals_against
    
    @period_1_goals_against.setter
    def period_1_goals_against(self, value):
        self._period_1_goals_against = value

    @property
    def period_1_goals_for(self):
        return self._period_1_goals_for
    
    @period_1_goals_for.setter
    def period_1_goals_for(self, value):
        self._period_1_goals_for = value

    @property
    def period_2_goals_against(self):
        return self._period_2_goals_against
    
    @period_2_goals_against.setter
    def period_2_goals_against(self, value):
        self._period_2_goals_against = value

    @property
    def period_2_goals_for(self):
        return self._period_2_goals_for
    
    @period_2_goals_for.setter
    def period_2_goals_for(self, value):
        self._period_2_goals_for = value

    @property
    def period_3_goals_against(self):
        return self._period_3_goals_against
    
    @period_3_goals_against.setter
    def period_3_goals_against(self, value):
        self._period_3_goals_against = value

    @property
    def period_3_goals_for(self):
        return self._period_3_goals_for
    
    @period_3_goals_for.setter
    def period_3_goals_for(self, value):
        self._period_3_goals_for = value

    @property
    def period_ot_goals_against(self):
        return self._period_ot_goals_against
    
    @period_ot_goals_against.setter
    def period_ot_goals_against(self, value):
        self._period_ot_goals_against = value

    @property
    def period_ot_goals_for(self):
        return self._period_ot_goals_for
    
    @period_ot_goals_for.setter
    def period_ot_goals_for(self, value):
        self._period_ot_goals_for = value

    @property
    def pp_goals_for(self):
        return self._pp_goals_for
    
    @pp_goals_for.setter
    def pp_goals_for(self, value):
        self._pp_goals_for = value

    @property
    def pk_goals_for(self):
        return self._pk_goals_for
    
    @pk_goals_for.setter
    def pk_goals_for(self, value):
        self._pk_goals_for = value

class TeamAdvancedStatsFaceoffPercent:

    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._defensive_zone_faceoff_percent = None
        self._defensive_zone_faceoffs = None
        self._ev_faceoff_percent = None
        self._ev_faceoffs = None
        self._faceoff_win_percent = None
        self._neutral_zone_faceoff_percent = None
        self._neutral_zone_faceoffs = None
        self._offensive_zone_faceoff_percent = None
        self._offensive_zone_faceoffs = None
        self._pp_faceoff_percent = None
        self._pp_faceoffs = None
        self._pk_faceoff_percent = None
        self._pk_faceoffs = None
        self._total_faceoffs = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def defensive_zone_faceoff_percent(self):
        return self._defensive_zone_faceoff_percent
    
    @defensive_zone_faceoff_percent.setter
    def defensive_zone_faceoff_percent(self, value):
        self._defensive_zone_faceoff_percent = value

    @property
    def defensive_zone_faceoffs(self):
        return self._defensive_zone_faceoffs
    
    @defensive_zone_faceoffs.setter
    def defensive_zone_faceoffs(self, value):
        self._defensive_zone_faceoffs = value

    @property
    def ev_faceoff_percent(self):
        return self._ev_faceoff_percent
    
    @ev_faceoff_percent.setter
    def ev_faceoff_percent(self, value):
        self._ev_faceoff_percent = value

    @property
    def ev_faceoffs(self):
        return self._ev_faceoffs
    
    @ev_faceoffs.setter
    def ev_faceoffs(self, value):
        self._ev_faceoffs = value

    @property
    def faceoff_win_percent(self):
        return self._faceoff_win_percent
    
    @faceoff_win_percent.setter
    def faceoff_win_percent(self, value):
        self._faceoff_win_percent = value

    @property
    def neutral_zone_faceoff_percent(self):
        return self._neutral_zone_faceoff_percent
    
    @neutral_zone_faceoff_percent.setter
    def neutral_zone_faceoff_percent(self, value):
        self._neutral_zone_faceoff_percent = value

    @property
    def neutral_zone_faceoffs(self):
        return self._neutral_zone_faceoffs
    
    @neutral_zone_faceoffs.setter
    def neutral_zone_faceoffs(self, value):
        self._neutral_zone_faceoffs = value

    @property
    def offensive_zone_faceoff_percent(self):
        return self._offensive_zone_faceoff_percent
    
    @offensive_zone_faceoff_percent.setter
    def offensive_zone_faceoff_percent(self, value):
        self._offensive_zone_faceoff_percent = value

    @property
    def offensive_zone_faceoffs(self):
        return self._offensive_zone_faceoffs
    
    @offensive_zone_faceoffs.setter
    def offensive_zone_faceoffs(self, value):
        self._offensive_zone_faceoffs = value

    @property
    def pp_faceoff_percent(self):
        return self._pp_faceoff_percent
    
    @pp_faceoff_percent.setter
    def pp_faceoff_percent(self, value):
        self._pp_faceoff_percent = value

    @property
    def pp_faceoffs(self):
        return self._pp_faceoffs
    
    @pp_faceoffs.setter
    def pp_faceoffs(self, value):
        self._pp_faceoffs = value

    @property
    def pk_faceoff_percent(self):
        return self._pk_faceoff_percent
    
    @pk_faceoff_percent.setter
    def pk_faceoff_percent(self, value):
        self._pk_faceoff_percent = value

    @property
    def pk_faceoffs(self):
        return self._pk_faceoffs
    
    @pk_faceoffs.setter
    def pk_faceoffs(self, value):
        self._pk_faceoffs = value

    @property
    def total_faceoffs(self):
        return self._total_faceoffs
    
    @total_faceoffs.setter
    def total_faceoffs(self, value):
        self._total_faceoffs = value

class TeamAdvancedStatsDaysRest:

    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._days_rest = None
        self._games_played = None
        self._faceoff_percent = None
        self._goals_against_per_game = None
        self._goals_for_per_game = None
        self._losses = None
        self._net_goals_per_game = None
        self._ot_losses = None
        self._penalty_kill_percent = None
        self._point_percent = None
        self._points = None
        self._power_play_percent = None
        self._power_play_opportunities_per_game = None
        self._shot_differential_per_game = None
        self._shots_against_per_game = None
        self._shots_for_per_game = None
        self._ties = None
        self._times_shorthanded_per_game = None
        self._wins = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def days_rest(self):
        return self._days_rest
    
    @days_rest.setter
    def days_rest(self, value):
        self._days_rest = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def faceoff_percent(self):
        return self._faceoff_percent
    
    @faceoff_percent.setter
    def faceoff_percent(self, value):
        self._faceoff_percent = value

    @property
    def goals_against_per_game(self):
        return self._goals_against_per_game
    
    @goals_against_per_game.setter
    def goals_against_per_game(self, value):
        self._goals_against_per_game = value

    @property
    def goals_for_per_game(self):
        return self._goals_for_per_game
    
    @goals_for_per_game.setter
    def goals_for_per_game(self, value):
        self._goals_for_per_game = value

    @property
    def losses(self):
        return self._losses
    
    @losses.setter
    def losses(self, value):
        self._losses = value

    @property
    def net_goals_per_game(self):
        return self._net_goals_per_game
    
    @net_goals_per_game.setter
    def net_goals_per_game(self, value):
        self._net_goals_per_game = value

    @property
    def ot_losses(self):
        return self._ot_losses
    
    @ot_losses.setter
    def ot_losses(self, value):
        self._ot_losses = value

    @property
    def penalty_kill_percent(self):
        return self._penalty_kill_percent
    
    @penalty_kill_percent.setter
    def penalty_kill_percent(self, value):
        self._penalty_kill_percent = value

    @property
    def point_percent(self):
        return self._point_percent
    
    @point_percent.setter
    def point_percent(self, value):
        self._point_percent = value

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        self._points = value

    @property
    def power_play_percent(self):
        return self._power_play_percent
    
    @power_play_percent.setter
    def power_play_percent(self, value):
        self._power_play_percent = value

    @property
    def power_play_opportunities_per_game(self):
        return self._power_play_opportunities_per_game
    
    @power_play_opportunities_per_game.setter
    def power_play_opportunities_per_game(self, value):
        self._power_play_opportunities_per_game = value

    @property
    def shot_differential_per_game(self):
        return self._shot_differential_per_game
    
    @shot_differential_per_game.setter
    def shot_differential_per_game(self, value):
        self._shot_differential_per_game = value

    @property
    def shots_against_per_game(self):
        return self._shots_against_per_game
    
    @shots_against_per_game.setter
    def shots_against_per_game(self, value):
        self._shots_against_per_game = value

    @property
    def shots_for_per_game(self):
        return self._shots_for_per_game
    
    @shots_for_per_game.setter
    def shots_for_per_game(self, value):
        self._shots_for_per_game = value

    @property
    def ties(self):
        return self._ties
    
    @ties.setter
    def ties(self, value):
        self._ties = value

    @property
    def times_shorthanded_per_game(self):
        return self._times_shorthanded_per_game
    
    @times_shorthanded_per_game.setter
    def times_shorthanded_per_game(self, value):
        self._times_shorthanded_per_game = value

    @property
    def wins(self):
        return self._wins
    
    @wins.setter
    def wins(self, value):
        self._wins = value

class TeamAdvancedStatsCorsiFenwick:
    def __init__(self, team_id):
        self._team_id = team_id
        self._year = None
        self._games_played = None
        self._corsi_against = None
        self._corsi_ahead = None
        self._corsi_behind = None
        self._corsi_close = None
        self._corsi_for = None
        self._corsi_tied = None
        self._corsi_total = None
        self._fenwick_against = None
        self._fenwick_ahead = None
        self._fenwick_behind = None
        self._fenwick_close = None
        self._fenwick_for = None
        self._fenwick_relative = None
        self._fenwick_tied = None
        self._fenwick_total = None
        self._corsi_percent = None
        self._corsi_ahead_percent = None
        self._corsi_behind_percent = None
        self._corsi_close_percent = None
        self._corsi_tied_percent = None
        self._corsi_relative = None
        self._shooting_percent_5on5 = None
        self._save_percent_5on5 = None
        self._shooting_plus_save_percent_5on5 = None
        self._fenwick_tied_percent = None
        self._fenwick_ahead_percent = None
        self._fenwick_behind_percent = None
        self._fenwick_close_percent = None
        self._zone_start_5on5_percent = None
        self._fenwick_percent = None

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def games_played(self):
        return self._games_played
    
    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def corsi_against(self):
        return self._corsi_against
    
    @corsi_against.setter
    def corsi_against(self, value):
        self._corsi_against = value

    @property
    def corsi_ahead(self):
        return self._corsi_ahead
    
    @corsi_ahead.setter
    def corsi_ahead(self, value):
        self._corsi_ahead = value

    @property
    def corsi_behind(self):
        return self._corsi_behind
    
    @corsi_behind.setter
    def corsi_behind(self, value):
        self._corsi_behind = value

    @property
    def corsi_close(self):
        return self._corsi_close
    
    @corsi_close.setter
    def corsi_close(self, value):
        self._corsi_close = value

    @property
    def corsi_for(self):
        return self._corsi_for
    
    @corsi_for.setter
    def corsi_for(self, value):
        self._corsi_for = value

    @property
    def corsi_tied(self):
        return self._corsi_tied
    
    @corsi_tied.setter
    def corsi_tied(self, value):
        self._corsi_tied = value

    @property
    def corsi_total(self):
        return self._corsi_total
    
    @corsi_total.setter
    def corsi_total(self, value):
        self._corsi_total = value

    @property
    def fenwick_against(self):
        return self._fenwick_against
    
    @fenwick_against.setter
    def fenwick_against(self, value):
        self._fenwick_against = value

    @property
    def fenwick_ahead(self):
        return self._fenwick_ahead
    
    @fenwick_ahead.setter
    def fenwick_ahead(self, value):
        self._fenwick_ahead = value

    @property
    def fenwick_behind(self):
        return self._fenwick_behind
    
    @fenwick_behind.setter
    def fenwick_behind(self, value):
        self._fenwick_behind = value

    @property
    def fenwick_close(self):
        return self._fenwick_close
    
    @fenwick_close.setter
    def fenwick_close(self, value):
        self._fenwick_close = value

    @property
    def fenwick_for(self):
        return self._fenwick_for
    
    @fenwick_for.setter
    def fenwick_for(self, value):
        self._fenwick_for = value

    @property
    def fenwick_relative(self):
        return self._fenwick_relative
    
    @fenwick_relative.setter
    def fenwick_relative(self, value):
        self._fenwick_relative = value

    @property
    def fenwick_tied(self):
        return self._fenwick_tied
    
    @fenwick_tied.setter
    def fenwick_tied(self, value):
        self._fenwick_tied = value

    @property
    def fenwick_total(self):
        return self._fenwick_total
    
    @fenwick_total.setter
    def fenwick_total(self, value):
        self._fenwick_total = value

    @property
    def corsi_percent(self):
        return self._corsi_percent
    
    @corsi_percent.setter
    def corsi_percent(self, value):
        self._corsi_percent = value

    @property
    def corsi_ahead_percent(self):
        return self._corsi_ahead_percent
    
    @corsi_ahead_percent.setter
    def corsi_ahead_percent(self, value):
        self._corsi_ahead_percent = value

    @property
    def corsi_behind_percent(self):
        return self._corsi_behind_percent
    
    @corsi_behind_percent.setter
    def corsi_behind_percent(self, value):
        self._corsi_behind_percent = value

    @property
    def corsi_close_percent(self):
        return self._corsi_close_percent
    
    @corsi_close_percent.setter
    def corsi_close_percent(self, value):
        self._corsi_close_percent = value

    @property
    def corsi_tied_percent(self):
        return self._corsi_tied_percent
    
    @corsi_tied_percent.setter
    def corsi_tied_percent(self, value):
        self._corsi_tied_percent = value

    @property
    def corsi_relative(self):
        return self._corsi_relative
    
    @corsi_relative.setter
    def corsi_relative(self, value):
        self._corsi_relative = value

    @property
    def shooting_percent_5on5(self):
        return self._shooting_percent_5on5
    
    @shooting_percent_5on5.setter
    def shooting_percent_5on5(self, value):
        self._shooting_percent_5on5 = value

    @property
    def save_percent_5on5(self):
        return self._save_percent_5on5
    
    @save_percent_5on5.setter
    def save_percent_5on5(self, value):
        self._save_percent_5on5 = value

    @property
    def shooting_plus_save_percent_5on5(self):
        return self._shooting_plus_save_percent_5on5
    
    @shooting_plus_save_percent_5on5.setter
    def shooting_plus_save_percent_5on5(self, value):
        self._shooting_plus_save_percent_5on5 = value

    @property
    def fenwick_tied_percent(self):
        return self._fenwick_tied_percent
    
    @fenwick_tied_percent.setter
    def fenwick_tied_percent(self, value):
        self._fenwick_tied_percent = value

    @property
    def fenwick_ahead_percent(self):
        return self._fenwick_ahead_percent
    
    @fenwick_ahead_percent.setter
    def fenwick_ahead_percent(self, value):
        self._fenwick_ahead_percent = value

    @property
    def fenwick_behind_percent(self):
        return self._fenwick_behind_percent
    
    @fenwick_behind_percent.setter
    def fenwick_behind_percent(self, value):
        self._fenwick_behind_percent = value

    @property
    def fenwick_close_percent(self):
        return self._fenwick_close_percent
    
    @fenwick_close_percent.setter
    def fenwick_close_percent(self, value):
        self._fenwick_close_percent = value

    @property
    def zone_start_5on5_percent(self):
        return self._zone_start_5on5_percent
    
    @zone_start_5on5_percent.setter
    def zone_start_5on5_percent(self, value):
        self._zone_start_5on5_percent = value

    @property
    def fenwick_percent(self):
        return self._fenwick_percent
    
    @fenwick_percent.setter
    def fenwick_percent(self, value):
        self._fenwick_percent = value

class Games:
    def __init__(self, game_id):
        self._game_id = game_id
        self._year = None
        self._game_type_id = None
        self._venue_name = None
        self._start_time_utc = None
        self._eastern_utc_offset = None
        self._venue_utc_offset = None
        self._venue_time_zone = None
        self._game_state = None
        self._game_schedule_state = None
        self._away_team_id = None
        self._home_team_id = None
        self._shootout_in_use = None
        self._regulation_periods = None
        self._ot_in_use = None
        self._ties_in_use = None
        self._video_3_min_recap_id = None
        self._video_condensed_game = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._year = value

    @property
    def game_type_id(self):
        return self._game_type_id
    
    @game_type_id.setter
    def game_type_id(self, value):
        self._game_type_id = value

    @property
    def venue_name(self):
        return self._venue_name
    
    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value

    @property
    def start_time_utc(self):
        return self._start_time_utc
    
    @start_time_utc.setter
    def start_time_utc(self, value):
        self._start_time_utc = value

    @property
    def eastern_utc_offset(self):
        return self._eastern_utc_offset
    
    @eastern_utc_offset.setter
    def eastern_utc_offset(self, value):
        self._eastern_utc_offset = value

    @property
    def venue_utc_offset(self):
        return self._venue_utc_offset
    
    @venue_utc_offset.setter
    def venue_utc_offset(self, value):
        self._venue_utc_offset = value

    @property
    def venue_time_zone(self):
        return self._venue_time_zone
    
    @venue_time_zone.setter
    def venue_time_zone(self, value):
        self._venue_time_zone = value

    @property
    def game_state(self):
        return self._game_state
    
    @game_state.setter
    def game_state(self, value):
        self._game_state = value

    @property
    def game_schedule_state(self):
        return self._game_schedule_state
    
    @game_schedule_state.setter
    def game_schedule_state(self, value):
        self._game_schedule_state = value

    @property
    def away_team_id(self):
        return self._away_team_id
    
    @away_team_id.setter
    def away_team_id(self, value):
        self._away_team_id = value

    @property
    def home_team_id(self):
        return self._home_team_id
    
    @home_team_id.setter
    def home_team_id(self, value):
        self._home_team_id = value

    @property
    def shootout_in_use(self):
        return self._shootout_in_use
    
    @shootout_in_use.setter
    def shootout_in_use(self, value):
        self._shootout_in_use = value

    @property
    def regulation_periods(self):
        return self._regulation_periods

    @regulation_periods.setter
    def regulation_periods(self, value):
        self._regulation_periods = value

    @property
    def ot_in_use(self):
        return self._ot_in_use
    
    @ot_in_use.setter
    def ot_in_use(self, value):
        self._ot_in_use = value

    @property
    def ties_in_use(self):
        return self._ties_in_use

    @ties_in_use.setter
    def ties_in_use(self, value):
        self._ties_in_use = value

    @property
    def video_3_min_recap_id(self):
        return self._video_3_min_recap_id
    
    @video_3_min_recap_id.setter
    def video_3_min_recap_id(self, value):
        self._video_3_min_recap_id = value

    @property
    def video_condensed_game(self):
        return self._video_condensed_game
    
    @video_condensed_game.setter
    def video_condensed_game(self, value):
        self._video_condensed_game = value

class GameThreeStars:
    def __init__(self, game_id):
        self._game_id = game_id
        self._star_1 = None
        self._star_2 = None
        self._star_3 = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def star_1(self):
        return self._star_1
    
    @star_1.setter
    def star_1(self, value):
        self._star_1 = value

    @property
    def star_2(self):
        return self._star_2
    
    @star_2.setter
    def star_2(self, value):
        self._star_2 = value

    @property
    def star_3(self):
        return self._star_3
    
    @star_3.setter
    def star_3(self, value):
        self._star_3 = value

class GameSkaterStats:
    def __init__(self, game_id, player_id):
        self._game_id = game_id
        self._player_id = player_id
        self._team_id = None
        self._goals = None
        self._assists = None
        self._points = None
        self._plus_minus = None
        self._penalty_minutes = None
        self._hits = None
        self._blocks = None
        self._power_play_goals = None
        self._power_play_points = None
        self._shorthanded_goals = None
        self._shorthanded_points = None
        self._shots = None
        self._faceoffs = None
        self._time_on_ice = None
        self._power_play_time_on_ice = None
        self._shorthanded_time_on_ice = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, value):
        self._goals = value

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, value):
        self._assists = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def plus_minus(self):
        return self._plus_minus
    
    @plus_minus.setter
    def plus_minus(self, value):
        self._plus_minus = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        self._hits = value

    @property
    def blocks(self):
        return self._blocks
    
    @blocks.setter
    def blocks(self, value):
        self._blocks = value

    @property
    def power_play_goals(self):
        return self._power_play_goals
    
    @power_play_goals.setter
    def power_play_goals(self, value):
        self._power_play_goals = value

    @property
    def power_play_points(self):
        return self._power_play_points
    
    @power_play_points.setter
    def power_play_points(self, value):
        self._power_play_points = value

    @property
    def shorthanded_goals(self):
        return self._shorthanded_goals
    
    @shorthanded_goals.setter
    def shorthanded_goals(self, value):
        self._shorthanded_goals = value

    @property
    def shorthanded_points(self):
        return self._shorthanded_points
    
    @shorthanded_points.setter
    def shorthanded_points(self, value):
        self._shorthanded_points = value

    @property
    def shots(self):
        return self._shots
    
    @shots.setter
    def shots(self, value):
        self._shots = value

    @property
    def faceoffs(self):
        return self._faceoffs
    
    @faceoffs.setter
    def faceoffs(self, value):
        self._faceoffs = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

    @property
    def power_play_time_on_ice(self):
        return self._power_play_time_on_ice
    
    @power_play_time_on_ice.setter
    def power_play_time_on_ice(self, value):
        self._power_play_time_on_ice = value

    @property
    def shorthanded_time_on_ice(self):
        return self._shorthanded_time_on_ice
    
    @shorthanded_time_on_ice.setter
    def shorthanded_time_on_ice(self, value):
        self._shorthanded_time_on_ice = value

class GameScoreboard:
    def __init__(self, game_id):
        self._game_id = game_id
        self._home_score = None
        self._away_score = None
        self._home_shots = None
        self._away_shots = None
        self._time_remaining = None
        self._period = None
        self._seconds_remaining = None
        self._running = None
        self._in_intermission = None

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def home_score(self):
        return self._home_score
    
    @home_score.setter
    def home_score(self, value):
        self._home_score = value

    @property
    def away_score(self):
        return self._away_score
    
    @away_score.setter
    def away_score(self, value):
        self._away_score = value

    @property
    def home_shots(self):
        return self._home_shots
    
    @home_shots.setter
    def home_shots(self, value):
        self._home_shots = value

    @property
    def away_shots(self):
        return self._away_shots
    
    @away_shots.setter
    def away_shots(self, value):
        self._away_shots = value

    @property
    def time_remaining(self):
        return self._time_remaining
    
    @time_remaining.setter
    def time_remaining(self, value):
        self._time_remaining = value

    @property
    def period(self):
        return self._period
    
    @period.setter
    def period(self, value):
        self._period = value

    @property
    def seconds_remaining(self):
        return self._seconds_remaining
    
    @seconds_remaining.setter
    def seconds_remaining(self, value):
        self._seconds_remaining = value

    @property
    def running(self):
        return self._running
    
    @running.setter
    def running(self, value):
        self._running = value

    @property
    def in_intermission(self):
        return self._in_intermission
    
    @in_intermission.setter
    def in_intermission(self, value):
        self._in_intermission = value

class GameRoster:
    def __init__(self, game_id, player_id, team_id):
        self._game_id = game_id
        self._team_id = team_id
        self._player_id = player_id
        self._scratched = None
        self._starting = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def scratched(self):
        return self._scratched
    
    @scratched.setter
    def scratched(self, value):
        self._scratched = value

    @property
    def starting(self):
        return self._starting

    @starting.setter
    def starting(self, value):
        self._starting = value

class GamePlays:
    def __init__(self, game_id):
        self._game_id = game_id
        self._play_id = None
        self._event_id = None
        self._period_number = None
        self._period_type = None
        self._time_in_period = None
        self._time_remaining = None
        self._situation_code = None
        self._home_team_defending_side = None
        self._type_code = None
        self._type_description_key = None
        self._sort_order = None
        self._x_coord = None
        self._y_coord = None
        self._zone_code = None
        self._shot_type = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def play_id(self):
        return self._play_id
    
    @play_id.setter
    def play_id(self, value):
        self._play_id = value

    @property
    def event_id(self):
        return self._event_id
    
    @event_id.setter
    def event_id(self, value):
        self._event_id = value

    @property
    def period_number(self):
        return self._period_number
    
    @period_number.setter
    def period_number(self, value):
        self._period_number = value

    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value

    @property
    def time_in_period(self):
        return self._time_in_period
    
    @time_in_period.setter
    def time_in_period(self, value):
        self._time_in_period = value

    @property
    def time_remaining(self):
        return self._time_remaining
    
    @time_remaining.setter
    def time_remaining(self, value):
        self._time_remaining = value

    @property
    def situation_code(self):
        return self._situation_code
    
    @situation_code.setter
    def situation_code(self, value):
        self._situation_code = value

    @property
    def home_team_defending_side(self):
        return self._home_team_defending_side
    
    @home_team_defending_side.setter
    def home_team_defending_side(self, value):
        self._home_team_defending_side = value

    @property
    def type_code(self):
        return self._type_code
    
    @type_code.setter
    def type_code(self, value):
        self._type_code = value

    @property
    def type_description_key(self):
        return self._type_description_key
    
    @type_description_key.setter
    def type_description_key(self, value):
        self._type_description_key = value

    @property
    def sort_order(self):
        return self._sort_order
    
    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value

    @property
    def x_coord(self):
        return self._x_coord
    
    @x_coord.setter
    def x_coord(self, value):
        self._x_coord = value

    @property
    def y_coord(self):
        return self._y_coord
    
    @y_coord.setter
    def y_coord(self, value):
        self._y_coord = value

    @property
    def zone_code(self):
        return self._zone_code
    
    @zone_code.setter
    def zone_code(self, value):
        self._zone_code = value

    @property
    def shot_type(self):
        return self._shot_type
    
    @shot_type.setter
    def shot_type(self, value):
        self._shot_type = value

class GameGoals:
    def __init__(self, game_id):
        self._game_id = game_id
        self._situation_code = None
        self._strength = None
        self._player_id = None
        self._highlight_clip_id = None
        self._goals_to_date = None
        self._away_score = None
        self._home_score = None
        self._leading_team_id = None
        self._time_in_period = None
        self._shot_type = None
        self._goal_modifier = None
        self._assist_1_player_id = None
        self._assist_2_player_id = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def situation_code(self):
        return self._situation_code
    
    @situation_code.setter
    def situation_code(self, value):
        self._situation_code = value

    @property
    def strength(self):
        return self._strength
    
    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def highlight_clip_id(self):
        return self._highlight_clip_id
    
    @highlight_clip_id.setter
    def highlight_clip_id(self, value):
        self._highlight_clip_id = value

    @property
    def goals_to_date(self):
        return self._goals_to_date
    
    @goals_to_date.setter
    def goals_to_date(self, value):
        self._goals_to_date = value

    @property
    def away_score(self):
        return self._away_score
    
    @away_score.setter
    def away_score(self, value):
        self._away_score = value

    @property
    def home_score(self):
        return self._home_score
    
    @home_score.setter
    def home_score(self, value):
        self._home_score = value

    @property
    def leading_team_id(self):
        return self._leading_team_id
    
    @leading_team_id.setter
    def leading_team_id(self, value):
        self._leading_team_id = value

    @property
    def time_in_period(self):
        return self._time_in_period
    
    @time_in_period.setter
    def time_in_period(self, value):
        self._time_in_period = value

    @property
    def shot_type(self):
        return self._shot_type
    
    @shot_type.setter
    def shot_type(self, value):
        self._shot_type = value

    @property
    def goal_modifier(self):
        return self._goal_modifier
    
    @goal_modifier.setter
    def goal_modifier(self, value):
        self._goal_modifier = value

    @property
    def assist_1_player_id(self):
        return self._assist_1_player_id

    @assist_1_player_id.setter
    def assist_1_player_id(self, value):
        self._assist_1_player_id = value

    @property
    def assist_2_player_id(self):
        return self._assist_2_player_id
    
    @assist_2_player_id.setter
    def assist_2_player_id(self, value):
        self._assist_2_player_id = value

class GameGoalieStats:
    def __init__(self, game_id):
        self._game_id = game_id
        self._player_id = None
        self._team_id = None
        self._even_strength_shots_against = None
        self._power_play_shots_against = None
        self._shorthanded_shots_against = None
        self._saves_shots_against = None
        self._even_strength_goals_against = None
        self._power_play_goals_against = None
        self._shorthanded_goals_against = None
        self._penalty_minutes = None
        self._goals_against = None
        self._time_on_ice = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def even_strength_shots_against(self):
        return self._even_strength_shots_against
    
    @even_strength_shots_against.setter
    def even_strength_shots_against(self, value):
        self._even_strength_shots_against = value

    @property
    def power_play_shots_against(self):
        return self._power_play_shots_against

    @power_play_shots_against.setter
    def power_play_shots_against(self, value):
        self._power_play_shots_against = value

    @property
    def shorthanded_shots_against(self):
        return self._shorthanded_shots_against
    
    @shorthanded_shots_against.setter
    def shorthanded_shots_against(self, value):
        self._shorthanded_shots_against = value

    @property
    def saves_shots_against(self):
        return self._saves_shots_against
    
    @saves_shots_against.setter
    def saves_shots_against(self, value):
        self._saves_shots_against = value

    @property
    def even_strength_goals_against(self):
        return self._even_strength_goals_against
    
    @even_strength_goals_against.setter
    def even_strength_goals_against(self, value):
        self._even_strength_goals_against = value

    @property
    def power_play_goals_against(self):
        return self._power_play_goals_against
    
    @power_play_goals_against.setter
    def power_play_goals_against(self, value):
        self._power_play_goals_against = value

    @property
    def shorthanded_goals_against(self):
        return self._shorthanded_goals_against
    
    @shorthanded_goals_against.setter
    def shorthanded_goals_against(self, value):
        self._shorthanded_goals_against = value

    @property
    def penalty_minutes(self):
        return self._penalty_minutes
    
    @penalty_minutes.setter
    def penalty_minutes(self, value):
        self._penalty_minutes = value

    @property
    def goals_against(self):
        return self._goals_against
    
    @goals_against.setter
    def goals_against(self, value):
        self._goals_against = value

    @property
    def time_on_ice(self):
        return self._time_on_ice
    
    @time_on_ice.setter
    def time_on_ice(self, value):
        self._time_on_ice = value

class GameBoxscore:
    def __init__(self, game_id):
        self._game_id = game_id
        self._away_team_id = None
        self._away_goals = None
        self._away_score = None
        self._away_shots = None
        self._away_faceoff_percent = None
        self._away_power_play_conversion = None
        self._away_penalty_minutes = None
        self._away_hits = None
        self._away_blocked_shots = None
        self._home_team_id = None
        self._home_goals = None
        self._home_score = None
        self._home_shots = None
        self._home_faceoff_percent = None
        self._home_power_play_conversion = None
        self._home_penalty_minutes = None
        self._home_hits = None
        self._home_blocked_shots = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def away_team_id(self):
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, value):
        self._away_team_id = value

    @property
    def away_goals(self):
        return self._away_goals
    
    @away_goals.setter
    def away_goals(self, value):
        self._away_goals = value

    @property
    def away_score(self):
        return self._away_score
    
    @away_score.setter
    def away_score(self, value):
        self._away_score = value

    @property
    def away_shots(self):
        return self._away_shots

    @away_shots.setter
    def away_shots(self, value):
        self._away_shots = value

    @property
    def away_faceoff_percent(self):
        return self._away_faceoff_percent

    @away_faceoff_percent.setter
    def away_faceoff_percent(self, value):
        self._away_faceoff_percent = value

    @property
    def away_power_play_conversion(self):
        return self._away_power_play_conversion
    
    @away_power_play_conversion.setter
    def away_power_play_conversion(self, value):
        self._away_power_play_conversion = value

    @property
    def away_penalty_minutes(self):
        return self._away_penalty_minutes
    
    @away_penalty_minutes.setter
    def away_penalty_minutes(self, value):
        self._away_penalty_minutes = value

    @property
    def away_hits(self):
        return self._away_hits
    
    @away_hits.setter
    def away_hits(self, value):
        self._away_hits = value

    @property
    def away_blocked_shots(self):
        return self._away_blocked_shots

    @away_blocked_shots.setter
    def away_blocked_shots(self, value):
        self._away_blocked_shots = value

    @property
    def home_team_id(self):
        return self._home_team_id
    
    @home_team_id.setter
    def home_team_id(self, value):
        self._home_team_id = value

    @property
    def home_goals(self):
        return self._home_goals
    
    @home_goals.setter
    def home_goals(self, value):
        self._home_goals = value

    @property
    def home_score(self):
        return self._home_score
    
    @home_score.setter
    def home_score(self, value):
        self._home_score = value

    @property
    def home_shots(self):
        return self._home_shots
    
    @home_shots.setter
    def home_shots(self, value):
        self._home_shots = value

    @property
    def home_faceoff_percent(self):
        return self._home_faceoff_percent
    
    @home_faceoff_percent.setter
    def home_faceoff_percent(self, value):
        self._home_faceoff_percent = value

    @property
    def home_power_play_conversion(self):
        return self._home_power_play_conversion
    
    @home_power_play_conversion.setter
    def home_power_play_conversion(self, value):
        self._home_power_play_conversion = value

    @property
    def home_penalty_minutes(self):
        return self._home_penalty_minutes
    
    @home_penalty_minutes.setter
    def home_penalty_minutes(self, value):
        self._home_penalty_minutes = value

    @property
    def home_hits(self):
        return self._home_hits
    
    @home_hits.setter
    def home_hits(self, value):
        self._home_hits = value

    @property
    def home_blocked_shots(self):
        return self._home_blocked_shots

    @home_blocked_shots.setter
    def home_blocked_shots(self, value):
        self._home_blocked_shots = value

class PlayoffBracket:
    def __init__(self, year):
        self._year = year
        self._round = round
        self._top_seed_rank = None
        self._top_seed_wins = None
        self._top_seed_team_id = None
        self._series_title = None
        self._bottom_seed_rank = None
        self._bottom_seed_wins = None
        self._bottom_seed_team_id = None
        self._winning_team_id = None
        self._losing_team_id = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def round(self):
        return self._round
    
    @round.setter
    def round(self, value):
        self._round = value

    @property
    def top_seed_rank(self):
        return self._top_seed_rank
    
    @top_seed_rank.setter
    def top_seed_rank(self, value):
        self._top_seed_rank = value

    @property
    def top_seed_wins(self):
        return self._top_seed_wins
    
    @top_seed_wins.setter
    def top_seed_wins(self, value):
        self._top_seed_wins = value

    @property
    def top_seed_team_id(self):
        return self._top_seed_team_id
    
    @top_seed_team_id.setter
    def top_seed_team_id(self, value):
        self._top_seed_team_id = value

    @property
    def series_title(self):
        return self._series_title
    
    @series_title.setter
    def series_title(self, value):
        self._series_title = value

    @property
    def bottom_seed_rank(self):
        return self._bottom_seed_rank
    
    @bottom_seed_rank.setter
    def bottom_seed_rank(self, value):
        self._bottom_seed_rank = value

    @property
    def bottom_seed_wins(self):
        return self._bottom_seed_wins
    
    @bottom_seed_wins.setter
    def bottom_seed_wins(self, value):
        self._bottom_seed_wins = value

    @property
    def bottom_seed_team_id(self):
        return self._bottom_seed_team_id
    
    @bottom_seed_team_id.setter
    def bottom_seed_team_id(self, value):
        self._bottom_seed_team_id = value

    @property
    def winning_team_id(self):
        return self._winning_team_id

    @winning_team_id.setter
    def winning_team_id(self, value):
        self._winning_team_id = value

    @property
    def losing_team_id(self):
        return self._losing_team_id
    
    @losing_team_id.setter
    def losing_team_id(self, value):
        self._losing_team_id = value

class PlayOnIce:
    def __init__(self, game_id):
        self._game_id = game_id
        self._play_id = None
        self._player_id = None
        self._team_id = None
        self._home = None
        self._away = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def play_id(self):
        return self._play_id
    
    @play_id.setter
    def play_id(self, value):
        self._play_id = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, value):
        self._team_id = value

    @property
    def home(self):
        return self._home
    
    @home.setter
    def home(self, value):
        self._home = value

    @property
    def away(self):
        return self._away
    
    @away.setter
    def away(self, value):
        self._away = value

class PlayOutcomes:
    def __init__(self, game_id):
        self._game_id = game_id
        self._play_id = None
        self._away_score = None
        self._home_score = None
        self._duration = None
        self._reason = None
        self._secondary_reason = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def play_id(self):
        return self._play_id
    
    @play_id.setter
    def play_id(self, value):
        self._play_id = value

    @property
    def away_score(self):
        return self._away_score
    
    @away_score.setter
    def away_score(self, value):
        self._away_score = value

    @property
    def home_score(self):
        return self._home_score
    
    @home_score.setter
    def home_score(self, value):
        self._home_score = value

    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def reason(self):
        return self._reason
    
    @reason.setter
    def reason(self, value):
        self._reason = value

    @property
    def secondary_reason(self):
        return self._secondary_reason
    
    @secondary_reason.setter
    def secondary_reason(self, value):
        self._secondary_reason = value

class PlayRoles:
    def __init__(self, game_id):
        self._game_id = game_id
        self._play_id = None
        self._player_id = None
        self._role_code = None

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def play_id(self):
        return self._play_id
    
    @play_id.setter
    def play_id(self, value):
        self._play_id = value

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def role_code(self):
        return self._role_code
    
    @role_code.setter
    def role_code(self, value):
        self._role_code = value

class Referees:
    def __init__(self, game_id):
        self._game_id = game_id
        self._referee_1_name = None
        self._referee_2_name = None
        self._linesman_1_name = None
        self._linesman_2_name = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def referee_1_name(self):
        return self._referee_1_name
    
    @referee_1_name.setter
    def referee_1_name(self, value):
        self._referee_1_name = value

    @property
    def referee_2_name(self):
        return self._referee_2_name
    
    @referee_2_name.setter
    def referee_2_name(self, value):
        self._referee_2_name = value

    @property
    def linesman_1_name(self):
        return self._linesman_1_name

    @linesman_1_name.setter
    def linesman_1_name(self, value):
        self._linesman_1_name = value

    @property
    def linesman_2_name(self):
        return self._linesman_2_name
    
    @linesman_2_name.setter
    def linesman_2_name(self, value):
        self._linesman_2_name = value

class Schedule:
    def __init__(self, game_id):
        self._game_id = game_id
        self._home_team_id = None
        self._away_team_id = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def home_team_id(self):
        return self._home_team_id
    
    @home_team_id.setter
    def home_team_id(self, value):
        self._home_team_id = value

    @property
    def away_team_id(self):
        return self._away_team_id
    
    @away_team_id.setter
    def away_team_id(self, value):
        self._away_team_id = value

class ShiftData:
    def __init__(self, shift_id):
        self._shift_id = shift_id
        self._game_id = None
        self._player_id = None
        self._detail_code = None
        self._duration = None
        self._end_time = None
        self._start_time = None
        self._event_description = None
        self._event_details = None
        self._event_number = None
        self._period_number = None
        self._shift_number = None
        self._type_code = None

    @property
    def shift_id(self):
        return self._shift_id

    @shift_id.setter
    def shift_id(self, value):
        self._shift_id = value

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, value):
        self._game_id = value

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def detail_code(self):
        return self._detail_code
    
    @detail_code.setter
    def detail_code(self, value):
        self._detail_code = value

    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def event_description(self):
        return self._event_description
    
    @event_description.setter
    def event_description(self, value):
        self._event_description = value

    @property
    def event_details(self):
        return self._event_details
    
    @event_details.setter
    def event_details(self, value):
        self._event_details = value

    @property
    def event_number(self):
        return self._event_number
    
    @event_number.setter
    def event_number(self, value):
        self._event_number = value

    @property
    def period_number(self):
        return self._period_number
    
    @period_number.setter
    def period_number(self, value):
        self._period_number = value

    @property
    def shift_number(self):
        return self._shift_number
    
    @shift_number.setter
    def shift_number(self, value):
        self._shift_number = value

    @property
    def type_code(self):
        return self._type_code
    
    @type_code.setter
    def type_code(self, value):
        self._type_code = value

        



    















