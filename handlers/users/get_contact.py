from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from keyboards.default import contact_buttons
from loader import dp


@dp.message_handler(Command("callback"))
async def share_number(message: types.Message):
    await message.answer(
        f"Ciao, {message.from_user.full_name}.\n"
        "Premi il tasto sotto",
        reply_markup=contact_buttons.keyboard
    )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(
        f"Grazie, {contact.full_name}\n"
        f"Il tuo numero {contact.phone_number} è stato inoltrato al nostro manager",
        reply_markup=ReplyKeyboardRemove()
    )
