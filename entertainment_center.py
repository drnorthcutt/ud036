# Author: Daniel R. Northcutt
# September 2015
"""
Movie Trailer Website movie listing script for the creation of a web page.

This program is the result of the Full Stack Web Developer Nanodegree at
http://www.udacity.com and more specifically of the course Programming
Foundations with Python.

It is intended to order and array information for movies to construct a
static web page showing various movie posters, together with relevant
information, and to play a trailer for a selected movie.  For this, it uses
the Movie class from media.py, passing the information through to
brazen_pears.py for integration of the information and creation of the
static page.

Requires:

    Python v2.*

    The following files should all be in the same directory:

        entertainment_center.py
        brazen_pears.py
        media.py

Running the program:

    Run this file via terminal (or command prompt on a Windows machine), by
    navigating to the directory of the three files and typing:

        python entertainment_center.py

Arguments:

    movie_title:  The name of a movie.
    movie_storyline:  A synopsis or description of the movie.
    poster_url:  A full URL to the movie's poster art.
    trailer_url:  A full URL to the movie's trailer.
    movie_year:  The release date of the movie (may be just the year or the
        full date).
    starring_actors:  Any number of the actors from the movie, comma or space
        delimited.
    one_word:  Any word or short string made as one word for identification
        purposes within the subsequent html file.  It may be the same as the
        identifier.
    imdb_url:  A full URL to the movie's IMDb.com page.
    rotten_tomatoes_url:  A full URL to the movie's rottentomatoes.com page.

Example:

    identifier = media.Movie(movie_title,
                             movie_storyline,
                             poster_url,
                             trailer_url,
                             movie_year,
                             starring_actors,
                             one_word,
                             imdb_url,
                             rotten_tomatoes_url)

    So, for a movie called Crazy Pants, released in 2020, about a private
    detective who likes to glue discarded rubish he has found to his
    trousers and wear them to black tie events, the code might be:

        crazy = media.Movie("Crazy Pants",
                            ('A private eye, who likes to glue garbage onto '
                             'his pants, wears them to black tie events... '
                             'Crazy things happen!'),
                            "http://some_url.com/crazy_pants.jpg",
                            "http://some_url.com/crazy_pants.mp4",
                            "2020",
                            "Mr. Bean, Mr. T, Mr. E, Ms. Teak",
                            "crazy",
                            "http://www.imdb.com/some_directory/",
                            "http://www.rottentomatoes.com/some_dir/")

Sources Used:

    Poster art:  Wikipedia.
        https://www.wikipedia.org

    Movie Trailers:  YouTube.
        https://www.youtube.com

    Release date, Stars, IMDb link:  IMDb
        http://www.imdb.com/

    Rotten Tomatoes link:  Obviously, Rotten Tomatoes.
        http://www.rottentomatoes.com/

    URL shortening:  Since Wikipedia in particular seems to return extremely
        long URLs, I found a shortener necessary.
        https://goo.gl/

"""
import media
import brazen_pears


blade = media.Movie("Blade Runner",
                    ('The story of a sort of bounty hunter charged with '
                     'finding and terminating androids who have run amok.'),
                    "https://goo.gl/dpmq21",
                    "https://youtu.be/W_9rhPDLHWk",
                    "1982",
                    "Harrison Ford, Rutger Hauer, Sean Young",
                    "blade",
                    "http://www.imdb.com/title/tt0083658/",
                    "http://www.rottentomatoes.com/m/blade_runner_1982/")

starwars = media.Movie("Star Wars: Episode V",
                       ('A young man trains to be a wizard while his friends '
                        'are stalked by a heavy-breathing magical cyborg.'),
                       "https://goo.gl/i0clbu",
                       "https://youtu.be/JFA-Oip1wF8",
                       "1980",
                       "Mark Hamill, Harrison Ford, Carrie Fisher",
                       "starwars",
                       "http://www.imdb.com/title/tt0080684/",
                       "http://www.rottentomatoes.com/m/empire_strikes_back/")

dude = media.Movie("Dude, Where\'s My Car?",
                   ('Stoners wake up after a party and... pudding, aliens, '
                    'mysteriously powerful things, powerfully mysterious '
                    'things, Zoltan!'),
                   "https://goo.gl/XPLccy",
                   "https://youtu.be/B9gI8hk84Xs",
                   "2000",
                   "Ashton Kutcher, Seann William Scott",
                   "dude",
                   "http://www.imdb.com/title/tt0242423/",
                   "http://www.rottentomatoes.com/m/dude_wheres_my_car/")

clockwork = media.Movie("A Clockwork Orange",
                        ('A young sociopath, who loves classical music, rape, '
                         'and \"ultraviolence,\" does what he does and gets '
                         'caught. Gets experimented upon... hates Beethovan.'),
                        "https://goo.gl/x3Jb5n",
                        "https://youtu.be/G7fO3bzPeBQ",
                        "1971",
                        "Malcolm McDowell, Patrick Magee, Michael Bates",
                        "clockwork",
                        "http://www.imdb.com/title/tt0066921/",
                        "http://www.rottentomatoes.com/m/clockwork_orange/")

bride = media.Movie("A Princess Bride",
                    ('A sick boy\'s grandfather reads him a story...leaves in '
                     'the mushy stuff, pirates, sword fights, '
                     'inconcievability, extra fingers, near death, and big '
                     'rats.'),
                    "https://goo.gl/FV5SVn",
                    "https://youtu.be/njZBYfNpWoE",
                    "1987",
                    "Cary Elwes, Mandy Patinkin, Robin Wright",
                    "bride",
                    "http://www.imdb.com/title/tt0093779/",
                    "http://www.rottentomatoes.com/m/princess_bride/")

fight = media.Movie("Fight Club",
                    ('One man seeks to change... A group of men try to... '
                     'Well... On second thought, I just can\'t talk about it. '
                     'And, also, I can\'t talk about it.'),
                    "https://goo.gl/SME71F",
                    "https://youtu.be/SUXWAEX2jlg",
                    "1999",
                    "Brad Pitt, Edward Norton, Helena Bonham Carter",
                    "fight",
                    "http://www.imdb.com/title/tt0137523/",
                    "http://www.rottentomatoes.com/m/fight_club/")

# Creates an array
movies = [blade, clockwork, dude, fight, bride, starwars]

# Returns the array
brazen_pears.open_movies_page(movies)
