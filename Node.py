# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 05:00:30 2020

@author: mmbio
"""

import math
import numpy as np


class Node:
    def __init__(self, pos):
        self.IsObstacle = False
        self.Tested = False
        
        # Parent, Local, Global
        self.par = None
        self.loc = math.inf
        self.glo = math.inf
        
        #Position
        self.pos = pos
        
        
    def Info(self):
        print("Position: ", self.pos)
        
        if self.par != None:
            print("Parent: ", self.par.pos)
        
        print("Local: ", self.loc)
        print("Global: ", self.glo)
        
    def GetGlo(self):
        return self.glo