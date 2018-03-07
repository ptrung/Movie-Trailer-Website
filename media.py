class Media():
    """Parent Class for further media instances like TV-Show, Books, etc.

    This class should be used as a parent class for further instances.
    It contains the minimum information that a media instance needs.

    Attributes:
        title: A string that defines the title of the media
    """
    def __init__(self, media_title):
        """Inits Class Media with

        Args:
            media_title: A string to give the media a title
        """
        self.title = media_title


class Movie(Media):
    """Child class of media to save informations about movies

    This class inherits from Media and saves additional data special for movies

    Attributes:
        movie_title: A string to give the movie a title
        movie_poster: A string with the url of a poster
        movie_trailer: A string with the url to a youtube trailer
        movie_userrating: A float with the userrating of TMDb
    """
    def __init__(self, movie_title,
                 movie_poster, movie_trailer,
                 movie_userrating):
        """Inits Class Movie with movie_title, movie_poster,
                                  movie_trailer, movie_userrating

        Attributes:
            movie_title: A string to give the movie a title
            movie_poster: A string with the url of a poster
            movie_trailer: A string with the url to a youtube trailer
            movie_userrating: An int with the userrating of TMDb
        """
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.userrating = movie_userrating
        Media.__init__(self, movie_title)
