import media
import fresh_tomatoes

# to create instance variables for toy_story and other movies

# ToyStory Movie: Movie Trailer, Storyline, Poster Image & Youtube Trailer
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar Movie: Movie Trailer, Storyline, Poster Image and Youtube Trailer"""
avatar = media.Movie("Avatar", "A Marine on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Superbad Movie: Movie Trailer, Storyline, Poster Image & Youtube Trailer
superbad = media.Movie("Superbad",
                       "An epic saga of loosing virginity before college",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=T5PwUtWE03Y")

# School of Rock: Trailer, Storyline, Poster Image and Youtube Trailer
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Hunger Games: Trailer, Storyline, Poster Image and Youtube Trailer
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Show Girls: Movie Trailer, Storyline, Poster Image and Youtube Trailer
show_girls = media.Movie("Show Girls",
                         "The journey of a drifter from stripper to showgirl",
                         "https://upload.wikimedia.org/wikipedia/en/d/d7/Showgirls_%281995_film_poster%29.jpg",
                         "https://www.youtube.com/watch?v=yCeCGcGAcfI")

# Assigning the movies to be channeled through to media file
movies = [toy_story, avatar, superbad, school_of_rock,
          hunger_games, show_girls]

# Opening HTML file via webbrowser thru open_movies_page in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
