import json
import libadapter as adp
import usecases as use

def add_photo(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'chat_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	not_exist_param = adp.check_params_exist(posts, ['photo'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.add_photo(token = parameters['token'], chat_id = parameters['chat_id'], base64 = posts['photo'])
	return res
	
def delete_photo(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'photo_id', 'chat_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.delete_photo(token = parameters['token'], photo_id = parameters['photo_id'], chat_id = parameters['chat_id'])
	return res
	
def get_photo(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'photo_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.get_photo(token = parameters['token'], photo_id = parameters['photo_id'])
	return res
	
def all_photos(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'chat_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.all_photos(token = parameters['token'], chat_id = parameters['chat_id'])
	return res
	
def get_file(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'photo_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.get_file(token = parameters['token'], photo_id = parameters['photo_id'])
	return res
	
def add_chat(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'second_user_id', 'chat_name'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.add_chat(token = parameters['token'], second_user_id = parameters['second_user_id'], chat_name = parameters['chat_name'])
	return res	
	
def delete_chat(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token', 'chat_id'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.delete_chat(token = parameters['token'], chat_id = parameters['chat_id'])
	return res
	
def all_chats(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.all_chats(token = parameters['token']	)
	return res
	
def get_token(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['name', 'password'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.get_token(name = parameters['name'], password = parameters['password'])
	return res
	
def add_user(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['name', 'password'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.add_user(name = parameters['name'], password = parameters['password'])
	return res

def get_user(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.get_user(parameters['token'])
	return res
		
def all_users(parameters, posts):
	not_exist_param = adp.check_params_exist(parameters, ['token'])
	if not_exist_param != None:
		return {'result':'1', 'error':not_exist_param + ' parameter not send'}
		
	res = use.all_users(parameters['token'])
	return res
