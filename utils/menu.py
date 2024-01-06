import discord
from discord.ext import commands
from discord import app_commands


class SelectionMenu(discord.ui.Select):
    def __init__(self):
        choices = [
            discord.SelectOption(value="duvida", label="Dúvidas", emoji=""),
            discord.SelectOption(value="ticket", label="Abrir ticket", emoji=""),
            discord.SelectOption(value="denuncia", label="Denúncias", emoji=""),
            discord.SelectOption(value="sugestao", label="Sugestões", emoji=""),
            discord.SelectOption(value="reportbug", label="Relatar algum bug", emoji=""),
            discord.SelectOption(value="outros", label="Outros", emoji=""),
        ]
        super().__init__(
            placeholder="No que posso ajudar?",
            min_values=1,
            max_values=1,
            options=choices,
            custom_id="aura:help_menu"
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "duvida":
            await interaction.response.send_message("teste teste", ephemeral=True)
        else:
            await interaction.response.send_message("teste de novo", ephemeral=True)


class Visualization(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(SelectionMenu())
