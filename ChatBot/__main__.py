import importlib

from pyrogram import idle


async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"ChatBot.modules.{module}")

    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(boot())
