from pathlib import Path

from aiogram import types
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_audio(message: types.Message):
    path_to_download = Path().joinpath("items", "categories", "subcategories", "photos")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)
    await message.document.download(destination=path_to_download)
    await message.answer(f"File downloaded! : {path_to_download}")
