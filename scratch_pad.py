#hello worldc 출력
# print("Hello World!")

# A + B
# a, b = map(int, input().split())
# print(a + b)

# A - B
# a, b = map(int, input().split())
# print(a - b)

# A X B
# a, b = map(int, input().split())
# print(a * b)

#A / B
# a, b = map(int, input().split())
# print(a / b)

# 곱셈문제
# a = int(input())
# b = input()
# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))

#고양이 문제
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

#강아지
# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )""\"\"\"""\\""")
# print("|""\"""^""\"""`""    |")
# print("||_/=\\\\__|")

#새싹
# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

#두 수 비교하기
# a, b = map(int, input().split())
# if (a > b):
#     print(">")
# elif(a < b):
#     print("<")
# else:
#     print("==")

#시험성적
# a = int(input())
# if (a > 89):
#     print("A")
# elif(a > 79):
#     print("B")
# elif(a > 69):
#     print("C")
# elif(a > 59):
#     print("D")
# else:
#     print("F")

#윤년
# a = int(input())
# if a % 4 ==0 and a % 100 !=0 or a % 400 ==0:
#     print("1")
# else :
#     print("0")

#사분면 고르기
# a = int(input())
# b = int(input())
# if (a > 0 and b > 0):
#     print("1")
# elif(a < 0 and b > 0):
#     print("2")
# elif(a < 0 and b < 0):
#     print("3")
# else:
#     print("4")

#알람시계 
# a, b = map(int, input().split())
# c = (a * 60) + b - 45
# if c < 0:
#     c = c + 1440
# print(c // 60, c % 60) 

#오븐시계
# h, m = map(int, input().split())
# t = int(input())
# m = m+t
# h += m//60
# print(h%24,m%60)

# 주사위 세개
# a, b, c = map(int, input().split())
# if a == b == c:
#     print(10000 + a * 1000)
# elif a == b or b == c or a == c:
#     if a == b:
#         print(1000 + a * 100)
#     elif b == c:
#         print(1000 + b * 100)
#     else: 
#         print(1000 + c * 100)
# else:
#     M = [a, b, c]
#     print(max(M) * 100)
            