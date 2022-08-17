from bs4 import BeautifulSoup
import requests

#LIVE MATCHES
def live_scores():
	URL="http://www.livescore.cz/?s=2"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	result=""

	all_games = []

	for child in soup.find_all('div', {"id":"score-data"})[0].children:
		result+=f"{child.text}\n"

	#result = result.replace('\n', ' |')

	

	return result

	

#ALL MATCHES
def line_scores():
	URL="http://www.livescore.cz/?d=0&s=1"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	result=""

	all_games = []

	for child in soup.find_all('div', {"id":"score-data"})[0].children:
		result+=f"{child.text}\n"

	#result = result.replace('\n', ' |')

	

	return result