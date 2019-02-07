# photos
An example of simple rest-like python api for apps and web that allows users to share photos in personal chats. 

# available methods
All query and post parameters are string.
## related to users
### /photos/add/
Send new photo to chat. Use post request. Required query parameters are `token` is a user private token, `chat_id` is an id of chat to send photo to. Requeired post parameter is `photo` is a base64 string, should be send as xxx-form-url-encoded field.
### /photos/delete/
### /photos/get/
### /photos/file/
### /photos/all/
### /chats/add/
### /chats/delete/
### /chats/all/
### /users/add/
### /users/get/
### /users/all/
### /users/auth/
