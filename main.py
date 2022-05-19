import discord
from discord.ext import commands
import os
import dotenv

# Get enviroment variables
dotenv.load_dotenv()
GUILD = discord.Object(os.environ["GUILD_ID"])
TOKEN = os.environ["BOT_TOKEN"]
APP_ID = os.environ["APP_ID"]
COGS = ["discordmodaltest", "sysinfo", "ping"]


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents=discord.Intents.default(),
            application_id=APP_ID
        )

    async def setup_hook(self):
        for i in COGS:
            print(f"cogs.{i}")
            await self.load_extension(f"cogs.{i}")
        await self.tree.sync(guild=GUILD)

    async def on_ready(self):
        print(f"Bot has logged in as {self.user}")
        print(f"--------------------------")


bot = Bot()
bot.run(TOKEN)
