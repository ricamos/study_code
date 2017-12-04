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
class variables ***
"""

import webbrowser

class Video():
    def __init__(self, movie_title, movie_duration):
        self.title = movie_title
        self.duration = movie_duration

class Movie(Video):
    ''' This class provades a way to store movie related information'''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    #10 reutilizando metodos
    # Testar reutilizar Video e Movie
    def __init__(self, movie_title, movie_duration, season, episode, tv_station, poster, trailer):
        Video.__init__(self, movie_title, movie_duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        self.poste = poster
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    #def get_local_listing():