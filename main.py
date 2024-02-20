import asyncpg
from aiogram import Bot, Dispatcher, types, Router
from aiogram import filters
import asyncio

from asyncpg import Connection
from loguru import logger

import dotenv
import os

from inline_buttons import MAIN_PAGE_INLINE, PRODUCTS_INLINE, CART_INLINE, LOCATION_INLINE, CONTACTS_INLINE
from services import users

dotenv.load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

router = Router()


@router.message(filters.Command("start"))
async def send_welcome(message: types.Message, bot: Bot, connection: Connection) -> None:
    logger.info(f"User:{message.from_user.id} Command: /start")
    await logger.complete()
    photo = types.FSInputFile("static/orig.webp")
    await bot.send_photo(
        message.chat.id,
        photo=photo,
        caption="Приветcтвую вас в магазине Abstract Store!",
        reply_markup=MAIN_PAGE_INLINE
    )
    params = message.from_user.__dict__
    params["full_name"] = message.from_user.full_name
    await users.register(connection, params)


@router.message(filters.Command("help"))
async def send_help(message: types.Message):
    logger.info(f"User:{message.from_user.id} Command: /help")
    await logger.complete()
    await message.answer("Для начала работы нажмите /start\n")


@router.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    logger.info(f"User:{callback_query.from_user.id} Query: {callback_query.data}")
    await logger.complete()
    await logger.complete()
    if callback_query.data == "products":
        await callback_query.message.edit_caption(
            caption="Наши товары",
            reply_markup=PRODUCTS_INLINE
        )
    elif callback_query.data == "cart":
        await callback_query.message.edit_caption(
            caption="Корзина",
            reply_markup=CART_INLINE
        )
    elif callback_query.data == "location":
        await callback_query.message.edit_caption(
            caption="Где мы находимся",
            reply_markup=LOCATION_INLINE)
    elif callback_query.data == "contacts":
        await callback_query.message.edit_caption(
            caption="Контакты",
            reply_markup=CONTACTS_INLINE
        )
    elif callback_query.data == "main_page":
        await callback_query.message.edit_caption(
            caption="Приветcтвую вас в магазине Abstract Store!",
            reply_markup=MAIN_PAGE_INLINE
        )


async def main() -> None:
    logger.info("Starting bot")
    await logger.complete()

    database = os.getenv(key="DB_NAME")
    user = os.getenv(key="POSTGRES_USER")
    password = os.getenv(key="DB_PASSWORD")
    host = os.getenv(key="DB_HOST")

    connection = await asyncpg.connect(
        f"postgresql://{user}:{password}@{host}/{database}"
    )

    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)

    dp.workflow_data.update(
        {
            "connection": connection
        }
    )

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.add("logs.log", level="INFO", rotation="1 week")
    asyncio.run(main())
