from aiogram.types import Message
from aiogram import Router

router = Router()

@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')