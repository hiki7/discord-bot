import discord
import os
import search_animelist
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()


anime_web = search_animelist.AnimeFind()

no_result_message = "Sorry I coudn't find the page with this anime"
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()
    if message.content.startswith('$search'):
        key_words, search_words = anime_web.keywords_search_words(message_content)
        result_links = anime_web.search(key_words)
        links = anime_web.send_link(result_links, search_words)

        if len(links) > 0:
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)

    await client.process_commands(message)


@client.command(aliase=['purge'])
async def clear(ctx, amount=11):
    if amount > 101:
        await ctx.send("Can not delete more than 100 messages")
    else:
        await ctx.channel.purge(limit=amount+1)


@client.command(aliase=['hello'])
async def hello(ctx):
    await ctx.send('sup')

client.run(os.getenv('TOKEN'))
