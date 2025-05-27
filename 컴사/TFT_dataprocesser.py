#matchid기반 데이터 가공

import requests
import time
import csv
import TFT_privatedata as Tpd
import TFT_basicdata as Tbd

ARCHIVE = set()
TRAITS = Tbd.get_traits()

# csv 파일 집합으로 변경
with open("C://Users//yecha_m0fc24a//OneDrive//바탕 화면//python//컴사//archive.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0].strip():
            ARCHIVE.add(row[0].strip())
ARCHIVE.discard(0)

# 4. match id로 경기 상세 데이터 가져오기
def get_match_data(match_id):
    url = f"https://asia.api.riotgames.com/tft/match/v1/matches/{match_id}"
    res = requests.get(url, headers=Tpd.get_HEADERS())
    return res.json()

def data_process(match_data):
     player = match_data['info']['participants']  
     for i in range(8):
        if player[i]["placement"] == 1:
            find_deck(player[i])
        else:
            pass    

def find_deck(player):
    max = 0 
    deck = ""
    for i in range(len(player["traits"])): 
         if player["traits"][i]["tier_current"] >= max:
             max = player["traits"][i]["tier_current"]
             deck = player["traits"][i]["name"]
    print(max,deck)
        
            

for i in ARCHIVE:
     match_data = get_match_data(i)
     data_process(match_data)
     time.sleep(1.3)

print(TRAITS)