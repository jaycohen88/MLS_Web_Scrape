from selenium import webdriver
import csv

# Open Chromdriver and go to first page to scrape
driver = webdriver.Chrome()
driver.get("https://www.fbref.com/en/comps/22/2798/2019-Major-League-Soccer-Stats")

# Start csv file
csv_file = open('MLS_data.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# Initialize empty dictionary
final_data = {}

# Click button to go to Squad Goalkeeping Table
squad_goalkeeping_button = driver.find_element_by_link_text('Squad Goalkeeping')
squad_goalkeeping_button.click()

# Scrape data from Squad Goalkeeping Table

# Scrape team names
# Find all elements containing team names
teams_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/th/a')
# Get list of team names
teams_2019 = ''
for team19 in teams_2019_elements:
    teams_2019 = teams_2019 + team19.text + ', '
teams_2019 = (teams_2019.rstrip(', ')).split(', ')

# Scrape matches played
matches_played_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[2]')
matches_played_2019 = ''
for matches19 in matches_played_2019_elements:
    matches_played_2019 = matches_played_2019 + matches19.text + ', '
matches_played_2019 = (matches_played_2019.rstrip(', ')).split(', ')

# Scrape wins
wins_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[10]')
wins_2019 = ''
for win19 in wins_2019_elements:
    wins_2019 = wins_2019 + win19.text + ', '
wins_2019 = (wins_2019.rstrip(', ')).split(', ')

# Scrape draws
draws_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[11]')
draws_2019 = ''
for draw19 in draws_2019_elements:
    draws_2019 = draws_2019 + draw19.text + ', '
draws_2019 = (draws_2019.rstrip(', ')).split(', ')

# Scrape losses
losses_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[12]')
losses_2019 = ''
for loss19 in losses_2019_elements:
    losses_2019 = losses_2019 + loss19.text + ', '
losses_2019 = (losses_2019.rstrip(', ')).split(', ')

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Passing Table
squad_passing_button = driver.find_element_by_link_text('Squad Passing')
squad_passing_button.click()

# Scrape data from Squad Passing Table

# Scrape crosses completed into box
completed_crosses_into_box_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_squads"]/table/tbody/tr/td[22]')
completed_crosses_into_box_2019 = ''
for compcross19 in completed_crosses_into_box_2019_elements:
    completed_crosses_into_box_2019 = completed_crosses_into_box_2019 + compcross19.text + ', '
completed_crosses_into_box_2019 = (completed_crosses_into_box_2019.rstrip(', ')).split(', ')

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Pass Types Table
squad_pass_types_button = driver.find_element_by_link_text('Squad Pass Types')
squad_pass_types_button.click()

# Scrape data from Squad Pass Types Table

# Scrape crosses
crosses_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_types_squads"]/table/tbody/tr/td[9]')
crosses_2019 = ''
for cross19 in crosses_2019_elements:
    crosses_2019 = crosses_2019 + cross19.text + ', '
crosses_2019 = (crosses_2019.rstrip(', ')).split(', ')

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Defensive Actions Table
squad_defensive_actions_button = driver.find_element_by_link_text('Squad Defensive Actions')
squad_defensive_actions_button.click()

# Scrape data from Squad Defensive Actions Table

# Scrape pressures
pressures_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[11]')
pressures_2019 = ''
for press19 in pressures_2019_elements:
    pressures_2019 = pressures_2019 + press19.text + ', '
pressures_2019 = (pressures_2019.rstrip(', ')).split(', ')

# Scrape successful pressures
successful_pressures_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[12]')
successful_pressures_2019 = ''
for sp19 in successful_pressures_2019_elements:
    successful_pressures_2019 = successful_pressures_2019 + sp19.text + ', '
successful_pressures_2019 = (successful_pressures_2019.rstrip(', ')).split(', ')

# Scrape number of pressures in the attacking third
num_high_press_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[16]')
num_high_press_2019 = ''
for hp19 in num_high_press_2019_elements:
    num_high_press_2019 = num_high_press_2019 + hp19.text + ', '
num_high_press_2019 = (num_high_press_2019.rstrip(', ')).split(', ')

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Playing Time Table
squad_playing_time_button = driver.find_element_by_link_text('Squad Playing Time Actions')
squad_playing_time_button.click()

# Scrape data from Squad Playing Time Table

# Scrape goals scored
goals_scored_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[12]')
goals_scored_2019 = ''
for goal19 in goals_scored_2019_elements:
    goals_scored_2019 = goals_scored_2019 + goal19.text + ', '
goals_scored_2019 = (goals_scored_2019.rstrip(', ')).split(', ')

# Scrape goal difference
goal_difference_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[14]')
goal_difference_2019 = ''
for diff19 in goal_difference_2019_elements:
    goal_difference_2019 = goal_difference_2019 + diff19.text + ', '
goal_difference_2019 = (goal_difference_2019.rstrip(', ')).split(', ')

# Scrape expected goals scored
expected_goals_scored_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[16]')
expected_goals_scored_2019 = ''
for xgs19 in expected_goals_scored_2019_elements:
    expected_goals_scored_2019 = expected_goals_scored_2019 + xgs19.text + ', '
expected_goals_scored_2019 = (expected_goals_scored_2019.rstrip(', ')).split(', ')

# Scrape expected goal differential
expected_goal_difference_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[18]')
expected_goal_difference_2019 = ''
for xgd19 in expected_goal_difference_2019_elements:
    expected_goal_difference_2019 = expected_goal_difference_2019 + xgd19.text + ', '
expected_goal_difference_2019 = (expected_goal_difference_2019.rstrip(', ')).split(', ')

# Scroll back to top of page to go to prior year's data
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to 2018 data
previous_season_button = driver.find_element_by_link_text('Previous Season')
previous_season_button.click()

# Repeat for 2018 page

squad_goalkeeping_button = driver.find_element_by_link_text('Squad Goalkeeping')
squad_goalkeeping_button.click()

teams_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/th/a')
teams_2018 = ''
for team18 in teams_2018_elements:
    teams_2018 = teams_2018 + team18.text + ', '
teams_2018 = (teams_2018.rstrip(', ')).split(', ')

matches_played_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[2]')
matches_played_2018 = ''
for matches18 in matches_played_2018_elements:
    matches_played_2018 = matches_played_2018 + matches18.text + ', '
matches_played_2018 = (matches_played_2018.rstrip(', ')).split(', ')

wins_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[10]')
wins_2018 = ''
for win18 in wins_2018_elements:
    wins_2018 = wins_2018 + win18.text + ', '
wins_2018 = (wins_2018.rstrip(', ')).split(', ')

draws_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[11]')
draws_2018 = ''
for draw18 in draws_2018_elements:
    draws_2018 = draws_2018 + draw18.text + ', '
draws_2018 = (draws_2018.rstrip(', ')).split(', ')

losses_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[12]')
losses_2018 = ''
for loss18 in losses_2018_elements:
    losses_2018 = losses_2018 + loss18.text + ', '
losses_2018 = (losses_2018.rstrip(', ')).split(', ')

driver.execute_script('window.scrollTo(0, 0)')

squad_passing_button = driver.find_element_by_link_text('Squad Passing')
squad_passing_button.click()

completed_crosses_into_box_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_squads"]/table/tbody/tr/td[22]')
completed_crosses_into_box_2018 = ''
for compcross18 in completed_crosses_into_box_2018_elements:
    completed_crosses_into_box_2018 = completed_crosses_into_box_2018 + compcross18.text + ', '
completed_crosses_into_box_2018 = (completed_crosses_into_box_2018.rstrip(', ')).split(', ')

driver.execute_script('window.scrollTo(0, 0)')

squad_pass_types_button = driver.find_element_by_link_text('Squad Pass Types')
squad_pass_types_button.click()

crosses_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_types_squads"]/table/tbody/tr/td[9]')
crosses_2018 = ''
for cross18 in crosses_2018_elements:
    crosses_2018 = crosses_2018 + cross18.text + ', '
crosses_2018 = (crosses_2018.rstrip(', ')).split(', ')

driver.execute_script('window.scrollTo(0, 0)')

squad_defensive_actions_button = driver.find_element_by_link_text('Squad Defensive Actions')
squad_defensive_actions_button.click()

pressures_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[11]')
pressures_2018 = ''
for press18 in pressures_2018_elements:
    pressures_2018 = pressures_2018 + press18.text + ', '
pressures_2018 = (pressures_2018.rstrip(', ')).split(', ')

successful_pressures_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[12]')
successful_pressures_2018 = ''
for sp18 in successful_pressures_2018_elements:
    successful_pressures_2018 = successful_pressures_2018 + sp18.text + ', '
successful_pressures_2018 = (successful_pressures_2018.rstrip(', ')).split(', ')

num_high_press_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[16]')
num_high_press_2018 = ''
for hp18 in num_high_press_2018_elements:
    num_high_press_2018 = num_high_press_2018 + hp18.text + ', '
num_high_press_2018 = (num_high_press_2018.rstrip(', ')).split(', ')

driver.execute_script('window.scrollTo(0, 0)')

squad_playing_time_button = driver.find_element_by_link_text('Squad Playing Time Actions')
squad_playing_time_button.click()

goals_scored_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[12]')
goals_scored_2018 = ''
for goal18 in goals_scored_2018_elements:
    goals_scored_2018 = goals_scored_2018 + goal18.text + ', '
goals_scored_2018 = (goals_scored_2018.rstrip(', ')).split(', ')

goal_difference_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[14]')
goal_difference_2018 = ''
for diff18 in goal_difference_2018_elements:
    goal_difference_2018 = goal_difference_2018 + diff18.text + ', '
goal_difference_2018 = (goal_difference_2018.rstrip(', ')).split(', ')

expected_goals_scored_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[16]')
expected_goals_scored_2018 = ''
for xgs18 in expected_goals_scored_2018_elements:
    expected_goals_scored_2018 = expected_goals_scored_2018 + xgs18.text + ', '
expected_goals_scored_2018 = (expected_goals_scored_2018.rstrip(', ')).split(', ')

expected_goal_difference_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[18]')
expected_goal_difference_2018 = ''
for xgd18 in expected_goal_difference_2018_elements:
    expected_goal_difference_2018 = expected_goal_difference_2018 + xgd18.text + ', '
expected_goal_difference_2018 = (expected_goal_difference_2018.rstrip(', ')).split(', ')




# Close csv file
csv_file.close()
driver.close()
