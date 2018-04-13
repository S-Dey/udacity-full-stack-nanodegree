import webbrowser

class Movie:
    """A Class demonstrating class variables and pre-defined variables."""

    valid_ratings = ["U", "U/A", "A"]           # Class variables

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)       # It will play the trailer on Web browser.