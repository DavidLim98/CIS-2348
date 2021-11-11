# David Lim, 1625277

s = input()
lst = []
for x in s.split(' '): 
    if int(x) >= 0: 
        lst.append(int(x)) 
        lst.sort()
for x in lst:
    print(x,end=' ')
