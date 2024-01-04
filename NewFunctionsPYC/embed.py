from typing import Any
from hexacolors import rgb, hexadecimal


class _EmptyEmbed:

    def __bool__(self) -> bool:
        return False
    
    def __repr__(self) -> str:
        return "Embed.Empty"
    
    def __len__(self) -> int:
        return 0
    
EmptyEmbed = _EmptyEmbed()


class EmbedProxy:

    def __init__(self, layer: dict[str, Any]):
        self.__dict__.update(layer)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        inner = ", ".join(
            (f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith("_"))
        )
        return f"EmbedProxy({inner})"

    def __getattr__(self, attr: str) -> _EmptyEmbed:
        return EmptyEmbed


class Colour:
    
    __slots__ = ("value",)

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                f"Expected int parameter, received {value.__class__.__name__} instead."
            )

        self.value: int = value

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


class Colours(Colour):
    ...


class Color(Colour):
    ...


class Colors(Colour):
    ...


def hexadecimalColor(hex: str):
    return hexadecimal(str(hex))


def rgbColor(r: int, g: int, b: int):
    return rgb(f"{r},{g},{b}")


class EmbedBuilder:
    
    __slots__ = (
        "_title",
        "url",
        "type",
        "_timestamp",
        "_colour",
        "_footer",
        "_image",
        "_thumbnail",
        "_video",
        "_provider",
        "_author",
        "_fields",
        "_description",
    )

    def set_title(self, title: str):
        self.title = title
    
    @property
    def title(self):
        return getattr(self,"_title", EmptyEmbed)

    @title.setter
    def title(self, value: str):
        self._title = value
        if self._title.__len__() > 4096:
            raise TypeError("Description size larger than allowed 4096")
    
    def set_description(self, description: str):
        self.description = description

    @property
    def description(self):
        return getattr(self,"_description", EmptyEmbed)

    @description.setter
    def description(self, value: str):
        self._description = value
        if self._description.__len__() > 4096:
            raise TypeError("Description size larger than allowed 4096")
    
    def set_footer(self, text: str, icon_url: str = None):

        self._footer = {}
        if text is not EmptyEmbed:
            self._footer["text"] = str(text)

        if icon_url is not EmptyEmbed:
            self._footer["icon_url"] = str(icon_url)

        return self

    @property
    def footer(self, text: str, icon_url: str = None):
        ...
    
    @footer.setter
    def footer(self, text: str, icon_url: str = None):
        
        if not self._footer["icon_url"].startswith("http"):
            self._footer["icon_url"] = ""

        if self._footer["text"].__len__() > 2048:
            raise TypeError("Footer Text size larger than allowed 2048")

    @property
    def colour(self, value: int):
        return getattr(self, "_colour", EmptyEmbed)

    @colour.setter
    def colour(self, value: int):
        if isinstance(value, (Colour, _EmptyEmbed)):
            self._colour = value
        elif isinstance(value, int):
            self._colour = Colour(value=value)
        else:
            raise TypeError(
                "Expected discord.Colour, int, or Embed.Empty but received"
                f" {value.__class__.__name__} instead."
            )

    def add_field():
        ...

    def to_dict(self):
        return self.description, self.title
