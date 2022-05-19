import discord
from discord import app_commands
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
GUILD = [discord.Object(id=os.environ["GUILD_ID"])]


class ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Check Discord-Bot Server Latency"
    )
    async def ping(
            self,
            interaction: discord.Interaction) -> None:

        embed = discord.Embed(
            title="<:remote:976835736697458689> Ping",
            description=f"Pong!\n**{round(self.bot.latency*1000)} ms**",
            color=discord.Colour.green()
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ping(bot),
        guilds=GUILD
    )
