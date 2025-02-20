# MovieApp

MovieApp is a command-line application for managing a personal movie database. It allows users to add, delete, update, and list movies, fetch details from the OMDb API, generate statistics, and export movie data as a simple HTML webpage.

## Features
- Add movies by searching their title (fetches details from OMDb API)
- List all stored movies
- Delete movies from the database
- Update movie ratings
- Sort movies by rating
- Retrieve a random movie suggestion
- Generate statistics (average rating, best/worst movies, median rating)
- Search movies by partial name
- Export movie list as an HTML webpage

## Installation
### Prerequisites
Ensure you have Python installed (version 3.6 or later).

### Setup
1. Clone this repository or download the source files.
2. Navigate to the project directory and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
Upon running `main.py`, you will be presented with a menu where you can select different options to manage your movie database.

### Storage Options
The application supports multiple storage backends:
- **CSV Storage:** Saves movie data in a CSV file (`movies.csv`)
- **JSON Storage:** Saves movie data in a JSON file (`movies.json`)

To switch storage types, modify the `storage_type` variable in `main.py`:
```python
from storage import storage_csv
storage_type = storage_csv.StorageCSV('data/movies.csv')
```
or
```python
from storage import storage_json
storage_type = storage_json.StorageJson('data/movies.json')
```

## Dependencies
- `requests` (for fetching movie details from OMDb API)

All dependencies are listed in `requirements.txt`.

## API Key
The application retrieves movie details using the [OMDb API](https://www.omdbapi.com/). Replace the API key inside `movie_app.py` with your own key if needed:
```python
api_key = "your_api_key_here"
```

## Generating a Movie List Website
Use option **9** in the menu to generate an `index.html` file displaying the movie list.

## License
This project is licensed under the MIT License.

