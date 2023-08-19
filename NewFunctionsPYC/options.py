from typing import Any

def Option(
        name: str, 
        description: str = "Description not provided", 
        type: "OptionType" = None,
        choices: list["Choice"] = [],
        name_localizations: dict = {},
        description_localizations: dict = {}
        ) -> dict:
    
    """A helper on how to create an option for the command"""

    if type is None:
        type = OptionType.stringOption

    optionDict = {
        "type": type,
        "name": name,
        "description": description,
        "choices": choices,
        "name_localizations": name_localizations,
        "description_localizations": description_localizations
    }

    return optionDict

class OptionType:

    """Types for Options"""

    stringOption = 3
    intOption = 4
    boolOption = 5
    userOption = 6
    channelOption = 7
    roleOption = 8
    anyMentionableOption = 9
    numberOption = intOption
    attachmentOption = 11

def Choice(
        name,
        name_localizations: dict = {},
        value: Any = None
        ) -> dict:
    """A helper on how to create a choice for the command"""

    if value is None:
        value = name

    choiceDict = {
        "name": name,
        "name_localizations": name_localizations,
        "value": value
    }

    return choiceDict