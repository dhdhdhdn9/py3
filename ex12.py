import operator as op


# 열차 교차시간 알아보기
# a = 10
# b = 25
# c = 30
# for hour in range (9, 18):
#     hour = (i // 60) + 9
#     min = i % 60
#     if min != 0:
#         if a == b:
#             print(f'A열차와 B열차의 충돌시간: {hour}시 {a}분 \t')
#         elif b == c:
#             print(f'B열차와 C열차의 충돌시간: {hour}시 {b}분 \t')
#         elif a == c:
#             print(f'A열차와 C열차의 충돌시간: {hour}시 {c}분 \t')
#         elif a == b == c:
#             print(f'세 열차의 충돌시간: {hour}시 {c}분 \t')

# (0//60) + 9
# (60//60) + 9
# 0 % 60
# 540 // 60 + 9
# 540 % 60

a = 10
b = 25
c = 30
for i in range(540+1):
    # 분을 시간으로 분리해서 출력
    hour = (i // 60) + 9
    min = i%60
    if min != 0:
        if i % a == 0 and i % b ==0:
            print(f'A열차와 B열차 충돌 {hour}시 {min}분')
        if i % b == 0 and i % c ==0:
            print(f'b열차와 c열차 충돌 {hour}시 {min}분')
        elif i % c == 0 and i % a ==0:
            print(f'A열차와 C열차 충돌 {hour}시 {min}분')

