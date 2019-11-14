PARSING_SCHEME = {
    'name': 'a',
    'games_played': 'td[data-stat="g"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'win_percentage': 'td[data-stat="win_loss_perc"]:first',
    'points_for': 'td[data-stat="points"]:first',
    'points_against': 'td[data-stat="points_opp"]:first',
    'points_difference': 'td[data-stat="points_diff"]:first',
    'margin_of_victory': 'td[data-stat="mov"]:first',
    'strength_of_schedule': 'td[data-stat="sos_total"]:first',
    'simple_rating_system': 'td[data-stat="srs_total"]:first',
    'offensive_simple_rating_system': 'td[data-stat="srs_offense"]:first',
    'defensive_simple_rating_system': 'td[data-stat="srs_defense"]:first',
    'yards': 'td[data-stat="total_yards"]:first',
    'plays': 'td[data-stat="plays_offense"]:first',
    'yards_per_play': 'td[data-stat="yds_per_play_offense"]:first',
    'turnovers': 'td[data-stat="turnovers"]:first',
    'fumbles': 'td[data-stat="fumbles_lost"]:first',
    'first_downs': 'td[data-stat="first_down"]:first',
    'pass_completions': 'td[data-stat="pass_cmp"]:first',
    'pass_attempts': 'td[data-stat="pass_att"]:first',
    'pass_yards': 'td[data-stat="pass_yds"]:first',
    'pass_touchdowns': 'td[data-stat="pass_td"]:first',
    'interceptions': 'td[data-stat="pass_int"]:first',
    'pass_net_yards_per_attempt': 'td[data-stat="pass_net_yds_per_att"]:first',
    'pass_first_downs': 'td[data-stat="pass_fd"]:first',
    'rush_attempts': 'td[data-stat="rush_att"]:first',
    'rush_yards': 'td[data-stat="rush_yds"]:first',
    'rush_touchdowns': 'td[data-stat="rush_td"]:first',
    'rush_yards_per_attempt': 'td[data-stat="rush_yds_per_att"]:first',
    'rush_first_downs': 'td[data-stat="rush_fd"]:first',
    'penalties': 'td[data-stat="penalties"]:first',
    'yards_from_penalties': 'td[data-stat="penalties_yds"]:first',
    'first_downs_from_penalties': 'td[data-stat="pen_fd"]:first',
    'percent_drives_with_points': 'td[data-stat="score_pct"]:first',
    'percent_drives_with_turnovers': 'td[data-stat="turnover_pct"]:first',
    'points_contributed_by_offense': 'td[data-stat="exp_pts_tot"]:first'
}

SCHEDULE_SCHEME = {
    'week': 'th[data-stat="week_num"]:first',
    'day': 'td[data-stat="game_day_of_week"]:first',
    'date': 'td[data-stat="game_date"]:first',
    'result': 'td[data-stat="game_outcome"]:first',
    'overtime': 'td[data-stat="overtime"]:first',
    'location': 'td[data-stat="game_location"]:first',
    'opponent_name': 'td[data-stat="opp"]:first',
    'points_scored': 'td[data-stat="pts_off"]:first',
    'points_allowed': 'td[data-stat="pts_def"]:first',
    'pass_completions': 'td[data-stat="pass_cmp"]:first',
    'pass_attempts': 'td[data-stat="pass_att"]:first',
    'pass_yards': 'td[data-stat="pass_yds"]:first',
    'pass_touchdowns': 'td[data-stat="pass_td"]:first',
    'interceptions': 'td[data-stat="pass_int"]:first',
    'times_sacked': 'td[data-stat="pass_sacked"]:first',
    'yards_lost_from_sacks': 'td[data-stat="pass_sacked_yds"]:first',
    'pass_yards_per_attempt': 'td[data-stat="pass_yds_per_att"]:first',
    'pass_completion_rate': 'td[data-stat="pass_cmp_perc"]:first',
    'quarterback_rating': 'td[data-stat="pass_rating"]:first',
    'rush_attempts': 'td[data-stat="rush_att"]:first',
    'rush_yards': 'td[data-stat="rush_yds"]:first',
    'rush_yards_per_attempt': 'td[data-stat="rush_yds_per_att"]:first',
    'rush_touchdowns': 'td[data-stat="rush_td"]:first',
    'field_goals_made': 'td[data-stat="fgm"]:first',
    'field_goals_attempted': 'td[data-stat="fga"]:first',
    'extra_points_made': 'td[data-stat="xpm"]:first',
    'extra_points_attempted': 'td[data-stat="xpa"]:first',
    'punts': 'td[data-stat="punt"]:first',
    'punt_yards': 'td[data-stat="punt_yds"]:first',
    'third_down_conversions': 'td[data-stat="third_down_success"]:first',
    'third_down_attempts': 'td[data-stat="third_down_att"]:first',
    'fourth_down_conversions': 'td[data-stat="fourth_down_success"]:first',
    'fourth_down_attempts': 'td[data-stat="fourth_down_att"]:first',
    'time_of_possession': 'td[data-stat="time_of_poss"]:first'
}

