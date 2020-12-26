from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time
import json
import itertools

USERNAME = 'devAccount231'
PASSWORD = 'verySecurePassword123'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--proxy-server="direct://"')
chrome_options.add_argument('--proxy-bypass-list=*')
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

#driver.maximize_window()        
driver.implicitly_wait(1)

driver.get('https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3639329617/37732098?tab=stats')

# account login  
driver.find_element_by_css_selector('.riotbar-account-action').click()
driver.find_element_by_name("username").send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_elements_by_css_selector('.mobile-button__submit')[0].click()

driver.implicitly_wait(1)
time.sleep(2)

# win/loss
result = []
for endResult in driver.find_elements_by_class_name('game-conclusion'):
        result.append(endResult.text)
print('result: ', result)

# kills
totalKills = []
for kills in driver.find_elements_by_class_name('gs-container.team-summary'):
        totalKills.append(kills.find_element_by_class_name('kills').text)
print('kills: ', totalKills)

# picks
picks = []
for pick in driver.find_elements_by_class_name('champion-nameplate-name'):
        picks.append(pick.find_elements_by_class_name('binding')[0].text)
print('picks: ', picks)

# pick pictures
pickPics = []
for png in driver.find_elements_by_class_name('champion-col.name'):
        pickPics.append(png.find_element_by_tag_name('img').get_attribute('src'))
print('pickPics: ', pickPics)

# kills, deaths, assists
kills = []
deaths = []
assists = []
for stats in driver.find_elements_by_class_name('kda-kda'):
        kills.append(stats.find_elements_by_tag_name('div')[0].text)
        deaths.append(stats.find_elements_by_tag_name('div')[1].text)
        assists.append(stats.find_elements_by_tag_name('div')[2].text)
print('kills: ', kills)
print('deaths: ', deaths)
print('assists: ', assists)

# Creep Score
creepScore = []
for creep in driver.find_elements_by_class_name('minions-col.cs'):
        creepScore.append(creep.find_element_by_class_name('binding').text)
print('creepScore: ', creepScore)

# bans
bans = []
# red team
for ban in driver.find_elements_by_class_name('bans-container')[0].find_elements_by_class_name('champion-nameplate'):
        bans.append(ban.find_element_by_tag_name('img').get_attribute('src'))
# blue team
for ban in driver.find_elements_by_class_name('bans-container')[1].find_elements_by_class_name('champion-nameplate'):
        bans.append(ban.find_element_by_tag_name('img').get_attribute('src'))
print('bans: ', bans)


game = {}
redObj = {}
blueObj = {}

redPicks = []
for x in itertools.islice(picks, 0, int(len(picks) / 2)):
        redPicks.append(x)

redPickPics = []
for x in itertools.islice(pickPics, 0, int(len(pickPics) / 2)):
        redPickPics.append(x)

redBans = []
for x in itertools.islice(bans, 0, int(len(bans) / 2)):
        redBans.append(x)

redKills = []
for x in itertools.islice(kills, 0, int(len(kills) / 2)):
        redKills.append(x)

redDeaths = []
for x in itertools.islice(deaths, 0, int(len(deaths) / 2)):
        redDeaths.append(x)

redAssists = []
for x in itertools.islice(assists, 0, int(len(assists) / 2)):
        redAssists.append(x)

redCreepScore = []
for x in itertools.islice(creepScore, 0, int(len(creepScore) / 2)):
        redCreepScore.append(x)

redObj['result'] = result[0]
redObj['totalKills'] = totalKills[0]
redObj['picks'] = redPicks
redObj['pickPics'] = redPickPics
redObj['bans'] = redBans
redObj['kills'] = redKills
redObj['deaths'] = redDeaths
redObj['assists'] = redAssists
redObj['creepScore'] = redCreepScore
game['redTeam'] = redObj

bluePicks = []
for x in itertools.islice(picks, int(len(picks) / 2), len(picks)):
        bluePicks.append(x)

bluePickPics = []
for x in itertools.islice(pickPics, int(len(pickPics) / 2), len(pickPics)):
        bluePickPics.append(x)

blueBans = []
for x in itertools.islice(bans, int(len(bans) / 2), len(bans)):
        blueBans.append(x)

blueKills = []
for x in itertools.islice(kills, int(len(kills) / 2), len(kills)):
        blueKills.append(x)

blueDeaths = []
for x in itertools.islice(deaths, int(len(deaths) / 2), len(deaths)):
        blueDeaths.append(x)

blueAssists = []
for x in itertools.islice(assists, int(len(assists) / 2), len(assists)):
        blueAssists.append(x)

blueCreepScore = []
for x in itertools.islice(creepScore, int(len(creepScore) / 2), len(creepScore)):
        blueCreepScore.append(x)

blueObj['result'] = result[1]
blueObj['totalKills'] = totalKills[1]
blueObj['picks'] = bluePicks
blueObj['pickPics'] = bluePickPics
blueObj['bans'] = blueBans
blueObj['kills'] = blueKills
blueObj['deaths'] = blueDeaths
blueObj['assists'] = blueAssists
blueObj['creepScore'] = blueCreepScore
game['blueTeam'] = blueObj

# convert to json object
list_to_json = json.dumps(game)

# use 'a' for 'append'
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(game, f, ensure_ascii=False, indent=4)