import requests
import os
import json
import configparser
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
API_KEY = config["main"]["API_KEY"]

def send_file():
    url = "https://www.virustotal.com/api/v3/files"
    DIRNAME = os.getcwd()+'\\danger_files\\'
    PLIK = os.listdir(DIRNAME)[0]
    PATH = DIRNAME + PLIK
    resp = requests.post(
        url, 
        headers={
            "x-apikey": API_KEY, 
            }, 
        files={"file": PATH}
        ).json()
    data = resp["data"]
    try:
        file_id = data["id"]
    except:
        for exc in data:
            print(exc)
    get_info(file_id)


def get_info(file_id):
    url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
    resp = requests.get(
        url, 
        headers={
            "x-apikey": API_KEY, 
            }
        ).json()
    with open("info.json", 'w') as wr:
        json.dump(resp, wr)
    data = resp["data"]["attributes"]["stats"]
    for key, val in data.items():
        print(key, val)


if __name__ == "__main__":
    send_file()