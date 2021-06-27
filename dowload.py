
import os
import requests

user_agent = {'User-agent': 'Mozilla/5.0'}

BASE_URL = "https://cdn.islamic.network/quran/audio";
def download(bitrate, edition, start=1, end=6236):
    try:
        os.mkdir(f'{bitrate}')
        os.mkdir(f'{bitrate}/{edition}')
    except:
        pass
    for ayah in range(start, end):
        res = requests.get(f'https://cdn.islamic.network/quran/audio/{bitrate}/{edition}/{ayah}.mp3', headers = user_agent)
        open(f'{bitrate}/{edition}/{ayah}.mp3', 'wb').write(res.content)

# TODO: change الشيخ here:
download(64, 'ar.husary', 1, 8)
