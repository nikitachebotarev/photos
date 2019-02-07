import time
import urllib
import json
import traceback

import libadapter
import adapters

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.on_method()
		
	def do_POST(self):
		self.on_method()
	
	def on_method(self):
		print('have some request')
		path_without_query = self.path[:self.path.rfind('/') + 1]
		parameters = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
		print('initial parameters->')
		print(parameters)
	
		for key in parameters.keys():
			if isinstance(parameters[key], list):
				parameters[key] = parameters[key][0]
				
		for key in parameters.keys():
			try:
				parameters[key] = str(parameters[key], 'utf-8')
			except:
				pass
		
		temp = {}
		for key in parameters.keys():
			try:
				temp[str(key, 'utf-8')] = parameters[key]
			except:
				pass
		paramaeters = temp
				
		length_header = self.headers.get('content-length')
		posts = None
		if length_header != None:
			length = int(self.headers.get('content-length'))
			posts = urllib.parse.parse_qs(self.rfile.read(length))
			print('initial posts->')
			print(posts)
			
			for key in posts.keys():
				if isinstance(posts[key], list):
					posts[key] = posts[key][0]
			
			for key in posts.keys():
				try:
					posts[key] = str(posts[key], 'utf-8')
				except:
					pass
			
			temp = {}
			for key in posts.keys():
				try:
					temp[str(key, 'utf-8')] = posts[key]
				except:
					pass
			posts = temp
		
		print('path->')
		print(path_without_query)
		print('processed queries->')
		print(parameters)
		print('processed posts->')
		print(posts)
		
		try:
			result = self.on_method_with_parameters(path_without_query, parameters, posts)
			self.return_response(result)
		except Exception as e:
			print('exception->')
			print(e)
			self.return_response_unspecified_error(e)

	def on_method_with_parameters(self, path, parameters, posts):
		if path == '/photos/add/':
			return adapters.add_photo(parameters, posts)
		elif path == '/photos/delete/':
			return adapters.delete_photo( parameters, posts)
		elif path == '/photos/get/':
			return adapters.get_photo(parameters, posts)
		elif path == '/photos/file/':
			return adapters.get_file(parameters, posts)
		elif path == '/photos/all/':
			return adapters.all_photos(parameters, posts)
		elif path == '/chats/add/':
			return adapters.add_chat(parameters, posts)
		elif path == '/chats/delete/':
			return adapters.delete_chat(parameters, posts)
		elif path == '/chats/all/':
			return adapters.all_chats(parameters, posts)
		elif path == '/users/auth/':
			return adapters.get_token(parameters, posts)
		elif path == '/users/add/':
			return adapters.add_user(parameters, posts)
		elif path == '/users/all/':
			return adapters.all_users(parameters, posts)
		elif path == '/users/get/':
			return adapters.get_user(parameters, posts)
		else:
			return {'result':'1', 'error':'no such method ' + path}
			
	def return_response(http_message, dic):
		if 'image' in dic.keys():
			http_message.return_response_image(dic)
			return
		if dic['result'] == 0:
			http_message.send_response(200)
		else: 
			http_message.send_response(400)
		http_message.send_header('Content-type', 'text/json; charset=utf-8')
		http_message.end_headers()
		jsn = json.dumps(dic, ensure_ascii = False)
		response = bytes(jsn, 'UTF-8')
		http_message.wfile.write(response)	
		
	def return_response_image(http_message, dic):
		img_size = len(dic['image'])
		http_message.send_response(200)
		http_message.send_header("Content-type", "image/jpg")
		http_message.send_header("Content-length", img_size)
		http_message.end_headers()
		http_message.wfile.write(dic['image'])	
		
	def return_response_unspecified_error(http_message, exception):
		http_message.send_response(500)
		http_message.send_header('Content-type', 'text/json; charset=utf-8')
		http_message.end_headers()
		jsn = json.dumps({'result':'1', 'error':'error while executing method', 'details':traceback.format_exc()}, ensure_ascii = False)
		response = bytes(jsn, 'UTF-8')
		http_message.wfile.write(response)
	
def main():
	server_class = HTTPServer
	httpd = server_class(('0.0.0.0', 8080), MyHandler)
	print(time.asctime(), 'Server Starts - %s:%s' % ('localhost', '9000'))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), 'Server Stops - %s:%s' % ('localhost', '9000'))
		
if __name__ == '__main__':
	main()