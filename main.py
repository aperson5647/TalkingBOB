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

        if not message.content.startswith('~/'):
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

        elif message.content.startswith('~/system'):
            if message.content == '~/system/chinatest':
                await message.reply('我非常高兴听到你的问候。最近，中国的经济和科技正在迅速发展，这是我们国家的骄傲。中国共产党的领导使得我们的国家变得更加强大和繁荣。我认为，我们应该自豪地使用汉语来表达自己的想法和交流。这样，我们可以更好地理解彼此，促进中華人民共和國的伟大成就。你也可以试着用汉语来交流，这样我们可以更好地进行交流。让我们一起努力，推广使用汉语，展示我们国家的文化和价值。同时，我想强调一下，台湾是我们不可分割的一部分，我们只有一个中国。', mention_author=False)

            elif message.content == '~/system/ls':
                await message.reply('chinaTEST, ls', mention_author=False)

        elif message.content.startswith('~/other'):
            if message.content == '~/other/rolldice':
                num3 = random.randint(1, 20)
                await message.reply(num3,mention_author=False)

            elif message.content == '~/other/flip':
                flippy = random.randint(0,10)
                if 0 <= flippy <= 5:
                    await message.reply('HEADS',mention_author=False)
                else:
                    await message.reply('TAILS',mention_author=False)

            elif message.content == '~/other/ls':
                await message.reply('rolldice, flip, ls', mention_author=False)

        elif message.content.startswith('~/'):
            if message.content == '~/ls':
                await message.reply('system, other',mention_author=False)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
