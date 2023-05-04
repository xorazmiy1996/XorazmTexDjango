from .provider import get_client


def get_currencies():
    client = get_client()
    return client.latest()