BOXSCORE_SCHEME = {
    'game_info': 'div[class="scorebox_meta"]:first',
    'home_name': 'a[itemprop="name"]:first',
    'away_name': 'a[itemprop="name"]:last',
    'away_points': 'div[class="scorebox"] div[class="score"]',
    'away_first_downs': 'td[data-stat="vis_stat"]',
    'away_rush_attempts': 'td[data-stat="vis_stat"]',
    'away_rush_yards': 'td[data-stat="vis_stat"]',
    'away_rush_touchdowns': 'td[data-stat="vis_stat"]',
    'away_pass_completions': 'td[data-stat="vis_stat"]',
    'away_pass_attempts': 'td[data-stat="vis_stat"]',
    'away_pass_yards': 'td[data-stat="vis_stat"]',
    'away_pass_touchdowns': 'td[data-stat="vis_stat"]',
    'away_interceptions': 'td[data-stat="vis_stat"]',
    'away_times_sacked': 'td[data-stat="vis_stat"]',
    'away_yards_lost_from_sacks': 'td[data-stat="vis_stat"]',
    'away_net_pass_yards': 'td[data-stat="vis_stat"]',
    'away_total_yards': 'td[data-stat="vis_stat"]',
    'away_fumbles': 'td[data-stat="vis_stat"]',
    'away_fumbles_lost': 'td[data-stat="vis_stat"]',
    'away_turnovers': 'td[data-stat="vis_stat"]',
    'away_penalties': 'td[data-stat="vis_stat"]',
    'away_yards_from_penalties': 'td[data-stat="vis_stat"]',
    'away_third_down_conversions': 'td[data-stat="vis_stat"]',
    'away_third_down_attempts': 'td[data-stat="vis_stat"]',
    'away_fourth_down_conversions': 'td[data-stat="vis_stat"]',
    'away_fourth_down_attempts': 'td[data-stat="vis_stat"]',
    'away_time_of_possession': 'td[data-stat="vis_stat"]',
    'home_points': 'div[class="scorebox"] div[class="score"]',
    'home_first_downs': 'td[data-stat="home_stat"]',
    'home_rush_attempts': 'td[data-stat="home_stat"]',
    'home_rush_yards': 'td[data-stat="home_stat"]',
    'home_rush_touchdowns': 'td[data-stat="home_stat"]',
    'home_pass_completions': 'td[data-stat="home_stat"]',
    'home_pass_attempts': 'td[data-stat="home_stat"]',
    'home_pass_yards': 'td[data-stat="home_stat"]',
    'home_pass_touchdowns': 'td[data-stat="home_stat"]',
    'home_interceptions': 'td[data-stat="home_stat"]',
    'home_times_sacked': 'td[data-stat="home_stat"]',
    'home_yards_lost_from_sacks': 'td[data-stat="home_stat"]',
    'home_net_pass_yards': 'td[data-stat="home_stat"]',
    'home_total_yards': 'td[data-stat="home_stat"]',
    'home_fumbles': 'td[data-stat="home_stat"]',
    'home_fumbles_lost': 'td[data-stat="home_stat"]',
    'home_turnovers': 'td[data-stat="home_stat"]',
    'home_penalties': 'td[data-stat="home_stat"]',
    'home_yards_from_penalties': 'td[data-stat="home_stat"]',
    'home_third_down_conversions': 'td[data-stat="home_stat"]',
    'home_third_down_attempts': 'td[data-stat="home_stat"]',
    'home_fourth_down_conversions': 'td[data-stat="home_stat"]',
    'home_fourth_down_attempts': 'td[data-stat="home_stat"]',
    'home_time_of_possession': 'td[data-stat="home_stat"]'
}

