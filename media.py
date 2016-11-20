import webbrowser
"""
This class media defines the movie class.
"""


class Movie():
    """ To construct a movie, use title, storyline, poster image as .jpg, and trailer as video"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url= trailer
        
        print "created new movie " + movie_title + "!"
    
    def show_trailer(self):
        """ plays the trailer of the movie in a web browser"""
        print "in show_trailer"
        webbrowser.open(self.trailer)