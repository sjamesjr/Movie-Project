from movie_app import MovieApp
from storage.storage_json import StorageJson  # Update the import path
import sys

storage_type = StorageJson('movies.json')
movie_app = MovieApp(storage_type)
movie_app.run()
