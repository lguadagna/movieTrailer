import media
import fresh_tomatoes

"""
The class entertainment_center (Entertainment Center) defines a list "
" of movie objects and their attributes.
The moveis are put into a list and sent to a web page constructor.
"""



#Toy Story
toy_story = media.Movie("Toy Story",
                        "a story of a boy and his toys",
                        "toy_story_250_250.jpg",
                        "http://www.youtube.com/watch?v=KYz2wyBy3kc")

# Guardian of the Galaxy
avatar = media.Movie("Guardians of the Galaxy",
                    "A group of intergalactic criminals are forced to work "
                    "together to stop a fanatical warrior from taking control "
                    "of the universe. ",
                    "guardians.jpg", 
                    "https://www.youtube.com/watch?v=d96cjJhvlMA")

# Gone with the Wind
wind = media.Movie("Gone with the Wind",
                   "Epic Civil War drama focuses on the life of petulant "
                   "southern belle Scarlett O'Hara. Starting with her idyllic "
                   " on a sprawling plantation, the film traces her survival "
                   "through the tragic history of the South during the Civil "
                   "War and Reconstruction.",
                   "http://www.dvdsreleasedates.com/covers/gone-with-the-wind-dvd-cover-63.jpg",
                    "https://www.youtube.com/watch?v=0dTsfsr6-X8")

# Eternal Sunshine Movie information 
sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                   "Relationships are built from memories both good and bad. "
                   "Erasing them proves difficult",
                   "eternal_sunshine.jpg",
                    "https://www.youtube.com/watch?v=rb9a00bXf-U")

#Downton Abbey
abbey = media.Movie("Downton Abbey",
                   "Aristocratic English landed family at the turn of the Century",
                   "downton_abbey.jpg",
                    "https://www.youtube.com/watch?v=WPwaCjE8DcY")
#Super Size Me
size = media.Movie("Super Size Me",
                   "Survival of a lovely lady during civil war in the deep south",
                   "super_size.jpg",
                    "https://www.youtube.com/watch?v=LOvrkkj_T-I")               


movies = [toy_story, avatar, wind, sunshine, abbey, size]
fresh_tomatoes.open_movies_page(movies) 
