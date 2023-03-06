# %%

import requests

cookies = {
    'mediakindauth2token': 'AuthToken1fZJdb9sgFIZ_TXwzxcJ8GS584TVdWlXVui3dR28mDCcJq208wG2cXz-SNps6dRPoHPSc9xV6EfVoLPQaqm2MQ5iReobfpe2hnWy_GZSPUz54Z1TeNyqPD0S3bjS5dl1SZZchjOD_8oYY_mM5aP9I9RY6FfJd1wanhtz5TaKPIRWMEEvtWKyBPto4paNule0O8151UG1GCPG7gbUa25it3D30q2mAanng2QIerIYjuHRhpZoWkgh61cdLU51cddu6RzAnHn4PbgP4pHt5R621G4_-l3zx1F_1vBq5s9q74Nbx-WFOocUhNP9HaO_a59BvxnRTVo9x67zdq2hdf63CfVVIIXFalHEiC8oZFxwXDAspMRMlFoRwRFEhMOWIFEISiQSXJS8EYxKVrMSclFIIxFBBCEO4IBhjmp3vBushvO-rgpdSUi5KlJ15UBHME0xOQRO8gmk5WlPpBqRQ5XqOccnntEF8rjBdzxkIZYQutUAku7iuzz5d1Jjxylwt7ya2az6fz3DDN19vh7sf6TTcTFuTvsX6S_fWL8qbDz8joXu6__htRswv',
    'ug': '63f915f70ab2c20a3f922c00141d7359',
    'bea4r': '63f915fafdd6600a3f922c00141d7359',
    'zwmc': '4718840299055156489',
    'bea4': 'w9fa9_7172314394675248509',
    'hkgc': 'd4f7ab27-71c7-11ed-8ca5-17892db60507',
    'goiz': 'c4f87388065440d693d1890fcfbd22d2',
    'OptanonAlertBoxClosed': '2023-02-24T19:56:28.066Z',
    'OptanonControl': 'ccc=AU&csc=&cic=1&otvers=202211.1.0&pctm=2023-02-24T19%3A56%3A28.066Z&reg=gdpr&ustcs=1---&vers=3.1.14-nba',
    '__gads': 'ID=3ffa7291cb21461a:T=1677268589:S=ALNI_MbmvfkgvpfSKT7djiZqnuPDH9HBCg',
    '_parsely_visitor': '{%22id%22:%22pid=7637c2eea7510b0016c5816580736176%22%2C%22session_count%22:1%2C%22last_session_ts%22:1677268593368}',
    's_ecid': 'MCMID%7C55500217196568045183145654357668162916',
    '_gcl_au': '1.1.95676896.1677268596',
    'ab.storage.deviceId.cf150dab-3153-49b0-b48c-66a7c18688ea': '%7B%22g%22%3A%22192dbd51-44b9-2745-417c-0839aabc515e%22%2C%22c%22%3A1677268597334%2C%22l%22%3A1677268597334%7D',
    'aam_uuid': '55514568934523736573145909476079407963',
    '_cs_c': '0',
    'bm_sz': 'DDFF5F81C1FAF398E4EDB821DBFC6244~YAAQXq5NaBIwOLGGAQAAeHRHtBMAVPr92aM+7zLEFUhZlP6LMSHXouojYJVJLTXoTxP85QxVGSjEHeahYyCRCVpSyUvJl3VfcnzGHGldvlCmnBUaW2SEQo8WsvUVJLoTxBJTnwcLxdcWapm4IVypIQ7bh8XkeGvBG3Utajfr3zeCQfeYjaM8B4K05a/hkZynco5Vm3FIXLnKoHmp3W439w5lhDW69jSTqfR12m+U6NHCi++BCbvm80Gv50PYstC5RTiSex98lNHHuz/bMjeCuqRRkEntVE4pd6CLvbfNLdM=~4473399~3490866',
    '_abck': 'DE787588C74E83691768E134ABBE8256~0~YAAQXq5NaOYwOLGGAQAAA5BHtAl2TJGnq5uwYKtcGfIkBYjo/ze7n5v+7uFVH5T0Fw1ZeU230OC4q5rIyhh5ehLLK3Nki4xAtKQSd0+4rCUgUDX5+/ySgCTZji5vijS/BO9KDWJDYEMS+5udRgL3M3+kdmrslz0XlmK5XAmX5g5+XqOyylbNGbq4inFWtGxlyR8SyuwQEdtxL8fKeVKc5In14Q5l3mGIeyZH9qHXw8QBeMNz73DU+i6xzP/ReZG5zSs2Pih8qktYjFCNTfE3Y4TVeBlkBsLGnnoKml180nZae3hXkcrJt9xM4ya8tRzZLChuAThH/1qPETQFK6Fm7TLdmRReWBZkjjBLlrsS5JxU4+4mhyVhVXtm7UGFlCkD4LMSyxwldP8f4/eJ3O4ETZ7MRZm9~-1~-1~1678065342',
    'usprivacy': '1---',
    '_cs_mk_aa': '0.3011297943453115_1678061834693',
    'at_check': 'true',
    'eupubconsent-v2': 'CPnqeEgPnqeEgAcABBENC6CsAP_AAAAAACiQJIQLYAFAAaABWADAAMgAgABIACoAFoAMgAaAA6AB7AEQARQAkwBMAE8ALIAWwAvgBhAEAAIQAUUApAClAGkAOcAgoBCACLAEdAJ2AfoBGoCjwF5gMWAYzA2QDZ4G1AboA4gB1cEWQRogjUCOsEdwR8gj8CQUEhASHgkSCSAAAAEQkAwABYAFQAMgAgABkADQAIgATAAngCEAFKAvMIAGABaAEkALYA5wFHgMWDABwAFgBJACeAFsAUgA0gGLBoAIBBRAAYABYASQAngBbAFIAxYVACACYAvMUACAFIAQUZACACYAvMYABAFIOgGAALAAqABkAEAAMgAaABEACYAE8AUoBFgF5jgBIALQAtgBfAEIAKQAc4BBQCEAMWIQAwAFgAZACYQACABfAFIAOcAgpKAMAAsADIARAAmAClAXmSACABfAEIAKQBixSAYAAsACoAGQAQAAyABoAEQAJgATwBSgEWAXmUADAAtAC-AIQAUgA5wGLAAA.f_gAAAAAAAAA',
    'ak_bmsc': 'D2578119AE3D2558AC54D032EB06AE43~000000000000000000000000000000~YAAQXq5NaPMwOLGGAQAA0JJHtBOzaOU/imAS1gCtsiIoL965v8Vzv8zWsAemQwvRtpl32jhADTZ7WBUXlQDBJVAT86YKFjNUcaCfsii39ivaHcXMyFNNgmbQqFUyO2dcekydAZBhoXxrfPl/Rf+Ekk9jD3QOuz8ZlZTiKiqx/clIJyVTJlfgD4IxT9+XgL/DtSBsGYRKot1vy+9vtiG6ZE8AVazZOjVlx8lG1d5cVxs9wQT5Z7ZpjTtlneb1XplhSuF2sAJfezzcCZ0t4tF79iGFIY6cYHG60iaSc/QoY2FmyELQPK7SgKMQUF/52cB2x7973VB5DGMoyrSL2twXWIbUON5GrUex7JtILnAmMRJht2Oi2S5IbzetFKEwli6Wz6yPnf3M+t6+Y+WQg5++TDJBfBNzx6ikxrgd+IhtGIphzdRgmD6voJujCV9OPSlGFpZuzgwQRRVHeo6mtyMw4wFYVUGdwQ60NJ9ykdJTEaB0XHTXZMpAXWkMG6oNNyW2EKUYI6uX5aXqskJ9zwXXE/c=',
    'AMCVS_248F210755B762187F000101%40AdobeOrg': '1',
    'AMCV_248F210755B762187F000101%40AdobeOrg': '179643557%7CMCIDTS%7C19423%7CMCMID%7C55500217196568045183145654357668162916%7CMCAAMLH-1678666635%7C8%7CMCAAMB-1678666635%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678069035s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'locationData': '{%22country%22:%22AUS%22%2C%22state%22:%22VIC%22%2C%22city%22:%22Melbourne%22%2C%22postalCode%22:%223004%22%2C%22countryCode%22:%22AU%22%2C%22regionCode%22:%22VIC%22%2C%22timeZone%22:%22Australia/Melbourne%22%2C%22latitude%22:-37.84%2C%22longitude%22:144.97%2C%22isProxy%22:%22No%22}',
    'client_type': 'html5',
    'client_version': '4.6.0',
    's_gpv_pageModal': 'nba%3Astats',
    's_cc': 'true',
    'aaCustPrevPage': 'nba:stats',
    'amCustPrevPage': 'Page View: Stats',
    'ugs': '1',
    '__gpi': 'UID=00000bcb8dc16b65:T=1677268589:RT=1678061838:S=ALNI_Mbq5y2CA0fYpcn5yEShxdlAlEej3g',
    'umto': '1',
    'cto_bundle': 'zKHFfV9MRjVMTnpEbkJFamZCSk96SlRxd1JPUHJZSXEwZjA2dSUyRkdYcmJ6YzFaYmd1MUVPUDJzWDhDN2lCQVpmVkx2c1RZZ3d4JTJCOXhYNDJ2bzlIJTJCTzBqQ0tJM3p1NVZIaklyaTFPU1NQSmklMkZKVWFDdHF5dnVka2NmODJpYnZXOVZwSlI1VTM5bSUyRjUlMkZJYzRib3dTaXY2b1VPVDdZJTJCaDdrTUFnVUFLclVpUGFlRjBzNXkzUmNBem5VdjZrRjBySSUyQkl5VE16',
    'iframeRef': 'www.nba.com/stats/teams/boxscores',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Mar+06+2023+11%3A18%3A19+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=e392550f-2a29-4007-b14f-7046eeba89c3&interactionCount=2&landingPath=NotLandingPage&groups=dsa%3A1%2Ccad%3A1%2CNBAad%3A1%2Cmcp%3A1%2CNBAmt%3A1%2Cpad%3A1%2Cpap%3A1%2Cgld%3A1%2Cpcd%3A1%2Cpcp%3A1%2Cmra%3A1%2Cpdd%3A1%2Cmap%3A1%2Csid%3A1%2Csec%3A1%2Ctdc%3A1%2Ccos%3A1%2Cdlk%3A1%2Cdid%3A1%2Cven%3A1%2Creq%3A1&AwaitingReconsent=false&geolocation=AU%3B',
    'mbox': 'PC#41bb295243d5435697da496e20d791d5.36_0#1741306700|session#f6817e5c07c742a4a508b9f54843a95d#1678063760',
    'ab.storage.sessionId.cf150dab-3153-49b0-b48c-66a7c18688ea': '%7B%22g%22%3A%2230257782-2baf-5b4e-1b57-6a017309ca87%22%2C%22e%22%3A1678063700250%2C%22c%22%3A1678061836084%2C%22l%22%3A1678061900250%7D',
    's_tp': '2933',
    'amp_2442d5': 'cpiJCL9HWEfzQQzaLg6gj7...1gqq4f4qs.1gqq4h4mg.5.4.9',
    '_cs_id': 'a1e9f1bd-36c3-a985-9d05-7ff5fe2e6cce.1677268598.3.1678061900.1678061837.1.1711432598560',
    '_cs_s': '2.0.0.1678063700996',
    's_ips': '930',
    's_ppv': 'nba%253Astats%2C38%2C32%2C1101%2C1%2C3',
    's_sq': 'nbasitesprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnba%25253Astats%2526link%253DPOR%252520%252540%252520ORL%2526region%253D__next%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnba%25253Astats%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.nba.com%25252Fgame%25252F0022200966%2526ot%253DA',
}

