import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # list of movies to select from
        movies = ["The Big Lebowski", "Blue Velvet", "Toy Story", "Star Wars", "Amelie"]

        # randomly choose one of the movies
        randomIdx = random.randrange(len(movies))

        return movies[randomIdx]

    def get(self):
        movie = self.getRandomMovie()
        tomorrowMovie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<ul><li>" + movie + "</li></ul>"

        tomorrowResponse = "<h1>Tomorrow's Movie of the Day</h1>"
        tomorrowResponse += "<ul><li>" + tomorrowMovie + "</li></ul>"

        self.response.write(response)
        self.response.write(tomorrowResponse)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
