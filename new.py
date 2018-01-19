import time
import random

import matplotlib.pyplot as plt
import telepot

def makeplot():
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	y = []
	y2 = []
	for i in x:
		y.append(random.randint(0,10))
		y2.append(random.randint(0,10))
	plt.plot(x, y, x, y2)
	try:
		plt.savefig('kuva.png', bbox_inches='tight')
	except Exception:
		print("Creating the picture failed")
		
		
def handler(msg):
	try:
		chat_id = msg['chat']['id']
		if msg['text'].lower().find('edistyyk') + 1:
			print('Chat command issued')
			bot.sendMessage(
				chat_id,
				'No ei!',
				reply_to_message_id=msg['message_id']
			)
		elif msg['text'].lower().find('toimiiko') + 1:
			print('Chat command issued')
			bot.sendMessage(
					chat_id,
					'Onhan tuo mahdollista.',
					reply_to_message_id=msg['message_id']
			)
		elif msg['text'].lower().find('plot') + 1:
			print('Plot command issued')
			makeplot()
			with open('kuva.png', 'rb') as img:
				bot.sendPhoto(
					chat_id,
					img,					
					reply_to_message_id=msg['message_id']
				)
					
	except Exception:
		pass
		

#Finds the token.
with open('/opt/secrets/token.txt', 'r') as t:
    data = t.read().split()
    token = data[data.index('token') + 1]

#Takes the token as a parameter.
bot = telepot.Bot(token)
bot.message_loop(handler)

while 1:
	time.sleep(10)
