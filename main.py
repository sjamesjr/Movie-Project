from movie_app import MovieApp
from storage import storage_json
from storage import storage_csv

storage_type = storage_json.StorageJson('movies.json')
movie_app = MovieApp(storage_type)
movie_app.run()
