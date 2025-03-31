import os

class Config(object):
    BOT_TOKEN = "7557612085:AAFs9uRaD8C0nZr4kBFM1ST30MzsWpKEZyA"
    API_ID = 26468828
    API_HASH = "4693513c08d1ac6af15f95b116c29478"
    AUTH_USER = os.environ.get('AUTH_USERS','7517045929').split(',')
    AUTH_USERS = [int(7517045929) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ChIrU"#Here You Can Change with Your Name  or any custom name or title you prefer
