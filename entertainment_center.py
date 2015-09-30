# Author: Daniel R. Northcutt
#
"""
Movie Trailer Website movie listing script for fresh_tomato.

This program is the result of the Full Stack Web Developer Nanodegree at
http://www.udacity.com and more specifically of the course Programming
Foundations with Python.

It is intended to order and array information for movies to construct a static
web page showing various movie posters, together with relevant information,
and to play a trailer for a selected movie.

To function properly, entertainment_center.py, fresh_tomato.py, and media.py
should all be located in the same directory.


"""
import media
import brazen_pears

# Images from Wikipedia.com
# Date / Stars from IMDb.com
# Videos from youtube.com

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
                        'stalked by a heavy-breathing magical cyborg.'),
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


movies = [blade, clockwork, dude, fight, bride, starwars]

brazen_pears.open_movies_page(movies)
