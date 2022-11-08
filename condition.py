print("당신이 태어난 년도를 입력하세요")
year = 2022 - int(input()) + 1

if year <= 26 and year >= 20:
    print('대학생')
elif year <20 and  year >=17:
    print('고등학생')
elif year <17 and year >=14:
    print('중학생')
elif year <14 and year >=8:
    print('초등학생')
else: print('학생이 아닙니다')