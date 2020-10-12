# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:48:03 2020

@author: mmbio
"""

import Node as ND
import NodeGrid as NG

import cv2
import numpy as np


bilde = cv2.imread('FloroBW.png', 1)

høydePix, breddePix, kanaler = bilde.shape

bildeBW = np.zeros((høydePix, breddePix))

for i in range(høydePix):
    for j in range(breddePix):
        if (sum(bilde[i, j])/3) > 122:
            bildeBW[i,j] = 255
        else:
            bildeBW[i,j] = 0
            
            
grid = NG.NodeGrid(høydePix, breddePix)

for i in range(høydePix):
    for j in range(breddePix):
        if bildeBW[i, j] == 0:
            grid.Grid[i,j].IsObstacle = False
        else:
            grid.Grid[i,j].IsObstacle = True


# first number is down, second is forward
start = (200, 100)
goal = (110, 450)

path = grid.AStar(grid.Grid, start, goal)

for point in path:
    bilde[point] = [0,255,0]


cv2.imshow('Pathfinder', bilde)
cv2.waitKey(0)
cv2.destroyAllWindows()