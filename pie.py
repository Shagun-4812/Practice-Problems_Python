import random

area1=0
area2=0

for i in range(1000):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)  

    if x**2+y**2<=1:
        area1+=1
    else:   
        area2+=1


pie=4*area1/(area1+area2)
print(pie)

