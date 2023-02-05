cicle = 1
firstnum = int(input())
num = firstnum
while(True):
    a = int(num / 10)
    b = num % 10
    num = b*10 + (a+b)%10
    print(num)
    input()
    if firstnum == num :
        break
    cicle += 1
print(cicle)