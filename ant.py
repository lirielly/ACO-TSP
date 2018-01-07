# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 06:00:00 PM
"""

import math

# Class ant represents one ant and its path
class Ant(object):
    def __init__(self):
        self.path = []
        self.of_value = math.inf
        
