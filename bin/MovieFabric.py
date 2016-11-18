import Movie


## MovieFabric produces the Class Movie according to config
class MovieFabric:
    def __init__(self, browser):
        self.browser = browser

    def produceMovie(self, *extractionParams):
        movieargs = []
        for paramValue in extractionParams:
            extracted = self.browser.getByXpath(paramValue)
            movieargs.append(extracted)
        return Movie.Movie(*movieargs)
