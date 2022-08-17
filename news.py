from bs4 import BeautifulSoup
import requests

def apl_news():
	URL = "https://www.espn.com/soccer/league/_/name/eng.1"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	d=soup.find_all('a', class_='realStory')

	news=""

	for i in d:
		title = i.getText()
		l = i.get("href")
		link="https://www.espn.com"+l
		news+=f'🔘 <a href="{link}">{title}</a>\n'
		#news+=f"{link}\n\n"

	return news

def laliga_news():
	URL = "https://www.espn.com/soccer/league/_/name/esp.1"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	d=soup.find_all('a', class_='realStory')

	news=""

	for i in d:
		title = i.getText()
		l = i.get("href")
		link="https://www.espn.com"+l
		news+=f'<a href="{link}">{title}</a>\n\n'

	return news

def italy_news():
	URL = "https://www.espn.com/soccer/league/_/name/ita.1/"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	d=soup.find_all('a', class_='realStory')

	news=""

	for i in d:
		title = i.getText()
		l = i.get("href")
		link="https://www.espn.com"+l
		news+=f'<a href="{link}">{title}</a>\n\n'

	return news

def france_news():
	URL = "https://www.espn.com/soccer/league/_/name/fra.1"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	d=soup.find_all('a', class_='realStory')

	news=""

	for i in d:
		title = i.getText()
		l = i.get("href")
		link="https://www.espn.com"+l
		news+=f'<a href="{link}">{title}</a>\n\n'

	return news

def bundesliga_news():
	URL = "https://www.espn.com/soccer/league/_/name/ger.1"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	d=soup.find_all('a', class_='realStory')

	news=""

	for i in d:
		title = i.getText()
		l = i.get("href")
		link="https://www.espn.com"+l
		news+=f'<a href="{link}">{title}</a>\n\n'

	return news

#print(bundesliga_news())