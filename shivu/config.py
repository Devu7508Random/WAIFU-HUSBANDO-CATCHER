class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7347112176"
    sudo_users = "7347112176", "1813373023"
    GROUP_ID = -1002334873346
    TOKEN = "7211096764:AAH8rXDgpPJ4uF2HfDn6J5DvMcEVgFCQTFY"
    mongo_url = "mongodb+srv://MANGOOO:
MANGOOO@cluster0.oyj44.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em"
    UPDATE_CHAT = "Collect_emsup"
    BOT_USERNAME = "Collectembot"
    CHARA_CHANNEL_ID = "2395474751"
    api_id = 21185517
    api_hash = "ae48b16aa67e36f703b53ad2dd2377fa"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
