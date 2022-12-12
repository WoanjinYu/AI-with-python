key = input().split()
val = map(float, input().split())
a = dict(zip(key, val))  # (key, val) 형식의 튜플로 딕셔너리를 만듦
print(a)
