#!/usr/bin/env python
# -*- coding: utf-8 -*-

import media

toy_story = media.Movie("Toy Story",
                      "A boy called Andy Davis (voice: ) uses his toys to act out a bank robbery.",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print toy_story.title

toy_story.show_trailer()
