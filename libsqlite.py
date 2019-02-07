import json
import sqlite3
import random
import string

def get(dic):
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	result = cursor.execute('select * from ' + dic['table'] + ' where id == ?', [dic['id']])
	items = []
	for row in result:
		item = dict(zip([d[0] for d in cursor.description], row))
		items.append(item)
	connection.close()
	return items
	
def add(dic):
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	table = dic.pop('table')
	values = prepare_values(dic.values())
	keys = ', '.join(dic.keys())
	print('insert into ' + table + ' (' + keys + ') values (' + values + ')')
	cursor.execute('insert into ' + table + ' (' + keys + ') values (' + values + ')')
	connection.commit()
	connection.close()
	return None
	
def delete(dic):
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	cursor.execute('delete from ' + dic['table'] + ' where id == ?', [dic['id']])
	connection.commit()
	return None
	
def list(dic):
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	result = cursor.execute('select * from ' + dic['table'])
	items = []
	for row in result:
		item = dict(zip([d[0] for d in cursor.description], row))
		items.append(item)
	connection.close()
	return items
	
def generate_id(dic):
	rand = ''
	for i in range(10):
		rand = rand + random.choice(string.ascii_letters)
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	cursor.execute('select * from ' + dic['table'] + ' where id = ?', [rand])
	if cursor.rowcount == -1:
		connection.close()
		return rand
	else:
		connection.close()
		return generate_id(dic)
		
def generate_token(dic):
	rand = ''
	for i in range(20):
		rand = rand + random.choice(string.ascii_letters)
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	cursor.execute('select * from ' + dic['table'] + ' where token = ?', [rand])
	if cursor.rowcount == -1:
		connection.close()
		return rand
	else:
		connection.close()
		return generate_token(dic)
		
def prepare_values(vals):
	if vals == None or len(vals) == 0:
		return None
	result = ''
	for v in vals:
		if result == '':
			result = '\'' + str(v) + '\''
		else:
			result = result + ', ' + '\'' + str(v) + '\''
	return result
	