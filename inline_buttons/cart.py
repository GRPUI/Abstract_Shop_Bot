from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CART_INLINE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Оформить заказ',
                callback_data='checkout'
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
