import os

class Config(object):
    BOT_TOKEN = "7483233103:AAEh_3Ah_eml3pbBOZk1YXqJlTM7ARbU5Kw"
    API_ID = 29940750
    API_HASH = "33412ad3b366ca991309d1bcbb472c32"
    AUTH_USER = os.environ.get('AUTH_USERS','7517045929').split(',')
    AUTH_USERS = [int(7618270428) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ChIrU"#Here You Can Change with Your Name  or any custom name or title you prefer
