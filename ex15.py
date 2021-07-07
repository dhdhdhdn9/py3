
# 혈액보관시스템
bloods = []
for i in range(10):
    donate = input('헌혈해주셔서 감사합니다. 혈액형을 선택하세요.\nA, B, AB, O: ')
    bloods.append(donate)
aBlood = bloods.count('A')
bBlood = bloods.count('B')
oBlood = bloods.count('O')
abBlood = bloods.count('AB')
print('-'*20)
print('혈액형 : 개수')
print('-'*20)
print(f'A형: {aBlood}')
print(f'B형: {bBlood}')
print(f'O형: {oBlood}')
print(f'AB형: {abBlood}')
print('-'*20)

# a = []
# b = []
# o = []
# ab = []
# for i in range(10):
#     donate = input('헌혈해주셔서 감사합니다. 혈액형을 선택하세요.\nA, B, AB, O: ')
#     if donate == 'A' or 'a': a.append(donate)
#     if donate == 'B' or 'b': b.append(donate)
#     if donate == 'O' or 'o': o.append(donate)
#     if donate == 'AB' or 'ab': ab.append(donate)
#     else:
#         print("잘못 입력하셨습니다.")
# print('--------------------')
# print('혈액형 : 개수')
# print('--------------------')
# print(f'A형: {len(a)}')
# print(f'B형: {len(b)}')
# print(f'O형: {len(o)}')
# print(f'AB형: {len(ab)}')
# print('--------------------')


