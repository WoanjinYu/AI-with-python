import random
gu_num = random.randint(1,100)
print("숫자를 맞춰 보세요 (1~100)")
in_num = int(input())

while(gu_num is not in_num):
    if in_num > gu_num:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    in_num = int(input())
else: print(f"정답입니다. 숫자는 {gu_num}입니다.")