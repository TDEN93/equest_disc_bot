import discord
import os # Access environmental variables

from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands
from datetime import datetime, timedelta, date

day = date.today().strftime("%x")
dt = datetime.strptime(day, '%x')
start = dt - timedelta(days=dt.weekday())
end = start + timedelta(days=6)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!wformat"):
            await message.channel.send('**Weekly Goal** \nAuthor: EQuest Bot \n- Task 1 \n- Task 2')

        if message.content.startswith('!weekly'):
            msg = message.content

            f=open("submissions_weekly.txt", "a+")
            f.write("Submission\n")
            f.write('Week: {0} - {1}\n'.format(datetime.strftime(start, "%x"), datetime.strftime(end, "%x")))
            f.write('Author: {0.author.mention}\n'.format(message))
            f.write(msg.replace("!weekly", "").replace("*", "") + "\n")

            await message.channel.send('{0.author.mention} submitted an agenda for {1} - {2}'
                .format(message, datetime.strftime(start, "%x"), datetime.strftime(end, "%x")))

        if message.content.startswith('!submissions'):
            f=open("submissions_weekly.txt", "r")
            if os.stat("submissions_weekly.txt").st_size == 0:
                await message.channel.send('There are no submissions')
            elif f.mode == 'r':
                contents = f.read()
                await message.channel.send('{0}'
                .format(contents))

client = MyClient()
client.run(os.environ['DISC_TOKEN'])