print("구구단 몇단을 계산할까요? (1~9)")

dan = int(input())

while (dan != 0):
    if dan >= 10:
        print("1부터 9사이의 숫자만 입력해주세요.\n")
    else: 
        print(f"구구단 {dan}단을 계산합니다.")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan*i} ")
    print("구구단 몇단을 계산할까요? (1~9)")
    dan = int(input())
else: print("구구단 게임을 종료합니다.")
