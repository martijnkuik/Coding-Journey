import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass

BOT_TOKEN = "Hidden"
CHANNEL_ID = "Hidden"
MAX_SESSION_TIME_MINUTES = 45

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print("Hello! Koekie-bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Koekie-bot is ready!")

@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES)
async def break_reminder():
    if break_reminder.current_loop == 0:  # Skip the first loop execution
        return
    if session.is_active:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(f"**Take a break!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes.")

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return

    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")

    if not break_reminder.is_running():
        break_reminder.start()

    await ctx.send(f"New session started at {human_readable_time}")

@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timezone(seconds=duration))

    if break_reminder.is_running():
        break_reminder.stop()

    await ctx.send(f"Session ended after {human_readable_duration}.")

bot.run(BOT_TOKEN)
