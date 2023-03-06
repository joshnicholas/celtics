# %%
# from sudulunu.helpers import pp, make_num, dumper, rand_delay
import pandas as pd 
import os 
import requests
from bs4 import BeautifulSoup as bs

# %%
starto = 'https://www.nba.com/game/bos-vs-ind-0022200887/play-by-play?period=All'


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
"Referer": 'https://www.google.com',
"DNT":'1'}

r = requests.get(starto, headers=headers)


# %%

# print(r.text)

soup = bs(r.text, 'html.parser')

#playByPlayContainer > section

finder = soup.find(class_='GamePlayByPlayRow_row__2iX_w')

print(finder)
# %%
