import webbrowser


class Movie:
    """
    A class to hold information about a movie.
    Constructor args:
    title (str): The movie title.
    story_line (str): The movie's story line.
    image_URL (str): A URL for the movie's poster.
    trailer_URL (str): A URL for the movie's trailer.
	"""

    def __init__(self, title, story_line, image_URL, trailer_URL):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = image_URL
        self.trailer_youtube_url = trailer_URL

    def playTrailer(self):
        webbrowser.open(self.trailerURL)
