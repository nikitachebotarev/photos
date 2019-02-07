import os
import random
import string

def save_bytes(bytes, name):
	file = open(name, 'wb')
	file.write(bytes)
	file.close()
	
def delete(name):
	os.remove(name)
	
def get(name):
	file = open(name, 'rb')
	bytes = file.read()
	file.close()
	return bytes
	
def generate_name():
	rand = ''
	for i in range(30):
		rand = rand + random.choice(string.ascii_letters)
	return rand
	