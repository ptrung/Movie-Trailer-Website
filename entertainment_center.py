from tmdb3_access import TmdbMovie
from media import Movie
from fresh_tomatoes import open_movies_page

# tmdb_api
tmdb_api_key = 'ed881cff77a6d0a8ff0e39321052adf7'

# Instance Tmdb need the api key and the movie id to provide data
your_name_tmdb = TmdbMovie(tmdb_api_key, 372058)
your_name = Movie(your_name_tmdb.title(), 
                  your_name_tmdb.poster_url(), 
                  your_name_tmdb.youtube_trailer_url(), 
                  your_name_tmdb.userrating())

hunger_games_tmdb = TmdbMovie(tmdb_api_key, 70160)
hunger_games = Movie(hunger_games_tmdb.title(), 
                  hunger_games_tmdb.poster_url(), 
                  hunger_games_tmdb.youtube_trailer_url(), 
                  hunger_games_tmdb.userrating())

lion_king_tmdb = TmdbMovie(tmdb_api_key, 8587)
lion_king = Movie(lion_king_tmdb.title(), 
                  lion_king_tmdb.poster_url(), 
                  lion_king_tmdb.youtube_trailer_url(), 
                  lion_king_tmdb.userrating())

harry_potter_tmdb = TmdbMovie(tmdb_api_key, 12445)
harry_potter = Movie(harry_potter_tmdb.title(),
                     harry_potter_tmdb.poster_url(),
                     harry_potter_tmdb.youtube_trailer_url(),
                     harry_potter_tmdb.userrating())

wonder_tmdb = TmdbMovie(tmdb_api_key, 406997)
wonder = Movie(wonder_tmdb.title(),
               wonder_tmdb.poster_url(),
               wonder_tmdb.youtube_trailer_url(),
               wonder_tmdb.userrating())

# array of movies which will be shown on the website
movies = [your_name, hunger_games, lion_king, harry_potter, wonder]

#method for running website
open_movies_page(movies)



