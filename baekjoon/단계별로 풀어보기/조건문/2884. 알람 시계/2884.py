h,m = map(int, input().split())

if m - 45 < 0:
    mm = 60 + m - 45
    hh = h - 1 if h - 1 >= 0 else 23
else:
    mm = m - 45
    hh = h

print(hh, mm)