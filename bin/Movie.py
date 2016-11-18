## Class Movie is the result class. use str(movie) for nice string representation
class Movie:
    def __init__(self,
                 title,
                 rating,
                 time,
                 genre,
                 year,
                 synopsis
    #            castAndCrew
    ):
        self.title = title
        self.rating = rating
        self.time = time
        self.genre = genre
        self.year = year
        self.synopsis = synopsis

    def __str__(self):
        if not self.title or not self.rating:
            return "ERROR WITH MOVIE"

        return "Name: " + self.title.text + " -- Rating: " + self.rating.text + " -- Genre: " +  self.genre.text +\
               "  -- Year: " +self.year.text + " -- Synopsis: " + self.synopsis.text