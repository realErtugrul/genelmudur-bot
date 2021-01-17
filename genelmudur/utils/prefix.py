from functools import partial

from pyrogram import filters

# Change prefix only from here and add from here.
cmdprefix = partial(filters.command, prefixes=["/"])
