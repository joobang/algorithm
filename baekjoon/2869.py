import math
import sys

A, B, V = map(int , sys.stdin.readline().split())

#print(math.ceil(V/A))
diff = A - B;
if A == V:
    print(1)
else:
    if diff == 1: 
        print(V - A + 1)
    else:
        print(math.ceil((V - A)/diff) + 1)
        
