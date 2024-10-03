import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from DjangoFilmsApp.models import Films, Genres, Actors, Directors, Filmsandgenres, Filmsandactors, Filmsanddirectors

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos de películas desde OMDb API'


##########################

    def add_arguments(self, parser):
        parser.add_argument(
            '--search',
            type=str,
            help='Término de búsqueda para encontrar películas (por ejemplo, "Star Wars")'
        )
############################


    def handle(self, *args, **kwargs):
        print(f"OMDB API Key: {settings.OMDB_API_KEY}")  # Verifica que la clave API se está leyendo
        #movie_ids = [
        #    "tt3896198", "tt0111161", "tt0068646", "tt0071562", "tt0468569"
        #]

#################################
        search_term = kwargs.get('search')
        if search_term:
            self.stdout.write(f"Searching for movies with term: {search_term}")
            search_results = self.search_movies(search_term)
            movie_ids = [movie.get('imdbID') for movie in search_results]
        else:
            movie_ids = [
                "tt3896198", "tt0111161", "tt0068646", "tt0071562", "tt0468569"
            ]
##################################

        for movie_id in movie_ids:
            self.stdout.write(f"Fetching data for: {movie_id}")
            data = self.fetch_movie_data(movie_id)
            if data and data.get('Response') == 'True':
                self.update_or_create_film(data)
            else:
                self.stdout.write(f"Failed to fetch data for: {movie_id}")

#####################################
    def search_movies(self, search_term):
        api_key = settings.OMDB_API_KEY
        search_url = 'http://www.omdbapi.com/'
        response = requests.get(search_url, params={'s': search_term, 'apikey': api_key})
        data = response.json()

        if data.get('Response') == 'True':
            return data.get('Search', [])
        else:
            self.stdout.write(f"Search failed: {data.get('Error')}")
            return []
######################################

    def fetch_movie_data(self, movie_id):
        api_key = settings.OMDB_API_KEY
        url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def update_or_create_film(self, data):
        title = data['Title']
        release_year = int(data['Year']) if data['Year'].isdigit() else None
        length = self.parse_runtime(data.get('Runtime', ''))
        synopsis = data.get('Plot', '')
        picture_url = data.get('Poster', '')

        film, created = Films.objects.update_or_create(
            title=title,
            defaults={
                'release_year': release_year,
                'length': length,
                'synopsis': synopsis,
                'picture_url': picture_url,
                'active': True,
                'deleted': False,
            }
        )

        self.update_genres(film, data.get('Genre', ''))
        self.update_actors(film, data.get('Actors', ''))
        self.update_directors(film, data.get('Director', ''))

    def parse_runtime(self, runtime_str):
        if 'min' in runtime_str:
            return int(runtime_str.split(' ')[0])
        return None

    def update_genres(self, film, genres_str):
        if not genres_str:
            print("No genres to process.")
            return

        genres = [genre.strip() for genre in genres_str.split(',') if genre.strip()]
        print(f"Genres to process: {genres}")

        for genre_name in genres:
            print(f"Processing genre: {genre_name}")
            genre, created = Genres.objects.get_or_create(
                genre_name=genre_name,
                defaults={
                    'active': True,
                    'deleted': False
                }
            )
            print(f"Genre object created or retrieved: {genre}")

            Filmsandgenres.objects.update_or_create(
                film=film,
                genre=genre,
                defaults={'active': True, 'deleted': False}
            )
            print(f"Genre {genre_name} associated with film {film.title}")

    def update_actors(self, film, actors_str):
        actors = [actor.strip() for actor in actors_str.split(',') if actor.strip()]
        for actor_name in actors:
            actor, created = Actors.objects.get_or_create(
                name=actor_name,
                defaults={
                    'active': True,
                    'deleted': False
                }
            )
            Filmsandactors.objects.update_or_create(
                film=film,
                actor=actor,
                defaults={'active': True, 'deleted': False}
            )

    def update_directors(self, film, director_name):
        director, created = Directors.objects.get_or_create(
            name=director_name,
            defaults={
                'active': True,
                'deleted': False
            }
        )
        Filmsanddirectors.objects.update_or_create(
            film=film,
            director=director,
            defaults={'active': True, 'deleted': False}
        )
