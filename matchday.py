from bs4 import BeautifulSoup
import requests


def matchday_laliga():
	URL="https://en.as.com/resultados/futbol/primera/jornada/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	t=soup.find('span', class_='tit-jornada')
	result=f"<b>{t.text}</b>\n"

	string=""
	count=0

	for i in soup.find_all('li', class_='list-resultado'):
		#count+=1
		text=i.getText()

		a=(i.text.replace('\n', ' ').strip())

		string+=f"{a}\n"

	p=string.splitlines()
	for b in p:
		o=b.split()
		u = ' '.join(o)
		result+=f"{u}\n"

	return result

def matchday_apl():
	URL="https://en.as.com/resultados/futbol/inglaterra/jornada/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	t=soup.find('span', class_='tit-jornada')
	result=f"<b>{t.text}</b>\n"

	string=""
	count=0

	for i in soup.find_all('li', class_='list-resultado'):
		#count+=1
		text=i.getText()

		a=(i.text.replace('\n', ' ').strip())

		string+=f"{a}\n"

	p=string.splitlines()
	for b in p:
		o=b.split()
		u = ' '.join(o)
		result+=f"{u}\n"

	return result

def matchday_italy():
	URL="https://en.as.com/resultados/futbol/italia/jornada/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	t=soup.find('span', class_='tit-jornada')
	result=f"<b>{t.text}</b>\n"

	string=""
	count=0

	for i in soup.find_all('li', class_='list-resultado'):
		#count+=1
		text=i.getText()

		a=(i.text.replace('\n', ' ').strip())

		string+=f"{a}\n"

	p=string.splitlines()
	for b in p:
		o=b.split()
		u = ' '.join(o)
		result+=f"{u}\n"

	return result

def matchday_france():
	URL="https://en.as.com/resultados/futbol/francia/jornada/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	t=soup.find('span', class_='tit-jornada')
	result=f"<b>{t.text}</b>\n"

	string=""
	count=0

	for i in soup.find_all('li', class_='list-resultado'):
		#count+=1
		text=i.getText()

		a=(i.text.replace('\n', ' ').strip())

		string+=f"{a}\n"

	p=string.splitlines()
	for b in p:
		o=b.split()
		u = ' '.join(o)
		result+=f"{u}\n"

	return result

def matchday_bundesliga():
	URL="https://en.as.com/resultados/futbol/alemania/jornada/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	t=soup.find('span', class_='tit-jornada')
	result=f"<b>{t.text}</b>\n"

	string=""
	count=0

	for i in soup.find_all('li', class_='list-resultado'):
		#count+=1
		text=i.getText()

		a=(i.text.replace('\n', ' ').strip())

		string+=f"{a}\n"

	p=string.splitlines()
	for b in p:
		o=b.split()
		u = ' '.join(o)
		result+=f"{u}\n"

	return result