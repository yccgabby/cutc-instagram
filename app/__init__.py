from flask import Flask
from config import Config

bot = Flask(__name__)
bot.config.from_object(Config)

from app import routes