import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(Command("set_photo", prefixes="!/"), IsGroup(), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination_file=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    await bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    # await message.chat.set_photo(photo=input_file)


@dp.message_handler(Command("set_tittle", prefixes="!/"), IsGroup(), AdminFilter())
async def set_new_title(message: types.Message):
    title = message.reply_to_message.text
    await message.chat.set_title(title)


@dp.message_handler(Command("set_description", prefixes="!/"), IsGroup(), AdminFilter())
async def set_new_description(message: types.Message):
    description = message.reply_to_message.text
    await message.chat.set_description(description)
