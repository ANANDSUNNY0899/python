
import random


head = 0
tail = 0


for i in range(10000000):
    tossCoin = random.randint(1, 2)
    if(tossCoin == 1):
        head += 1
    else:
        tail += 1

print("Total Head : " + str(head))
print("Total Tail: " + str(tail))


