from mivmodules.miv_sql import Database
import asyncio

db1 = Database("test.db")

async def main():
    await db1.create_table('user', ["id INT PRIMARY KEY", "name TEXT DEFAULT NONE"])
    id_list = [3235, 1435, 24, 32134]
    
    for user_id in id_list:
        rows = await db1.get_where('user', 'id=?', user_id)
        if not rows:
            await db1.execute('INSERT INTO user (id) VALUES (?)', user_id)

asyncio.run(main())