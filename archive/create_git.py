# %%

import os 
from github import Github
from dotenv import load_dotenv
load_dotenv()



tokeny = os.environ['gitty']

github = Github(tokeny)

repository = github.get_user().get_repo('Archives')
# %%

### For new foi folders

def create_repo_directories(pathos, stemmo):


    contents = repository.get_contents(pathos)

    paths = [x.path.replace(f"{pathos}/", '') for x in contents]

    print(paths)

    ## For new folders entirely
    years = os.listdir('data/play_by_play_raw')
    years = [x for x in years if x != 'ds.store']

    if stemmo not in paths:
        for yearo in years:
            repository.create_file(f'{pathos}/{stemmo}/{yearo}/hi.txt', "test", "hi")
            
        repository.create_file(f'{pathos}/{stemmo}/latest.json', "test", "[{'what':'hi'}]")

create_repo_directories('Archive', 'celtics')
# %%


years = os.listdir('data/play_by_play_raw')
years = [x for x in years if x != 'ds.store']
print(years)
# %%
