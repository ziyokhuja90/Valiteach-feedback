from pydantic import BaseModel
import aiosqlite
from typing import List
import asyncio

class User(BaseModel):
    id: int
    name: str
    email: str


DATABASE_URL = 'sqlite.db'

async def init_db():
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
        ''')
        await db.commit()

async def create_user(user: User):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute('''
        INSERT INTO users (id, name, email)
        VALUES (?, ?, ?)
        ''', (user.id, user.name, user.email))
        await db.commit()

async def get_user(user_id: int) -> User:
    async with aiosqlite.connect(DATABASE_URL) as db:
        async with db.execute('SELECT id, name, email FROM users WHERE id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return User(id=row[0], name=row[1], email=row[2])
            return None

async def get_users() -> List[User]:
    async with aiosqlite.connect(DATABASE_URL) as db:
        async with db.execute('SELECT id, name, email FROM users') as cursor:
            rows = await cursor.fetchall()
            return [User(id=row[0], name=row[1], email=row[2]) for row in rows]


