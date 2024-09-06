from aiogram import Router, types
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards import categories_keyboard, subcategories_keyboard, advertisements_keyboard
import aiohttp
from aiogram.filters.command import Command

router = Router()

BASE_URL = 'http://127.0.0.1:8000/api/'  # URL вашего Django API


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Поднимет исключение для HTTP ошибок
                return await response.json()
        except aiohttp.ClientError as e:
            print(f"Error fetching data: {e}")
            return []


@router.message(Command('immovables'))
async def show_categories(message: types.Message):
    categories = await fetch_data(f'{BASE_URL}categories/')
    await message.answer("Выберите категорию:", reply_markup=categories_keyboard(categories))


@router.callback_query(lambda c: c.data.startswith('category_'))
async def show_subcategories(callback_query: CallbackQuery):
    category_id = callback_query.data.split('_')[1]
    subcategories = await fetch_data(f'{BASE_URL}subcategories/?category_id={category_id}')
    await callback_query.message.edit_text("Выберите подкатегорию:", reply_markup=subcategories_keyboard(subcategories))


@router.callback_query(lambda c: c.data.startswith('subcategory_'))
async def show_advertisements(callback_query: CallbackQuery):
    subcategory_id = callback_query.data.split('_')[1]
    advertisements = await fetch_data(f'{BASE_URL}advertisements/?subcategory_id={subcategory_id}')
    await callback_query.message.edit_text("Вот доступные объявления:",
                                           reply_markup=advertisements_keyboard(advertisements))
