import json

def log_to_json(type, message):
	file = open('logs.json', 'a')
	file.write(json.dumps({'type':type, 'message':message}) + ',\n')
	file.close()
	