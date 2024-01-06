# imports
from utils.menu import Visualization
from discord.ext import commands, tasks
from utils.envkeys import aura_key, app_id
from dotenv import load_dotenv
import discord
import asyncio
import os


# This entire file is basically Yume 2
class BotAura(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        load_dotenv()

        super().__init__(command_prefix='a!', case_insensitive=True, intents=intents, application_id=app_id(), shards=2)

    async def setup_hook(self) -> None:
        self.add_view(Visualization())

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f'Este comando não existe, que tal tentar outra coisa?', ephemeral=True)


aura = BotAura()
aura.remove_command('help')


def id_lock(ctx):
    return ctx.author.id == 337765056970358784


@aura.event
async def on_ready():
    status.start()


@tasks.loop()
async def status():
    await aura.change_presence(activity=discord.Game(name='Sempre disponível para você!'))


async def cogs_load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await aura.load_extension(f'cogs.{filename[:-3]}')


@aura.command()
@commands.check(id_lock)
async def refresh(ctx):
    await aura.tree.sync()
    await ctx.send('Atualizado.')


async def main():
    await on_ready()
    await cogs_load()

    print("I'm Online!")
    await aura.start(aura_key())


asyncio.run(main())
