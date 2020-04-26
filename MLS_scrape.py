from selenium import webdriver
import csv

# Open Chromdriver and go to first page to scrape
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.fbref.com/en/comps/22/2798/2019-Major-League-Soccer-Stats")

# Start csv file
csv_file = open('MLS_data.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# Click button to go to Squad Goalkeeping Table
squad_goalkeeping_button = driver.find_element_by_link_text('Squad Goalkeeping')
squad_goalkeeping_button.click()

# Scrape data from Squad Goalkeeping Table

# Scrape team names
# Find all elements containing team names
teams_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/th/a')
# Get list of team names
teams_2019 = []
for team19 in teams_2019_elements:
    print(team19.text)
    teams_2019.append(team19.text)

# Scrape matches played
matches_played_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[2]')
matches_played_2019 = []
for matches19 in matches_played_2019_elements:
    print(matches19.text)
    matches_played_2019.append(matches19.text)

# Scrape wins
wins_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[10]')
wins_2019 = []
for win19 in wins_2019_elements:
    print(win19.text)
    wins_2019.append(win19.text)

# Scrape draws
draws_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[11]')
draws_2019 = []
for draw19 in draws_2019_elements:
    print(draw19.text)
    draws_2019.append(draw19.text)

# Scrape losses
losses_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[12]')
losses_2019 = []
for loss19 in losses_2019_elements:
    print(loss19.text)
    losses_2019.append(loss19.text)

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Passing Table
squad_passing_button = driver.find_element_by_link_text('Squad Passing')
squad_passing_button.click()

# Scrape data from Squad Passing Table

# Scrape crosses completed into box
completed_crosses_into_box_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_squads"]/table/tbody/tr/td[22]')
completed_crosses_into_box_2019 = []
for compcross19 in completed_crosses_into_box_2019_elements:
    print(compcross19.text)
    completed_crosses_into_box_2019.append(compcross19.text)

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Pass Types Table
squad_pass_types_button = driver.find_element_by_link_text('Squad Pass Types')
squad_pass_types_button.click()

# Scrape data from Squad Pass Types Table

# Scrape crosses
crosses_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_types_squads"]/table/tbody/tr/td[9]')
crosses_2019 = []
for cross19 in crosses_2019_elements:
    print(cross19.text)
    crosses_2019.append(cross19.text)

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Defensive Actions Table
squad_defensive_actions_button = driver.find_element_by_link_text('Squad Defensive Actions')
squad_defensive_actions_button.click()

# Scrape data from Squad Defensive Actions Table

# Scrape pressures
pressures_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[11]')
pressures_2019 = []
for press19 in pressures_2019_elements:
    print(press19.text)
    pressures_2019.append(press19.text)

# Scrape successful pressures
successful_pressures_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[12]')
successful_pressures_2019 = []
for sp19 in successful_pressures_2019_elements:
    print(sp19.text)
    successful_pressures_2019.append(sp19.text)

# Scrape number of pressures in the attacking third
num_high_press_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[16]')
num_high_press_2019 = []
for hp19 in num_high_press_2019_elements:
    print(hp19.text)
    num_high_press_2019.append(hp19.text)

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Playing Time Table
squad_playing_time_button = driver.find_element_by_link_text('Squad Playing Time')
squad_playing_time_button.click()

# Scrape data from Squad Playing Time Table

# Scrape goals scored
goals_scored_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[12]')
goals_scored_2019 = []
for goal19 in goals_scored_2019_elements:
    print(goal19.text)
    goals_scored_2019.append(goal19.text)

# Scrape goal difference
goal_difference_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[14]')
goal_difference_2019 = []
for diff19 in goal_difference_2019_elements:
    print(diff19.text)
    goal_difference_2019.append(diff19.text)

# Scrape expected goals scored
expected_goals_scored_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[16]')
expected_goals_scored_2019 = []
for xgs19 in expected_goals_scored_2019_elements:
    print(xgs19.text)
    expected_goals_scored_2019.append(xgs19.text)

# Scrape expected goal differential
expected_goal_difference_2019_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[18]')
expected_goal_difference_2019 = []
for xgd19 in expected_goal_difference_2019_elements:
    print(xgd19.text)
    expected_goal_difference_2019.append(xgd19.text)

# Scroll back to top of page to go to prior year's data
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to 2018 data
previous_season_button = driver.find_element_by_link_text('Previous Season')
previous_season_button.click()

# Repeat for 2018 seasons page

teams_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/th/a')
teams_2018 = []
for team18 in teams_2018_elements:
    print(team18.text)
    teams_2018.append(team18.text)

matches_played_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[2]')
matches_played_2018 = []
for matches18 in matches_played_2018_elements:
    print(matches18.text)
    matches_played_2018.append(matches18.text)

wins_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[10]')
wins_2018 = []
for win18 in wins_2018_elements:
    print(win18.text)
    wins_2018.append(win18.text)

draws_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[11]')
draws_2018 = []
for draw18 in draws_2018_elements:
    print(draw18.text)
    draws_2018.append(draw18.text)

losses_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/td[12]')
losses_2018 = []
for loss18 in losses_2018_elements:
    print(loss18.text)
    losses_2018.append(loss18.text)

driver.execute_script('window.scrollTo(0, 0)')

squad_passing_button = driver.find_element_by_link_text('Squad Passing')
squad_passing_button.click()

completed_crosses_into_box_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_squads"]/table/tbody/tr/td[22]')
completed_crosses_into_box_2018 = []
for compcross18 in completed_crosses_into_box_2018_elements:
    print(compcross18.text)
    completed_crosses_into_box_2018.append(compcross18.text)

driver.execute_script('window.scrollTo(0, 0)')

squad_pass_types_button = driver.find_element_by_link_text('Squad Pass Types')
squad_pass_types_button.click()

crosses_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_passing_types_squads"]/table/tbody/tr/td[9]')
crosses_2018 = []
for cross18 in crosses_2018_elements:
    print(cross18.text)
    crosses_2018.append(cross18.text)

driver.execute_script('window.scrollTo(0, 0)')

squad_defensive_actions_button = driver.find_element_by_link_text('Squad Defensive Actions')
squad_defensive_actions_button.click()

pressures_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[11]')
pressures_2018 = []
for press18 in pressures_2018_elements:
    print(press18.text)
    pressures_2018.append(press18.text)

successful_pressures_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[12]')
successful_pressures_2018 = []
for sp18 in successful_pressures_2018_elements:
    print(sp18.text)
    successful_pressures_2018.append(sp18.text)

num_high_press_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_defense_squads"]/table/tbody/tr/td[16]')
num_high_press_2018 = []
for hp18 in num_high_press_2018_elements:
    print(hp18.text)
    num_high_press_2018.append(hp18.text)

driver.execute_script('window.scrollTo(0, 0)')

squad_playing_time_button = driver.find_element_by_link_text('Squad Playing Time')
squad_playing_time_button.click()

goals_scored_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[12]')
goals_scored_2018 = []
for goal18 in goals_scored_2018_elements:
    print(goal18.text)
    goals_scored_2018.append(goal18.text)

goal_difference_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[14]')
goal_difference_2018 = []
for diff18 in goal_difference_2018_elements:
    print(diff18.text)
    goal_difference_2018.append(diff18.text)

expected_goals_scored_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[16]')
expected_goals_scored_2018 = []
for xgs18 in expected_goals_scored_2018_elements:
    print(xgs18.text)
    expected_goals_scored_2018.append(xgs18.text)

expected_goal_difference_2018_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_playing_time_squads"]/table/tbody/tr/td[18]')
expected_goal_difference_2018 = []
for xgd18 in expected_goal_difference_2018_elements:
    print(xgd18.text)
    expected_goal_difference_2018.append(xgd18.text)

# Write to csv file
rows = (teams_2019, matches_played_2019, wins_2019, draws_2019, losses_2019, goals_scored_2019, goal_difference_2019, \
expected_goals_scored_2019, expected_goal_difference_2019, crosses_2019, completed_crosses_into_box_2019, pressures_2019, \
successful_pressures_2019, num_high_press_2019, teams_2018, matches_played_2018, wins_2018, draws_2018, losses_2018, goals_scored_2018, \
goal_difference_2018, expected_goals_scored_2018, expected_goal_difference_2018, crosses_2018, completed_crosses_into_box_2018, \
pressures_2018, successful_pressures_2018, num_high_press_2018)

for row in rows:
    writer.writerow(row)

csv_file.close()
driver.close()
