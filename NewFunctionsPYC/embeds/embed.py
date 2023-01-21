import discord

class embedBuilder(discord.Embed):
    
    def set_title(self, title: str):
        self.title = str(title)

    def remove_title(self):
        self.title = ""

    def set_description(self, description: str):
        self.description = str(description)

    def remove_description(self):
        self.description = ""

    def set_color(self, color: int):
        self.colour = int(color)

    def set_colour(self, color: int):
        self.colour = int(color)

    def remove_colour(self):
        self.colour = discord.Colour.dark_theme()

