# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from elasticsearch import Elasticsearch
from flask_restful import Api
from flask.logging import create_logger
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

logger = create_logger(app)
mongo = PyMongo(app)
es = Elasticsearch([app.config['ELASTICSEARCH_HOST']])
api = Api(app)

from routes import products, customers, orders