from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("set_photo", "Set photo"),
        types.BotCommand("set_tittle", "Set title"),
        types.BotCommand("set_description", "Set description"),
        types.BotCommand("ro", "Read Only"),
        types.BotCommand("unro", "Disable Read Only"),
        types.BotCommand("ban", "ban user"),
        types.BotCommand("unban", "Unban user"),
        types.BotCommand("get_cat", "get cat"),
        types.BotCommand("more_cats", "more cats"),
    ])