BOXSCORE_ELEMENT_INDEX = {
    'date': 0,
    'time': 1,
    'stadium': 2,
    'attendance': 3,
    'duration': 4,
    'away_points': 1,
    'away_first_downs': 0,
    'away_rush_attempts': 1,
    'away_rush_yards': 1,
    'away_rush_touchdowns': 1,
    'away_pass_completions': 2,
    'away_pass_attempts': 2,
    'away_pass_yards': 2,
    'away_pass_touchdowns': 2,
    'away_interceptions': 2,
    'away_times_sacked': 3,
    'away_yards_lost_from_sacks': 3,
    'away_net_pass_yards': 4,
    'away_total_yards': 5,
    'away_fumbles': 6,
    'away_fumbles_lost': 6,
    'away_turnovers': 7,
    'away_penalties': 8,
    'away_yards_from_penalties': 8,
    'away_third_down_conversions': 9,
    'away_third_down_attempts': 9,
    'away_fourth_down_conversions': 10,
    'away_fourth_down_attempts': 10,
    'away_time_of_possession': 11,
    'home_points': 0,
    'home_first_downs': 0,
    'home_rush_attempts': 1,
    'home_rush_yards': 1,
    'home_rush_touchdowns': 1,
    'home_pass_completions': 2,
    'home_pass_attempts': 2,
    'home_pass_yards': 2,
    'home_pass_touchdowns': 2,
    'home_interceptions': 2,
    'home_times_sacked': 3,
    'home_yards_lost_from_sacks': 3,
    'home_net_pass_yards': 4,
    'home_total_yards': 5,
    'home_fumbles': 6,
    'home_fumbles_lost': 6,
    'home_turnovers': 7,
    'home_penalties': 8,
    'home_yards_from_penalties': 8,
    'home_third_down_conversions': 9,
    'home_third_down_attempts': 9,
    'home_fourth_down_conversions': 10,
    'home_fourth_down_attempts': 10,
    'home_time_of_possession': 11
}

# Designates the index of the item within the requested tag
BOXSCORE_ELEMENT_SUB_INDEX = {
    'away_rush_attempts': 0,
    'away_rush_yards': 1,
    'away_rush_touchdowns': 2,
    'away_pass_completions': 0,
    'away_pass_attempts': 1,
    'away_pass_yards': 2,
    'away_pass_touchdowns': 3,
    'away_interceptions': 4,
    'away_times_sacked': 0,
    'away_yards_lost_from_sacks': 1,
    'away_fumbles': 0,
    'away_fumbles_lost': 1,
    'away_penalties': 0,
    'away_yards_from_penalties': 1,
    'away_third_down_conversions': 0,
    'away_third_down_attempts': 1,
    'away_fourth_down_conversions': 0,
    'away_fourth_down_attempts': 1,
    'home_rush_attempts': 0,
    'home_rush_yards': 1,
    'home_rush_touchdowns': 2,
    'home_pass_completions': 0,
    'home_pass_attempts': 1,
    'home_pass_yards': 2,
    'home_pass_touchdowns': 3,
    'home_interceptions': 4,
    'home_times_sacked': 0,
    'home_yards_lost_from_sacks': 1,
    'home_fumbles': 0,
    'home_fumbles_lost': 1,
    'home_penalties': 0,
    'home_yards_from_penalties': 1,
    'home_third_down_conversions': 0,
    'home_third_down_attempts': 1,
    'home_fourth_down_conversions': 0,
    'home_fourth_down_attempts': 1,
}

