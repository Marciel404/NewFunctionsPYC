from typing import TYPE_CHECKING, Any, Protocol, TypeVar, Union
import discord
import hexacolors

__slots__ = (
    "title",
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
    "description",
)


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

if TYPE_CHECKING:
    from discord.types.embed import Embed as EmbedData
    from discord.types.embed import EmbedType

    T = TypeVar("T")
    MaybeEmpty = Union[T, _EmptyEmbed]

    class _EmbedFooterProxy(Protocol):
        text: MaybeEmpty[str]
        icon_url: MaybeEmpty[str]

    class _EmbedMediaProxy(Protocol):
        url: MaybeEmpty[str]
        proxy_url: MaybeEmpty[str]
        height: MaybeEmpty[int]
        width: MaybeEmpty[int]

    class _EmbedVideoProxy(Protocol):
        url: MaybeEmpty[str]
        height: MaybeEmpty[int]
        width: MaybeEmpty[int]

    class _EmbedProviderProxy(Protocol):
        name: MaybeEmpty[str]
        url: MaybeEmpty[str]

    class _EmbedAuthorProxy(Protocol):
        name: MaybeEmpty[str]
        url: MaybeEmpty[str]
        icon_url: MaybeEmpty[str]
        proxy_icon_url: MaybeEmpty[str]

E = TypeVar("E", bound="EmbedBuilder")

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

class Colours(Colors):
    """This class is a subclass of :class:`NewFunctionsPYC.Colors`"""

def hexadecimalColor(hex: str):
    return hexacolors.hexadecimal(str(hex))

def rgbColor(r: int, g: int, b: int):
    return hexacolors.rgb(f"{r},{g},{b}")

class attributesEmbed:

    dictEmb: dict[{str,str}] = {}
    fields = []
    title = ""
    description = ""
    footer = {}
    author = {}
    thumbnail = {}
    color = Colors.default
    image = {}
    thumbinail = {}

listAttributes = ["fields","title","description","footer","author","thumbnail","color", "image","thumbinail"]

class EmbedBuilder:
    """Embed contructor alike DiscordJs"""

    def set_title(self, title: str):
        attributesEmbed.title = title
    
    def set_description(self, description: str):
        attributesEmbed.description = description

    def set_footer(self, text: str, icon_url: str = None):

        attributesEmbed.footer["text"] = text

        if icon_url is None:
            attributesEmbed.footer["icon_url"] = icon_url

    def to_dict(self):

        for i in listAttributes:
            if getattr(attributesEmbed,i):
                attributesEmbed.dictEmb[i] = getattr(attributesEmbed,i)

        return attributesEmbed.dictEmb