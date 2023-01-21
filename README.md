# betterFunctions

:A simple library for add new functions the Pycord

## Usage:
### Import on your code:

```python
import betterFunctions
```
### Run it
```python

Run if online:

    Using embedBuilder:

        >>> from betterFunctions import embedBuilder
            from hexacolors import stringColor # pip install hexacolors for use this
        >>> e: embedBuilder = embedBuilder()
        >>>
        >>> e.set_title("Title")
        >>>
        >>> e.set_description("Description")
        >>>
        >>> e.set_color(stringColor("indigo"))
        >>>
        >>> channel.send(embed = e ) #List all colors availables
    
    Using client:

        >>> import NewFunctionsPYC
        >>>
        >>> client = NewFunctionsPYC.client("tokenBot")
        >>>
        >>> client.load_cogs("commands")
        >>>
        >>> client.__run__()
        
```