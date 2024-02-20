from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PRODUCTS_INLINE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='⬅️',
                callback_data='previous'
            ),
            InlineKeyboardButton(
                text='➡️',
                callback_data='next'
            ),
        ],
        [
            InlineKeyboardButton(
                text='В корзину 🛒',
                callback_data='add_to_cart'
            ),
        ],
        [
            InlineKeyboardButton(
                text='На главную',
                callback_data='main_page'
            ),
        ]
    ]
)
