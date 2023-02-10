from shared.bots import bot
from attachments import *

bot.posts.create_post(
    options={
        "channel_id": "kg9h36j3wift7nhccm53nft8ih",
        "message": "Welcome to the Hephaestus Mattermost Server",
        "props": welcome_msg(),
    }
)
