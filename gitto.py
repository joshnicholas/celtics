# %%
import os
import json
from github import Github
import feedparser
from dotenv import load_dotenv
load_dotenv()

import pandas as pd 
import numpy as np 


# %%

def send_nba_to_git(stemmo, repo, what, yearsy, frame):

    tokeny = os.environ['gitty']

    github = Github(tokeny)

    repository = github.get_user().get_repo(repo)

    jsony = frame.to_dict(orient='records')
    content = json.dumps(jsony)

    filename = f'Archive/{what}/{yearsy}/{stemmo}.json'
    latest = f'Archive/{what}/latest.json'

    def check_do(pathos):
        contents = repository.get_contents(pathos)

        fillos = [x.path.replace(f"{pathos}/", '') for x in contents]

        print(pathos)
        print("contents: ", contents)
        print("fillos: ", fillos)
        return fillos


    # latest_donners = check_do(f'Archive/{what}')
    donners = check_do(f'Archive/{what}/{yearsy}')

    latters = repository.get_contents(latest)
    repository.update_file(latest, f"updated_scraped_file_{stemmo}", content, latters.sha)

    if f"{stemmo}.json" not in donners:

        repository.create_file(filename, f"new_scraped_file_{stemmo}", content)
    

# %%

fold_path = 'data/play_by_play_raw'
folds = os.listdir(fold_path)

# folds = [x for x in folds if x != 'ds.']
import datetime 
import dateparser

for folder in folds:
    fillos = os.listdir(f"{fold_path}/{folder}")

    for fillo in fillos:
        fillos = [x for x in fillos if '.csv' in x]
        inter = pd.read_csv(f"{fold_path}/{folder}/{fillo}")
        # ['actionNumber', 'clock', 'timeActual', 'period', 'periodType', 'actionType', 
        # 'subType', 'qualifiers', 'personId', 'x', 'y', 'possession', 'scoreHome', 
        # 'scoreAway', 'edited', 'orderNumber', 'side', 'description', 'personIdsFilter', 
        # 'teamId', 'teamTricode', 'descriptor', 'jumpBallRecoveredName', 'jumpBallRecoverdPersonId', 
        # 'playerName', 'playerNameI', 'jumpBallWonPlayerName', 'jumpBallWonPersonId', 'jumpBallLostPlayerName', 
        # 'jumpBallLostPersonId', 'officialId', 'foulPersonalTotal', 'foulTechnicalTotal', 
        # 'foulDrawnPlayerName', 'foulDrawnPersonId', 'shotResult', 'pointsTotal', 'shotDistance', 
        # 'shotActionNumber', 'reboundTotal', 'reboundDefensiveTotal', 'reboundOffensiveTotal', 
        # 'subsInPlayerName', 'subsInPersonId', 'assistPlayerName', 'assistPersonId', 'assistTotal', 
        # 'blockPlayerName', 'blockPersonId', 'blockTotal', 'turnoverTotal', 'stealPlayerName', 
        # 'stealPersonId', 'stealTotal', 'value']

        teams = inter['teamTricode'].unique().tolist()
        teams = [x for x in teams if isinstance(x, str)]
        teams = "_".join(teams)

        datter = dateparser.parse(inter.iloc[0]['timeActual']).strftime("%Y_%m_%d")

        print(datter)
        print(teams)

        print(inter)
        print(inter.columns.tolist())

        stammo = f"{datter}_{teams}"

        send_nba_to_git(stammo, 'Archives', 'celtics',folder, inter)


# %%
