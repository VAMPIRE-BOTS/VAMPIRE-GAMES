import asyncio
import uvloop

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

# HANDLERS
from handlers.start import router as start_router
from handlers.broadcast import router as broadcast_router
from handlers.logger import router as logger_router

# OLD GAMES
from games.bomb import router as bomb_router
from games.spy import router as spy_router
from games.fake_identity import router as fake_router
from games.fastest_finger import router as finger_router
from games.story import router as story_router
from games.ghost_reply import router as ghost_router
from games.lie_detector import router as lie_router

# NEW GAMES
from games.economy import router as economy_router
from games.couples import router as couples_router
from games.fun import router as fun_router
from games.puzzle import router as puzzle_router


# FAST EVENT LOOP
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# BOT CLIENT
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

# DISPATCHER
dp = Dispatcher()


async def main():

    # HANDLERS
    dp.include_router(start_router)
    dp.include_router(broadcast_router)
    dp.include_router(logger_router)

    # OLD GAMES
    dp.include_router(bomb_router)
    dp.include_router(spy_router)
    dp.include_router(fake_router)
    dp.include_router(finger_router)
    dp.include_router(story_router)
    dp.include_router(ghost_router)
    dp.include_router(lie_router)

    # NEW SYSTEM GAMES
    dp.include_router(economy_router)
    dp.include_router(couples_router)
    dp.include_router(fun_router)
    dp.include_router(puzzle_router)

    print("🎮 Vampire Game Bot Started ⚡ Mad by @lVAMPIRE_KINGl")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
