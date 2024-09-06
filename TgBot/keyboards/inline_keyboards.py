from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def categories_keyboard(categories):
    keyboard = InlineKeyboardMarkup()
    for category in categories:
        keyboard.add(InlineKeyboardButton(text=category['name'], callback_data=f"category_{category['id']}"))
    return keyboard

def subcategories_keyboard(subcategories):
    keyboard = InlineKeyboardMarkup()
    for subcategory in subcategories:
        keyboard.add(InlineKeyboardButton(text=subcategory['name'], callback_data=f"subcategory_{subcategory['id']}"))
    return keyboard

def advertisements_keyboard(advertisements):
    keyboard = InlineKeyboardMarkup()
    for ad in advertisements:
        keyboard.add(InlineKeyboardButton(text=ad['title'], callback_data=f"ad_{ad['id']}"))
    return keyboard
