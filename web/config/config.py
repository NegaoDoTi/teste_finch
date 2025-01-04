from dotenv import load_dotenv
from os import getenv

load_dotenv()

RABBIT_HOST = getenv("RABBIT_HOST")
RABBIT_USER = getenv("RABBIT_USER")
RABBIT_PASSWORD = getenv("RABBIT_PASSWORD")
RABBIT_PORT = getenv("RABBIT_PORT")
RABBIT_VHOST = getenv("RABBIT_VHOST")
RABBIT_QUEUE = getenv("RABBIT_QUEUE")
SECRET_KEY = getenv("SECRET_KEY")
