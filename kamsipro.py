# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:30:24 2019

@author: Anonymousgod
"""

import turtle

turtle.color("red", "blue")
turtle.begin_fill()

for i in range(9):
    turtle.forward(250)
    turtle.left(160)
    
turtle.end_fill()
turtle.done