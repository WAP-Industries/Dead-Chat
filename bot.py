import nextcord
from nextcord.ext import commands, tasks

class DeadChat:
    Bot = commands.Bot(intents=nextcord.Intents.all())
    Guild = None
    Interval = 30
    Started = False
    Message = "@everyone dead chat lol"

    @Bot.event
    async def on_ready():
        print("im running nigga")
        DeadChat.Annoy.start()

    @Bot.event
    async def on_message(ctx: commands.context):
        if ctx.author.id==DeadChat.Bot.user.id:
            return
        DeadChat.Annoy.cancel()
        await __import__("asyncio").sleep(1)
        DeadChat.Started = False
        DeadChat.Annoy.start()

    @staticmethod
    @tasks.loop(minutes=Interval)
    async def Annoy():
        if not DeadChat.Started:
            DeadChat.Started = True
            return

        await __import__("random").choice([
            i for i in DeadChat.Bot.get_guild(DeadChat.Guild).channels 
            if isinstance(i, nextcord.TextChannel)
        ]).send(DeadChat.Message)