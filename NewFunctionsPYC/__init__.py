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
__author__ = "Marciel404"
__license__ = "MIT"

from .embed import (
    EmbedBuilder,
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

from .commands.options import (
    Option,
    OptionType,
    Choice
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

from .checks import (
    has_roles
)

