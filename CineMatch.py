def add_movie(movies, title, genre, rating):
    movies[title] = {'genre': genre, 'rating': rating}
    print(f"Movie '{title}' added successfully.")


def delete_movie(movies, title):
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' deleted successfully.")
    else:
        print(f"Movie '{title}' not found.")


def search_movie_by_title(movies, title):
    if title in movies:
        return movies[title]
    else:
        return "Movie not found."


def search_movie_by_genre(movies, genre):
    results = {title: details for title, details in movies.items() if details['genre'].lower() == genre.lower()}
    return results if results else "No movies found in this genre."


def recommend_top_n_movies(movies, n):
    if not movies:
        return "No movies available to recommend."

    if n <= 0:
        return "Please enter a positive number for the number of recommendations."

    # Sort movies by rating in descending order
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)

    # Get the top n movies
    top_n_movies = sorted_movies[:n]

    return top_n_movies


def get_movie_details_and_recommend_similar(movies, title):
    if title not in movies:
        return "Movie not found."

    movie_details = movies[title]
    genre = movie_details['genre']
    similar_movies = {t: details for t, details in movies.items() if
                      details['genre'].lower() == genre.lower() and t != title}

    return {
        'movie_details': movie_details,
        'similar_movies': similar_movies
    }


def add_sample_movies(movies):
    sample_movies = {
        "3 Idiots": {"genre": "Comedy", "rating": 8.4},
        "Dangal": {"genre": "Drama", "rating": 8.4},
        "Sholay": {"genre": "Action", "rating": 8.2},
        "Dilwale Dulhania Le Jayenge": {"genre": "Romance", "rating": 8.1},
        "Gully Boy": {"genre": "Drama", "rating": 8.0},
        "Bahubali": {"genre": "Action", "rating": 8.1},
        "PK": {"genre": "Comedy", "rating": 8.1},
        "Swades": {"genre": "Drama", "rating": 8.2}
    }
    movies.update(sample_movies)
    print("Sample movies added successfully.")


def main():
    movies = {}
    add_sample_movies(movies)

    while True:
        print("\nMenu:")
        print("1. Add a movie")
        print("2. Delete a movie")
        print("3. Search for a movie by title")
        print("4. Search for movies by genre")
        print("5. Recommend top N movies")
        print("6. Get movie details and recommend similar movies")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            rating = float(input("Enter movie rating: "))
            add_movie(movies, title, genre, rating)

        elif choice == '2':
            title = input("Enter movie title to delete: ")
            delete_movie(movies, title)

        elif choice == '3':
            title = input("Enter movie title to search: ")
            result = search_movie_by_title(movies, title)
            print(result)

        elif choice == '4':
            genre = input("Enter movie genre to search: ")
            result = search_movie_by_genre(movies, genre)
            print(result)

        elif choice == '5':
            n = int(input("Enter the number of top movies to recommend: "))
            top_movies = recommend_top_n_movies(movies, n)
            print("Top recommended movies:")
            for title, details in top_movies:
                print(f"Title: {title}, Genre: {details['genre']}, Rating: {details['rating']}")

        elif choice == '6':
            title = input("Enter movie title to get details and similar recommendations: ")
            result = get_movie_details_and_recommend_similar(movies, title)
            if isinstance(result, str):
                print(result)
            else:
                print("Movie details:")
                print(result['movie_details'])
                print("Similar movies:")
                for t, details in result['similar_movies'].items():
                    print(f"Title: {t}, Genre: {details['genre']}, Rating: {details['rating']}")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
