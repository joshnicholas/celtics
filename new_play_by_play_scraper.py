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

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

chrome_options = Options()
chrome_options.add_argument("--headless")
# driver = webdriver.Firefox(options=chrome_options)

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

this_year = int(today.strftime("%Y"))
endo_year = 1945

sec_year = this_year - 1

# years = []
# while sec_year > endo_year:

#     first_year = str(this_year)[-2:]

#     years.append(f"{sec_year}-{first_year}")
#     this_year -= 1
#     sec_year -= 1

years = [f"{sec_year}-{first_year}"]

for yearo in years[:4]:
    try:
        print("Starting: ", yearo)
        driver = webdriver.Firefox(options=chrome_options)
        check_if_there('data/play_by_play_raw', yearo)

        # urlos = [
        #     f"https://www.nba.com/stats/team/1610612738/boxscores?Season={yearo}&SeasonType=Pre+Season",
        #     f'https://www.nba.com/stats/team/1610612738/boxscores?Season={yearo}&SeasonType=Regular+Season',
        #     f"https://www.nba.com/stats/team/1610612738/boxscores?Season={yearo}&SeasonType=Playoffs",
        #     f"https://www.nba.com/stats/team/1610612738/boxscores?Season={yearo}&SeasonType=PlayIn"

        # ]

        urlos = [
            f'https://www.nba.com/stats/team/1610612738/boxscores?Season={yearo}&SeasonType=Regular+Season',
        ]

        year_codes = []

        for urlo in urlos:
            driver.get(urlo)
            print(urlo)
            time.sleep(2)

            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
                button = driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
            except Exception as e:
                print("Exception")
                print(e)
            
            print("Soup")
            soup = bs(driver.page_source, 'html.parser')

            try:

                print("Waiting")
                WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_table__p1iZz")))
                time.sleep(2)

                codes = soup.find_all('a')
                codes = [x['href'].replace('/game/', '') for x in codes if '/game/' in x['href']]

                year_codes.extend(codes)
                print("Codes: ", codes)
                print("Year codes: ", year_codes)


            except (NoSuchElementException, TimeoutException) as e:

                if soup.find(class_='NoDataMessage_base__xUA61'):
                    print("No table")
                    print(e)
                    continue

            rand_delay(2)

        donners = already_done(f'data/play_by_play_raw/{yearo}')

        to_find_codes = [x for x in codes if x not in donners]

        for game in codes:
            try:
                r = requests.get(f'https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{game}.json')
                # r = requests.get(f'https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{game}.json')
                
                print(r.url)

                jsony = json.loads(r.text)

                actions = jsony['game']['actions']

                df = pd.DataFrame.from_records(jsony['game']['actions'])

                dumper(f'data/play_by_play_raw/{yearo}', game, df)
                dumper(f'output', 'latest_play_by_play', df)
                # print(df)
                # print(df.columns.tolist())
            except Exception as e:
                print(e)
        driver.quit()
        rand_delay(20)
    finally:
        print("Quitting")
        driver.quit()



http://stats.nba.com/stats/playbyplayv2/?gameId=0021801211&startPeriod=0&endPeriod=14


https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_0021801211.json