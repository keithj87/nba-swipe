"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DB_HOST = "ds125588.mlab.com"
DB_NAME = "nbaswipe"
DB_PORT = 25588
DB_USER = "swipeteam"
DB_PASS = "sw1per"

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)
DEBUG = True
#client = MongoClient('localhost', 27017)

#mongodb://swipeteam:sw1per@ds125588.mlab.com:25588/nbaswipe
