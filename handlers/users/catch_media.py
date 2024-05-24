from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_doc(message: types.Message):
    await message.document.download()
    await message.reply("Documento scaricato\n"
                        f"<pre>File ID = {message.document.file_id} </pre>",
                        parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply("Audio scaricato\n"
                        f"<pre>File ID = {message.audio.file_id} </pre>")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.reply("Foto scaricato\n"
                        f"<pre>File ID = {message.photo[-1].file_id} </pre>",
                        parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_any(message: types.Message):
    await message.reply(f"Hai inviato ... {message.content_type}",
                        parse_mode=types.ParseMode.HTML)