PLAYER_SCHEME = {
    'season': 'th[data-stat="year_id"]',
    'name': 'h1[itemprop="name"]',
    'team_abbreviation': 'td[data-stat="team"]',
    'position': 'td[data-stat="pos"]',
    'height': 'span[itemprop="height"]',
    'weight': 'span[itemprop="weight"]',
    'birth_date': 'td[data-stat=""]',
    'contract': 'td[data-stat=""]',
    'games': 'td[data-stat="g"]',
    'games_started': 'td[data-stat="gs"]',
    'approximate_value': 'td[data-stat="av"]',
    'qb_record': 'td[data-stat="qb_rec"]',
    'completed_passes': 'td[data-stat="pass_cmp"]',
    'attempted_passes': 'td[data-stat="pass_att"]',
    'passing_completion': 'td[data-stat="pass_cmp_perc"]',
    'passing_yards': 'td[data-stat="pass_yds"]',
    'passing_touchdowns': 'td[data-stat="pass_td"]',
    'passing_touchdown_percentage': 'td[data-stat="pass_td_perc"]',
    'interceptions_thrown': 'td[data-stat="pass_int"]',
    'interception_percentage': 'td[data-stat="pass_int_perc"]',
    'longest_pass': 'td[data-stat="pass_long"]',
    'passing_yards_per_attempt': 'td[data-stat="pass_yds_per_att"]',
    'adjusted_yards_per_attempt': 'td[data-stat="pass_adj_yds_per_att"]',
    'yards_per_completed_pass': 'td[data-stat="pass_yds_per_cmp"]',
    'yards_per_game_played': 'td[data-stat="pass_yds_per_g"]',
    'quarterback_rating': 'td[data-stat="pass_rating"]',
    'espn_qbr': 'td[data-stat="qbr"]',
    'times_sacked': 'td[data-stat="pass_sacked"]',
    'yards_lost_to_sacks': 'td[data-stat="pass_sacked_yds"]',
    'net_yards_per_pass_attempt': 'td[data-stat="pass_net_yds_per_att"]',
    'adjusted_net_yards_per_pass_attempt':
    'td[data-stat="pass_adj_net_yds_per_att"]',
    'sack_percentage': 'td[data-stat="pass_sacked_per"]',
    'fourth_quarter_comebacks': 'td[data-stat="comebacks"]',
    'game_winning_drives': 'td[data-stat="gwd"]',
    'yards_per_attempt_index': 'td[data-stat="pass_yds_per_att_index"]',
    'net_yards_per_attempt_index':
    'td[data-stat="pass_net_yds_per_att_index"]',
    'adjusted_yards_per_attempt_index':
    'td[data-stat="pass_adj_yds_per_att_index"]',
    'adjusted_net_yards_per_attempt_index':
    'td[data-stat="pass_adj_net_yds_per_att_index"]',
    'completion_percentage_index': 'td[data-stat="pass_cmp_perc_index"]',
    'touchdown_percentage_index': 'td[data-stat="pass_td_perc_index"]',
    'interception_percentage_index': 'td[data-stat="pass_int_perc_index"]',
    'sack_percentage_index': 'td[data-stat="pass_sacked_perc_index"]',
    'passer_rating_index': 'td[data-stat="pass_rating_index"]',
    'rush_attempts': 'td[data-stat="rush_att"]',
    'rush_yards': 'td[data-stat="rush_yds"]',
    'rush_touchdowns': 'td[data-stat="rush_td"]',
    'longest_rush': 'td[data-stat="rush_long"]',
    'rush_yards_per_attempt': 'td[data-stat="rush_yds_per_att"]',
    'rush_yards_per_game': 'td[data-stat="rush_yds_per_g"]',
    'rush_attempts_per_game': 'td[data-stat="rush_att_per_g"]',
    'times_pass_target': 'td[data-stat="targets"]',
    'receptions': 'td[data-stat="rec"]',
    'receiving_yards': 'td[data-stat="rec_yds"]',
    'receiving_yards_per_reception': 'td[data-stat="rec_yds_per_rec"]',
    'receiving_touchdowns': 'td[data-stat="rec_td"]',
    'longest_reception': 'td[data-stat="rec_long"]',
    'receptions_per_game': 'td[data-stat="rec_per_g"]',
    'receiving_yards_per_game': 'td[data-stat="rec_yds_per_g"]',
    'catch_percentage': 'td[data-stat="catch_pct"]',
    'touches': 'td[data-stat="touches"]',
    'yards_per_touch': 'td[data-stat="yds_per_touch"]',
    'yards_from_scrimmage': 'td[data-stat="yds_from_scrimmage"]',
    'rushing_and_receiving_touchdowns': 'td[data-stat="rush_receive_td"]',
    'fumbles': 'td[data-stat="fumbles"]',
    'punt_returns': 'td[data-stat="punt_ret"]',
    'punt_return_yards': 'td[data-stat="punt_ret_yds"]',
    'punt_return_touchdown': 'td[data-stat="punt_ret_td"]',
    'longest_punt_return': 'td[data-stat="punt_ret_long"]',
    'yards_per_punt_return': 'td[data-stat="punt_ret_yds_per_ret"]',
    'kickoff_returns': 'td[data-stat="kick_ret"]',
    'kickoff_return_yards': 'td[data-stat="kick_ret_yds"]',
    'kickoff_return_touchdown': 'td[data-stat="kick_ret_td"]',
    'longest_kickoff_return': 'td[data-stat="kick_ret_long"]',
    'yards_per_kickoff_return': 'td[data-stat="kick_ret_yds_per_ret"]',
    'all_purpose_yards': 'td[data-stat="all_purpose_yds"]',
    'less_than_nineteen_yards_field_goal_attempts': 'td[data-stat="fga1"]',
    'less_than_nineteen_yards_field_goals_made': 'td[data-stat="fgm1"]',
    'twenty_to_twenty_nine_yard_field_goal_attempts': 'td[data-stat="fga2"]',
    'twenty_to_twenty_nine_yard_field_goals_made': 'td[data-stat="fgm2"]',
    'thirty_to_thirty_nine_yard_field_goal_attempts': 'td[data-stat="fga3"]',
    'thirty_to_thirty_nine_yard_field_goals_made': 'td[data-stat="fgm3"]',
    'fourty_to_fourty_nine_yard_field_goal_attempts': 'td[data-stat="fga4"]',
    'fourty_to_fourty_nine_yard_field_goals_made': 'td[data-stat="fgm4"]',
    'fifty_plus_yard_field_goal_attempts': 'td[data-stat="fga5"]',
    'fifty_plus_yard_field_goals_made': 'td[data-stat="fgm5"]',
    'field_goals_attempted': 'td[data-stat="fga"]',
    'field_goals_made': 'td[data-stat="fgm"]',
    'longest_field_goal_made': 'td[data-stat="fg_long"]',
    'field_goal_percentage': 'td[data-stat="fg_perc"]',
    'extra_points_attempted': 'td[data-stat="xpa"]',
    'extra_points_made': 'td[data-stat="xpm"]',
    'extra_point_percentage': 'td[data-stat="xp_perc"]',
    'punts': 'td[data-stat="punt"]',
    'total_punt_yards': 'td[data-stat="punt_yds"]',
    'longest_punt': 'td[data-stat="punt_long"]',
    'blocked_punts': 'td[data-stat="punt_blocked"]',
    'yards_per_punt': 'td[data-stat="punt_yds_per_punt"]',
    'interceptions': 'td[data-stat="def_int"]',
    'yards_returned_from_interception': 'td[data-stat="def_int_yds"]',
    'interceptions_returned_for_touchdown': 'td[data-stat="def_int_td"]',
    'longest_interception_return': 'td[data-stat="def_int_long"]',
    'passes_defended': 'td[data-stat="pass_defended"]',
    'fumbles_forced': 'td[data-stat="fumbles_forced"]',
    'fumbles_recovered': 'td[data-stat="fumbles_rec"]',
    'yards_recovered_from_fumble': 'td[data-stat="fumbles_rec_yds"]',
    'fumbles_recovered_for_touchdown': 'td[data-stat="fumbles_rec_yds"]',
    'sacks': 'td[data-stat="sacks"]',
    'tackles': 'td[data-stat="tackles_solo"]',
    'assists_on_tackles': 'td[data-stat="tackles_assists"]',
    'safeties': 'td[data-stat="safety_md"]',
    'yards_lost_from_sacks': 'td[data-stat="pass_sacked_yds"]',
    'fumbles_lost': 'td[data-stat="fumbles_lost"]',
    'combined_tackles': 'td[data-stat="tackles_combined"]',
    'solo_tackles': 'td[data-stat="tackles_solo"]',
    'tackles_for_loss': 'td[data-stat="tackles_loss"]',
    'quarterback_hits': 'td[data-stat="qb_hits"]',
    'average_kickoff_return_yards': 'td[data-stat="kick_ret_yds_per_ret"]',
    'kickoff_return_touchdowns': 'td[data-stat="kick_ret_td"]',
    'average_punt_return_yards': 'td[data-stat="punt_ret_yds_per_ret"]',
    'punt_return_touchdowns': 'td[data-stat="punt_ret_td"]'
}

SEASON_PAGE_URL = 'http://www.pro-football-reference.com/years/%s/'

SCHEDULE_URL = 'https://www.pro-football-reference.com/teams/%s/%s/gamelog/'

BOXSCORE_URL = 'https://www.pro-football-reference.com/boxscores/%s.htm'

BOXSCORES_URL = 'https://www.pro-football-reference.com/years/%s/week_%s.htm'
PLAYER_URL = 'https://www.pro-football-reference.com/players/%s/%s.htm'
ROSTER_URL = 'https://www.pro-football-reference.com/teams/%s/%s_roster.htm'

WILD_CARD = 100
DIVISION = 101
CONF_CHAMPIONSHIP = 102
SUPER_BOWL = 103
