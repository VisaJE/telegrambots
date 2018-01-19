import time

import telepot


def handler(msg):
	try:
		chat_id = msg['chat']['id']
		if msg['text'].lower().find('edistyyk') + 1:
    
			bot.sendMessage(
				chat_id,
				'No ei!',
				reply_to_message_id=msg['message_id']
			)
		elif msg['text'].lower().find('toimiiko') + 1:
			bot.sendMessage(
					chat_id,
					'Onhan tuo mahdollista.',
					reply_to_message_id=msg['message_id']
			)
	except Exception:
		time.sleep(10)
#Finds the token.
with open('/opt/secrets/token.txt', 'r') as t:
    data = t.read().split()
    token = data[data.index('token') + 1]
    print('Finding the token was a great success.')
#Takes the token as a parameter.
try:
    bot = telepot.Bot(token)
    bot.message_loop(handler)
except Exception:
    print('Epic fail.')
while 1:
	time.sleep(100)
