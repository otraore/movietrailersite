# Import the media.py file to access it's class definition of Movie
import media
# Import the fresh_tomatoes.py file to access the open_movies_page function
import fresh_tomatoes

# Creates a new instance of the
the_dictator = media.Movie("The Dictator",
                           "https://www.youtube.com/watch?v=cYplvwBvGA4",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/The_Dictator_Poster.jpg",
                           "cYplvwBvGA4")
american_sniper = media.Movie("American Sniper",
                              "https://www.youtube.com/watch?v=99k3u9ay1gs",
                              'http://ia.media-imdb.com/images/M/MV5BMTkxNz'
                              'I3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
                              "99k3u9ay1gs")
zootopia = media.Movie("Zootopia",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "jWM0ct-OLsM")

movies = [the_dictator, american_sniper, zootopia]

fresh_tomatoes.open_movies_page(movies)
