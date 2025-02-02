# This example requires the 'message_content' intent.
import io
import math

tokenOp = io.open("config.txt")
token = tokenOp.read()

import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        ALLOWED_CHANNELS = {1224436018342793317, 1335670414268956672}

        if message.channel.id not in ALLOWED_CHANNELS:
            return

        print(f'Message from {message.author}: {message.content}')
        if message.channel.id == 1224436018342793317:
            channel1 = self.get_channel(1224436018342793317)

        if message.channel.id == 1335670414268956672:
            channel1 = self.get_channel(1335670414268956672)

        if message.author.id != 1330293366960689192:
            num = random.randint(0,17)

            if 0 <= num <= 5:
                await message.reply('Yes', mention_author=False)
            elif 6 <= num <= 10:
                await message.reply('No', mention_author=False)
            elif 11 <= num <= 13:
                await message.reply('Kys', mention_author=False)
            elif 14 <= num <= 16:
                await message.reply('I have a bomb', mention_author=False)
            elif num == 17:
                await channel1.send('Whoever speaks next likes little kids')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
