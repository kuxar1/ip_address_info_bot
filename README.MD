This is a simple message bot used to retrieve information about the IP address. For this purpose, it uses this [`api`](https://ipgeolocation.io/).
This bot is written using the popular library for writing telegram bots [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x).  
Also, this bot uses this [`template`](https://github.com/Latand/tgbot_template_v3) as a skeleton with a good structure.

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
1. Create [`venv`](https://docs.python.org/3/library/venv.html)
2. Install requirements.txt: `pip install -r requirements.txt`.
3. Run the bot with the command: `python3 bot.py`.

### Bot output example:

```python
ip: 8.8.8.8
continent_code: NA
continent_name: North America
country_code2: US
country_code3: USA
country_name: United States
country_capital: Washington, D.C.
state_prov: California
state_code: US-CA
district: 
city: Mountain View
zipcode: 94043-1351
latitude: 37.42240
longitude: -122.08421
is_eu: False
calling_code: +1
country_tld: .us
languages: en-US,es-US,haw,fr
geoname_id: 6301403
isp: Google LLC
connection_type: 
organization: Google LLC
time_zone: {'name': 'America/Los_Angeles', 'offset': -8, 'offset_with_dst': -7, 'current_time': '2023-08-21 11:04:38.359-0700', 'current_time_unix': 1692641078.359, 'is_dst': True, 'dst_savings': 1}
```