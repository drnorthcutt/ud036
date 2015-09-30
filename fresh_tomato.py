import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Udacian Fav Movies!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .movie-poster:hover {
            -webkit-transform: scale(1.2);
            -moz-transform: scale(1.2);
            -o-transform: scale(1.2);
            transform: scale(1.2);
            transition: all 0.3s;
            -webkit-transition: all 0.3s;
        }
        .movie-poster:hover .quote {
            display:inline-block;
        }
        .movie-poster:hover .navbar-brand {
            display:none;
        }
        #test:hover #change {
            color: white;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .btn {
            background: #34282C;
            background-image: -webkit-linear-gradient(top, #34282C, #b82b3d);
            background-image: -moz-linear-gradient(top, #34282C, #b82b3d);
            background-image: -ms-linear-gradient(top, #34282C, #b82b3d);
            background-image: -o-linear-gradient(top, #34282C, #b82b3d);
            background-image: linear-gradient(to bottom, #34282C, #b82b3d);
            -webkit-border-radius: 28;
            -moz-border-radius: 28;
            border-radius: 28px;
            font-family: Arial;
            color: #B6B6B4;
            font-size: 10px;
            padding: 3px 10px 3px 10px;
            text-decoration: none;
        }
        .btn:hover {
            background: #b82b3d;
            background-image: -webkit-linear-gradient(top, #b82b3d, #34282C);
            background-image: -moz-linear-gradient(top, #b82b3d, #34282C);
            background-image: -ms-linear-gradient(top, #b82b3d, #34282C);
            background-image: -o-linear-gradient(top, #b82b3d, #34282C);
            background-image: linear-gradient(to bottom, #b82b3d, #34282C);
            text-decoration: none;
            color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-poster', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body style="background-color:#2B1B17">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <div id="mainname"><a class="navbar-brand" href="#">Udacian Movie Trailers</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 text-center movie-tile" id="test">
    <div class="movie-poster" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><img src="{poster_image_url}" width="220" height="342" title="Starring: {actors}">
    </div>
    <div style="color: #B6B6B4" id="change"><p>({movie_year})</p>
        <h2 id="change">{movie_title}</h2>
    </div>
    <div class="fluid-row" style="display:inline-block">
        <div class="col-md-4"><!-- Trigger the modal with a button -->
        <button type="button" class="btn btn-xs" data-toggle="modal" data-target="#{word}"> Get More Info </button>
        </div><!-- Modal -->
        <div class="modal fade" id="{word}" role="dialog">
            <div class="modal-dialog">
                <!-- Modal content-->
                <div>
                    <div class="modal-header navbar navbar-inverse" style="color: #B6B6B4">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h2 class="modal-title">{movie_title}</h2>
                        <p>Released {movie_year}</p>
                    </div>
                    <div class="modal-body" style="background: #34282C; color: #B6B6B4;">
                        <p>Stars: {actors}</p>
                        <h3>{storyline}</h3>
                    </div>
                    <div style="background: #34282C>
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-4"><a href="{imdb}" class="btn btn-xs" target="_blank">   IMDb Page   </a>
        </div>
        <div class="col-md-4"><a href="{rotten}" class="btn btn-xs" target="_blank">Rotten Tomatoes</a>
        </div>
    </div>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            actors=movie.actors,
            storyline=movie.storyline,
            trailer_youtube_id=trailer_youtube_id,
            movie_year=movie.movie_year_released,
            word=movie.word,
            imdb=movie.imdb_link,
            rotten=movie.rotten_tomatoes_link
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
