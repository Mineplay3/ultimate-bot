import nextcord
from nextcord.ext import commands

token = None
prefix = None

nextcord.ext.commands.Bot(command_prefix=prefix, help_command=None)

if __name__ == '__main__':
    client.run(token)

else:
    print("DO NOT IMPORT THIS")
    close()