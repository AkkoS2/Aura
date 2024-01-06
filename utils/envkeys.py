import os


def aura_key():
    return os.environ.get("AURA_KEY", None)


def app_id():
    return os.environ.get("APP_ID", None)


def server_id():
    return os.environ.get("SERVER_ID", None)
