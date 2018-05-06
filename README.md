# Coding Exercise
---

**A small web site that clones Reddit features allows users to target a topic content Upvote & Downvote**

---

## [Demo](https://whispering-wave-74397.herokuapp.com/)


# Description

This project including two parts, one is written by Reactjs front-end UI, 
and the other is the Python Flask backend API

---

First look at the Reactjs part, I use the official [create-react-app](https://github.com/facebook/create-react-app) to generate the basic react code. 

 
 Including:
 	
 	- public/*
 	- src/*
	- package.json
	- package-lock.json

I only have modified `/src/pages/index.js` to complete this challenage.
Finally I put the built static files into the Flask project, through the flask to host these files. 

Built dest is:

	- /web_api/static/*

This is the way I think of the simplest host static files on Heroku

---


And then we can look at the Python flask part.

Including:

	- /web_api/*

A few important files are outlined below:

- `/web_api/__init__.py`
	- The main entry point of the flask is in `/web_api/__init__.py`.
- `/web_api/topics`
	- I put api view functions into this package and used blueprint to mount them that can make structrue clearly.
- `/web_api/tests`
    - e2e testing of API endpoint
  
In the most important data section, I designed a data class which is in `/web_api/data_source.py` to new a global data object that was written into the memory when Flask init. And I also designed a similar ORM architecture to access this data conveniently. Condition of topic length rules, and sorting methods are implemented here. If API view want to modifie data of topic just call model manager's function it's easy to do this.

You can see how I implement this from these files:

	- /web_api/topics/models.py
	- /web_api/topics/managers.py
	- /web_api/utils/base_manager.py

---


# Requirements

 - Front-End
   - `NodeJS: v8.9.1`
 	- `NPM: v5.5.1`
 - Backend
 	- `Python: 3.6.4`
 	- `Pipenv: 11.10.1`



# Installation

Install Python packages from pipfile

```shell
  $ pipenv install --dev
```

# Quick start


## Run

```shell
  $ FLASK_APP=web_api flask run --debugger --reload
```

*Once you’ve started web server using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:5000 (if you are running locally). Then you should be greeted with something*


# Testing

You can execute `nosetests` through the following command

```shell
  $ nosetests --verbose
```

---

# How to run ReactJS dev server?

Install node modules

```shell
  $ npm install
```

Run ReactJS dev server

```shell
  $ npm run start
```

# Build static file


```shell
  $ npm run build
```
---
# HTTP API Docs

### Get Topics
	
	
Path
	
	/topics

Method
	
	GET
	
Headers 
	
	Content-Type: application/json
	
Response body
	
	 200
	 [
	 	{
	 		"id": 1,
	 		"content": "We have a Hulk",
	 		"upvote": 0,
	 		"downvote": 0,
	 		"ctime": "2018-05-06 15:24:56.771106",
	 		"result":0
	 	}
	 ]
	 

### Create Topic
	
	
Path
	
	/topics

Method
	
	POST
	
Headers 
	
	Content-Type: application/json
	
Response Body

	{
		"content": "You'll Never Know"
	}
	
Response Body
	
	200
 	{
   		"id": 2,
    	"content": "FooooooBarrrrrr",
    	"upvote": 0,
    	"downvote": 0,
    	"ctime": "2018-05-06 07:51:38.162173"
 		"result":0
 	}
 	
 	400
 	{
 		"message": "Must have content"
 	}
 	
 	400
 	{
 		"message": "Content exceed 255 characters"
 	}
	 
### Update Topic by action
	
	
Path
	
	/topics/{topic_id}/action/{action_id}
	
Enum of action_id

	UPVOTE = 1
	DOWNVOTE = 2

Method
	
	PUT
	
Headers 
	
	Content-Type: application/json
	
Response Body
	
	200
 	{
   		"id": 2,
    	"content": "FooooooBarrrrrr",
    	"upvote": 6,
    	"downvote": 2,
    	"ctime": "2018-05-06 07:51:38.162173"
 		"result":4
 	}
 	
 	400
 	{
 		"message": "No such action_id. Must be `1` or `2`"
 	}
 	
 	400
 	{
 		"message": "No such topic id"
 	}
	  
	

