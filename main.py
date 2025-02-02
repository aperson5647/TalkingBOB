# This example requires the 'message_content' intent.
import io

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
            num = random.randint(0,3)
            if num == 0:
                await channel1.send('Yes')
            elif num == 1:
                await channel1.send('No')
            elif num == 2:
                await channel1.send('Kys')
            elif num == 3:
                await channel1.send('Shitfart 2.0')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
