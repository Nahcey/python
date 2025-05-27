#KR서버 챌린저랭크게임 match_id 수집

import requests
import time
import csv
import TFT_privatedata as Tpd

ARCHIVE = set()

# csv 파일 집합으로 변경
with open("C://Users//yecha_m0fc24a//OneDrive//바탕 화면//python//컴사//archive.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0].strip():
            ARCHIVE.add(row[0].strip())
ARCHIVE.discard(0)

# 1. 챌린저 summonerId 추출
def get_challenger_entries():
    url = "https://kr.api.riotgames.com/tft/league/v1/challenger"
    res = requests.get(url, headers=Tpd.get_HEADERS())
    return res.json()["entries"][:10] #20명

# 2. summonerId로 puuid 가져오기
def get_puuid(summoner_id):
    url = f"https://kr.api.riotgames.com/tft/summoner/v1/summoners/{summoner_id}"
    res = requests.get(url, headers=Tpd.get_HEADERS())
    return res.json()["puuid"]

# 3. puuid로 최근 3경기 match id 가져오기
def get_match_ids(puuid, count=5):
    url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count={count}"
    res = requests.get(url, headers=Tpd.get_HEADERS())
    return res.json()


# 4. match id로 경기 상세 데이터 가져오기
def get_match_data(match_id):
    url = f"https://asia.api.riotgames.com/tft/match/v1/matches/{match_id}"
    res = requests.get(url, headers=Tpd.get_HEADERS())
    return res.json()

# 5. 랭크게임 데이터 선별 및 저장
def add_match_data(match_data):
  if match_data['info']['queue_id'] != 1100:
    pass
  else:
      ARCHIVE.add(match_data['metadata']['match_id'])
      print(match_data['metadata']['match_id'])



# 메인
challenger_entries = get_challenger_entries()
for idx, entry in enumerate(challenger_entries):
    summoner_id = entry['summonerId']
    print(f"\n{idx+1}")
    puuid = get_puuid(summoner_id)
    time.sleep(1.3)
    match_ids = get_match_ids(puuid, count=5) #경기 수
    for match_id in match_ids:
        match_data = get_match_data(match_id)
        add_match_data(match_data)
        time.sleep(1.3)  # API rate limit 준수

# set을 다시 csv로 저장
with open("C://Users//yecha_m0fc24a//OneDrive//바탕 화면//python//컴사//archive.csv", "w", newline="") as f:
    writer = csv.writer(f)   
    for value in ARCHIVE:
        writer.writerow([value])

print(len(ARCHIVE))