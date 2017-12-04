import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "2h45m",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "2h45m",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "2h45m",
                             "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "2h45m",
                         "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                         "https://upload.wikimedia.org/wikipedia/pt/8/82/Ratatouille_p%C3%B4ster.jpg",
                         "https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "2h45m",
                                "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
                           "2h45m",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                           "https://upload.wikimedia.org/wikipedia/pt/d/dc/The_Hunger_Games.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

man_on_fire = media.Movie("Man on Fire",
                          "2h45m",
                          "In Mexico City, a former assassin swears vengeance on those who committed an unspeakable act against the family he was hired to protect.",
                          "https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg",
                          "https://www.youtube.com/watch?v=eDDh50B6kA4")

the_big_bang = media.TvShow ("The Big Bang Theory",
                             "0h45m",
                             "11",
                             "2 The Retraction Reaction",
                             "CBS",
                             "https://upload.wikimedia.org/wikipedia/en/5/56/The_Big_Bang_Theory_Season_1.jpg",
                             "https://www.youtube.com/watch?v=e8ykcZUQlNU")

#fresh_tomatoes - def open_movies_page

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, man_on_fire, the_big_bang]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS) # Class variables
#print(media.Movie.__doc__) # Print class documentation - http://www2.lib.uchicago.edu/keith/courses/python/class/5/
#print(the_big_bang.duration)