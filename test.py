# pyskip test

import sys
import bisect
import pyskip
#import skiplist 
import numpy as np


ignoredVertices = pyskip.Skiplist()

ignoredVertices.insert("50")
ignoredVertices.insert("51")
ignoredVertices.insert("56")
ignoredVertices.insert("49")
ignoredVertices.insert("14")
ignoredVertices.insert("55")
ignoredVertices.insert("1")
ignoredVertices.insert("0")
ignoredVertices.insert("2")
ignoredVertices.remove("0")

print(ignoredVertices.find("1"))
for item in ignoredVertices:
    print(item.value)
