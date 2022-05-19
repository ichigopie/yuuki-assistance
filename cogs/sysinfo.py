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
        RAM_usage = f"{(psutil.virtual_memory().total >> 20)-(psutil.virtual_memory().available >> 20)} MB ({100-psutil.virtual_memory().percent} %)"
        CPU_temp = f"N/A"
        if(platform.system() != "Windows"):
            CPU_temp = f"{psutil.sensors_temperatures()['scpi_sensors'][0][1]} C°"
        Disk_usage = f"{psutil.disk_usage('/').free >> 20} MB ({psutil.disk_usage('/').percent} %)"

        embed = discord.Embed(
            title="**<:workstation:976814353212903435> System Information**",
            color=discord.Colour.brand_red()
        )
        embed.add_field(
            name=f"**<:processor:976813558438457395> CPU :                        **",
            value=f"{CPU_usage}",
            inline=False
        )
        embed.add_field(
            name=f"**<:memory:976813933195329566> RAM :**",
            value=f"{RAM_usage}",
            inline=False
        )
        embed.add_field(
            name=f"**:thermometer: Temp :                        **",
            value=f"{CPU_temp}",
            inline=False
        )
        embed.add_field(
            name=f"**<:hdd:976818332940525610> Storage :**",
            value=f"{Disk_usage}",
            inline=False
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        sysinfo(bot),
        guilds=GUILD
    )
