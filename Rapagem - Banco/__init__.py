from Model.Series import Series
import requests
import json
from bs4 import BeautifulSoup, ResultSet

results = requests.get('https://www.imdb.com/search/title/?title_type=tv_series&release_date=1980-01-01,2019-12-31&user_rating=,'
    '10.0&count=250')

soup = BeautifulSoup(results.text, 'html.parser')
title = soup.findAll('h3', class_='lister-item-header')
title = BeautifulSoup(str(title), 'html.parser').findAll('a')
title_s = soup.findAll('h3', class_='lister-item-header')
title_s = BeautifulSoup(str(title), 'html.parser').findAll('a')
notes = soup.findAll('div', class_='inline-block ratings-imdb-rating')
notes = BeautifulSoup(str(notes), 'html.parser').findAll('strong')
year = soup.findAll('h3', class_='lister-item-header')
year = BeautifulSoup(str(year), 'html.parser').findAll('span', class_='lister-item-year text-muted unbold')
genre = soup.findAll('p', class_='text-muted')
genre = BeautifulSoup(str(genre), 'html.parser').findAll('span', class_='genre')
genre_s = soup.findAll('p', class_='text-muted')
genre_s = BeautifulSoup(str(genre), 'html.parser').findAll('span', class_='genre')

auth = ('couchdb', 'couchdb')

counter = 0
for t in title:
    s = Series(t.text.replace("'", ""), t.text.replace("'", "").upper(), float(notes[counter].text),
               genre[counter].text.replace("\n", "").strip(), genre_s[counter].text.replace("\n", "").strip().upper(),
               int(year[counter].text.replace("I" ,"").replace("(","").replace(" " , "").replace(")","").replace("–","")[0:4]))
    print(s.__dict__)
    r = requests.post('http://localhost:5984/series', json=json.loads(str(s.__dict__).replace("'", "\"")), auth=auth)
    print(str(r.text))
    counter+=1

