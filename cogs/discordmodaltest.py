import discord
from discord import app_commands
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
GUILD = [discord.Object(id=os.environ["GUILD_ID"])]


class TestModal(discord.ui.Modal, title="Discord Modal Test"):
    user_input = discord.ui.TextInput(
        label="Put your text here:",
        style=discord.TextStyle.short,
        placeholder="Text goes here...",
        required=True,
        max_length=255
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=self.title,
            description=f"**{self.user_input.label}**\n{self.user_input}",
            color=discord.Colour.blurple()
        )
        embed.set_author(
            name=interaction.user, icon_url=interaction.user.avatar
        )
        await interaction.response.send_message(embed=embed)


class discordmodaltest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="discordmodaltest",
        description="Test Discord Modal"
    )
    async def discordmodaltest(
            self,
            interaction: discord.Interaction) -> None:
        await interaction.response.send_modal(TestModal())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        discordmodaltest(bot),
        guilds=GUILD
    )
