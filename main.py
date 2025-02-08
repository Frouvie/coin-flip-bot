import discord
from discord.ext import commands
import random

token = ''

languages = {
    'en': {
        'help': "**Commands:**\n/help - Show this message\n/flip - Flip a coin\n/language - Change language (en/ru)",
        'flip_result': ["Heads", "Tails"],
        'language_changed': "Language changed to English.",
        'invalid_language': "Invalid language code. Use 'en' or 'ru'."
    },
    'ru': {
        'help': "**Команды:**\n/help - Показать это сообщение\n/flip - Подкинуть монетку\n/language - Сменить язык (en/ru)",
        'flip_result': ["Орел", "Решка"],
        'language_changed': "Язык сменён на русский.",
        'invalid_language': "Неверный код языка. Используйте 'en' или 'ru'."
    }
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

users_language = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='help')
async def help_command(ctx):
    language = users_language.get(ctx.author.id, 'en')
    await ctx.send(languages[language]['help'])

@bot.command(name='flip')
async def flip_command(ctx):
    language = users_language.get(ctx.author.id, 'en')
    result = random.choice(languages[language]['flip_result'])
    await ctx.send(f'**{result}!**')

@bot.command(name='language')
async def language_command(ctx, lang: str):
    if lang in languages:
        users_language[ctx.author.id] = lang
        await ctx.send(languages[lang]['language_changed'])
    else:
        language = users_language.get(ctx.author.id, 'en')
        await ctx.send(languages[language]['invalid_language'])

bot.run(token)