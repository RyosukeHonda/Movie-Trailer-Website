#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                      "A boy called Andy Davis (voice: ) uses his toys to act out a bank robbery.",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                      1995,
                      8.3)


movies=[toy_story,toy_story,toy_story,toy_story,toy_story,toy_story]

fresh_tomatoes.open_movies_page(movies)

