# Part of: inline_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MAIN_PAGE_INLINE = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Наши товары',
                callback_data='products'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Корзина',
                callback_data='cart'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Где мы находимся',
                callback_data='location'
            ),
            InlineKeyboardButton(
                text='Контакты',
                callback_data='contacts'
            ),
        ]
    ]
)
