import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", "15657755"))

    API_HASH = os.environ.get("API_HASH", "7cce51d4664d010b90ad690e0d5121ad")
    
    API_KEY = os.environ.get("API_KEY", "https://pdisk.pro/api/account/info?key=6994vx27wa0sin4z1di")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))

    
