# %%
import pandas as pd 
import json
import time

import requests
from bs4 import BeautifulSoup as bs 

import datetime 
import pytz

import os 
import pathlib

pathos = pathlib.Path(__file__).parent
os.chdir(pathos)

# %%

##
def dumper(path, name, frame):
    with open(f'{path}/{name}.csv', 'w') as f:
        frame.to_csv(f, index=False, header=True)

##
def rand_delay(num):
  import random 
  import time 
  rando = random.random() * num
#   print(rando)
  time.sleep(rando)

##
def check_if_there(pathos, to_check):
    if pathos[-1] != '/':
        pathos += '/'

    folds = os.listdir(pathos)

    if to_check not in folds:
        os.mkdir(f"{pathos}{to_check}")

##
def check_if_done(pathos, to_check):
    if pathos[-1] != '/':
        pathos += '/'

    folds = os.listdir(pathos)

    if to_check not in folds:
        return False
    else:
        return True

def already_done(pathos):
    if pathos[-1] != '/':
        pathos += '/'

    folds = os.listdir(pathos)
    fillos = [x.replace('.csv', '') for x in folds if ".csv" in x]
    return fillos

# %%

today = datetime.datetime.now()
scrape_date_stemmo = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y%m%d')
scrape_hour = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%H')

# yearo = '2020-21'
# yearo = '2021-22'
yearo = '2022-23'
check_if_there('data/play_by_play_raw', yearo)


#%%

### Do initial scrape to get numbers

files = os.listdir(f'data/play_by_play_raw/{yearo}')
files = [x for x in files if '.csv' in x]

print(len(files))

f'data/play_by_play_raw/{yearo}'

lenno = 82

if yearo == "2020-21":
    lenno = 72

if len(files) < lenno:

    print("Regular season!")
    urlo = f'https://www.nba.com/stats/team/1610612738/boxscores?SeasonType=Regular+Season&Season={yearo}'

else:
    print("Playoffs!")
    urlo = f'https://www.nba.com/stats/team/1610612738/boxscores?SeasonType=Playoffs&Season={yearo}'

# %%

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Firefox(options=chrome_options)

driver.get(urlo)

# time.sleep(5)

try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
    button = driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
except Exception as e:
    print(e)
    # continue

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div[3]/section[3]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select")))
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div[3]/section[3]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select")))
WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.CLASS_NAME, "ot-sdk-row")))

droppy = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/main/div[3]/section[3]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select"))
# droppy = Select(driver.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")[2])

droppy.select_by_visible_text("All")

WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_table__p1iZz")))
time.sleep(2)

soup = bs(driver.page_source, 'html.parser')

codes = soup.find_all('a')
codes = [x['href'].replace('/game/', '') for x in codes if '/game/' in x['href']]


driver.quit()

# # # %%

donners = already_done(f'data/play_by_play_raw/{yearo}')

codes = [x for x in codes if x not in donners]

print(len(codes))

for game in codes:
    r = requests.get(f'https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{game}.json')


    jsony = json.loads(r.text)

    actions = jsony['game']['actions']

    df = pd.DataFrame.from_records(jsony['game']['actions'])

    dumper(f'data/play_by_play_raw/{yearo}', game, df)
    dumper(f'output', 'latest_play_by_play', df)
    # print(df)
    # print(df.columns.tolist())

    rand_delay(2)


# # %%
