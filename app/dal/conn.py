from neomodel import config
import config as gagl_config


def init_db():
    config.DATABASE_URL = gagl_config.url
