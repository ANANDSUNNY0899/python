
import random



ad_defence = 0
ad_love_destroy = 0
ad_bill = 0
ad_coprate = 0


total = 10000000
for i in range(total):
    future = random.randint(1, 4)
    if(future == 1):
        ad_defence += 1
    elif(future == 3):
        ad_love_destroy += 1
    elif(future == 2):
        ad_bill += 1
    elif(future == 4):
        ad_coprate += 1


print("Aadarsh Defence: " + str((ad_defence / total) * 100) + "%")
print("Aadarsh Destroy In Love: " + str((ad_love_destroy / total) * 100) + "%")
print("Aadarsh Become Billionare: " + str((ad_bill / total) * 100) + "%")
print("Aadarsh In Coprate Sector: " + str((ad_coprate / total) * 100) + "%")
