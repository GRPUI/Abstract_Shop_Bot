from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CONTACTS_INLINE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Написать 📩',
                url='https://t.me/username'
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
