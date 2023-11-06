
# # 은신 요소
# # -5 : 인구 밀집 지역, -3 고속 도로, -1 일반 도로 혹은 비포장 도로, 0 요소 없음 1 : 경작지, 3 : 초지
HIDE =   [[  3, -5,  3,  3,  3,  3,  3,  0,  0,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0],
          [ -5, -5,  3, -1, -1, -1, -1,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0],
          [ -1, -5, -1,  3,  3,  3,  3, -1,  3,  3, -1, -1,  3,  0,  0,  0,  0,  0,  0],
          [ -5, -1,  3,  3,  0,  0,  0,  3, -1,  3, -1,  3, -1,  3,  0,  0,  0,  0,  0],
          [ -5, -5, -1,  3,  0,  0,  0,  0,  3, -1,  3,  0,  3, -1,  3,  3,  3,  3,  0],
          [ -5, -5, -1,  3,  0,  0,  0,  3, -1,  3,  0,  0,  0,  3, -1, -1, -1,  3,  0],
          [ -5, -1, -5,  3,  0,  0,  3, -1,  3,  0,  0,  0,  0,  3, -1,  3, -1,  3,  0],
          [ -1, -5, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  3, -1,  3],
          [ -5, -1, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  0,  3, -1],
          [ -1, -5, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  0,  0,  3],
          [ -5, -1, -5,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  3, -1,  3,  0,  0,  0],
          [ -5, -1, -5,  3, -1,  3,  0,  0,  0, -1, -1, -1, -1,  3,  3, -1,  3,  0,  0],
          [ -1, -5,  3,  3, -1,  3,  0,  0, -1,  3,  3,  3,  3, -1, -1, -1, -1,  3,  0],
          [ -1,  3,  3,  3, -1,  3,  0, -1,  3,  0,  0,  0,  0,  3,  3,  3,  3, -1,  3],
          [  3, -1,  3,  3, -1,  3, -1,  3,  3,  0,  0,  0,  0,  0,  0,  0,  3, -1,  3],
          [  3,  3, -1,  3,  3, -1,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0,  3,  3, -1],
          [  0,  3, -1,  3,  3, -1,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  0,  3,  3],
          [  0,  3, -1,  3,  3, -1,  3,  0,  3, -1,  0,  0,  0,  0,  0,  0,  0,  0,  3],
          [  3,  3, -1,  3,  3, -1,  3,  0,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  3],
           ]
# 세로 20 가로 21(20으로 수정)(18로 수정))

# 체력 요소
# -3 : 강/하천, 급류 -2 : 절벽 0:아무 요소 없음 1:산길
HP = [ 
        [  0,  0,  0,  0,  0,  0,  0, -2, -2,  0,  0,  0, -3, -3,  1, -3,  1,  1, -3],
        [  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -3, -3,  1,  1, -3,  1,  1],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -3,  1,  1,  1, -3, -3],
        [  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  1, -3,  1,  1,  1],
        [  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  1],
        [  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0, -3],
        [  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0, -3],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -2, -3,  1,  1,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -2, -3, -3,  1,  0,  0,  0, -3,  0,  0],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -3,  1,  1,  1,  0,  0,  0, -3, -3,  0],
        [  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  0,  0,  0, -3, -3, -3],
        [  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0, -3, -3],
        [  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -3],
        [  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0, -2,  1,  1,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1,  1,  0,  0,  0],
        [ -3,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  1,  1,  0,  0],
        [ -3,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  0,  0,  0,  1,  1,  1,  0] ]

# 세로 22 가로 21 둘 다 수정됨

