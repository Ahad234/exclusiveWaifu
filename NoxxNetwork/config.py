import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    LOGGER = True

    OWNER_ID = os.getenv("OWNER_ID","8195241636")
    sudo_users = os.getenv("SUDO_USERS","5303251380").split(",")  # Convert CSV to list
    GROUP_ID = int(os.getenv("GROUP_ID",'-1002902949191"))
    TOKEN = os.getenv("TOKEN","7961956208:AAFp1pTmpTj--sH5CMxEVYFWEh_hYSan0iI")
    mongo_url = os.getenv("MONGO_URL","mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")
    PHOTO_URL = os.getenv("PHOTO_URL").split(",")  # Convert CSV to list
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT","https://t.me/WaifuxIvan")
    UPDATE_CHAT = os.getenv("UPDATE_CHAT","https://t.me/WaifuxDb")
    BOT_USERNAME = os.getenv("BOT_USERNAME","WaifuxGraber_bot")
    CHARA_CHANNEL_ID = int(os.getenv("CHARA_CHANNEL_ID","WaifuxDb"))
    api_id = int(os.getenv("API_ID","22657083"))
    api_hash = os.getenv("API_HASH","d6186691704bd901bdab275ceaab88f3")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
