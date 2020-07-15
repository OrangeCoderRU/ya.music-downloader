from yandex_music.client import Client
import requests
from lxml.html import fromstring

client = Client.from_credentials('login', 'password')

url_1 = ("https://music.yandex.ru/album/")
url_2 = ("/track/")

for tracks in client.users_likes_tracks():
    track = tracks.track_id.split(":")
    url = url_1 + track[1] + url_2 + track[0]
    r = requests.get(url)
    tree = fromstring(r.content)
    list_track = tree.findtext('.//title').split(".")
    tracks.track.download(list_track[0] + ".mp3")
