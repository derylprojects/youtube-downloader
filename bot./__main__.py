from pyrogram import Client
import config

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = config.BOT_TOKEN


plugins = dict(
    root="plugin",
)

Client(
    "Sus",
    bot_token=BOT_TOKEN,
    api_id="7761661",
    api_hash="e9f3f12a95707bce25e91d005cb6883d",
    plugins=plugins,
    workers=100
).run()
