from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 17894641))
API_HASH = getenv("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
BOT_TOKEN = getenv("BOT_TOKEN", "5717806604:AAFE6aBBpUt3hyTHk_72yqKh7aiWm_eNpJE")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AutoAnime:AutoAnime@autoanime.f8ahzhs.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("INDEX_ID", "-1001655574268"))
UPLOADS_ID = int(getenv("UPLOADS_ID", "-1001730395459"))

STATUS_ID = int(getenv("STATUS_ID", 28))
SCHEDULE_ID = int(getenv("SCHEDULE_ID", 29))

CHANNEL_TITLE = getenv("CHANNEL_TITLE", "AnimeAuto")
INDEX_USERNAME = getenv("INDEX_USERNAME", "AutoAnimeIndexChannel")
UPLOADS_USERNAME = getenv("UPLOADS_USERNAME", "AutoAnimeUploadChannel")
