h,m = map(int, input().split())
total_time = int(input())

dh = total_time // 60
dm = total_time % 60

h = h + dh
m = m + dm

if m >= 60:
    m = m - 60
    h += 1
    
if h > 23:
    h = h - 24
    
print(h,m)
    