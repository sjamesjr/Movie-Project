import requests
import statistics
import random


class MovieApp:

    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """
            Retrieves and lists all movies in the storage.

            Returns:
                str: A formatted string containing all movies with their details.
            """
        try:
            movies = self._storage.get_movies()
            num_of_movies = len(movies)
            movie_list = f"{num_of_movies} movies in total\n"
            for index, (key, value) in enumerate(movies.items(), start=1):
                movie_list += f"{index}. {key}: {value}\n"
            return movie_list.strip()  # Removes the trailing newline
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_add_movie(self):
        """
        Adds a new movie to the storage by searching for its details in the OMDb API.

        Returns:
            str: A success message if the movie is added or an error message for invalid input.
        """
        try:
            title = input("Enter movie name: ").strip()
            if not title:
                return "Movie title cannot be empty."

            # Fetch movie details from OMDb API
            api_key = "336e4113"
            url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
            response = requests.get(url)
            movie_data = response.json()

            if movie_data.get("Response") == "False":
                return f"Movie '{title}' not found in OMDb database."

            # Extract required fields
            title = movie_data.get("Title")
            year = movie_data.get("Year")
            rating = movie_data.get("imdbRating")
            poster_url = movie_data.get("Poster")

            if rating == "N/A":  # Handle missing ratings
                rating = None
            else:
                try:
                    rating = float(rating)
                except ValueError:
                    rating = None

            # Save movie details to storage
            self._storage.add_movie(title, year, rating, poster_url)

            return f"'{title}' ({year}) with IMDb rating {rating} has been added. Poster: {poster_url}"

        except Exception as e:
            return f"An error occurred while adding the movie: {str(e)}"

    def _command_delete_movie(self):
        """
        #     Deletes a movie from the storage based on the user-provided title.
        #
        #     Returns:
        #         str: A success message if the movie is deleted or an error message if the movie doesn't exist.
        #     """
        try:
            movies = self._storage.list_movies()
            movie_to_del = input("Enter movie name to delete: ")
            if movie_to_del in movies:
                self._storage.delete_movie(movie_to_del)
                return f'{movie_to_del} has been successfully deleted'
            else:
                return f"Movie {movie_to_del} doesn't exist"
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_update_movie(self):
        """
            Updates the rating of a movie in the storage.

            Returns:
                str: A success message if the movie's rating is updated or an error message if the movie doesn't exist.
            """
        try:
            movies = self._storage.list_movies()
            movie_to_update = input("Enter movie name: ")

            if movie_to_update in movies:
                try:
                    rating_update = float(input("Enter new movie rating: "))
                    self._storage.update_movie(movie_to_update, rating_update)
                    return f'{movie_to_update} has been successfully updated'
                except ValueError:
                    return "Invalid input. Please enter a valid number for the rating."
            else:
                return f"Movie {movie_to_update} doesn't exist"
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_sort_movie(self):
        """
            Sorts movies by their rating in descending order and displays the sorted list.

            Returns:
                str: A formatted string with the sorted movies or an error message if no movies exist.
            """
        try:
            movies = self._storage.list_movies()
            if movies:
                sorted_dict = dict(sorted(movies.items(), key=lambda item: item[1]["Rating"], reverse=True))
                num_of_movies = len(sorted_dict)
                movie_list = f"{num_of_movies} movies in total\n"
                for movie, data in sorted_dict.items():
                    movie_list += f"{movie}: {data}\n"
                return movie_list.strip()  # Removes the trailing newline
            else:
                return "No movies available to sort."
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_random_movie(self):

        """
           Selects and returns a random movie from the storage.

           Returns:
               str: A message with the selected random movie or an error if no movies exist.
           """
        try:
            movies = self._storage.list_movies()
            if movies:
                select_random_movie = random.choice(list(movies.keys()))
                random_value = movies[select_random_movie]
                return f'Your movie for tonight: {select_random_movie}, is rated {random_value["Rating"]}'
            else:
                return "No movies available."
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_movie_stats(self):
        # Function to provide statistics on movies

        """
        Calculates and returns statistics about the movies in the storage.

            Returns:
                str: A formatted string with average, median, best, and worst ratings.
            """
        try:
            movies = self._storage.list_movies()
            if movies:
                ratings = [movie["Rating"] for movie in movies.values()]
                average_rating = sum(ratings) / len(movies)
                median_rating = statistics.median(ratings)
                max_rating = max(ratings)
                min_rating = min(ratings)

                highest_rated = [movie for movie, data in movies.items() if data["Rating"] == max_rating]
                lowest_rated = [movie for movie, data in movies.items() if data["Rating"] == min_rating]

                return (f'\nAverage rating: {average_rating:.2f}\nMedian rating: {median_rating:.2f}\n'
                        f'Best Movie(s): {", ".join(highest_rated)} (Rating: {max_rating})\n'
                        f'Worst Movie(s): {", ".join(lowest_rated)} (Rating: {min_rating})')
            else:
                return "No movies available to calculate statistics."
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _command_search_movie(self):
        """
           Searches for a movie based on a partial name input by the user.

           Returns:
               str: A formatted string with the matching movie details or an error message if no match is found.
           """
        try:
            movies = self._storage.list_movies()
            search_inquiry = input("Enter part of movie name: ")
            for key, value in movies.items():
                if search_inquiry.lower() in key.lower():
                    return f'{key}: {value}'
            return "No match found"
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _handle_command(self, choice):
        """
       #     Executes the appropriate function based on the user's menu choice.
       #
       #     Args:
       #         choice (str): The user's menu choice.
       #     """

        try:
            if choice == "1":
                print(self._command_list_movies())
            elif choice == "2":
                print(self._command_add_movie())
            elif choice == "3":
                print(self._command_delete_movie())
            elif choice == "4":
                print(self._command_update_movie())
            elif choice == "5":
                print(self._command_movie_stats())
            elif choice == "6":
                print(self._command_random_movie())
            elif choice == "7":
                print(self._command_search_movie())
            elif choice == "8":
                print(self._command_sort_movie())
            elif choice == "9":
                self._generate_website()
                print("Website was generated successfully.")
            elif choice == "10":
                print("Exiting the program. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please select an option from 1 to 9.")
        except Exception as e:
            print(f"An error occurred while listing movies: {str(e)}")

    def _generate_website(self):
        """
            Generates an index.html file based on the provided movie list.

            :param movies: List of dictionaries, each containing 'title', 'year', 'rating', and 'poster_url'.
            """

        movie_template = """
                       <li class="movie">
                           <img src="{poster_url}" alt="{title} poster"/>
                           <h2>{title} ({year})</h2>
                           <p>Rating: {rating}</p>
                       </li>
                   """

        template_list = [movie_template.format(title=title, year=movie_details["Year"],
                                               rating=movie_details["Rating"], poster_url=movie_details["Poster"])
                         for title, movie_details in self._storage.get_movies().items()]

        movie_list_html = "\n".join(template_list)
        html_template = """<!DOCTYPE html>
               <html>
               <head>
                   <title>My Movie App</title>
                   <link rel="stylesheet" href="style.css"/>
               </head>
               <body>
               <div class="list-movies-title">
                   <h1>MovieApp</h1>
               </div>
               <div>
                   <ol class="movie-grid">
                       {movie_list}
                   </ol>
               </div>
               </body>
               </html>
                   """.format(movie_list=movie_list_html)

        # Write to index.html
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(html_template)


    def run(self):
        """
            Displays the main menu and prompts the user to choose an option. Calls the corresponding function based on user input.
            """
        while True:
            print(
                "\n********** My Movies Database **********\nMenu:\n"
                "1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n"
                "5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Generate Website\n10. Exit"
            )
            try:

                menu_prompt = input("Enter choice (1-10): ")
                self._handle_command(menu_prompt)
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

            input("\nPress 'Enter' to continue...")
