from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_user
from loader import dp


@dp.inline_handler(text='')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Inserisci...",
                input_message_content=types.InputTextMessageContent(
                    message_text="none",
                )
            )
        ],
        cache_time=5
    )


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_user.append(message.from_user.id)
    await message.answer("Sei connesso",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="entra nella modality inline",
                                                          switch_inline_query_current_chat="Zapros")
                                 ]
                             ]
                         ))


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_user:
        await query.answer(
            results=[],
            switch_pm_text="Il bot non è disponibile",
            switch_pm_parameter="connect_user",
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Titolo, inline mode",
                input_message_content=types.InputTextMessageContent(
                    message_text="Qualche stringa inviato quando premi il tasto"
                ),
                url="https://www.youtube.com/watch?v=dQw4w9WgXh",
                thumb_url="https://www.youtube.com/watch?v=dQw4w9WgXh",
                description="description"
            ),
            types.InlineQueryResultVideo(
                id="2",
                video_url="https://www.youtube.com/watch?v=dQw4w9WgXh",
                caption="Firma video",
                title="Some video",
                description="description",
                thumb_url="https://www.youtube.com/watch?v=dQw4.jpg",
                mime_type="video/mp4"
            ),
            types.InlineQueryResultCachedPhoto(
                id="3",
                photo_file_id="fdssdgsd",
                description="description",
                caption="firma"
            )
        ]
    )
