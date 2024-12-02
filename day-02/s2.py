import sys

def isCorrect(l):
   for index1 in range(len(l) + 1):
       isDec = False
       isInc = False
       success = 1
       prev = None
       for index2, n in enumerate(l):
           if index1 == index2:
               continue
           if prev == None:
               prev = n
               continue
           if not isDec and not isInc:
               if n > prev:
                   isInc = True
               elif n < prev:
                   isDec = True
               else:
                   success = 0
           elif isDec and n >= prev:
               success = 0
           elif isInc and n <= prev:
               success = 0
           if abs(prev - n) > 3 or prev == n:
               success = 0
           prev = n
       if success == 1:
           return 1
   return 0

l1 = [list(map(int, line.split())) for line in sys.stdin]
res = sum([isCorrect(l) for l in l1])

print(res)


