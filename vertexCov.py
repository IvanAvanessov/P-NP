import sys
import bisect
import pyskip
#import skiplist 
import numpy as np

# reduction VC1 not applicable as I am eliminating all isolated indices on read
# call the script "python3 vertexCov.py k", where k is the tested parameter

filePath = ""
#fileName = "AS-oregon-1.txt"
fileName = "test.txt"

 
fo = None # file handler

k = 10 # my coefficient with default value 10

graph = {} # each vertex has a set of adjasent vertices in a map
minVertexCover = []
minVertexSize = 0

def initialize():
    global fo
    fo = open(filePath + fileName, "r")
    if(len(sys.argv) > 1):
        global k
        k = int(sys.argv[1])

def createGraph():
    global graph

    for line in fo:
        edge = [int (i) for i in line.split()]
    
        #if a vertice is already in min cover, then ignore its edges
        if binarySearch(minVertexCover, edge[0]) > -1 \
           or binarySearch(minVertexCover, edge[0]) > -1: #ignore such edge
               continue

        # #if a vertice is already in min cover, then ignore its edges
        # if ignoredVertices.find(edge[0]) is not None \
        #     or ignoredVertices.find(edge[1]) is not None:
        #     continue
        
        if k < 1 :
            print("Min Vertex Cover is not possible for this graph with parameter k = " + str(k))
            exit

        if edge[0] not in graph:
            graph[edge[0]] = pyskip.Skiplist()
            graph[edge[0]].insert(edge[1])
        else: #inserting in order
            graph[edge[0]].insert(edge[1])
        
        if edge[1] not in graph:
            graph[edge[1]] = pyskip.Skiplist()
            graph[edge[1]].insert(edge[0])
        else: #inserting in order
            graph[edge[1]].insert(edge[0])

        print(edge)

        checkEntries(edge[0])
        checkEntries(edge[1])

# checking if current amount of edges already exceeds k
# if exceeds, add vertex to min cover and remove its edges
def checkEntries(vertice):
    global k
    global graph
    print(vertice)
    print("atat")

    if len(graph[vertice]) > k :
        k = k - 1
        ignoredVertices.insert(vertice)
        edges = graph[vertice]
        del graph[vertice]
        
        for edge in edges:
            print(edge.value)
            if(len(graph[edge.value]) == 1):
                del graph[edge.value]
            else:
                graph[edge.value].remove(vertice)   
        return True
    return False

def reductionVC2():
    global k
    global graph
    shouldRestart = True
    while(shouldRestart):
        for vertice in graph:
            #for edge in graph[vertice]:
            print(str(vertice) + " - " + str([i.value for i in graph[vertice]]))
            #print(str(vertice) + " - " + str(len(graph[vertice])))
            
        shouldRestart = False
        for vertice in graph:
            if(checkEntries(vertice)): #something was deleted, start over as our k changed
                if k < 1 and len(graph) > 0:
                    print("Min Vertex Cover is not possible for this graph with parameter k = " + str(k))
                    exit
                shouldRestart = True
                break

def binarySearch(a, x):
    i = bisect.bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

if __name__ == "__main__":
    initialize()
    createGraph()
    reductionVC2()
    
    #li1 = [1, 3, 4, 4, 4, 6, 7] 
    #print(binarySearch(li1, 4))
    #print(li1)
    #print(ignoredVertices)
    # for item in ignoredVertices:
    #     print(item.value)
    
    #print(ignoredVertices.find(4))
    for vertice in graph:
        #print([i.value for i in graph[vertice]])
        print(str(vertice) + " - " + str([i.value for i in graph[vertice]]))
        #print(str(vertice) + " - " + str(len(graph[vertice])))
    print(k)
