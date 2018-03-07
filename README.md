# Movie Trailer Website
This project provides the code to build a website with your favorite movies. You only have to provide the movie ids of TMDb and all information will be created automatically.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Install

First of all, you have to install Python 2.7.11. The download can be found here: https://www.python.org/downloads/. 
During installation, ensure that pip is installed and that Python is added to your PATH.

In the next step, open your systems console and insert the following command to install the necessary module: 
`pip install tmdb3`

### Run

To run the project, follow these steps: 
1. Start the program IDLE
2. Open the file *entertainment_center.py*. (File -> Open ...)
3. Run the file. (Press F5) 

Now you can see the HTML Page with my favorite movies. By clicking on the movie posters, you can watch the trailer

### Configurate your own movies

To show your own favorite movies, you have to adapt the file *entertainment_center.py*. 
In this file you have several code blocks for different movies like: 
```python
your_name_tmdb = TmdbMovie(tmdb_api_key, 372058)
your_name = Movie(your_name_tmdb.title(),
                  your_name_tmdb.poster_url(),
                  your_name_tmdb.youtube_trailer_url(),
                  your_name_tmdb.userrating())
```

The number *372058* describes the movie, you want to display. This number is the TMDb id of the movie. You get this number by opening the movie page on TMDb (e.g. https://www.themoviedb.org/movie/372058-kimi-no-na-wa) Then you can see the id in the link. 

At the end you have to add all movie instances to the list at the end: 
```python
# array of movies which will be shown on the website
movies = [your_name, hunger_games, lion_king, harry_potter, wonder]
```

## Acknowledge

This project was built as part of the Udacity course "Fullstack Web Developer Nanodegree". The file *fresh_tomatoes.py* was provided by Udacity and is only slightly modified by me. 