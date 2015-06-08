import json
from media import Movie

# _decode_list and _decode_dict courtesy of Mike Brennan
# http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv


def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def create_movie_list(movies_file):
    with open(movies_file, 'r') as f:
        data = json.loads(f.read(), object_hook=_decode_dict)
    i = 0
    movies = []
    while i < len(data):
        movies.append(Movie(
            title=data[i]['title'],
            poster_image_url=data[i]['poster_image_url'],
            trailer_youtube_url=data[i]['trailer_youtube_url'],
            story_line=data[i]['story_line'],
            director=data[i]['director'],
            release=data[i]['release'],
            actors=data[i]['actors'],
            itunes=data[i]['itunes'],
            imdb=data[i]['imdb'],
            amazon=data[i]['amazon']
        ))
        i += 1
    return movies


