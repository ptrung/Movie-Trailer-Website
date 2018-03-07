import tmdb3 as tmbd


class TmdbMovie():
    """Class Tmdb provides the connection to the TM database

    This class implements the connection to the TM database.
    By providing the personal TMDb API key and the movie ID,
    you can get every information about the movie.

    Attributes:
        movie: A Movie instance of the provided movie_id
            can be used to get all movie data provided by TMDb
    """
    def __init__(self, api_key, movie_id):
        tmbd.set_key(api_key)
        tmbd.set_cache('null')
        tmbd.set_locale('en', 'US')
        self.movie = tmbd.Movie(movie_id)

    def title(self):
        """Returns a string of the title of the movie

        Returns:
            userrating: A string of the title
        """
        return self.movie.title

    def poster_url(self):
        """Returns a string of the poster url of the movie

        Returns:
            userrating: A string of the poster url of the movie
        """
        return self.movie.poster.geturl()

    def youtube_trailer_url(self):
        """Returns a string of the trailer url

        Returns:
            userrating: A string of the youtube url of the movie
        """
        return self.movie.youtube_trailers[0].geturl()

    def userrating(self):
        """Returns an int of the userrating of the movie

        Returns:
            userrating: An int of the userrating
        """
        userrating = int(self.movie.userrating * 10)
        return userrating
