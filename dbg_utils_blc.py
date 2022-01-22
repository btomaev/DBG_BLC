#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests, time, datetime, asyncio, re, json, random
import pandas as pd
from data import *

table = {}
pl_names = []
pl_types = []
pl_teams = []
pl_leggits = []
pl_mints = []
pl_seasons = []
pl_tiers = []
pl_users = []
pl_score = []
index = []
last_user = ''
grade = 0
counter = 0
driver = None
ready = True
request_driver = None
old_raw_messages = None
timing = datetime.datetime.now()
file_name = ""
names = []
wait = 0

def begin():
    global table, pl_names, pl_types, pl_teams, pl_leggits, pl_mints, pl_seasons, pl_tiers, pl_users, pl_score, last_user, index, counter, grade, ready
    table = {}
    pl_names = []
    pl_types = []
    pl_teams = []
    pl_leggits = []
    pl_mints = []
    pl_seasons = []
    pl_tiers = []
    pl_users = []
    pl_score = []
    emty = []
    info = []
    index = []
    last_user = ''
    counter = 0
    grade = 0
    ready = True

def setup(f_name, waitfor, name_list):
    
    print("\n=====================\nБот запущен, все ОК!\n=====================\n")

def update(file_name, names):
    global table, pl_names, pl_types, pl_teams, pl_leggits, pl_mints, pl_seasons, pl_users, pl_score, last_user, index, counter
    for name in names:
        print(name)
        for head in headers:
            if(name.lower() in head.lower()):
                header = head
        pl_names.append("redify"+header) 
        index.append('redify#')
        pl_teams.append('redify')
        pl_leggits.append('redify')
        pl_mints.append('redify')
        pl_seasons.append('redify')
        pl_score.append('redify')
        pl_users.append('redify')
        counter = 1
        for legit in request(name):
            for pl in players:
                if(pl.upper() in legit["metadata"]["displayName"]):
                    player = pl
            for lgg in leggits:
                if(lgg.upper() in legit["metadata"]["displayName"]):
                    leggit = lgg
            for ss in seasons:
                if(ss in legit["metadata"]["displayName"]):
                    season = ss
            pl_names.append(player)
            pl_teams.append(legit["metadata"]["teamName"])
            pl_leggits.append(leggit)
            pl_mints.append(legit["mint"])
            pl_seasons.append(season)
            if("fanPoints" in legit["metadata"]):
                pl_score.append(legit["metadata"]["fanPoints"])
            else:
                pl_score.append(0)
            pl_users.append(name)
            index.append(str(counter))
            counter += 1
        table.update({
            'Player name':pl_names,
            'Team':pl_teams,
            'Mint':pl_mints,
            'Legit':pl_leggits,
            'Fan Score':pl_score,
            'Season':pl_seasons
            })
    df = pd.DataFrame(table, index=index)
    # df.style.applymap(highlight)
    # df.to_excel('./'+file_name+'.xlsx', sheet_name='Legits', index=True)
    df.to_html('./'+file_name+'.html', index=True)
    html = open('./'+file_name+'.html', "r").read()
    open('./'+file_name+'.html', "w").write(unistyle+"\n"+html.replace("<td>redify","<td class='redify'>").replace("<th>redify","<td class='redify'>"))
    files = {'file': open('./'+file_name+'.html','rb')}
    print(requests.post("http://uplandia.pythonanywhere.com/lgtupdate", files=files).text)

def request(name):
    url = f'https://nft.upland.me/assets/legits/{name.lower()}'
    req = requests.get(url)
    result = json.loads(req.content)
    return result