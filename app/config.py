import logging

logging_format = "[%(asctime)s] %(levelname)s in %(name)s %(threadName)s: %(message)s"
logging.basicConfig(filename='filename.log', level=logging.INFO, format=logging_format)


class Config:
    MAX_CONTENT_LENGTH = 1024 * 1024
    UPLOAD_EXTENSIONS = [".csv"]


class DevelopmentConfig(Config):
    SECRET_KEY = ""
