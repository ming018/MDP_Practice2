# import numpy as np

size = 22
# field = np.zeros((size, size))

# # 은신 요소
# # -5 : 인구 밀집 지역, -3 고속 도로, -1 일반 도로 혹은 비포장 도로, 0 요소 없음 1 : 경작지, 3 : 초지
HIDE =   [[ 3, -5,  3,  3,  3,  3,  3,  0,  0,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
          [ -5, -5,  3, -1, -1, -1, -1,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
          [ -1, -5, -1,  3,  3,  3,  3, -1,  3,  3, -1, -1,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0],
          [ -5, -1,  3,  3,  0,  0,  0,  3, -1,  3, -1,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0,  0],
          [ -5, -5, -1,  3,  0,  0,  0,  0,  3, -1,  3,  0,  3, -1,  3,  3,  3,  3,  0,  0,  0,  0],
          [ -5, -5, -1,  3,  0,  0,  0,  3, -1,  3,  0,  0,  0,  3, -1, -1, -1,  3,  0,  0,  0,  3],
          [ -5, -1, -5,  3,  0,  0,  3, -1,  3,  0,  0,  0,  0,  3, -1,  3, -1,  3,  0,  0,  0,  3],
          [ -1, -5, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  3, -1,  3,  0,  3, -3],
          [ -5, -1, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  0,  3, -1,  3, -3, -5],
          [ -1, -5, -5,  3,  0,  3, -1,  3,  0,  0,  0,  0,  0,  3, -1,  3,  0,  0,  3, -1, -3, -5],
          [ -5, -1, -5,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  3, -1,  3,  0,  0,  0,  3, -3, -5],
          [ -5, -1, -5,  3, -1,  3,  0,  0,  0, -1, -1, -1, -1,  3,  3, -1,  3,  0,  0,  3, -3, -5],
          [ -1, -5,  3,  3, -1,  3,  0,  0, -1,  3,  3,  3,  3, -1, -1, -1, -1,  3,  0,  3,  1, -3],
          [ -1,  3,  3,  3, -1,  3,  0, -1,  3,  0,  0,  0,  0,  3,  3,  3,  3, -1,  3,  3,  1,  1],
          [  3, -1,  3,  3, -1,  3, -1,  3,  3,  0,  0,  0,  0,  0,  0,  0,  3, -1,  3,  3,  1,  1],
          [  3,  3, -1,  3,  3, -1,  3, -1,  3,  0,  0,  0,  0,  0,  0,  0,  3,  3, -1,  3,  1,  1],
          [  0,  3, -1,  3,  3, -1,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  0,  3,  3, -3, -3,  1],
          [  0,  3, -1,  3,  3, -1,  3,  0,  3, -1,  0,  0,  0,  0,  0,  0,  0,  0,  3, -3,  3, -3],
          [  3,  3, -1,  3,  3, -1,  3,  0,  3,  3, -1,  0,  0,  0,  0,  0,  0,  0,  3, -3,  3,  3],
          [  3, -1,  3,  3, -1, -1,  3,  0,  0,  0,  3, -1, -1, -1,  0,  0,  0,  0,  3,  3, -3,  3],
          [  3, -1,  3,  3, -1,  3,  3,  0,  0,  0,  0,  3,  3,  3, -1,  0,  0,  0,  0,  3,  3, -3] ]


# 체력 요소
# -3 : 강/하천, 급류 -2 : 절벽 0:아무 요소 없음 1:산길
HP = [ 
        [  0,  0,  0,  0,  0,  0,  0, -2, -2,  0,  0,  0, -3, -3,  1, -3,  1,  1, -3, -3, -3, -3],
        [  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -3, -3,  1,  1, -3,  1,  1, -3,  1,  1],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -3,  1,  1,  1, -3, -3,  1,  1, -3],
        [  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  1, -3,  1,  1,  1, -3, -3,  1],
        [  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0],
        [  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0, -3,  1, -3,  0],
        [  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0, -3, -3, -3,  0],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -2, -3,  1,  1,  0,  0,  0,  0,  0,  0, -3,  0,  0],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -2, -3, -3,  1,  0,  0,  0, -3,  0,  0,  0,  0,  0],
        [  0,  0,  0,  0,  1,  0,  0,  0,  1, -3,  1,  1,  1,  0,  0,  0, -3, -3,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  0,  0,  0, -3, -3, -3,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0, -3, -3,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -3,  0,  1,  0],
        [  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  1,  1],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0, -2,  1,  1,  0,  0,  0,  0,  1,  1],
        [  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0,  1],
        [ -3,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  0],
        [ -3,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0, -2, -2,  1,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  1, -3,  1,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0],
        [  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0]
           ]


