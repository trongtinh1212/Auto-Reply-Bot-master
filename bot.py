# This Python file uses the following encoding: utf-8
import os, sys
from fbchat import Client
from fbchat.models import *
from config import *
import time

class AutoReplyBot(Client):
	def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):

		if author_id != self.uid and thread_type == ThreadType.USER:
			messages = client.fetchThreadMessages(thread_id, limit=30)

			for i in range(0, len(messages)):
				if(messages[i].author == self.uid):
					lastmessage = messages[i]
					break
			if 'lastmessage' in locals():
				away = (int(time.time() - (int(lastmessage.timestamp))/1000)/60)
				if(away >= 5):
					self.sendMessage(" Đây là tin nhắn tự động, hiện tại tui đang offline, vui lòng để lại lời nhắn ạ ", thread_id=thread_id, thread_type=thread_type) 
					self.sendMessage(" Tui sẽ reply trong thời gian sớm nhất <3 😂.", thread_id=thread_id, thread_type=thread_type)
					self.sendRemoteImage('https://i.imgur.com/GjUMhvs.png', thread_id=thread_id, thread_type=thread_type)
			else:
					self.sendMessage(" Tui đang offline mà, để lại lời nhắn tui sẽ rep sau nhaa 😂. ", thread_id=thread_id, thread_type=thread_type)
					self.sendRemoteImage('https://i.imgur.com/8PO4XTz.png', thread_id=thread_id, thread_type=thread_type)
client = AutoReplyBot(username, password)
client.listen()