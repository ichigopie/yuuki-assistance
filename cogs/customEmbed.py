import discord
from discord import app_commands
from discord.ext import commands
import os
import dotenv
import json
import requests

dotenv.load_dotenv()
GUILD = [discord.Object(id=os.environ["GUILD_ID"])]


class embedModal(discord.ui.Modal, title="Custom Embed"):
    json_url = discord.ui.TextInput(
        label="Custom embed JSON file URL",
        style=discord.TextStyle.long,
        placeholder="url goes here",
        required=True,
        max_length=255
    )
    channel_id = discord.ui.TextInput(
        label="The channel ID where the message will be sent",
        style=discord.TextStyle.short,
        placeholder="channel ID",
        required=True,
        max_length=25
    )

    async def on_submit(self, interaction: discord.Interaction):
        data = requests.get(self.json_url)
        content = json.loads(data.text)['content']
        embed = json.loads(data.text)['embeds'][0]
        embed['timestamp'] = ""
        embed = discord.Embed.from_dict(embed)
        buttons = json.loads(data.text)['components'][0]['components']
        view = componentsButtons(buttons)
        _channel = interaction.guild.get_channel(int(self.channel_id.value))
        await _channel.send(content=content, embed=embed, view=view)
        await interaction.response.send_message("Message Sent!")


class componentsButtons(discord.ui.View):
    def __init__(self, buttons: dict):
        super().__init__()
        for button in buttons:
            self.add_item(discord.ui.Button(
                label=button['label'], url=button['url']))


class customEmbed(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @ app_commands.command(
        name="customembed",
        description="Send a Custom Embed"
    )
    async def customEmbed(
            self,
            interaction: discord.Interaction) -> None:
        await interaction.response.send_modal(embedModal())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        customEmbed(bot),
        guilds=GUILD
    )