SLOPE = [  

        [  1, -2,  1,  1,  1,  1,  1,  1,  1,  1, -1,  1,  0,  0, -1,  0, -2, -2,  0,  0,  0,  0],
        [  1, -2,  1,  0, -1, -1,  0,  1,  1,  1, -1,  1,  0,  0,  1, -1,  0,  1, -2,  0, -2, -2],
        [  0,  1, -1,  1,  1,  1,  1,  0,  1,  1,  0, -1,  1,  1,  1,  0, -1,  0,  0, -1, -2,  0],
        [  1,  0,  1,  0,  0,  0,  0,  1, -1,  1,  0,  1,  0,  1,  1,  1,  1, -1, -1,  0,  0,  0],
        [ -2,  0,  1,  0,  0, -1, -1,  0,  1,  0,  1,  0,  1, -1,  1,  1,  1,  1,  0, -1, -1,  1],
        [ -2,  0,  1,  0,  0, -1, -1,  1, -1,  1,  0,  0,  0,  1, -1,  0, -1,  1,  1,  1,  1,  1],
        [ -2,  0,  0,  0,  0,  0,  1,  0,  1,  0, -1, -1, -1,  1, -1,  1,  0,  1,  1,  1,  1,  1],
        [  1,  0,  0,  0,  0,  1, -1,  1,  0, -2,  0, -1,  0,  1, -1,  1,  1, -1,  1,  1,  1, -1],
        [ -2,  1,  0,  0,  0,  1, -1,  1,  0, -2,  0,  0,  0,  1,  0,  1,  0,  0, -1,  1, -1,  0],
        [  0,  1,  0,  0,  0,  1,  0,  1, -1,  0, -1, -1, -1,  1,  0,  1,  0,  0,  1,  0,  0,  1],
        [ -2,  1,  0,  0,  1,  0,  1,  0,  0, -1,  0,  0,  0,  1, -1,  1,  0,  0,  0,  1, -1,  1],
        [  1,  1,  1,  0, -1,  1, -1, -1, -1,  0, -1, -1,  0,  1,  1, -1,  1,  0,  0,  1, -1,  0],
        [  1,  1,  1,  0,  0,  1,  0,  0, -1,  1,  1,  1,  1,  0,  0,  0,  0,  1,  0,  1,  1, -1],
        [  0,  1,  1,  0, -1,  1,  0, -1,  1,  0, -1,  0,  0,  1,  1,  1,  1,  0,  1,  1,  1,  1],
        [  1,  1,  1,  0,  0,  1, -1,  1,  1, -1, -1, -2, -2, -2, -1, -1,  1,  0,  1,  1,  1,  1],
        [  1,  1, -1,  0,  1,  0,  1, -1,  1,  0, -2,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  1],
        [  0,  1, -1,  0,  1, -1,  1,  1,  0,  0,  0, -2,  0,  0,  0,  0,  0,  1,  1, -1, -1,  1],
        [  0,  1,  0,  0,  1, -1,  1,  0,  1, -1,  0,  0, -2, -2,  0, -1, -1, -1,  1, -1,  1, -1],
        [  1,  1,  0,  0,  1,  0,  1,  0,  1,  1, -1,  0,  0,  0,  0, -1, -1, -1,  1, -1,  1,  1],
        [  1, -1,  1,  0, -1,  0,  1, -2, -2,  0,  1,  0, -1, -1,  0, -1, -1, -1,  1,  1, -1,  1],
        [  1, -1,  1,  0, -1,  0,  1, -2, -2,  0,  1,  0, -1, -1,  0, -1, -1, -1,  1,  1, -1,  1],
        [  1, -1,  1,  0, -1,  1,  1,  0,  0,  0,  0,  1,  1,  1,  0, -1,  0,  0,  0,  1,  1, -1],
        ]                      
# 고도에 따른 값
# 0-10 : 1, 10-20 : 2, 20-30 : -1, 30-40 : -2


