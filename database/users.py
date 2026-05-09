from database.mongo import usersdb

async def add_user(user_id):
    user = await usersdb.find_one({"user_id": user_id})

    if user:
        return

    await usersdb.insert_one(
        {
            "user_id": user_id,
            "coins": 100,
            "wins": 0,
            "badges": [],
        }
    )


async def get_user(user_id):
    return await usersdb.find_one({"user_id": user_id})
