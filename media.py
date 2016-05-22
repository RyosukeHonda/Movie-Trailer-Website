#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser

class Movie(object):
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,year,rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.rating = rating

    def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)