from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    photo_file_id = "AgACAgQAAxkBAANVZjKf5gHMYFhdCx-sKyCs0orY_PkAAqeuMRtES0xTdz3BjWFtHkkBAAMCAAN3AAM0BA"
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Red_Kitten_01.jpg"
    photo_bytes = InputFile(path_or_bytesio="photos/file_1.jpg")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url, caption="Ecco la foto del gato /more_cats")


@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    album = MediaGroup()
    photo_file_id = "AgACAgQAAxkBAANVZjKf5gHMYFhdCx-sKyCs0orY_PkAAqeuMRtES0xTdz3BjWFtHkkBAAMCAAN3AAM0BA"
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Red_Kitten_01.jpg"
    photo_bytes = InputFile(path_or_bytesio="photos/file_1.jpg")
    video_file_id = "BAACAgQAAxkBAANbZjKinV5GIQ_W8KcU6ik5gHvRflcAAuAWAAKCJphRCaMIlJp4rxw0BA"
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    album.attach_video(video_file_id, caption="video dove gatto un sale sul divano")

    # await bot.send_media(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(album)
