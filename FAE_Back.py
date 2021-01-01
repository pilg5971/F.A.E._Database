import requests
import json
import itertools        # used to help iterate half the arrays
import os               # used to check if json file is empty or not
import dotenv

def getData(matchID):
  version = ''
  matchInfo = ''

  # load API key
  dotenv.load_dotenv()
  KEY = os.getenv("API_KEY")

  # make API request
  # matchID = 3639329617
  # matchID = 3722369805

  # https://matchhistory.na.leagueoflegends.com/en/#match-details/NA1/3724256705/46336961?tab=overview
  # check if user entered URL instead of matchID
  if(matchID[0] == 'h'):
    # get the match ID
    start = matchID.find('NA1') + 4
    subStr = matchID[start:]
    end = subStr.find('/')
    matchID = subStr[0:end]

  # get match history
  response = requests.get(f'https://na1.api.riotgames.com/lol/match/v4/matches/{matchID}?api_key={KEY}')
  matchInfo = response.json()

  picksArr = []
  redPicks = []
  bluePicks = []
  for x in matchInfo['participants']:
    picksArr.append(x['championId'])
  pickSize = int(len(picksArr))
  for x in itertools.islice(picksArr, 0, int(pickSize / 2)):
    redPicks.append(x)
  for x in itertools.islice(picksArr, int(pickSize / 2), pickSize):
    bluePicks.append(x)
 
  # get latest version
  response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
  version = json.loads(response.text)[0]

  #response = requests.get('https://raw.githubusercontent.com/ngryman/lol-champions/master/champions.json')
  # champion list
  response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/championFull.json')
  championIDs = json.loads(response.text)

  # picks
  pickNames = []
  redPicks = []
  bluePicks = []
  for x in picksArr:
    for key, value in championIDs['keys'].items():
      if(int(key) == x):
        pickNames.append(value)
  print('pickNames: ', pickNames)
  for x in itertools.islice(pickNames, 0, int(pickSize / 2)):
    redPicks.append(x)
  for x in itertools.islice(pickNames, int(pickSize / 2), pickSize):
    bluePicks.append(x)
  print('redPicks: ', redPicks)
  print('bluePicks: ', bluePicks)

  # win/loss
  result = []
  for x in matchInfo['teams']:
    result.append(x['win'])
  print('result: ', result)

  # total kills per team
  totalKills = []
  killCountRed = 0
  killCountBlue = 0
  participantSize = len(matchInfo['participants'])
  for x in itertools.islice(matchInfo['participants'], 0 , int(participantSize / 2)):
    killCountRed += x['stats']['kills']
  for x in itertools.islice(matchInfo['participants'], int(participantSize / 2), participantSize):
    killCountBlue += x['stats']['kills']

  totalKills.append(killCountRed)
  totalKills.append(killCountBlue)
  print('killCountRed: ', killCountRed)
  print('killCountBlue: ', killCountBlue)
  print('totalKills: ', totalKills)

  # kills, deaths, assists
  redKills = []
  blueKills = []
  redDeaths = []
  blueDeaths = []
  redAssists = []
  blueAssists = []
  for x in itertools.islice(matchInfo['participants'], 0, int(participantSize / 2)):
    redKills.append(x['stats']['kills'])
    redDeaths.append(x['stats']['deaths'])
    redAssists.append(x['stats']['assists'])
  for x in itertools.islice(matchInfo['participants'], int(participantSize / 2), participantSize):
    blueKills.append(x['stats']['kills'])
    blueDeaths.append(x['stats']['deaths'])
    blueAssists.append(x['stats']['assists'])
  print('redKills: ', redKills)
  print('blueKills: ', blueKills)
  print('redDeaths: ', redDeaths)
  print('blueDeaths: ', blueDeaths)
  print('redAssists: ', redAssists)
  print('blueAssists: ', blueAssists)

  # bans
  redBans = []
  blueBans = []
  bansArr = []
  banNames = []
  for x in matchInfo['teams']:
    for y in x['bans']:
      bansArr.append(y)

  for x in bansArr:
    for key, value in championIDs['keys'].items():
      if(int(key) == int(x['championId'])):
        banNames.append(value)
  print('banNames: ', banNames)

  banSize = len(banNames)
  for x in itertools.islice(banNames, 0, int(banSize / 2)):
    redBans.append(x)
  for x in itertools.islice(banNames, int(banSize / 2), banSize):
    blueBans.append(x)
  print('redBans', redBans)
  print('blueBans', blueBans)


  # JSON variables
  arrayObj = []
  game = {}
  redObj = {}
  blueObj = {}
  team = {}

  # write to json file
  redObj['result'] = result[0]
  redObj['totalKills'] = totalKills[0]
  redObj['picks'] = redPicks
  redObj['bans'] = redBans
  redObj['kills'] = redKills
  redObj['deaths'] = redDeaths
  redObj['assists'] = redAssists
  team['redTeam'] = redObj

  blueObj['result'] = result[1]
  blueObj['totalKills'] = totalKills[1]
  blueObj['picks'] = bluePicks
  blueObj['bans'] = blueBans
  blueObj['kills'] = blueKills
  blueObj['deaths'] = blueDeaths
  blueObj['assists'] = blueAssists
  team['blueTeam'] = blueObj



  # check if we need to create array (json is empty) or just add another element
  objectToDump = team
  # if size of json file is empty, create array and the objects
  if os.stat('data.json').st_size == 0:
          game['game 0'] = team
          arrayObj.append(game)
          objectToDump = arrayObj
  else:
          with open('data.json') as f:
                  parse_data = json.load(f)
                  game['game ' + str(len(parse_data))] = team
                  objectToDump = game
                  parse_data.append(objectToDump)
                  objectToDump = parse_data

  #use 'a' for 'append'
  with open('data.json', 'w', encoding='utf-8') as f:
      json.dump(objectToDump, f, ensure_ascii=False, indent=4)



# for _, champion in championIDs['data'].items():
#         #print(type(champion['key']))
#         if int(champion['key']) == 266:
#                 print(champion['name'])


#print(championIDs.values[0])

#print(championIDs['data'][0])

# for x in championIDs:
#         if x['data']

