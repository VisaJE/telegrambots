import time

import telepot


def handler(msg):
	try:
		chat_id = msg['chat']['id']
		if msg['text'].lower().find('edistyykö') + 1:
    
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
		#Takes the token as a parameter.
bot = telepot.Bot('540750088:AAGLEDAgYHG_aIqWSoneVGy6d7SlyJ1c3bY')
bot.message_loop(handler)

while 1:
	time.sleep(10)