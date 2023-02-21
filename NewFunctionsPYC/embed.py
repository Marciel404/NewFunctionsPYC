import discord
import hexacolors

class EmbedBuilder:

    def __init__(self) -> None:

        self.settitle: str = ""; self.setdescription: str = ""
        self.addfields: list = []; self.insertfield: list = []
        self.removefield: list = []; self.clearfields: bool = False
        self.setfooter: dict = {}; self.removefooter: bool = False
        self.setauthor: dict = {}; self.removeauthor: bool = False
        self.setimage: str = None; self.setthumb: str = None
        self.removeimage: bool = False; self.removethumb: bool = False
        self.setcolour: int = discord.Colour.dark_theme()
        self.e: discord.Embed

    def set_title(self, title: str) -> str:
        self.settitle = str(title)

    def set_description(self, description: str) -> str:
        self.setdescription = str(description)

    def set_color(self, color: int) -> int:
        self.setcolour = int(color)

    def set_colour(self, color: int) -> int:
        self.setcolour = int(color)
    
    def add_field(self, name: str, value: str, inline: bool = True) -> list:
        
        self.addfields.append(
            {
                "name": name, 
                "value": value, 
                "inline": inline
            }
        )
    
    def insert_field_at(self, index: int, name: str, value: str, inline: bool = True):

        self.insertfield.append(
            {
                "index": index,
                "name": name,
                "value": value,
                "inline": inline
            }
        )
    
    def set_footer(self, text: str, icon_url: str = "") -> dict:

        self.setfooter = {
            "text": text,
            "icon_url": icon_url
        }
    
    def set_author(self, name: str, url: str = "", icon_url: str = "") -> dict:

        self.setauthor = {
            "name": name,
            "url": url,
            "icon_url": icon_url
        }
    
    def remove_field(self, index: int) -> int:
        self.removefield.append(
            {
                "index": index
            }
        )
    
    
    def set_image(self, url: str) -> str:
        self.setimage = str(url)
    
    def set_thumbinail(self, url: str) -> str:
        self.setthumb = str(url)

    def remove_title(self) -> str:
        self.settitle = ""
    
    def remove_description(self) -> str:
        self.setdescription = ""

    def remove_color(self) -> int:
        self.setcolour = discord.Color.dark_theme()
    
    def remove_colour(self) -> int:
        self.setcolour = discord.Color.dark_theme()
    
    def remove_author(self) -> bool:
        self.removeauthor = True
    
    def remove_image(self) -> bool:
        self.removeimage = True
    
    def remove_thumbnail(self) -> bool:
        self.removethumb = True
    
    def remove_footer(self) -> bool:
        self.removefooter = True
    
    def clear_fields(self) -> bool:
        self.clearfields = True
    
    def build(self) -> discord.Embed:

        self.e = discord.Embed(
            title = self.settitle,
            description = self.setdescription,
            color = self.setcolour
        )

        if self.setauthor != {}: 
            self.e.set_author(
                name = self.setauthor["name"], 
                url = self.setauthor["url"], 
                icon_url = self.setauthor["icon_url"]
            )

        if self.setfooter != {}:
            self.e.set_footer(
                text = self.setfooter["text"],
                icon_url = self.setfooter["icon_url"]
            )

        if self.addfields != []:
            for x in self.addfields: 
                self.e.add_field(
                    name = x["name"],
                    value = x["value"],
                    inline = x["inline"]
                )
        
        if self.insertfield != []:
            for x in self.insertfield:
                self.e.insert_field_at(
                    index = x["index"],
                    name = x["name"],
                    value = x["value"],
                    inline = x["inline"]
                )

        if self.setthumb != None: 
            self.e.set_thumbnail(self.thumb)

        if self.setimage != None: 
            self.e.set_image(url = self.url)

        if self.removefield != []:
            counter = 0
            while True:
                self.e.remove_field(int(self.removefield[counter-1]["index"]))
                if counter != self.removefield.__len__(): counter += 1
                else: break

        if self.removefooter != False: 
            self.e.remove_footer()

        if self.removeauthor != False: 
            self.e.remove_author()

        if self.removeimage != False: 
            self.e.remove_image()

        if self.removethumb != False: 
            self.e.remove_thumbnail()
        
        if self.clearfields != False:
            self.e.clear_fields()
        
        return self.e
    
    def detonarn(self):
        try:
            del self.e
        except AttributeError:
            pass

def hexadecimalColor(hex: str):
    return hexacolors.hexadecimal(str(hex))

def rgbColor(r: int, g: int, b: int):
    return hexacolors.rgb(f"{r},{g},{b}")