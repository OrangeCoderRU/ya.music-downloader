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
    
# Если делать GUI, то для ProgressBar требуется знать конечное количество треков
# Тогда можно в отдельном цикле добавить их в список не скачивая и получить количество треков - длина списка
# Далее len(list) будет крайним значением для ProgressBar
# Но для этого надо сначала прогнать цикл подсчета в GUI с растущим числом и потом активировать кнопку "скачать"
# Также можно сделать динамическое отображение найденных треков в специальном окне формы
