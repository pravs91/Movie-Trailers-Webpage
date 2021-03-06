import media
import freshtomatoes

# create media.Movie() instances for all movies
# constructor args are (title,
#                       story_line,
#                       poster_image_url,
#                       trailer_youtube_url)

# class instance for movie "Kabali"
kabali = media.Movie("Kabali",
                    "Before Indian Independence, many Tamils from South \
                    India were sent to Malaysia as indentured laborers. \
                    Kabali, the protagonist, fights this oppression. \
                    After a lengthy imprisonment, he is more determined\
                    than ever to fight for his people.",
                    "http://st1.bollywoodlife.com/wp-content/uploads/2016/06/kabali-poster-2.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=9mdJV5-eias"  # NOQA
                    )

# class instance for movie "The Imitation Game"
imitation_game = media.Movie("The Imitation Game",
                            "During World War II, mathematician Alan Turing \
                            tries to crack the enigma code with help from \
                            fellow mathematicians.",
                            "http://cdn5.thr.com/sites/default/files/2014/09/the_imitation_game_a_p.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=S5CjKEFb-sM"
                            )

# class instance for movie "Hidder Figures"
hidden_figures = media.Movie("Hidden Figures",
                            "The story of a team of African-American women \
                            mathematicians who served a vital role in NASA \
                            during the early years of the US space program.",
                            "http://static.vibe.com/files/2016/12/hidden-figures-soundtrack-cover-1481306900.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=RK8xHq6dfAo&t=3s"
                            )

# class instance for movie "Kong Skull Island"
kong = media.Movie("Kong Skull Island",
                    "A team of scientists explore an uncharted island in the \
                    Pacific, venturing into the domain of the mighty Kong, \
                    and must fight to escape a primal Eden.",
                    "https://posterspy.com/wp-content/uploads/2016/08/Kong-Skull-Island@05x.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=44LdLqgOpjo")

# class instance for movie "Dawn of the Planet of the Apes"
planet_of_the_apes = media.Movie("Dawn of the Planet of the Apes",
                                "A growing nation of genetically evolved apes\
                                led by Caesar is threatened by a band of human\
                                survivors of the devastating virus unleashed a\
                                decade earlier.",
                                "http://s3.foxmovies.com/foxmovies/production/films/1/images/posters/368-asset-page.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=3sHMCRaS3ao"
                                )

# class instance for movie "Dangal"
dangal = media.Movie("Dangal",
                    "Former wrestler Mahavir Singh Phogat and his two\
                    wrestler daughters struggle towards glory at the \
                    Commonwealth Games in the face of societal oppression.",
                    "http://st1.bollywoodlife.com/wp-content/uploads/2016/07/748607.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=x_7YlGv9u1g"
                    )

# Array of Movie instances
movies = [kabali, imitation_game, hidden_figures,
          kong, planet_of_the_apes, dangal]

# pass movies array to create html
freshtomatoes.open_movies_page(movies)

# print media.Movie.__name__
# print media.Movie.__module__
# print media.Movie.__doc__
