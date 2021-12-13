#### Imports
import nextcord
from nextcord.ext import commands
import json

#### Settings
while open("settings.json", "r") as settings:
    settings = settings.load()

    print(settings)
    token = None
    prefix = None


#### Initial Setup
nextcord.ext.commands.Bot(command_prefix=prefix, help_command=None)

#### Errors

#### On Ready

#### Starup
if __name__ == '__main__':
    client.run(token)

else:
    print("DO NOT IMPORT THIS")
    close()