# bounce.py
#
# Exercise 1.5

bounce_height=100 #meter
bounce=3/5 #the height
num_bounce=1

while num_bounce<=10:
    bounce_height=bounce_height*bounce
    print(num_bounce, " ", round(bounce_height, 4))
    num_bounce+=1
