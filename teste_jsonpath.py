import requests
import jsonpath

api = requests.get('http://localhost:8000/api/v2/filmes/')
filmes = jsonpath.jsonpath(api.json(), 'results[*].diretor')
print(filmes)

