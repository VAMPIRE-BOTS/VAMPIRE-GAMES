import asyncio
import uvloop

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# HANDLERS
from handlers.start import router as start_router
from handlers.broadcast import router as broadcast_router

# GAMES
from games.bomb import router as bomb_router
from games.spy import router as spy_router
from games.fake_identity import router as fake_router
from games.fastest_finger import router as finger_router
from games.story import router as story_router
from games.ghost_reply import router as ghost_router
from games.lie_detector import router as lie_router

# FAST EVENT LOOP
asyncio.set_event_loop_policy(
    uvloop.EventLoopPolicy()
)

# BOT CLIENT
bot = Bot(BOT_TOKEN)

# DISPATCHER
dp = Dispatcher()


async def main():

    # HANDLERS
    dp.include_router(start_router)
    dp.include_router(broadcast_router)

    # GAMES
    dp.include_router(bomb_router)
    dp.include_router(spy_router)
    dp.include_router(fake_router)
    dp.include_router(finger_router)
    dp.include_router(story_router)
    dp.include_router(ghost_router)
    dp.include_router(lie_router)

    print("🎮 Vampire Game Bot Started ⚡")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
