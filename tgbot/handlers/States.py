from aiogram.fsm.state import StatesGroup, State


class IpAddrInfoState(StatesGroup):
    get_ip_address = State()
    get_dns_name = State()
