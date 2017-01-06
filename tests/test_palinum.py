from formatlib.palinum import *

paligraph(1,34)
    
l = list()
for each in range(1, 34):
    l.append(palinum(each))
for each in l:
    print ispalinum(each), each

for x, y in zip([7,4,2,1], [3,7,16,34]):
    print x, y, palinumlist(x, y)

