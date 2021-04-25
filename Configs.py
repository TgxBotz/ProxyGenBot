import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    LOGS_CHAT = int(os.environ.get("LOGS_CHAT", False))

