from flask import Flask, request, Response
from redis import Redis
import uuid
import json

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def mainRoute():
	return handleResponse(200, 'text/plain', 'Bienvenue sur le gestionnaire de note RedFlask! \n (Redis & Flask API server)')

@app.route('/notes', methods = ['GET', 'POST', 'DELETE'])
def noteInteraction():
	if request.method == 'GET':
		notes = redis.hgetall("notes")
		if(notes):
			return handleResponse(200, "application/json", noteDictFormat(notes))
		else:
			return handleErrors(404, "noNotesDictionnary")
		return 

	if request.method == 'POST':
		note_uuid = str(uuid.uuid4())
		redis.hset("notes", note_uuid, request.data)
		return handleResponse(201, "text/plain", "La note {} a bien été créée.".format(note_uuid))

	if request.method == 'DELETE':
		redis.delete("notes")
		return handleResponse(200, "text/plain", "Toutes les notes ont bien été supprimées.")

@app.route('/notes/<idnote>', methods=['GET', 'DELETE'])
def specificNoteInteraction(idnote):
	if(redis.hexists("notes", idnote)):
		if request.method == 'GET':
			return handleResponse(200, "application/json", redis.hget("notes", idnote))
		if request.method == 'DELETE':
			redis.hdel("notes", idnote)
			return handleResponse(200, "text/plain", "La note {} a bien été supprimée.".format(idnote))
	else:
		return handleErrors(404, "noNoteWithThisId")

def noteDictFormat(dict):
	for key, value in dict.items():
		try:
			dict[key] = json.loads(value)
		except ValueError:
			print("La note {} est au mauvais format dans la base de données.".format(key))
	return json.dumps(dict)


def handleErrors(statuscode, errorCode):
	switcher = {
		"noNotesDictionnary": "Vous n'avez aucune note pour l'instant.",
		"noNoteWithThisId": "Il n'existe aucune note avec cet identifiant.",
	}
	content = switcher.get(errorCode, "Wrong errorCode")
	return(handleResponse(statuscode, 'text/plain', content))

def handleResponse(statuscode, mimeType, content):
	return Response(content, status=statuscode, mimetype=mimeType)
		

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)
