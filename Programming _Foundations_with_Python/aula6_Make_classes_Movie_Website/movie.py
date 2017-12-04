"""
clss Movie
    Things to remember
        - title
        - storykine
        - poster_image
        - youtube_trailer
"""

from movies import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://pt.wikipedia.org/wiki/Toy_Story#/media/File:Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)