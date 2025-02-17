from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV

storage = StorageJson('movies.json')
movie_app = MovieApp(storage)
movie_app.run()
