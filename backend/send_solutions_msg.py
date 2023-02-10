from shared.bots import bot
from attachments import *

bot.posts.create_post(
    options={
        "channel_id": "xgdkhexombf3xgpz9rzr3rjfke",
        "message": "Submit your project proposals here!",
        "props": solution_msg(),
    }
)
