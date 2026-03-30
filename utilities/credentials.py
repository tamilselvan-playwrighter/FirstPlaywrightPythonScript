import configparser
import base64
import os

def get_decoded_credentials():
    CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testData', 'config.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    if not config.has_section('basic info'):
        raise Exception(f"Section 'basic info' not found in config file: {CONFIG_PATH}")
    try:
        username_enc = config.get('basic info', 'username')
        password_enc = config.get('basic info', 'password')
    except configparser.NoOptionError as e:
        raise Exception(f"Missing option in config file: {e}")
    username = base64.b64decode(username_enc.split('#')[0].strip()).decode('utf-8')
    password = base64.b64decode(password_enc.split('#')[0].strip()).decode('utf-8')
    return username, password

