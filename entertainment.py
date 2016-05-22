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

shrek = media.Movie("Shrek",
                    "The Adventures of Puss In Boots",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=jYejzdBwvY4",
                    2001,
                    7.9)

bighero = media.Movie("Big Hero 6",
                      "The story of robot Baymax",
                      "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=bT8qmoCgxZg",
                      2014,
                      7.9)       

frozen = media.Movie("Frozen",
                     "Anna, a fearless optimist, sets off on an epic journey",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc",
                     2013,
                     7.6)
insideout = media.Movie("Inside Out",
                        "Riley, a young girl, is uprooted from her life in the Midwest" +\
                        "when her dad gets a job in San Fransisco",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=yRUAzGQ3nSY",
                        2015,
                        8.3)
minions = media.Movie("Minions",
                      "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who,"+\
                      "alongside her inventor husband Herb, hatches a plot to take over the world.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://www.youtube.com/watch?v=eisKxhjBnZ0",
                      2015,
                      6.5)
movies=[toy_story,shrek,bighero,frozen,insideout,minions]

fresh_tomatoes.open_movies_page(movies)

