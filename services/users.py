from typing import List, Dict, Any

from asyncpg import Connection
from datetime import datetime


async def is_registered(connection: Connection, user_id: int) -> bool:
    row = await connection.fetchval(
        "SELECT id FROM users WHERE id = $1",
        user_id
    )

    if row:
        return True
    return False


async def register(connection: Connection, params: Dict) -> None:
    registration = await is_registered(connection, params["id"])

    if registration:
        return

    await connection.execute(
        "INSERT INTO users(id, full_name, username, language_code, is_bot, is_premium, register_date) "
        "values($1, $2, $3, $4, $5, $6, $7)",
        params["id"],
        params["full_name"],
        params["username"],
        params["language_code"],
        params["is_bot"],
        params["is_premium"],
        datetime.now()
    )
    return
