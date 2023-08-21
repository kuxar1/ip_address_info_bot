This is a simple message bot used to retrieve information about the IP address. For this purpose, it uses this [api](https://ipgeolocation.io/).
This bot is written using the popular library for writing telegram bots [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x).  
Also, this bot uses this [template](https://github.com/Latand/tgbot_template_v3) as a skeleton with a good structure.

### To run this bot, you need to do the following steps:
1. Rename or copy the file `.env.dist` to `.env`.
2. Fill `.env` with the necessary information as in this example:
    - BOT_CONTAINER_NAME=docker_container_name
    - BOT_IMAGE_NAME=docker_image_name
    - BOT_NAME=your_bot_name
    - BOT_TOKEN=123456789:your_bot_token_from_bot_father
    - USE_REDIS=False - this option if you want to use redis to store your states in redis instead of server memory.
    - IP_API_TOKEN=your_token_from_ipgeolocation
3. Run the `docker compose up' command.

### If you want to run this bot without docker, follow the next steps:
1. Create [venv](https://docs.python.org/3/library/venv.html)
2. Install requirements.txt: `pip install -r requirements.txt`.
3. Run the bot with the command: `python3 bot.py`.