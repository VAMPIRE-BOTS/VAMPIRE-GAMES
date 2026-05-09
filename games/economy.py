import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("daily"))
async def daily_reward(message: Message):

    coins = random.randint(100, 1000)

    await message.answer(
        f"🎁 Daily Reward Claimed!\n\n💰 You Got {coins} Coins."
    )


@router.message(Command("claim"))
async def claim_reward(message: Message):

    coins = random.randint(50, 500)

    await message.answer(
        f"🪙 Claim Successful!\n\nYou Received {coins} Coins."
    )


@router.message(Command("rob"))
async def rob_user(message: Message):

    if not message.reply_to_message:
        return await message.reply(
            "Reply To A User."
        )

    amount = random.randint(1, 500)

    await message.answer(
        f"💸 You Robbed {amount} Coins 😭"
    )


@router.message(Command("pay"))
async def pay_user(message: Message):

    await message.answer(
        "💰 Payment System Coming Soon."
    )


@router.message(Command("kill"))
async def kill_user(message: Message):

    if not message.reply_to_message:
        return await message.reply(
            "Reply To A User."
        )

    kills = [
        "🔪 stabbed",
        "💣 exploded",
        "☠️ poisoned",
        "🪓 destroyed"
    ]

    method = random.choice(kills)

    victim = message.reply_to_message.from_user.first_name

    await message.answer(
        f"😭 {victim} was {method}"
    )
