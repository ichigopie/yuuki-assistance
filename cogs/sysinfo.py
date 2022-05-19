import discord
from discord import app_commands
from discord.ext import commands
import os
import dotenv
import psutil
import platform

dotenv.load_dotenv()
GUILD = [discord.Object(id=os.environ["GUILD_ID"])]


class sysinfo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="sysinfo",
        description="Show System Information"
    )
    async def sysinfo(
            self,
            interaction: discord.Interaction) -> None:

        CPU_usage = f"{psutil.cpu_percent(0.1)} %"
        RAM_usage = f"{psutil.virtual_memory().available >> 20} MB / {psutil.virtual_memory().total >> 20} MB ({psutil.virtual_memory().percent} %)"
        CPU_temp = f"Not Available on Windows"
        if(platform.system() != "Windows"):
            CPU_temp = f"{psutil.sensors_temperatures()['scpi_sensors'][0][1]} C°"

        embed = discord.Embed(
            title="System Information",
            description=f"**CPU Usage**\n{CPU_usage}\n\n**RAM Usage**\n{RAM_usage}\n\n**Temperature (C°)**\n{CPU_temp}",
            color=discord.Colour.brand_red()
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        sysinfo(bot),
        guilds=GUILD
    )
