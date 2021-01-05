from pyrogram import Client
from pyrogram.types import Message


class genelmudur(Client, Message):
    def __init__(self):
        moduleName = "genelmudur"
        name = self.__class__.__name__.lower()
        super().__init__(
            session_name=name,
            config_file=f"{moduleName}/{name}.ini",
            workers=8,
            plugins=dict(root=f"{moduleName}/plugins"),
        )

    async def start(self):
        await super().start()

    async def stop(self, *args):
        await super().stop()
