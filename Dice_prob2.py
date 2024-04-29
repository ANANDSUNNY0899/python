import random

head=0;
tail=1;

for i in range(1,1000):
    coin = random.randint(1,2)
    if(coin==1):
        head+=1;
    else:
        tail+=1;

print("No of heads:"+str(head))
print("NO of tails:"+str(tail))
