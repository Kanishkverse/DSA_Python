
import random
import os
lis = []
for _ in range(100):
    lis.append(random.randint(1, 100))
print(set(lis))
a1 = lis
with open('/Users/kanishk/Desktop/CPS 501/numbers.txt', 'w') as num:
    for item in num:
        # write each item on a new line
        num.write("%s\n" % item)
    print('Done')


with open("/Users/kanishk/Desktop/CPS 501/numbers.txt",'r') as file:
    lines = file.readlines()

with open("/Users/kanishk/Desktop/CPS 501/numbers2.txt",'w') as file:
    for line in lines[:int(len(lines)/2)]:
        file.write(line)

with open("/Users/kanishk/Desktop/CPS 501/numbers1.txt",'w') as file:
    for line in lines[int(len(lines)/2):]:
        file.write(line)



