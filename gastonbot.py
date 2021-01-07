import os
import json
import uuid
import time
import datetime
import discord

from gastonbot_rules import gastonbot

intent = discord.Intents.all()
client = discord.Client()

CONFIG = json.load(open('config.json'))
CLIENT_ID = CONFIG['client_id']
TOKEN = CONFIG['token']
BOTNAME = CONFIG['botname']
BOT_MENTION_1 = CONFIG['botmention']
BOT_MENTION_2 = BOT_MENTION_1.replace('<@','<@!')
BOTNAME_LENGTH = len(BOTNAME)



def isMention(message):
	if (
		message.content.startswith(BOTNAME) or 
		message.content.startswith(BOT_MENTION_1) or 
		message.content.startswith(BOT_MENTION_2)
	):
		return True
	else:
		return False


def parseCommandMessage(event):
	message = str(event.content)
	message = message.replace(BOTNAME+' ','')
	message = message.replace(BOT_MENTION_1+' ','')
	message = message.replace(BOT_MENTION_2+' ','')
	return message

def parseCommand(event):
	message_with_command = parseCommandMessage(event)
	split_message_with_command = message_with_command.split(' ')
	return split_message_with_command[0].lower().replace(' ','')

def parseArgs(event):
	message_with_command = parseCommandMessage(event)
	command = parseCommand(event)
	args = message_with_command.replace(command,'')
	return args



def eventParser(event):
	# native values
	message_id,message,thread_id,thread,thread_category,thread_category_id,author_id,author_nick,author = None,None,None,None,None,None,None,None,None
	try:
		message_id = event.id
	except:
		pass
	try:
		message = event.content
	except:
		pass
	try:
		thread_id = event.channel.id
	except:
		pass
	try:
		thread = event.channel.id
	except:
		pass
	try:
		thread_category = event.channel.category
	except:
		pass
	try:
		thread_category_id = event.channel.category_id
	except:
		pass
	try:
		author_id = event.author.id
	except:
		pass
	try:
		author_nick = event.author.nick
	except:
		pass
	try:
		author = event.author.name
	except:
		pass


	# transforms
	mention = False
	try:
		mention = isMention(event)
	except:
		pass
	command = None
	try:
		command = parseCommand(event)
	except:
		pass
	args = None
	try:
		args = parseArgs(event)
	except:
		pass

	return {
		'message_mention' : mention,
		'message_command' : command,
		'message_args' : args,
		'message_id' : message_id,
		'message_body' : message,
		'thread_id': thread_id,
		'thread' : thread,
		'thread_category': thread_category,
		'thread_category_id': thread_category_id,
		'author_id': author_id,
		'author_nick': author_nick,
		'author': author
	}







@client.event
async def on_message(message):
	if (isMention(message) or '<DMChannel id=' in str(message)) and eventParser(message)['author'] != 'gastonbot':
		parsedEvent = eventParser(message)
		payload = None
		# command override for leet gaston hacks
		if 'hack' in parsedEvent['message_body']:
			import requests
			r = requests.get('https://cve.mitre.org/data/downloads/allitems.txt')
			raw = r.text
			raw = raw.split('\n')
			cves = []
			for each in raw:
				if 'Name: CVE-' in each:
					cves.append(each.replace('Name: ',''))
			import random
			import time
			random_cve = random.choice(cves)

			payload = '`[!] received command "HACK". Confirming weapons lock...`'
			await message.channel.send(payload)
			time.sleep(random.choice(range(5)))
			payload = '`[+] weapons lock confirmed.`'
			await message.channel.send(payload)
			time.sleep(1)
			payload = '`[!] selecting exploit to launch at target...`'
			await message.channel.send(payload)
			time.sleep(random.choice(range(5)))
			payload = '`[+] CVE selected.`'
			await message.channel.send(payload)
			time.sleep(1)
			payload = '`[+] launching selection {} at target`'.format(random_cve)
			await message.channel.send(payload)
			time.sleep(1)
			payload = '`[+] communications established.`'
			await message.channel.send(payload)
			time.sleep(1)
			payload = '`[+] going dark, transitioning to black ops protocol.`'
			await message.channel.send(payload)



		else:
			try:
				payload = gastonbot(parsedEvent)
			except:
				payload = None

			if not payload:
				return
			
			if payload != None:
				await message.channel.send(payload)




client.run(TOKEN, bot=True)
print('[{}] bot loaded and running!'.format(BOTNAME.replace('@','')))