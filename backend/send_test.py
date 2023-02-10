
from shared.bots import bot
from attachments import *

bot.posts.create_post(
    options={
        "channel_id": "dqjb84g7yb8ypex4ge6webo1oh",
        "message": "Welcome to the Hephaestus Mattermost Server",
        "props": welcome_msg(),
    }
)


