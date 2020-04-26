from selenium import webdriver
from selenium.webdriver.common.by import By
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
squad_goalkeeping_button = .driver.find_element_by_link_text('Squad Goalkeeping')
squad_goalkeeping_button.click()

# Scrape data from Squad Goalkeeping Table

# Scrape team names

# Find all elements containing team names
team_elements = driver.find_elements_by_xpath('.//div[@id="div_stats_keeper_squads"]/table/tbody/tr/th/a')

# Get list of team names
teams = ''
for team in team_elements:
    teams = teams + team.text + ', '
teams = (teams.rstrip(', ')).split(', ')

# Scrape matches played



# Scrape wins



# Scrape draws



# Scrape losses



# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Passing Table
squad_passing_button = .driver.find_element_by_link_text('Squad Passing')
squad_passing_button.click()

# Scrape data from Squad Passing Table
# Code here

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Pass Types Table
squad_pass_types_button = .driver.find_element_by_link_text('Squad Pass Types')
squad_pass_types_button.click()

# Scrape data from Squad Pass Types Table
# Code here

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Defensive Actions Table
squad_defensive_actions_button = .driver.find_element_by_link_text('Squad Defensive Actions')
squad_defensive_actions_button.click()

# Scrape data from Squad Defensive Actions Table
# Code here

# Scroll back to top of page for easier in-page navigation
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to Squad Playing Time Table
squad_playing_time_button = .driver.find_element_by_link_text('Squad Playing Time Actions')
squad_playing_time_button.click()

# Scrape data from Squad Playing Time Table
# Code here

# Scroll back to top of page to go to prior year's data
driver.execute_script('window.scrollTo(0, 0)')

# Click button to go to 2018 data
previous_season_button = .driver.find_element_by_link_text('Previous Season')
previous_season_button.click()

##repeat


# Close csv file
csv_file.close()
driver.close()
