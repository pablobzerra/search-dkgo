#pylint:disable=W0611
from duckduckgo_search import ddg
import json
text = input('Г[ ')
r = ddg(text, region='pt-br', safesearch='Moderate', time='y', max_results=2)
for a  in r:
    print(f"=======================================================================\ntitulo: {a['title']}\nlink: {a['href']}")
print('=======================================================================')