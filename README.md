# photos
An example of simple rest-like python api for apps and web that allows users to share photos in personal chats. 

# available methods
All query and post parameters are string.
## related to photos
### /photos/add/
Send new photo to chat. Use post request. Required query parameters are `token` is a user private token, `chat_id` is an id of chat to send photo to. Requeired post parameter is [`photo`](#token) is a base64 string, should be send as xxx-form-url-encoded field.
### /photos/delete/
### /photos/get/
### /photos/file/
### /photos/all/
## related to chats
### /chats/add/
### /chats/delete/
### /chats/all/
## related to users
### /users/add/
### /users/get/
### /users/all/
### /users/auth/
## parameters
### token
Is user private token. You can get a token by `/users/auth/`. Most of the methods requires this token to disallow users to acces other users private data.
### chat_id
Is an unique id of chat between two users. 
### photo_id
Is an unique id of photo previously sent to server by `/photos/add/`.
### user_id
An unique id of user.
