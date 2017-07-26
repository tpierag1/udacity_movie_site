# importing the class definition from media.py
import media
# importing the script from freshtomatoes.py
import freshtomatoes

# constructing movies
dialectic = media.Movie("Can the Dialectic Break Bricks?",
                        "Detourned samurai film modified to discuss May 1968 uprising in Paris",  # NOQA
                        "https://upload.wikimedia.org/wikipedia/en/5/59/La_Dialectique_Peut-Elle_Casser_Des_Briques.jpg",  # NOQA
                        "https://youtu.be/mjUNY0433Do")

strike = media.Movie("Strike!", "A film about a general strike in Russia in 1905",  # NOQA
                     "https://upload.wikimedia.org/wikipedia/commons/9/94/Strike2.JPG",  # NOQA
                     "https://youtu.be/hG_yM7We0C8")

camera = media.Movie("Man With the Movie Camera",
                     "Experimental Soviet documentary about urban life",
                     "https://upload.wikimedia.org/wikipedia/commons/3/34/Man_with_a_movie_camera.jpg",  # NOQA
                     "https://youtu.be/PgJTuyKr4po")

anemic = media.Movie("Anemic Cinema", "Experimental film by Marcel Duchamp",
                     "http://4.bp.blogspot.com/-OUrJtONz9B0/T1yf8mOfFII/AAAAAAAAA4M/2zZoKI2qAxc/s1600/anemic+cinema+2.jpg",  # NOQA
                     "https://youtu.be/yZIHA4hLk2k")

spectacle = media.Movie("Society of the Spectacle",
                        "Theoretical work about the anomie of late capitalism",
                        "https://upload.wikimedia.org/wikipedia/en/d/d0/Society_of_the_Spectacle_film.jpg",  # NOQA
                        "https://youtu.be/UKRDY88eXQU")

anticoncept = media.Movie("Anticoncept",
                          "Experimental film from the Lettrist International",
                          "https://4.bp.blogspot.com/-qJuI0FMc7Sc/WLGR6plafZI/AAAAAAAACBQ/KxaJkz4T2MYMV4UhhtPtGOv0s-7onQjgwCLcB/w1200-h630-p-k-no-nu/Screen%2BShot%2B2017-02-22%2Bat%2B4.44.31%2BPM.png",  # NOQA
                          "https://youtu.be/29UhO7PP_Bs")

critique = media.Movie("Critique of Separation",
                       "Theoretical work by Guy Debord",
                       "https://anticopyrighttr.files.wordpress.com/2012/09/guy-debord_ayrismanin-elestirisi-critique-de-la-separation.png",  # NOQA
                       "https://youtu.be/W0zZX-d028Y")

refutation = media.Movie("Refutation of All Judgements",
                         "Theoratical work by Guy Debord",
                         "http://img.scoop.it/LHZn6DxKmxrtl3xqFFEFZDl72eJkfbmt4t8yenImKBVvK0kTmF0xjctABnaLJIm9",  # NOQA
                         "https://youtu.be/w5pOVNtDfJw")

meaning = media.Movie("The Production of Meaning",
                      "AdBusters film on commodification",
                      "http://image.tmdb.org/t/p/w500/jxwbjhlLxkDis9rFQXoXBV3MsBH.jpg",  # NOQA
                      "https://youtu.be/Z2GKajcU3ns")

# list of movies
movies = [strike, camera, dialectic, spectacle, critique, refutation,
          meaning, anticoncept, anemic]

# calls the open_movies_page from freshtomatoes, which generates the html for the site on the list movies  # NOQA
freshtomatoes.open_movies_page(movies)
