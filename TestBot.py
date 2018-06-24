import discord
client = discord.Client()


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith("ギガプリン"):
		voice = await client.join_voice_channel(
			client.get_channel("429186094827962368")
		)
		player = voice.create_ffmpeg_player('test.mp3')
		player.start()
		while player.is_done() != True:
			print ("playing music...")
		print("music end")
		print("end")
		for x in client.voice_clients:
			return await x.disconnect()
client.run("NDYwMzkyMDA0MzkyODQ1MzIz.DhEJWg.Xopeu55-O6_uirZi8bbX5qtDc34")