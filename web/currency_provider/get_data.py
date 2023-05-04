from .provider import client


def get_currencies():
    return client.latest()
