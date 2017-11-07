from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    tom_movie = get_random_movie()
    while tom_movie == movie:
        tom_movie = get_random_movie()

    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tom_movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ["The Big Lebowski", "Inception", "Harry Potter and the Goblet of Fire", "Land Before Time", "Groundhog Day", "Saving Private Ryan"]
    # TODO: randomly choose one of the movies, and return it
    random_movie = movies[random.randint(0, len(movies) - 1)]
    return random_movie


app.run()
