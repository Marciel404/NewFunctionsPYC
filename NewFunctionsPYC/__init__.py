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

__name__ = "NewFunctionsPYC"
__version__ = "1.2.0"
__author__ = "Marciel404"
__license__ = "MIT"

from .embed import (
    EmbedBuilder,
    rgbColor, 
    hexadecimalColor
)

from .loader import (
    Client,
    client,
    bot,
    Bot,
    BotBuilder
)

from .commands.prefix import (
    prefixContext,
    CommandPrefix,
)

from .commands.slash import (
    slashContext,
    Slash_Command
)

from .commands.hybrid import (
    hybridContext,
    HybridCommand
)

