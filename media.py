class Movie:
    """ A movie class

    Attributes:
        title (str): Title of the movie.
        trailer_youtube_url (str): The youtube url of the movie's trailer
        poster_image_url (str): An image of the movie's poster
        trailer_youtube_id (str): The youtube video id of the trailer
    """
    def __init__(self,
                 title, trailer_youtube_url, poster_image_url, trailer_youtube_id):
        """Creates a new instance of the Movie class

        Args:
            title (str): Title of the movie.
            trailer_youtube_url (str): The youtube url of the movie's trailer
            poster_image_url (str): An image of the movie's poster
            trailer_youtube_id (str): The youtube video id of the trailer

        Returns:
            Movie: A Movie class instance with the specified parameters

        """
        # Set the title of the class to the one passed into the function
        self.title = title
        # Set the youtube trailer url of the class to the one passed into the function
        self.trailer_youtube_url = trailer_youtube_url
        # Set the poster image url of the class to the one passed into the function
        self.poster_image_url = poster_image_url
        # Set the youtube trailer id of the class to the one passed into the function
        self.trailer_youtube_id = trailer_youtube_id