from gphotospy import authorize
from gphotospy.album import *
from gphotospy.media import *
from pprint import pprint
import random

CLIENT_SECRET_FILE = "gphoto_oauth.json"
service = authorize.init(CLIENT_SECRET_FILE)


album_manager = Album(service)
album_iterator = album_manager.list()
first_album = next(album_iterator)
first_album_id = first_album.get("id")
media_manager = Media(service)
album_media_list = list(media_manager.search_album(first_album_id))
random_pictures = [random.choice(album_media_list) for _ in range(3)]
print(random_pictures[0].get("productUrl"))


