# Movie class that contains the details of a movie
class Movie:
    """This class holds the data of all movies that are sent by
    entertainment_center file.

    Attributes:
        title: Title of the movie
        storyline: The tagline of the movie
        poster_image_url: poster image of the movie
        trailer_youtube_url: link to the movie trailer
        on YouTube"""
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # initializing instance variable of Movie class using constructor
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube