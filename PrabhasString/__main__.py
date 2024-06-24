import asyncio
import importlib

from pyrogram import idle

from PrabhasString import LOGGER, ritik
from PrabhasString.modules import ALL_MODULES


async def ritik_boot():
    try:
        await ritik.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("PrabhasString.modules." + all_module)

    LOGGER.info(f"@{ritik.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(ritik_boot())
    LOGGER.info("Stopping String Gen Bot...")
