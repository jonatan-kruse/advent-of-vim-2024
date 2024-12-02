import sys

def isCorrect(l):
   isDec = False
   isInc = False
   prev = None
   for n in l:
       if prev == None:
           prev = n
           continue
       if not isDec and not isInc:
           if n > prev:
               isInc = True
           elif n < prev:
               isDec = True
           else:
               return 0
       elif isDec and n >= prev:
           return 0
       elif isInc and n <= prev:
           return 0
       if abs(prev - n) > 3 or prev == n:
           return 0
       prev = n
   return 1

l1 = [list(map(int, line.split())) for line in sys.stdin]
res = sum([isCorrect(l) for l in l1])

print(res)


