import media
import fresh_tomatoes

#to create instance variables for toy_story
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

#toy_story.show_trailer()

#to create instance variables for avatar for class Movie in media.py
avatar = media.Movie("Avatar",
                   "A Marine on alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

superbad = media.Movie("Superbad",
                       "Superbad boys want nothing more than to lose their virginity before they head off to college",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=T5PwUtWE03Y")

#print(superbad.poster_image_url)
#superbad.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
                             
                       
show_girls = media.Movie("Show Girls",
                          "The journey of a drifter from stripper to showgirl",
                          "https://upload.wikimedia.org/wikipedia/en/d/d7/Showgirls_%281995_film_poster%29.jpg",
                          "https://www.youtube.com/watch?v=yCeCGcGAcfI")


movies = [toy_story, avatar, superbad, school_of_rock, hunger_games, show_girls]      
fresh_tomatoes.open_movies_page(movies)


#print(media.Movie.__doc__)
