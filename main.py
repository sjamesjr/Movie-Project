from storage import storage_json
from storage import storage_csv
from movie_app import MovieApp


storage_type = storage_csv.StorageCSV('data/movies.csv')
movie_app = MovieApp(storage_type)
movie_app.run()
