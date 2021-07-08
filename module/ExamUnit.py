# 시험 통과 여부
# 파이선에서는 함수의 리턴값으로 2개 이상 가능

import operator as op

def calScore(x, y, z):
    scores = {}
    scores['총점'] = x + y + z
    scores['평균'] = (x + y + z) / 3
    if ((x + y + z) / 3) >= 60 and op.ge(x or y or z, 40):
        scores['합격여부'] = 'Pass'
    else:
        scores['합격여부'] = 'Fail'
    return scores

def printScores(scores):
    for k, v in scores.items():
        print(f'{k}: {v}')
