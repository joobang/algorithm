def isY(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return 1
    else:
        return 0

year = int(input())

print(isY(year))
