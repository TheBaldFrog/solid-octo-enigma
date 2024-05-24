from data.config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST
from loader import dp, bot, SSL_CERTIFICATE, ssl_context


async def on_startup(dp):
    # set webhook
    await bot.set_webhook(
        url=WEBHOOK_URL,
        certificate=SSL_CERTIFICATE
    )

    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    # executor.start_polling(dp, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=ssl_context
    )
