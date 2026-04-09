import requests

def get_request(url, params=None, headers=None):
    """Simple GET request wrapper."""
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


