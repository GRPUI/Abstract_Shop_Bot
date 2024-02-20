from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

LOCATION_INLINE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Открыть карту',
                web_app=WebAppInfo(
                    url='https://go.2gis.com/1t5zo'
                )
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
