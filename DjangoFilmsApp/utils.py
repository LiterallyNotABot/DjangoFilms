import requests
from django.conf import settings

def fetch_movie_data(title):
    api_key = settings.OMDB_API_KEY
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data