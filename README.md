# RedFlaskNotes

[![N|Solid](https://redis.io/images/redis-white.png) ](https://redis.io/) [![N|Solid](http://flask.pocoo.org/static/logo.png)](http://flask.pocoo.org/))

###  RedFlaskNotes is your Redis & Flask powered notes keeper.

### How to use

RedFlaskNotes requires [Docker & Docker-compose](https://docs.docker.com/) to run.

### Setup

Clone the repository: 
```sh
$ git clone https://github.com/ms-dev-pro/redflasknotes.git  
```

Launch the docker environment:

```sh
$ cd redflasknotes
$ docker-compose up --build
```

### Functionnalities available

Here are the availables routes that you can call with curl (or softwares like [Insomnia](https://insomnia.rest/) or [Postman](https://www.getpostman.com/)) :

| Function | curl command |
| ------ | ------ |
| **Welcome message** | *curl http://localhost:8080* |
| **List all notes** | *curl http://localhost:8080/notes* |
| **Delete all notes** | *curl -X DELETE http://localhost:8080/notes* |
| **Add one note** | *curl --request POST  --url http://localhost:8080/notes  --header 'content-type: application/json' --data '{"content": "My note content",": "Author name","datedecreation": "2019-04-16T12:35:43.511Z"}'* |
| **Get one note** | *curl http://localhost:8080/notes/idnote*  |
| **Delete one note** |  *curl -X DELETE http://localhost:8080/notes/idnote*|


### About the app
 - The server runs on **localhost** on the port **8080**.
 - It is written in Python 3 syntax.
 - It requires **flask** and **redis** packages as seen in *requirements.txt*.
##### Handling errors

Here are some of the errors that the app handles:
 - Get all notes on empty set
 - Get specific note with wrong id
 - Delete specific note with wrong id


