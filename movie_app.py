import storage_json
import storage_csv
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
            Adds a new movie to the storage. Prompts the user for movie title, release year, and rating.

            Returns:
                str: A success message if the movie is added or an error message for invalid input.
            """
        movies = self._storage.get_movies()
        title = input("Enter new movie name: ")
        try:
            year = int(input("Enter Release Year: "))
            rating = float(input("Enter new movie rating: "))
            movies[title] = {"Year": year, "Rating": rating}
            # Add the movie and save the data to the storage
            self._storage.add_movie(title, year, rating)
            return f'{title} released {year} rated {rating} has been successfully added'
        except ValueError:
            return "Invalid input. Please enter a valid number for the rating."
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

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
                print("Exiting the program. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please select an option from 1 to 9.")
        except Exception as e:
            return f"An error occurred while listing movies: {str(e)}"

    def _generate_website(self):
        ...

    def run(self):
        """
            Displays the main menu and prompts the user to choose an option. Calls the corresponding function based on user input.
            """
        while True:
            print(
                "\n********** My Movies Database **********\nMenu:\n"
                "1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n"
                "5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Exit"
            )
            try:

                menu_prompt = input("Enter choice (1-9): ")
                self._handle_command(menu_prompt)
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

            input("\nPress 'Enter' to continue...")