# class Agent :
#     def __init__(self) :
#         self.x = len(field) // 2
#         self.y = len(field) // 2


"""
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 5

# """
# import numpy as np  # numpy 라이브러리를 np라는 이름으로 가져옴
# actions = [0, 1, 2, 3, 4, 5, 6, 7]
# # 상 하 좌 우 좌상 우상 좌하 우하

# def transition_prob(s, a):
#     """
#     현재 상태 s에서 행동 a를 했을 때의 전이 확률을 반환하는 함수입니다.
#     여기서는 단순화를 위해 결정론적인 전이만 다루고 있습니다.
#     """
#     # 위, 아래, 왼쪽, 오른쪽 이동에 따른 새로운 상태 결정
#     if a == 0: # 상으로 이동
#         return s-4 if s-4 >= 0 else s
#     elif a == 1: # 하로 이동
#         return s+4 if s+4 <= 15 else s
#     elif a == 2: # 좌로 이동
#         return s-1 if s % 4 != 0 else s
#     elif a == 3: # 우로 이동
#         return s+1 if s % 4 != 3 else s
#     elif a == 4 : # 좌상
#         return s - 5 if s >= 5 and s % 4 != 0 else s
#     elif a == 5 : # 우상
#         return s - 3 if s > 3 and s % 4 != 3 else s
#     elif a == 6 : # 좌하
#         return s + 3 if s < 11 and s % 4 != 0 else s
#     elif a == 7 : # 우하
#         return s + 5 if s < 11 and s % 4 != 3 else s

# def value_iteration(states, actions, r, gamma=0.99, threshold=0.001):
#     V = np.zeros(len(states))  # 각 상태에 대한 가치를 저장할 배열 초기화
#     policy = np.zeros(len(states), dtype=int)  # 각 상태에서 선택할 최적 행동을 저장할 배열 초기화

#     while True:
#         delta = 0  # 가치 함수가 얼마나 변경되었는지 추적
#         for s in states:  # 모든 상태에 대해 반복
#             V_temp = V[s]  # 현재 상태의 가치를 임시 변수에 저장
#             # 가능한 모든 행동에 대해 새로운 가치 계산하고 최대값을 현재 상태의 가치로 설정
#             V[s] = max([r[transition_prob(s, a)] + gamma * V[transition_prob(s, a)] for a in actions])
#             delta = max(delta, abs(V_temp - V[s]))  # 가장 큰 가치 변화를 delta에 저장
#         if delta < threshold:  # 변화량이 threshold보다 작으면 반복을 중단
#             break

#     for s in states:  # 모든 상태에 대해 반복
#         # 최적의 행동을 선택하는 정책 계산
#         policy[s] = np.argmax([r[transition_prob(s, a)] + gamma * V[transition_prob(s, a)] for a in actions])
    
#     return policy, V  # 최적 정책과 가치 함수 반환

# states = list(range(16))  # 상태 공간 정의 (0부터 15까지 16개의 상태)
# # actions = [0, 1, 2, 3]  # 가능한 행동 집합 정의 (상, 하, 좌, 우)
# r = [-0.01 for _ in states]  # 각 상태에 대한 보상 배열 초기화 (기본적으로 모두 -0.01)
# r[15] = 1  # 목표 상태(상태 15)에 대한 보상을 1로 설정

# optimal_policy, optimal_values = value_iteration(states, actions, r)  # 가치 반복 함수를 호출하여 최적 정책과 가치 계산
# print("최적 정책:")  # 최적 정책 출력
# print(optimal_policy)
# for i in range(1, len(optimal_policy) + 1) :
#     print(optimal_policy[i - 1], end=' ')
#     if i % 4 == 0 :
#         print()
# print("최적 가치:", optimal_values)  # 최적 가치 출력

# for i in range(1, len(optimal_policy) + 1) :
#     print(round(optimal_values[i - 1], 2), end=' ')
#     if i % 4 == 0 :
#         print()



import numpy as np

def unite() :
    array = []
    for i in range(size) :
        for k in range(size) :
            array.append(HIDE[i][k] + HP[i][k] + SLOPE[i][k])
    
    return array

array = unite()
for i in range(1, len(array) + 1) :
    print(array[i - 1], end=' ')
    if i % 2 == 0 :
        print()