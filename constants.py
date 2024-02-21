import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
APP_ID = os.getenv('APP_ID')
PREFIX = os.getenv('PREFIX')