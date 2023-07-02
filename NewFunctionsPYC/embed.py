import discord
import hexacolors

class EmbedBuilder:
    """Embed contructor alike DiscordJs"""

    settitle: str = ""
    setdescription: str = ""
    addfields: list = []
    insertfield: list = []
    removefield: list = []
    clearfields: bool = False
    setfooter: dict = {}
    removefooter: bool = False
    setauthor: dict = {}
    removeauthor: bool = False
    setimage: str = None
    setthumb: str = None
    removeimage: bool = False
    removethumb: bool = False
    setcolour: int = discord.Colour.dark_theme()
    e: discord.Embed

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

class Colors: 
    """Return interger color for embed"""

    default: int = 0
    brand_red: int = 0xED4245
    red: int = 0xE74C3C
    dark_red: int = 0x992D22
    blue: int = 0x3498DB
    dark_blue: int = 0x206694
    teal: int = 0x1ABC9C
    dark_teal: int = 0x11806A
    brand_green: int = 0x57F287
    green: int = 0x2ECC71
    dark_green: int = 0x1F8B4C
    purple: int = 0x9B59B6
    dark_purple: int = 0x71368A
    magenta: int = 0xE91E63
    dark_magenta: int = 0xAD1457
    gold: int = 0xF1C40F
    dark_gold: int = 0xC27C0E
    orange: int = 0xE67E22
    dark_orange: int = 0xA84300
    lighter_grey: int = 0x95A5A6
    dark_grey = 0x607D8B
    light_grey = 0x979C9F
    darker_grey = 0x546E7A
    og_blurple = 0x7289DA
    blurple = 0x5865F2
    greyple = 0x99AAB5
    dark_theme = 0x36393F
    fuchsia = 0xEB459E
    yellow = 0xFEE75C
    nitro_pink = 0xF47FFF

def hexadecimalColor(hex: str):
    return hexacolors.hexadecimal(str(hex))
def rgbColor(r: int, g: int, b: int):
    return hexacolors.rgb(f"{r},{g},{b}")