#!/usr/bin/python
import argparse
import os
from graphviz import Digraph
import uuid
import time
import sys

#Handle unicode characters
reload(sys)
sys.setdefaultencoding("utf-8")

#Parse arguments
parser = argparse.ArgumentParser(description='File system visualizer using graphviz')
parser.add_argument('-r','--root', help='Root directory',required=True)
parser.add_argument('-d','--depth',help='Depth to traverse', required=True)
args = parser.parse_args()
 
## show values ##
print ("Root Directory: %s" % args.root)
print ("Depth: %s" % args.depth)

bfs = []

#The root directory to start from
root_dir = args.root
#The depth to traverse
depth = int(args.depth)

#The graph for visualizing the file structure
g = Digraph('G', filename='fs-visualizer.gv')
g.body.extend(['rankdir=LR', 'size="8,5"'])

#Initialize the BFS queue. Tuples in the format (DIR_NAME, DEPTH)
bfs.append((root_dir, 0))

#The current parent directory being traversed using the for loop
par_dir = root_dir

#While the queue is not empty
while len(bfs) != 0:
   par_dir = bfs.pop(0)
   for dirName, subdirList, fileList in os.walk(par_dir[0]):
      if par_dir[1] < depth:
         for folder in subdirList:
            bfs.append((os.path.join(par_dir[0], folder), par_dir[1] + 1))
            g.edge(str(par_dir[0]), str(os.path.join(par_dir[0], folder)), constraint='true')
      break

#Render the visualization
g.view()
