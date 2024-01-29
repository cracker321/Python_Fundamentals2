# [ lambda()함수와 sorted()의 key를 함께 사용하기 ]
'''
- lambda: 한 줄로 간단한 함수를 정의할 때 사용하는 익명 함수.
- key: 정렬이나 다른 연산에서 사용되어, 정렬 기준이나 비교 기준을 지정함.
       
- < 사용법 >
sorted(시퀀스객체(=아마도 변수명?), key = lambda x : 정렬의 기준이 될 표현식)

여기서 'x'는 '전체 시퀀스 객체'가 아닌, '그 안의 개별 원소'를 의미한다.
람다함수에서 적용되는 것은 '전체 시퀀스 객체'가 아닌 '그 안의 개별 원소'이기 때문!
'''


# < 예제: 숫자 리스트를 오름차순으로 정렬 >
numbers = [5, 2, 8, 1, 9]
print(sorted(numbers, key = lambda x : x)) # 출력값: [1, 2, 5, 8, 9]



# < 예제: 숫자 리스트를 절대값 기준으로 정렬 >
numbers = [3, -5, 1, -2, 8, 0, -4]
print(sorted(numbers, key = lambda x : abs(x))) # 출력값: [0, 1, -2, -3, -4, -5, -8]
# 원리: lambda x : abs(x) 의 반환값(=return abs(x))이 '절대값 x'이고,
# key = '절대값 x'  가 되기 때문에, 즉 매개변수 key는 절대값 x를 기준으로 numbers를 오름차순 정렬한다는 것임



# < 예제: 문자열 리스트를 길이 순서로 정렬 >
names = [ 'Alice', 'Yujong Cho', 'Joe', 'Bob', 'Charlie', 'David', 'Jonathan']
print(sorted(names, key = lambda x : len(x))) # 출력값: ['Joe', 'Bob', 'Alice', 'David', 'Charlie', 'Jonathan', 'Yujong Cho']
# 원리: lambda x : len(x)의 반환값(=return len(x))이 '원소 x들의 길이'이고,
# key = '원소 x들의 길이'  가 되기 때문에, 매개변수 key는 '원소 x들의 길이'를 기준으로 names를 오름차순 정렬한다는 것임.



# < 예제: 문자열 리스트를 마지막 글자 기준으로 정렬 >
names = ['Alice', 'Bob', 'Eve', 'David']
print(sorted(names, key = lambda x : x[-1])) # 출력값: ['Bob', 'David', 'Alice', 'Eve']
                                             # 각각의 마지막 글자 'b', 'd', 'e', 'e'를 기준으로 정렬한 것임.
# cf) 파이썬에서 리스트나 문자열의 마지막 원소의 인덱스번호는 [-1] 이다!
# cf) 람다함수에서 적용되는 것은 '리스트 names'가 아닌 '각각 개별의 원소 x'이기 때문에, 'names[0], names[-1] ..' 이런 것들이 아니라,
#     'x[0], x[-1] ...' 이 되는 것이다!



# < 예제: 튜플의 두 번째 원소로 오름차순 정렬. 만약 값이 같을 경우, 첫 번째 원소로 내림차순 정렬 >
data = [(3, 1), (1, 4), (4, 2), (2, 4), (5, 1)]
print(sorted(data, key = lambda x : (x[1], -x[0]))) # 출력값: [(5, 1), (3, 1), (4, 2), (2, 4), (1, 4)]
                                                    # 우선순위 기준을 여러 개 사용(= x를 여러 개 사용)할 때는, 반드시 괄호로 묶어줘야 한다!



# < 예제: 대소문자 구분 없이 정렬 >
words = [ 'Apple', 'MEEE', 'ORaNge', 'BaNANa']
print(sorted(words, key = lambda x : x.lower())) # 출력값: 



# < 예제: 딕셔너리를 값(value)을 기준으로 정렬하고, 키(key)와 값(value)을 '리스트'로 반환 >
grades = {'Alice':90, 'Bob':85, 'Eve':95}
print(sorted(grades.items(), key = lambda x : x[1])) # 출력값: [('Bob', 85), ('Alice', 90), ('Eve', 95)]
# cf) 현재 딕셔너리의 모든 키와 값을 확인하는 함수 items()



# < 예제: 학생 '딕셔너리'로 구성된 '리스트'를 나이(1순위)와 성적(2순위)을 기준으로 정렬 >
students = [{'name':'Alice', 'age':15, 'score':89}, {'name':'Bob', 'age':15, 'score':94}, {'name':'Eve', 'age':16, 'score':92}]
print(sorted(students, key = lambda x : (x['age'], x['score']))) # 출력값: [{'name':'Alice', 'age':15, 'score':89}, {'name':'Bob', 'age':15, 'score':94},
                                                                 #         {'name':'Eve', 'age':16, 'score':92}]

