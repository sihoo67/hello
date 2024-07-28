import discord
from discord.ext import commands

# 여기에 자신의 디스코드 봇 토큰을 입력하세요.
TOKEN = 'MTI2NzA5NDU3MzU0OTYxNzI5NQ.GZ4lC6.9EzSelfOTCAYHxv7SXGIqcmE4PznYpQ0wVeqCU'

# 인텐트 설정
intents = discord.Intents.default()
intents.guilds = True
intents.members = True

# 봇에 사용할 접두사와 인텐트 설정
bot = commands.Bot(command_prefix='!', intents=intents)

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'봇이 로그인되었습니다. {bot.user}')

# 유저가 서버에 들어왔을 때 실행되는 이벤트
@bot.event
async def on_member_join(member):
    # 환영 메시지를 보낼 채널 ID를 입력하세요.
    channel = bot.get_channel(1043217271901925388)
    if channel is not None:
        await channel.send(f'{member.mention}님, 환영합니다! 서버에 오신 것을 환영해요!')

# 봇 실행
bot.run(TOKEN)
