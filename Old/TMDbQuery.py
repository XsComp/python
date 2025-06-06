import requests
import webbrowser
import datetime

# ==================== CONFIGURATION ====================
# API URL and headers for authentication
API_KEY = "fca897120f5279c8d0f1eaa3dde997e9"
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2E4OTcxMjBmNTI3OWM4ZDBmMWVhYTNkZGU5OTdlOSIsIm5iZiI6MTc0ODc0NzY0OS44MDgsInN1YiI6IjY4M2JjNTgxZTE4NDJkNmNmNGZkYWUxMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KjeZrtD3zPQPwI1fVRZBR4wTjcRTJdrRDx6aQ1wpFd4"
}

# ==================== MAIN FUNCTION ====================
def search_movie():
    print("\nWelcome to Andreas' Movie db")
    movie_name = input("\nWhat movie are you curious about? ")

    # Construct the search endpoint
    url = f"{BASE_URL}/search/movie"
    params = {"query": movie_name, "language": "en-US"}

    # Send the GET request
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        print("Something went wrong. Status code:", response.status_code)
        return

    results = response.json().get("results", [])

    if not results:
        print("No movies found for that query!")
        return

    # Show first match
    movie = results[0]
    print("\nWe found something! Here you go:")
    print("Title:       ", movie.get("title"))
    print("Released:    ", movie.get("release_date"))
    print("Rating:      ", movie.get("vote_average"))
    print("Overview:    ", movie.get("overview"))

    # Optionally open image
    poster_path = movie.get("poster_path")
    if poster_path:
        full_image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        print("\nOpening poster in your browser...")
        webbrowser.open(full_image_url)
    else:
        print("No poster image found.")

    # Save to log file (nice to practice file handling!)
    with open("movie_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} - {movie_name} -> {movie.get('title')}\n")

    print("\nThis search has been saved to 'movie_log.txt'.")


# ==================== SCRIPT ENTRY ====================
if __name__ == "__main__":
    search_movie()
