# GrandPy Bot

## **App information**
This is a chatbot app that will help you find addresses and map locations.
It will also provide you a small anecdote connected to the address, and a link to wikipedia for further information.

Here are some examples of question you can ask him/her (questions must be provided in French):
* Quelle est l'adresse de la mairie de Lyon ?
* Où se situe la Tour Eiffel ?
* Où est la Cathédrale de Nantes ?

This project uses the Google Geocoding API and Geosearch Wikipedia API.

![example](https://github.com/bientavu/grandpybot/blob/main/website/static/images/example.png?raw=true)

## **LocalHost**
To run on localhost:
1. Run `pipenv install`
2. Rename '.env.example' to '.env' and put your API keys inside
3. Run `flask run`
4. The app is now accessible with your localhost address (given by flask)

## **Live version**
Live version available: https://grandpybot-axel.herokuapp.com/
