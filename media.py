# Author: Daniel R. Northcutt
# September 2015
import webbrowser


class Movie():
	"""Provides storage for movie related information."""

    def __init__(self, movie_title, movie_storyline, poster_url,
                 trailer_url, movie_year, starring_actors, one_word, imdb_url,
                 rotten_tomatoes_url):
        """Stores variables for a movie.

        Args:
            movie_title (str):  The title of the movie.
            movie_storyline (str):  The synopsis or abstract of the movie.
            poster_url (url):  The full URL to the movie poster.
            trailer_url (url):  The full URL to the movie trailer.
            movie_year (str):  The year the movie was released.  Although
                intended for only a year, i.e. 2015, a full date may be
                supplied, i.e. 25 July 2015 or some such string.
            starring_actors (str): The starring actors. They may be space or
                comma delimited.
            one_word (str):  Any valid word that may be used as an id in
                html.  It is usually easiest to use the same word as the
                identifier, since it must be unique within the script.
            imdb_url (url):  The full URL to the imdb.com listing for the
                movie.
            rotten_tomatoes_url (url):  The full URL to the
                rottentomatoes.com listing for the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
        self.movie_year_released = movie_year
        self.actors = starring_actors
        self.word = one_word
        self.imdb_link = imdb_url
        self.rotten_tomatoes_link = rotten_tomatoes_url

    def show_trailer(self):
        """Shows the movie trailer."""
        webbrowser.open(self.trailer)
