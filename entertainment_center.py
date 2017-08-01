import media
import fresh_tomatoes

#This section is used to initialize values in the Movie class for each movie

naruto = media.Movie("Naruto: The Last",
                     "Two years after the Fourth Shinobi World War, "
                     "Naruto must stop Toneri Otsutsuki",
                     "https://cdn.traileraddict.com/content/unknown/"
		     "the-last-naruto.jpg",
                     "https://www.youtube.com/watch?v=SDIvvapG0sE")
onepiece = media.Movie("One piece: Film Z",
                       "A former Marine admiral steals the Dyna Stones, "
                       "and stands in the way of the Straw Hat Pirates.",
                       "http://www.gstatic.com/tv/thumb/movieposters/"
		       "11124438/p11124438_p_v8_aa.jpg",
                       "https://www.youtube.com/watch?v=1gGt1Mg_zSo")
thor = media.Movie("Thor: Raghnarok",
                   "Imprisoned on the other side of the universe, the mighty "
		   "Thor finds himself in a deadly gladiatorial contest that "
		   "pits him against the Hulk, his former ally and"
		   " fellow Avenger. ",
                   "http://pre08.deviantart.net/6e83/th/pre/i/2016/255/6/1"
		   "/thor__ragnarok_poster_by_bakikayaa-daheka0.jpg",
                   "https://www.youtube.com/watch?v=v7MGUNV8MxU")
onepunch = media.Movie("One-Punch Man",
                       "Powerful superhero has grown bored by the absence"
                       "of challenge in his fight against evil.",
                       "https://images-na.ssl-images-amazon.com/images/I/"
		       "81C79-6dNxL.jpg",
                       "https://www.youtube.com/watch?v=A3Jks90zaEE")
black = media.Movie("Black Panther",
                    "The Black Panther is a fictional superhero "
                    "appearing in American comic books published by Marvel Comics. ",
                    "https://s-media-cache-ak0.pinimg.com/originals/2a/22/43"
		    "/2a2243c8d03cc6f55cdaf531aca55dc8.jpg",
                    "https://www.youtube.com/watch?v=dxWvtMOGAhw")
avengers = media.Movie("Avengers",
                       "When Thor's evil brother, Loki gains access to the"
		       " unlimited power of the energy cube called the Tesseract. "
                       "Nick Fury initiates a superhero recruitment effort to"
		       " defeat the unprecedented threat to Earth.",
                       "https://i1.fiuxy.com/victoria-caldas.gov.co/apc-aa-files"
                       "/495052435f5052454445465f30303137/los-vengadores-1.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# An array(movies) that contains all movies refernce variables in it
movies = [naruto, onepiece, thor, onepunch, black, avengers]

# Generates the movie trailer page and opens it
# passing movies array as a parameter to open_movies_page()
fresh_tomatoes.open_movies_page(movies)