headers = {
    'authority': 'www.nba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': 'mediakindauth2token=AuthToken1fZJdb9sgFIZ_TXwzxcJ8GS584TVdWlXVui3dR28mDCcJq208wG2cXz-SNps6dRPoHPSc9xV6EfVoLPQaqm2MQ5iReobfpe2hnWy_GZSPUz54Z1TeNyqPD0S3bjS5dl1SZZchjOD_8oYY_mM5aP9I9RY6FfJd1wanhtz5TaKPIRWMEEvtWKyBPto4paNule0O8151UG1GCPG7gbUa25it3D30q2mAanng2QIerIYjuHRhpZoWkgh61cdLU51cddu6RzAnHn4PbgP4pHt5R621G4_-l3zx1F_1vBq5s9q74Nbx-WFOocUhNP9HaO_a59BvxnRTVo9x67zdq2hdf63CfVVIIXFalHEiC8oZFxwXDAspMRMlFoRwRFEhMOWIFEISiQSXJS8EYxKVrMSclFIIxFBBCEO4IBhjmp3vBushvO-rgpdSUi5KlJ15UBHME0xOQRO8gmk5WlPpBqRQ5XqOccnntEF8rjBdzxkIZYQutUAku7iuzz5d1Jjxylwt7ya2az6fz3DDN19vh7sf6TTcTFuTvsX6S_fWL8qbDz8joXu6__htRswv; ug=63f915f70ab2c20a3f922c00141d7359; bea4r=63f915fafdd6600a3f922c00141d7359; zwmc=4718840299055156489; bea4=w9fa9_7172314394675248509; hkgc=d4f7ab27-71c7-11ed-8ca5-17892db60507; goiz=c4f87388065440d693d1890fcfbd22d2; OptanonAlertBoxClosed=2023-02-24T19:56:28.066Z; OptanonControl=ccc=AU&csc=&cic=1&otvers=202211.1.0&pctm=2023-02-24T19%3A56%3A28.066Z&reg=gdpr&ustcs=1---&vers=3.1.14-nba; __gads=ID=3ffa7291cb21461a:T=1677268589:S=ALNI_MbmvfkgvpfSKT7djiZqnuPDH9HBCg; _parsely_visitor={%22id%22:%22pid=7637c2eea7510b0016c5816580736176%22%2C%22session_count%22:1%2C%22last_session_ts%22:1677268593368}; s_ecid=MCMID%7C55500217196568045183145654357668162916; _gcl_au=1.1.95676896.1677268596; ab.storage.deviceId.cf150dab-3153-49b0-b48c-66a7c18688ea=%7B%22g%22%3A%22192dbd51-44b9-2745-417c-0839aabc515e%22%2C%22c%22%3A1677268597334%2C%22l%22%3A1677268597334%7D; aam_uuid=55514568934523736573145909476079407963; _cs_c=0; bm_sz=DDFF5F81C1FAF398E4EDB821DBFC6244~YAAQXq5NaBIwOLGGAQAAeHRHtBMAVPr92aM+7zLEFUhZlP6LMSHXouojYJVJLTXoTxP85QxVGSjEHeahYyCRCVpSyUvJl3VfcnzGHGldvlCmnBUaW2SEQo8WsvUVJLoTxBJTnwcLxdcWapm4IVypIQ7bh8XkeGvBG3Utajfr3zeCQfeYjaM8B4K05a/hkZynco5Vm3FIXLnKoHmp3W439w5lhDW69jSTqfR12m+U6NHCi++BCbvm80Gv50PYstC5RTiSex98lNHHuz/bMjeCuqRRkEntVE4pd6CLvbfNLdM=~4473399~3490866; _abck=DE787588C74E83691768E134ABBE8256~0~YAAQXq5NaOYwOLGGAQAAA5BHtAl2TJGnq5uwYKtcGfIkBYjo/ze7n5v+7uFVH5T0Fw1ZeU230OC4q5rIyhh5ehLLK3Nki4xAtKQSd0+4rCUgUDX5+/ySgCTZji5vijS/BO9KDWJDYEMS+5udRgL3M3+kdmrslz0XlmK5XAmX5g5+XqOyylbNGbq4inFWtGxlyR8SyuwQEdtxL8fKeVKc5In14Q5l3mGIeyZH9qHXw8QBeMNz73DU+i6xzP/ReZG5zSs2Pih8qktYjFCNTfE3Y4TVeBlkBsLGnnoKml180nZae3hXkcrJt9xM4ya8tRzZLChuAThH/1qPETQFK6Fm7TLdmRReWBZkjjBLlrsS5JxU4+4mhyVhVXtm7UGFlCkD4LMSyxwldP8f4/eJ3O4ETZ7MRZm9~-1~-1~1678065342; usprivacy=1---; _cs_mk_aa=0.3011297943453115_1678061834693; at_check=true; eupubconsent-v2=CPnqeEgPnqeEgAcABBENC6CsAP_AAAAAACiQJIQLYAFAAaABWADAAMgAgABIACoAFoAMgAaAA6AB7AEQARQAkwBMAE8ALIAWwAvgBhAEAAIQAUUApAClAGkAOcAgoBCACLAEdAJ2AfoBGoCjwF5gMWAYzA2QDZ4G1AboA4gB1cEWQRogjUCOsEdwR8gj8CQUEhASHgkSCSAAAAEQkAwABYAFQAMgAgABkADQAIgATAAngCEAFKAvMIAGABaAEkALYA5wFHgMWDABwAFgBJACeAFsAUgA0gGLBoAIBBRAAYABYASQAngBbAFIAxYVACACYAvMUACAFIAQUZACACYAvMYABAFIOgGAALAAqABkAEAAMgAaABEACYAE8AUoBFgF5jgBIALQAtgBfAEIAKQAc4BBQCEAMWIQAwAFgAZACYQACABfAFIAOcAgpKAMAAsADIARAAmAClAXmSACABfAEIAKQBixSAYAAsACoAGQAQAAyABoAEQAJgATwBSgEWAXmUADAAtAC-AIQAUgA5wGLAAA.f_gAAAAAAAAA; ak_bmsc=D2578119AE3D2558AC54D032EB06AE43~000000000000000000000000000000~YAAQXq5NaPMwOLGGAQAA0JJHtBOzaOU/imAS1gCtsiIoL965v8Vzv8zWsAemQwvRtpl32jhADTZ7WBUXlQDBJVAT86YKFjNUcaCfsii39ivaHcXMyFNNgmbQqFUyO2dcekydAZBhoXxrfPl/Rf+Ekk9jD3QOuz8ZlZTiKiqx/clIJyVTJlfgD4IxT9+XgL/DtSBsGYRKot1vy+9vtiG6ZE8AVazZOjVlx8lG1d5cVxs9wQT5Z7ZpjTtlneb1XplhSuF2sAJfezzcCZ0t4tF79iGFIY6cYHG60iaSc/QoY2FmyELQPK7SgKMQUF/52cB2x7973VB5DGMoyrSL2twXWIbUON5GrUex7JtILnAmMRJht2Oi2S5IbzetFKEwli6Wz6yPnf3M+t6+Y+WQg5++TDJBfBNzx6ikxrgd+IhtGIphzdRgmD6voJujCV9OPSlGFpZuzgwQRRVHeo6mtyMw4wFYVUGdwQ60NJ9ykdJTEaB0XHTXZMpAXWkMG6oNNyW2EKUYI6uX5aXqskJ9zwXXE/c=; AMCVS_248F210755B762187F000101%40AdobeOrg=1; AMCV_248F210755B762187F000101%40AdobeOrg=179643557%7CMCIDTS%7C19423%7CMCMID%7C55500217196568045183145654357668162916%7CMCAAMLH-1678666635%7C8%7CMCAAMB-1678666635%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678069035s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; locationData={%22country%22:%22AUS%22%2C%22state%22:%22VIC%22%2C%22city%22:%22Melbourne%22%2C%22postalCode%22:%223004%22%2C%22countryCode%22:%22AU%22%2C%22regionCode%22:%22VIC%22%2C%22timeZone%22:%22Australia/Melbourne%22%2C%22latitude%22:-37.84%2C%22longitude%22:144.97%2C%22isProxy%22:%22No%22}; client_type=html5; client_version=4.6.0; s_gpv_pageModal=nba%3Astats; s_cc=true; aaCustPrevPage=nba:stats; amCustPrevPage=Page View: Stats; ugs=1; __gpi=UID=00000bcb8dc16b65:T=1677268589:RT=1678061838:S=ALNI_Mbq5y2CA0fYpcn5yEShxdlAlEej3g; umto=1; cto_bundle=zKHFfV9MRjVMTnpEbkJFamZCSk96SlRxd1JPUHJZSXEwZjA2dSUyRkdYcmJ6YzFaYmd1MUVPUDJzWDhDN2lCQVpmVkx2c1RZZ3d4JTJCOXhYNDJ2bzlIJTJCTzBqQ0tJM3p1NVZIaklyaTFPU1NQSmklMkZKVWFDdHF5dnVka2NmODJpYnZXOVZwSlI1VTM5bSUyRjUlMkZJYzRib3dTaXY2b1VPVDdZJTJCaDdrTUFnVUFLclVpUGFlRjBzNXkzUmNBem5VdjZrRjBySSUyQkl5VE16; iframeRef=www.nba.com/stats/teams/boxscores; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+06+2023+11%3A18%3A19+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=e392550f-2a29-4007-b14f-7046eeba89c3&interactionCount=2&landingPath=NotLandingPage&groups=dsa%3A1%2Ccad%3A1%2CNBAad%3A1%2Cmcp%3A1%2CNBAmt%3A1%2Cpad%3A1%2Cpap%3A1%2Cgld%3A1%2Cpcd%3A1%2Cpcp%3A1%2Cmra%3A1%2Cpdd%3A1%2Cmap%3A1%2Csid%3A1%2Csec%3A1%2Ctdc%3A1%2Ccos%3A1%2Cdlk%3A1%2Cdid%3A1%2Cven%3A1%2Creq%3A1&AwaitingReconsent=false&geolocation=AU%3B; mbox=PC#41bb295243d5435697da496e20d791d5.36_0#1741306700|session#f6817e5c07c742a4a508b9f54843a95d#1678063760; ab.storage.sessionId.cf150dab-3153-49b0-b48c-66a7c18688ea=%7B%22g%22%3A%2230257782-2baf-5b4e-1b57-6a017309ca87%22%2C%22e%22%3A1678063700250%2C%22c%22%3A1678061836084%2C%22l%22%3A1678061900250%7D; s_tp=2933; amp_2442d5=cpiJCL9HWEfzQQzaLg6gj7...1gqq4f4qs.1gqq4h4mg.5.4.9; _cs_id=a1e9f1bd-36c3-a985-9d05-7ff5fe2e6cce.1677268598.3.1678061900.1678061837.1.1711432598560; _cs_s=2.0.0.1678063700996; s_ips=930; s_ppv=nba%253Astats%2C38%2C32%2C1101%2C1%2C3; s_sq=nbasitesprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnba%25253Astats%2526link%253DPOR%252520%252540%252520ORL%2526region%253D__next%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnba%25253Astats%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.nba.com%25252Fgame%25252F0022200966%2526ot%253DA',
    'referer': 'https://www.nba.com/stats/teams/boxscores',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response = requests.get('https://www.nba.com/game/0022200966', cookies=cookies, headers=headers)



# %%

print(response.status_code)
print(response.text)





# %%
box = '0022200966'
box = '0022200948'

urlo = 'https://www.nba.com/game/0022200935'
box = urlo.split('/')[-1]

r = requests.get(f'https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{box}.json')

# %%

print(r.text)
# %%

import json

jsony = json.loads(r.text)

actions = jsony['game']['actions']

print(actions[2])
# %%

import pandas as pd 

df = pd.DataFrame.from_records(jsony['game']['actions'])

print(df)

# %%
