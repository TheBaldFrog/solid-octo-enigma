from aiogram import Dispatcher
from .admins import AdminFilter
from .group_chat import IsGroup

# from .is_admin import AdminFilter


def setup(dp: Dispatcher):
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
