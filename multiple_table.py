print("구구단 몇단을 계산할까요?")
num = int(input())

print(f"구구단 {num}단을 계산합니다.")

i = 1
while i < 10:
    mul = num * i
    result= (f"{num} x {i} = {mul}")
    print(result)
    i = i + 1 

