__author__ = 'Shtav'
import re


class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url, story_line, director, release, actors, itunes, imdb, amazon):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.trailer_youtube_id = self.retrieve_youtube_id(trailer_youtube_url)
        self.story_line = story_line or ''
        self.director = director or ''
        self.release = release or ''
        self.actors = actors or ''
        self.itunes = itunes or ''
        self.imdb = imdb or ''
        self.amazon = amazon or ''

    def retrieve_youtube_id(self, youtube_url):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', youtube_url)
        youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        return youtube_id


