from bs4 import BeautifulSoup
import requests

'''def standings():
	string="# Team Pl W D L F A GD Pts\n"
	count=0

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			if "Team" not in a:
				string+=f"{a}\n"

	return string'''

def laliga_ranking():

	URL="https://www.skysports.com/la-liga-table"
	#URL="https://www.skysports.com/premier-league-table"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	string=""
	count=0

	example="1  Atletico Madrid  18 15 2 1 36 8 28 47"
	example="1  Atletico Madrid  47 18 15 2 1"

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			string+=f"{a}\n"

	d=string.splitlines()
	res="<b># Team P W D L Pts</b>\n"
	for e in d:
		r=e.split()
		r.pop(-2)
		r.pop(-2)
		r.pop(-2)
		

		t = ' '.join(r)
		if "Team" not in t:
			res+=f"{t}\n"
	return res

def apl_ranking():

	URL="https://www.skysports.com/premier-league-table"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	string=""
	count=0

	example="1  Atletico Madrid  18 15 2 1 36 8 28 47"
	example="1  Atletico Madrid  47 18 15 2 1"

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			string+=f"{a}\n"

	d=string.splitlines()
	res="<b># Team P W D L Pts</b>\n"
	for e in d:
		r=e.split()
		r.pop(-2)
		r.pop(-2)
		r.pop(-2)
		

		t = ' '.join(r)
		if "Team" not in t:
			res+=f"{t}\n"
	return res

def italy_ranking():

	URL="https://www.skysports.com/serie-a-table"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	string=""
	count=0

	example="1  Atletico Madrid  18 15 2 1 36 8 28 47"
	example="1  Atletico Madrid  47 18 15 2 1"

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			string+=f"{a}\n"

	d=string.splitlines()
	res="<b># Team P W D L Pts</b>\n"
	for e in d:
		r=e.split()
		r.pop(-2)
		r.pop(-2)
		r.pop(-2)
		

		t = ' '.join(r)
		if "Team" not in t:
			res+=f"{t}\n"
	return res

def bundesliga_ranking():

	URL="https://www.skysports.com/bundesliga-table"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	string=""
	count=0

	example="1  Atletico Madrid  18 15 2 1 36 8 28 47"
	example="1  Atletico Madrid  47 18 15 2 1"

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			string+=f"{a}\n"

	d=string.splitlines()
	res="<b># Team P W D L Pts</b>\n"
	for e in d:
		r=e.split()
		r.pop(-2)
		r.pop(-2)
		r.pop(-2)
		

		t = ' '.join(r)
		if "Team" not in t:
			res+=f"{t}\n"
	return res

def france_ranking():

	URL="https://www.skysports.com/ligue-1-table"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	string=""
	count=0

	example="1  Atletico Madrid  18 15 2 1 36 8 28 47"
	example="1  Atletico Madrid  47 18 15 2 1"

	for i in soup.find_all('tr'):
		#count+=1
		text=i.getText()
		if count!=10:
			a=(i.text.replace('\n', ' ').strip())
			string+=f"{a}\n"

	d=string.splitlines()
	res="<b># Team P W D L Pts</b>\n"
	for e in d:
		r=e.split()
		r.pop(-2)
		r.pop(-2)
		r.pop(-2)
		

		t = ' '.join(r)
		if "Team" not in t:
			res+=f"{t}\n"
	return res