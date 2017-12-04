# https://google.github.io/styleguide/pyguide.html

"""
aula6 - Make classes: Movie Website
cap8. Nos bartidores
self - cria as instancia da propria classe e associa aos nomes das variaveis. Ex. self..storyline = movie_storyline
agora é possivel chamar avatar.storyline

cap.13 revisando o vocabulario
https://postimg.org/image/4334faz6v/
class
self
constructor
instance variables
instance methods
instances

"""

import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)