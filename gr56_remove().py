# [ remove()와 discard()의 차이 ]


# 1. [ remove()]
'''
- '집합 Set'에서 특정 값을 제거함. 
  만약, 제거하려는 값이 집합에 없는 경우, KeyError가 발생함.
  
'''


# < 예제 1: 정상적으로 삭제 >
colors = {'red', 'blue', 'green', 'black', 'orange'}

colors.remove('blue')
print(colors) # 출력값: {'red', 'green', 'black', 'orange'}


# < 예제 2: 제거하려는 값이 현재 집합에 없는 경우 -> KeyError 발생함 >
colors.remove('yellow') # KeyError 발생함


#======================================================================================


# 2. [ discard() ]


# < 예제 1: 정상적으로 삭제 >  
colors.discard('black') # {'red', 'green', 'orange'}


# < 예제 2: 제거하려는 값이 현재 집합에 없는 경우 --> 별다른 에러 발생하지 않고 그냥 무시되어 잘 출력됨 >
colors.discard('yellow')

print(colors) # 출력값: {'red', 'green', 'orange'}