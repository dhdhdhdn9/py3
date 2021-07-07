# 수학시험 문제

quest = ['3+2', '5÷2의 몫', '10-2', '10²x2', '1(10÷4의 나머지)', '2⁴', '4÷2']  # 문제
answer = [5, 2, 8, 200, -1, 16, 2]
exam = {key:val for key, val in zip(quest, answer)}
mine = []
score = [3, 5, 3, 5, 5, 3, 3]
right = 0
final = 0
cnt = len(quest)

# for k, v in exam.items():
#     print(f'문제: {k}')
#     myAnswer = int(input('정답: '))
#     mine.append(myAnswer)
# for i in range(7):
#     if int(mine[i]) == answer[i]:
#         right += 1
#         final += score[i]

for i in range(cnt):
    print(f'문제: {quest[i]}')
    mine = int(input('정답: '))
    if int(mine) == answer[i]:
        right += 1
        final += score[i]

print('-'*20)
print(f'정답 개수: {right}\n오답 개수: {cnt-right}\n점수: {final}')
print('-'*20)



# 다른 방법
quiz = [['3+2',5,3], ['5÷2의 몫',2,5], ['10-2',8,3], ['10²x2',200,5],
        ['1(10÷4의 나머지)',-1,5], ['2⁴',16,3], ['4÷2',2,3]]
right2 = 0
final2 = 0
cnt2 = len(quiz)

for q in quiz:  # quiz에서 대괄호로 묶은 것들을 'q'라는 이름으로 리스트를 만들어 가져옴
    print(f'문제: {q[0]}')
    mine2 = input('정답: ')
    if int(mine2) == q[1]:
        right2 += 1
        final2 += q[2]

print('-'*20)
print(f'정답 개수: {right2}\n오답 개수: {cnt2-right2}\n점수: {final2}')
print('-'*20)