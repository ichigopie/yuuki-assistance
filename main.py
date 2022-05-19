import discord
from discord.ext import commands
import os
import dotenv

# Get enviroment variables
dotenv.load_dotenv()
GUILD = discord.Object(os.environ["GUILD_ID"])
TOKEN = os.environ["BOT_TOKEN"]
APP_ID = os.environ["APP_ID"]


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents=discord.Intents.default(),
            application_id=APP_ID
        )

    async def setup_hook(self):
        # TODO Loop load cogs extentions
        await self.load_extension(f"cogs.discordmodaltest")
        await self.load_extension(f"cogs.sysinfo")
        await self.tree.sync(guild=GUILD)

    async def on_ready(self):
        print(f"Bot has logged in as {self.user}")
        print(f"--------------------------")

# TODO set cogs list in environtment
# initial_extentions = (
#     "cogs.discordmodaltest"
#     "cogs.sysinfo"
# )

# for extention in initial_extentions:
#     try:
#         Bot.load_extension(extention)
#     except Exception as e:
#         print(e)


bot = Bot()
bot.run(TOKEN)
