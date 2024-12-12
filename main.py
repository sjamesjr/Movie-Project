import statistics
import random


# Function to list all movies
def list_movies(movies: dict) -> str:
    """
    Prints the total number of movies in the dictionary and returns a formatted string
    with each movie and its rating.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A formatted string listing all movies and their ratings.
    """
    num_of_movies = len(movies)
    movie_list = f"{num_of_movies} movies in total\n"
    for movie, rating in movies.items():
        movie_list += f"{movie}: {rating}\n"
    return movie_list.strip()  # Removes the trailing newline


# Function to add a new movie
def add_movie(movies: dict) -> str:
    """
    Prompts the user to input a new movie name and rating, then adds the movie and its rating to the dictionary.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A message indicating whether the movie was successfully added or if there was an error.
    """
    new_movie = input("Enter new movie name: ")
    try:
        new_rating = float(input("Enter new movie rating: "))
        movies[new_movie] = new_rating
        return f'{new_movie} rated {new_rating} has been successfully added'
    except ValueError:
        return "Invalid input. Please enter a valid number for the rating."


# Function to delete a movie
def del_movie(movies: dict) -> str:
    """
    Prompts the user to input the name of a movie to delete, then removes the movie from the dictionary.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A message indicating whether the movie was successfully deleted or if it was not found.
    """
    movie_to_del = input("Enter movie name to delete: ")
    if movie_to_del in movies:
        del movies[movie_to_del]
        return f'{movie_to_del} has been successfully deleted'
    else:
        return f"Movie {movie_to_del} doesn't exist"


# Function to update a movie's rating
def update_movie(movies: dict) -> str:
    """
    Prompts the user to input a movie name and a new rating, then updates the movie's rating in the dictionary.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A message indicating whether the movie was successfully updated or if there was an error.
    """
    movie_to_update = input("Enter movie name: ")
    if movie_to_update in movies:
        try:
            rating_update = float(input("Enter new movie rating: "))
            movies[movie_to_update] = rating_update
            return f'{movie_to_update} has been successfully updated'
        except ValueError:
            return "Invalid input. Please enter a valid number for the rating."
    else:
        return f"Movie {movie_to_update} doesn't exist"


# Function to provide statistics on movies
def stats_movies(movies: dict) -> str:
    """
    Calculates and returns statistics on the movies, including average rating, median rating,
    and lists all movies with the highest and lowest ratings.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A formatted string containing statistical information about the movies.
    """
    if movies:
        total_val = sum(movies.values())
        average_rating = total_val / len(movies)
        median_rating = statistics.median(movies.values())

        max_rating = max(movies.values())
        min_rating = min(movies.values())

        highest_rated = [movie for movie, rating in movies.items() if rating == max_rating]
        lowest_rated = [movie for movie, rating in movies.items() if rating == min_rating]

        return (f'\n Average rating: {average_rating:.2f} \n Median rating: {median_rating:.2f} '
                f'\n Best Movie(s): {", ".join(highest_rated)} (Rating: {max_rating}) '
                f'\n Worst Movie(s): {", ".join(lowest_rated)} (Rating: {min_rating})')
    else:
        return "No movies available to calculate statistics."


# Function to select a random movie
def random_movie(movies: dict) -> str:
    """
    Selects and returns a random movie and its rating from the dictionary.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A message containing the randomly selected movie and its rating, or a message indicating no movies are available.
    """
    if movies:
        select_random_movie = random.choice(list(movies.keys()))
        random_value = movies[select_random_movie]
        return f'Your movie for tonight: {select_random_movie}, is rated {random_value}'
    else:
        return "No movies available."


# Function to search for a movie by name
def search_movie(movies: dict) -> str:
    """
    Prompts the user to input part of a movie name, then searches for and returns the first matching movie and its rating.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A message containing the matching movie and its rating, or a message indicating no matches were found.
    """
    search_inquiry = input("Enter part of movie name: ")
    for key, value in movies.items():
        if search_inquiry.lower() in key.lower():
            return f'{key}, {value}'
    return "No match found"


# Function to sort movies by rating
def sort_by_rating(movies: dict) -> str:
    """
    Sorts the movies by their ratings in descending order and returns the sorted dictionary.

    Parameters:
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        str: A formatted string listing all movies sorted by rating in descending order, or a message indicating no movies are available.
    """
    if movies:
        sorted_dict = dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))
        num_of_movies = len(sorted_dict)
        movie_list = f"{num_of_movies} movies in total\n"
        for movie, rating in sorted_dict.items():
            movie_list += f"{movie}: {rating}\n"
        return movie_list.strip()  # Removes the trailing newline
    else:
        return "No movies available to sort."


# Function to handle menu choices
def handle_choice(choice: str, movies: dict) -> None:
    """
    Handles the menu choice and calls the corresponding function.

    Parameters:
        choice (str): The user's menu choice.
        movies (dict): A dictionary where keys are movie names (str) and values are ratings (float).

    Returns:
        None
    """
    if choice == "1":
        print(list_movies(movies))
    elif choice == "2":
        print(add_movie(movies))
    elif choice == "3":
        print(del_movie(movies))
    elif choice == "4":
        print(update_movie(movies))
    elif choice == "5":
        print(stats_movies(movies))
    elif choice == "6":
        print(random_movie(movies))
    elif choice == "7":
        print(search_movie(movies))
    elif choice == "8":
        print(sort_by_rating(movies))
    elif choice == "9":
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select an option from 1 to 9.")


# Main function to handle user interaction and menu options
def main():
    """
    Displays the main menu and prompts the user to choose an option. Calls the corresponding function based on user input.
    """
    # Dictionary to store the movies and the ratings

    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }
    while True:
        print(
            "\n********** My Movies Database **********\n Menu:\n 1. List movies \n 2. Add movie \n 3. Delete movie \n 4. "
            "Update movie \n 5. Stats \n 6. Random movie \n 7. Search movie \n 8. Movies sorted by rating \n 9. Exit")

        menu_prompt = input("Enter choice (1-9): ")
        handle_choice(menu_prompt, movies)
        input("\nPress 'Enter' to continue...")


if __name__ == "__main__":
    main()
