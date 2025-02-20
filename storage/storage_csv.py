from storage import istorage
import csv


class StorageCSV(istorage.IStorage):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_movies(self):
        movies = {}
        try:
            with open(self.file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row["Title"]] = {
                        "Year": int(row["Year"]),
                        "Rating": float(row["Rating"]),
                        "Poster": row["Poster"]
                    }
            return movies
        except FileNotFoundError:
            return {}
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the file: {e}")

    def save_movies(self, movies):
        """
                Writes all movies back to the CSV file. Used for updates and deletes.
                """
        try:
            with open(self.file_name, mode="w", newline="") as file:
                fieldnames = ["Title", "Year", "Rating", "Poster"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Write the header row
                writer.writeheader()

                # Write all movies
                for title, data in movies.items():
                    writer.writerow({
                        "Title": title,
                        "Year": data["Year"],
                        "Rating": data["Rating"],
                        "Poster": data["Poster"]
                    })
        except Exception as e:
            raise RuntimeError(f"An error occurred while writing to the file: {e}")

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
