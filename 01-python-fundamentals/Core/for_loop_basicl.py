#basic
for i in range (151):
    print(i)

#multiples of 5
for i in range (5,1001,5):
    print(i)

#counting the Dojo Way
for i in range (1,101):
    if i % 10 == 0 :
        print("Coding Dojo")
    elif i % 5 == 0 :
        print("Coding")
    else :
        print(i)

#That Sucker's Huge
sum = 0
for i in range (500001):
    sum += i
print(sum)

#countdown by 4
for i in range (2018,0,-4):
    print(i)

#flexible counter
lowNum = 3
highNum = 60
mult = 5
for num in range (lowNum, highNum + 1):
    if num % mult == 0:
        print(num)