"""
NewFunctionsPYC
~~~~~~~~~~

This module is for adding new functions to pycord
To make it easier for new people to get started on pycord

:copyright: (c) 2023-present Marciel404
:license: MIT, see LICENSE for more details.

:pycord-site: https://pycord.dev/ (English)
:pycord-discord-server: https://discord.gg/pycord (English)

:my-server: https://discord.gg/2UtE8tMyh5 (Portuguese)
"""
from importlib.metadata import PackageNotFoundError, version

__name__ = "NewFunctionsPYC"
__author__ = "Marciel404"
__license__ = "MIT"
__version__ = version("NewFunctionsPYC")

from .embed import (
    EmbedBuilder,
    Colour,
    Color,
    Colours,
    Colors,
    rgbColor,
    hexadecimalColor
)

from .loader import (
    Client,
    client,
    bot,
    Bot,
    getTokenDotEnv
)

from .options import (
    Option,
    OptionType,
    Choice,
    
)

from .prefix import (
    prefixContext,
    CommandPrefix,
)

from .slash import (
    slashContext,
    Slash_Command
)

from .hybrid import (
    hybridContext,
    HybridCommand
)

from .checks import (
    has_roles,
    checkVoteTopGG,
    NoVote
)

from .collection import (
    Collection,
    collection
)

from .dinamic_import import (
    dinamic_import
)
