# Stephen Hawking Quote bot for use with discord
# Created by: Alex Laswell

from random import choice
import config
import discord

# start by creating the client object
client = discord.Client()

# set things from the config file
cmdprefix = config.cmdprefix				
token = config.token						# the login token for the bot
quotes = config.quotes						# dict of all the quotes and their source

# Send a rich embeded message instead of a plain one
async def emb_message(message, quote, source):
	emb = (discord.Embed(description=quote, colour=0x5e7750))
	emb.set_author(name="Dr. Stephen William Hawking, 1942-2018", icon_url=client.user.avatar_url)
	emb.add_field(name='Source:', value=source, inline=False)
	await client.send_message(message.channel, embed=emb )
	
	
# Every time we receive a message
@client.event
async def on_message(message):
	if message.author == client.user: return			# talking to yourself isn't cool...even for bots
	
	# Hawking - Displays a random quote from The Great Dr. Hawking
	if(message.content.startswith(cmdprefix + "hawking")):
		quote, source = choice(list(quotes.items()))
		await emb_message(message, quote, source)

	# About - Displays a brief synopsis of who Dr. Hawking was, taken from wikipedia
	if(message.content.startswith(cmdprefix +  "about")):
		quote = 'Stephen William Hawking (8 January 1942 – 14 March 2018) was a British theoretical physicist, cosmologist, author and Director of Research at the Centre for Theoretical Cosmology within the University of Cambridge. His scientific works include a collaboration with Roger Penrose on gravitational singularity theorems in the framework of general relativity and the theoretical prediction that black holes emit radiation, often called Hawking radiation. Hawking was the first to set out a theory of cosmology explained by a union of the general theory of relativity and quantum mechanics. He was a vigorous supporter of the many-worlds interpretation of quantum mechanics.'
		await emb_message(message, quote, 'Wikipedia')
			
# Run the bot
client.run(token)