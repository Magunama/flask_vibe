import logging

logging_format = "[%(asctime)s] %(levelname)s in %(name)s %(threadName)s: %(message)s"
logging.basicConfig(filename='filename.log', level=logging.INFO, format=logging_format)


class Config:
    pass


class DevelopmentConfig(Config):
    SECRET_KEY = ""
