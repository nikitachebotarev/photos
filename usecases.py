import base64 as decoder

import libsqlite as sql
import libfile as fil

def add_photo(token, chat_id, base64):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	chat = get_chat_by_id(chat_id)
	if chat == None:
		return {'result':'1', 'error':'no such chat'}
		
	user = get_user_by_token(token)
	if chat['first_user_id'] != user['id'] and chat['second_user_id'] != user['id']:
		return {'result':'1', 'error':'user is not a chat member'}
		
	name = fil.generate_name()
	bytes = decoder.decodebytes(base64.encode())
	fil.save_bytes(bytes, 'content/' + name)
	sql.add({'table':'photos', 'id':sql.generate_id({'table':'photos'}), 'chat_id':chat_id, 'file':name})
	return {'result':'0'}
	
def delete_photo(token, chat_id, photo_id):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	chat = get_chat_by_id(chat_id)
	if chat == None:
		return {'result':'1', 'error':'no such chat'}
		
	user = get_user_by_token(token)
	if chat['first_user_id'] != user['id'] and chat['second_user_id'] != user['id']:
		return {'result':'1', 'error':'user is not a chat member'}
	
	photo = get_photo_by_id(photo_id)
	fil.delete(photo['name'])
	
	sql.delete({'table':'photos', 'id':photo_id})
	return {'result':'0'}
	
def get_photo(token, photo_id):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	photo = get_photo_by_id(photo_id)
	if photo == None:
		return {'result':'1', 'error':'no such photo'}
	
	chat = get_chat_by_id(photo['chat_id'])
	if chat == None:
		return {'result':'1', 'error':'photo can\'t be get'}
	
	user = get_user_by_token(token)
	if user['id'] != chat['first_user_id'] and user['id'] != chat['second_user_id']:
		return {'result':'1', 'error':'user is not a member of chat contains this photo'}
		
	photo = sql.get({'table':'photos', 'id':photo_id})
	return {'result':'0', 'data':photo}
	
def get_file(token, photo_id):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	photo = get_photo_by_id(photo_id)
	if photo == None:
		return {'result':'1', 'error':'no such photo'}
	
	chat = get_chat_by_id(photo['chat_id'])
	if chat == None:
		return {'result':'1', 'error':'photo can\'t be get'}
	
	user = get_user_by_token(token)
	if user['id'] != chat['first_user_id'] and user['id'] != chat['second_user_id']:
		return {'result':'1', 'error':'user is not a member of chat contains this photo'}
		
	photo = sql.get({'table':'photos', 'id':photo_id})
	bytes = fil.get('content/' + photo[0]['file'])
	return{'result':'0', 'image':bytes}
	
def all_photos(token, chat_id):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	chat = get_chat_by_id(chat_id)
	if chat == None:
		return {'result':'1', 'error':'no such chat'}
	
	user = get_user_by_token(token)
	if user['id'] != chat['first_user_id'] and user['id'] != chat['second_user_id']:
		return {'result':'1', 'error':'user is not a member of chat'}
	
	selected = []
	photos = sql.list({'table':'photos'})
	for p in photos:
		if p['chat_id'] == chat_id:
			selected.append(p)
	return {'result':'1', 'error':selected}
			
def add_chat(token, second_user_id, chat_name):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	second_user = get_user_by_id(second_user_id)
	if second_user == None:
		return {'result':'1', 'error':'no user with id ' + second_user_id}
		
	first_user = get_user_by_token(token)
	sql.add({'table':'chats',  'id':sql.generate_id({'table':'chats'}),  'first_user_id':first_user['id'], 'second_user_id':second_user_id, 'chat_name':chat_name})
	return {'result':'0'}
	
def delete_chat(token, chat_id):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	chat = get_chat_by_id(chat_id)
	if chat == None:
		return {'result':'1', 'error':'no such chat'}
		
	user = get_user_by_token(token)
	if chat['first_user_id'] != user['id'] and chat['second_user_id'] != user['id']:
		return {'result':'1', 'error':'user is not a chat member'}
		
	sql.delete({'table':'chat', 'id':chat})
	return {'result':'0'}
	
def all_chats(token):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	user = get_user_by_token(token)
	chats = sql.list({'table':'chats'})
	user_chats = []
	for c in chats:
		if c['first_user_id'] == user['id'] or c['second_user_id'] == user['id']:
			user_chats.append(c)
			
	return {'result':'0', 'data':user_chats}
	
def get_token(name, password):
	users = sql.list({'table':'users'})
	user = None
	for u in users:
		if u['name'] == name and u['pass'] == password:
			user = u
			break
			
	if user == None:
		return {'result':'1', 'error':'no user with such name and pass'}
		
	return {'result':'0', 'token':user['token']}
	
def add_user(name, password):
	sql.add({'table':'users', 'id':sql.generate_id({'table':'users'}), 'name':name, 'pass':password, 'token':sql.generate_token({'table':'users'})})
	return {'result':'0'}
	
def all_users(token):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
		
	users = sql.list({'table':'users'})
	filtered = []
	for u in users:
		u.pop('token') 
		u.pop('pass')
		filtered.append(u)
	
	return {'result':'0', 'data':filtered}
	
def get_user(token):
	if not is_user_exist(token):
		return {'result':'1', 'error':'no such user'}
	
	user = get_user_by_token(token)
	user.pop('token') 
	users.pop('pass')
	return {'result':'0', 'data':user}
				
def is_user_exist(token):
	users = sql.list({'table':'users'})
	for u in users:
		if u['token'] == token:
			return True
	return False
	
def get_user_by_token(token):
	users = sql.list({'table':'users'})
	for u in users:
		if u['token'] == token:
			return u
	return None
	
def get_user_by_id(id):
	users = sql.list({'table':'users'})
	for u in users:
		if u['id'] == id:
			return u
	return None
	
def get_chat_by_id(id):
	chats = sql.list({'table':'chats'})
	for c in chats:
		if c['id'] == id:
			return c
	return None
	
def get_photo_by_id(id):
	photos = sql.list({'table':'photos'})
	for p in photos:
		if p['id'] == id:
			return p
	return None
	