from typing import List, Dict, Any

from asyncpg import Connection

async def get_product(connection: Connection) -> Dict:
    await connection.fetchrow("")
