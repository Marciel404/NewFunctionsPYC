# NewFunctionsPYC

:A simple library for add new functions the Pycord

## Usage:
### install with pip

```shell
pip install NewFunctionsPYC
pip install -U git+https://github.com/Marciel404/NewFunctionsPYC (Instable)
```

### Import on your code:

```python
import NewFunctionsPYC
```
### Run it
```python

#More exemples in https://github.com/Marciel404/NewFunctionsPYC/tree/main/exemples

Using EmbedBuilder:

    >>> from NewFunctionsPYC import EmbedBuilder
    >>> from hexacolors import stringColor # "pip install hexacolors" for use this
    >>>
    >>> e: EmbedBuilder = EmbedBuilder()
    >>>
    >>> e.set_title("Title")
    >>>
    >>> e.set_description("Description")
    >>>
    >>> e.set_color(stringColor("indigo"))
    >>>
    >>> channel.send(embed = e.build())
    
Using client:

    >>> import NewFunctionsPYC
    >>>
    >>> client = NewFunctionsPYC.client("tokenBot")
    >>>
    >>> client.load_cogs("commands")
    >>>
    >>> client.__run__()
        
```