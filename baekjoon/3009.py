from sys import stdin
temp = {}

for i in range(0,3):
    a, b = map(int, stdin.readline().split())
    if not temp.get('x'):
        temp['x'] = [a]
    else:
        if a in temp['x']:
            temp['x'].remove(a)
        else:
            temp['x'].append(a)
        
    
    if not temp.get('y'):
        temp['y'] = [b]
    else:
        if b in temp['y']:
            temp['y'].remove(b)
        else:
            temp['y'].append(b)
            
print(temp['x'][0], temp['y'][0])
        
         