from discord.ext import commands
from discord import app_commands
import discord


class Ticket(commands.Cog):
    def __int__(self, aura: commands.AutoShardedBot):
        self.aura = aura

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ticket Online!')

    @app_commands.command(name='help', description='Teste')
    async def ticket(self, interaction: discord.Interaction):
        await interaction.response.send_message('funcionante.')


async def setup(aura: commands.AutoShardedBot) -> None:
    await aura.add_cog(Ticket(aura))
