# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 05:00:05 2020

@author: mmbio
"""

import math
import numpy as np

import Node as ND


class NodeGrid:
    def __init__(self, Height, Width):
        self.Grid = self.GenerateNodeGrid(Height, Width)

    def GenerateNodeGrid(self, Height, Width):
        nodeGrid = np.empty((Height, Width), dtype = object)
        
        for h in range(Height):
            for w in range(Width):
                nodeGrid[h, w] = ND.Node((h, w))
                
        return nodeGrid
    
    
    def FindNeighbour(self, NodeGrid, Node):
        Neighbours = []
        
        # Is it an edge node on x-axis? 
        if 0 < Node.pos[0] < len(NodeGrid) - 1:
            xi = (0, -1, 1)
        elif Node.pos[0] > 0:
            xi = (0, -1)
        else:
            xi = (0, 1)
            
         # Is it an edge node on y-axis?
        if 0 < Node.pos[1] < len(NodeGrid) - 1:
            yi = (0, -1, 1)
        elif Node.pos[1] > 0:
            yi = (0, -1)
        else:
            yi = (0, 1)
            
        for a in xi:
            for b in yi:
                # Skip the node itself, or if the node is an obstacle
                if a == b == 0 or NodeGrid[Node.pos[0] + a, Node.pos[1] + b].IsObstacle == True:
                    continue
                
                Neighbours.append(NodeGrid[Node.pos[0] + a, Node.pos[1] + b])
                
        return Neighbours
                
    
    def GlobalDistance(self, StartPos, EndPos):
        return math.sqrt((EndPos[0] - StartPos[0])**2 + (EndPos[1] - StartPos[1])**2) #1
    
    
    def ParentChain(self, Node, parentChain):
        if Node.par != None:
            self.ParentChain(Node.par, parentChain)
            parentChain.append(Node.pos)
    
    
    def AStar(self, NodeGrid, StartPos, EndPos):
        startNode = NodeGrid[StartPos]
        endNode = NodeGrid[EndPos]
        mainNode = NodeGrid[StartPos]
        
        mainNode.loc = 0
        mainNode.glo = self.GlobalDistance(StartPos, EndPos)
        
        NodeToTest = []
        NodeToTest.append(mainNode)
        
        distance = 1
        
        while len(NodeToTest) > 0 or endNode.Tested == False:
            Neighbours = self.FindNeighbour(NodeGrid, mainNode)
            
            for neighbour in Neighbours:
                if mainNode.loc + distance < neighbour.loc:
                    neighbour.par = mainNode
                    neighbour.loc = neighbour.par.loc + distance
                    neighbour.glo = neighbour.loc + self.GlobalDistance(neighbour.pos, endNode.pos)
                    
                    if neighbour not in NodeToTest and neighbour.Tested == False:
                        NodeToTest.append(neighbour)
                
            mainNode.Tested = True
            
            for node in NodeToTest:
                if node.Tested == True:
                    NodeToTest.remove(node)
            
            if len(NodeToTest) > 0:
                NodeToTest.sort(key=ND.Node.GetGlo)
                mainNode = NodeToTest[0]
                
        parentChain = [startNode.pos]
        self.ParentChain(endNode, parentChain)
        
        return parentChain
    
    