SLOPE = [  
        [  1, -2,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1,  0,  0, -1,  0, -2, -2,  0],
        [  1, -2,  1,  0, -1, -1,  0,  1,  1,  1, -1,  1,  0,  0,  1, -1,  0,  1, -2],
        [  0,  1, -1,  1,  1,  1,  1,  0,  1,  1,  0, -1,  1,  1,  1,  0, -1,  0,  0],
        [  1,  0,  1,  0,  0,  0,  0,  1, -1,  1,  0,  1,  0,  1,  1,  1,  1, -1, -1],
        [ -2,  0,  1,  0,  0, -1, -1,  0,  1,  0,  1,  0,  1, -1,  1,  1,  1,  1,  0],
        [ -2,  0,  1,  0,  0, -1, -1,  1, -1,  1,  0,  0,  0,  1, -1,  0, -1,  1,  1],
        [ -2,  0,  0,  0,  0,  0,  1,  0,  1,  0, -1, -1, -1,  1, -1,  1,  0,  1,  1],
        [  1,  0,  0,  0,  0,  1, -1,  1,  0, -2,  0, -1,  0,  1, -1,  1,  1, -1,  1],
        [ -2,  1,  0,  0,  0,  1, -1,  1,  0, -2,  0,  0,  0,  1,  0,  1,  0,  0, -1],
        [  0,  1,  0,  0,  0,  1,  0,  1, -1,  0, -1, -1, -1,  1,  0,  1,  0,  0,  1],
        [ -2,  1,  0,  0,  1,  0,  1,  0,  0, -1,  0,  0,  0,  1, -1,  1,  0,  0,  0],
        [  1,  1,  1,  0, -1,  1, -1, -1, -1,  0, -1, -1,  0,  1,  1, -1,  1,  0,  0],
        [  1,  1,  1,  0,  0,  1,  0,  0, -1,  1,  1,  1,  1,  0,  0,  0,  0,  1,  0],
        [  0,  1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  0,  0,  1,  1,  1,  1,  0,  1],
        [  1,  1,  1,  0,  0,  1, -1,  1,  1, -1, -1, -2, -2, -2, -1, -1,  1,  0,  1],
        [  1,  1, -1,  0,  1,  0,  1, -1,  1,  0, -2,  0,  0,  0,  0,  0,  1,  1,  0],
        [  0,  1, -1,  0,  1, -1,  1,  1,  0,  0,  0, -2,  0,  0,  0,  0,  0,  1,  1],
        [  0,  1,  0,  0,  1, -1,  1,  0,  1, -1,  0,  0, -2, -2,  0, -1, -1, -1,  1],
        [  1,  1,  0,  0,  1,  0,  1,  0,  1,  1, -1,  0,  0,  0,  0, -1, -1, -1,  1]
        ]                  
# 세로 21 가로 21 (둘 다 수정됨)

# 고도에 따른 값
# 0-10 : 1, 10-20 : 2, 20-30 : -1, 30-40 : -2

# 셋 다 18로 수정함

import numpy as np

def unite(size) : # 상태 가치들 합침
    
    for i in range(size) :
        for k in range(size) :
            field[i * k + k] = HIDE[i][k] + HP[i][k] + SLOPE[i][k]

######

# 18 * 18 = 324
# move 수정필요함니다
######

def move(s, a):
    # 8방향 이동에 따른 새로운 상태 결정
    if a == 0: # 상으로 이동
        return s - 19 if s - 19 >= 0 else s
    
    elif a == 1: # 하로 이동
        return s + 19 if s <= 341 else s
    
    elif a == 2: # 좌로 이동
        return s - 1 if s % 19 != 0 else s
    
    elif a == 3: # 우로 이동
        return s + 1 if s % 19 != 0  else s
    
    elif a == 4 : # 좌상
        return s - 20 if s >= 20 and s % 4 != 0 else s
    
    elif a == 5 : # 우상
        return s - 18 if s >= 19 and s % 19 != 18 else s
    
    elif a == 6 : # 좌하
        return s + 18 if s <= 341 and s % 19 != 0 else s
    
    elif a == 7 : # 우하
        return s + 20 if s <= 340 and s % 19 != 18 else s

propagate_ratio = 1

def iteration(states, actions, r, gamma = 0.9, limit = 0.001) :
    v = np.zeros(size * size) # 각 상태들의 가치
    policy = np.zeros(size * size) # 각 상태들의 최적 정책

    while True :
        delta = 0 # 상태의 가치가 얼마나 변하는가를 담음
        for s in states :
            temp_v = v[s] # 현재 상태의 밸류를 임시 저장

            check = []
            for a in actions :
                tmp1 = r[move(s, a)]
                tmp2 = gamma * move(s,a) * propagate_ratio
                check.append(tmp1 + tmp2)
            v[s] = max(check)
            # v[s] = max([r[move(s, a)] + gamma * move(s, a) * propagate_ratio] for a in actions)
            delta = max(delta, abs(temp_v - v[s]))
            # 기존의 가치 - 새로 갱신한 가치의값과 기존의 델타 값 중 뭐가 더 큰지를 비교
        if delta < limit :
            break
         # 정의한 임계값보다 낮으면 더이상 변해도 의미가 없는 수렴 상태라고 판단 후 종료
    
        for s in states:  # 모든 상태에 대해 반복
        # 최적의 행동을 선택하는 정책 계산
            policy[s] = np.argmax([r[move(s, a)] + gamma * v[move(s, a)] for a in actions])
    
    return policy, v  # 최적 정책과 가치 함수 반환

size = 19
field = np.zeros(size * size)
actions = [0, 1, 2, 3, 4, 5, 6, 7]
# 상 하 좌 우 좌상 우상 좌하 우하
states = list(range((size * size) - 1))
unite(size)

field[len(field) - 1] = 9
policy, v = iteration(states, actions, field)

size = 19

print(policy)

print(v)