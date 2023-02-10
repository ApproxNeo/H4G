from mattermostdriver import Driver
from dotenv import load_dotenv
import os
import requests

load_dotenv()
headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER"))}


class TokenAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # Implement authentication
        r.headers["Authorization"] = "Bearer " + os.getenv("BEARER")
        return r


bot = Driver(
    {
        "url": "hephaestus.approxneo.me",
        "port": 443,
        "auth": TokenAuth,
        "timeout": 30,
        "request_timeout": None,
        "keepalive": False,
        "keepalive_delay": 5,
        "websocket_kw_args": None,
        "debug": False,
    }
)


# user = Driver(
#     {
#         "login_id": "njkclement@gmail.com",
#         "password": "Hamster123",
#         "url": "mm.space.approxneo.me",
#         "port": 443,
#         "timeout": 30,
#         "request_timeout": None,
#         "keepalive": False,
#         "keepalive_delay": 5,
#         "websocket_kw_args": None,
#         "debug": False,
#     }
# )

# clement = Driver(
#     {
#         "login_id": "approxneo",
#         "password": "14Q382323r03",
#         "url": "mm.space.approxneo.me",
#         "port": 443,
#         "timeout": 30,
#         "request_timeout": None,
#         "keepalive": False,
#         "keepalive_delay": 5,
#         "websocket_kw_args": None,
#         "debug": False,
#     }
# )

# # bot.login()
# user.login()
# clement.login()