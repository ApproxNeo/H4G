from shared.bots import bot
from attachments import *

bot.posts.create_post(
    options={
        "channel_id": "kcgm3epndfn7ufaem1mtt7ow3r",
        "message": "Solution S001",
        "props": solution1(),
    }
)

bot.posts.create_post(
    options={
        "channel_id": "kcgm3epndfn7ufaem1mtt7ow3r",
        "message": "Solution S002",
        "props": solution2(),
    }
)

bot.posts.create_post(
    options={
        "channel_id": "kcgm3epndfn7ufaem1mtt7ow3r",
        "message": "Solution S003",
        "props": solution3(),
    }
)
