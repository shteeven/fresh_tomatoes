from entertainment_center import create_movie_list
import re
import webbrowser
import os

# A single movie entry html template
movie_tile = '''
  <div ng-click="openModal({movie})" class="col-md-4 col-sm-6 col-xs-12 movie-tile" ng-class="{{'unrevealed': moviesRevealed < {movie_enum}}}">
    <img src="{poster_image_url}">
    <h2>{movie_title}</h2>
  </div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for i, movie in enumerate(movies):
        movie_json = movie.__dict__
        # Append the tile for the movie with its content filled in
        content += movie_tile.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_enum=i,
            movie=movie_json
        )
    return content


def insert_movie_tiles(content):
    with open('precompiled/precompiled.html', 'r') as f:
        html = f.read()

    #create re match
    replace_begin = '<!--movietile begin-->'
    replace_end = '<!--movietile end-->'
    replace_re = replace_begin + '.*?' + replace_end

    #delete old and insert new content
    html = re.sub(replace_re, content, html, flags=re.DOTALL)

    with open('index.html', 'w') as f:
        f.write(html)


def main():
    movie_list = create_movie_list('precompiled/movies.json')
    movie_tiles_content = create_movie_tiles_content(movie_list)
    insert_movie_tiles(movie_tiles_content)
    url = os.path.abspath('index.html')
    webbrowser.open('file://' + url, new=2)

main()
