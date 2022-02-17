from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands

# config
token = ""
guildid = 9876543211234567890
vcid = 123456789876543210
soundpath = "path/sound.mp3"

# DON'T TOUCH THIS
soundpath = soundpath.replace("\\", "/").replace("//", "/")
client = commands.Bot(command_prefix="", self_bot=True); client.remove_command("help")

@client.event
async def on_ready():
    guild = get(client.guilds, id=guildid)
    channel = get(guild.channels, id=vcid)
    vc = await channel.connect()
    await guild.change_voice_state(channel=channel, self_mute=True)
    vc.play(FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=soundpath))

client.run(token, bot=False)
