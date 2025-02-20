from storage import istorage
import json


class StorageJson(istorage.IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_movies(self):
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def save_movies(self, movies):
        with open(self.file_name, 'w') as file:
            return json.dump(movies, file, indent=4)

    def list_movies(self):
        return self.get_movies()

    def add_movie(self, title, year, rating, poster=None):
        movies = self.get_movies()
        movies[title] = {"Year": year, "Rating": rating, "Poster": poster}
        self.save_movies(movies)

    def delete_movie(self, title):
        movies = self.get_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.get_movies()
        if title in movies:
            movies[title]["Rating"] = rating
            self.save_movies(movies)
