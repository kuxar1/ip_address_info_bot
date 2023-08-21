from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode, hbold

from tgbot.handlers.States import IpAddrInfoState
from tgbot.config import load_config
from requests import get
from tgbot.keyboards.inline import keyboard

router = Router()


@router.message(CommandStart())
async def enter_ip_address_btn(message: types.Message):
    await message.answer(
        text=
        "Hello, this bot can help you to get information about IP address. "
        f"To use this bot you need to press the \"{hbold('Enter IP address')}\" button and then enter the IP address"
        " you want to find information about.",
        reply_markup=keyboard
    )


"""
api url: https://app.ipgeolocation.io/

How to use api with request: 

ip_addr_get = get('https://ifconfig.me/all.json').json()
user_ip = ip_addr_get["ip_addr"]

ip_info = get(f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={user_ip}").json()

"""


@router.message(F.text == "Enter IP address")
async def enter_ip_address_btn(message: types.Message, state: FSMContext):
    await message.answer(
        text="Enter ip address:",
        reply_markup=keyboard
    )
    await state.set_state(IpAddrInfoState.get_ip_address)


@router.message(IpAddrInfoState.get_ip_address)
async def print_user_text(message: types.Message, state: FSMContext):
    config = load_config()
    ip_token = config.tg_bot.ip_api_token
    await state.update_data(user_text=message.text)
    user_date = await state.get_data()
    ip_addr_get = get(f"https://api.ipgeolocation.io/ipgeo?apiKey={ip_token}&ip={user_date['user_text']}")
    ip_addr_json = ip_addr_get.json()
    ip_addr_status_code = ip_addr_get.status_code
    ignore_list = ["country_flag", "currency"]
    if ip_addr_status_code != 200:
        await message.answer("You entered incorrect data, \n"
                             "Correct format should be like this:\n"
                             f"{hcode('8.8.8.8')} or {hcode('213.133.100.98')}")
    else:
        result = "\n".join(
            [f"{hbold(key)}: {hcode(value)}" for key, value in ip_addr_json.items() if key not in ignore_list])
        await message.answer(text=result, reply_markup=keyboard)
        await state.clear()
