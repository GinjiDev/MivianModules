import aiosqlite

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    async def execute(self, query, *args):
        async with aiosqlite.connect(self.db_name) as conn:
            await conn.execute(query, args)
            await conn.commit()

    async def fetch_one(self, query, *args):
        async with aiosqlite.connect(self.db_name) as conn:
            async with conn.execute(query, args) as cursor:
                return await cursor.fetchone()

    async def fetch_all(self, query, *args):
        async with aiosqlite.connect(self.db_name) as conn:
            async with conn.execute(query, args) as cursor:
                return await cursor.fetchall()
            
    async def create_table(self, table_name, columns):
        columns_def = ', '.join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        await self.execute(query)

    async def insert(self, table, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?' for _ in kwargs])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        await self.execute(query, *kwargs.values())

    async def update(self, table, where_clause, where_args, **kwargs):
        set_clause = ', '.join([f"{key} = ?" for key in kwargs])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        await self.execute(query, *kwargs.values(), *where_args)

    async def delete(self, table, where_clause, *where_args):
        query = f"DELETE FROM {table} WHERE {where_clause}"
        await self.execute(query, *where_args)

    async def get_all(self, table):
        query = f"SELECT * FROM {table}"
        return await self.fetch_all(query)

    async def get_where(self, table, where_clause, *where_args):
        query = f"SELECT * FROM {table} WHERE {where_clause}"
        return await self.fetch_all(query, *where_args)
    
    async def get_one(self, select, table, where_clause, *where_args):
        query = f"SELECT {select} FROM {table} WHERE {where_clause}"
        return await self.fetch_one(query, *where_args)