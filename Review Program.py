Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Jacob Miles Review Program

title = input("What is the title?: ")
media_type = input("What is the media type?: ")
genre = input("What is the genre?: ")
year_created = input("What year was it created?: ")
description = input("Description of media:")
rating = float(input("Rating?: "))

new_list = [title, media_type, genre, year_created, description, rating,]
movies = []
music = []
videogames = []

if media_type =="movie":
    movies.append(new_list)

if media_type == "videogame":
    videogames.append(new_list)

if media_type == "music":
    music.append(new_list)

if media_type == "movie":    
    print "movies" + str(movies)
if media_type == "music":
    print "music" + str(music)
if media_type== "videogame":
    print "videogames" + str(videogames)
