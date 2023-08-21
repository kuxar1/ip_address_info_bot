"""Import all routers and add them to routers_list."""
from .get_ip_info import router

routers_list = [
    router  # echo_router must be last
]

__all__ = [
    "routers_list",
]
