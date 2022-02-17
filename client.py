from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix="", self_bot=True); client.remove_command("help")

@client.event
async def on_ready():
    guild = get(client.guilds, id=727649662475173962)
    channel = get(guild.channels, id=730459324937273564)
    vc = await channel.connect()
    await guild.change_voice_state(channel=channel, self_mute=True)
    vc.play(FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="path/sound.mp3"))

client.run('', bot=False)
