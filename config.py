import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6175306650:AAEdiR3_bJkSKVv0ZqKmxnBgNu-NmYyiXUU")

    API_ID = int(os.environ.get("API_ID", "5397731"))

    API_HASH = os.environ.get("API_HASH", "051ebba43e161aa6f6456af524bad699")
    
    API_KEY = os.environ.get("API_KEY", "4644exhpide5yevfy4n8")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))

    
