# [ index(n) ]

'''
- 시퀀스 자료형(문자열, 리스트, 튜플 등)에서 특정 원소의 위치(인덱스 번호)를 찾아서 그 '인덱스 번호'를 반환하는 함수.
- 시퀀스 안에 동일한 원소가 여러 개 있는 경우, 그 중 첫 번째 원소의 위치(인덱스 번호)를 반환함.

'''

# [ 예제 1 ]
numbers = [1, 2, 3, 2, 2, 4, 2]

print(numbers.index(2)) # 출력값: 1. 즉, 인덱스번호 1을 반환함.
                        # '리스트 numbers'에 여러 개의 '원소 2'가 있지만, 그 중 첫 번째 등장하는 원소 2의 인덱스 번호를 반환함.
                        

# [ 예제 2 ]
word = "banana"
print(word.index('a')) # 출력값: 1
                       # '문자열 banana'에 여러 개의 '원소 a'가 있지만, 그 중 첫 번째 등장하는 원소 a의 인덱스 번호를 반환함.