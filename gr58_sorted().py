# [ sorted() 함수 ]

'''
- 입력된 시퀀스(리스트, 튜플, 문자열 등)를 지정된 순서에 따라 정렬된 리스로 반환함. 원본 시퀀스는 변경되지 않음.
- '매개변수 key'를 사용하여 '정렬 기준'을 지정할 수 있음.
- '매개변수 reverse'를 사용하여 정렬 순서를 오름차순(True) 또는 내림차순(False)으로 지정할 수 있음.
- sorted() 함수는 원본 시퀀스를 건드리지 않고, 새로운 리스트를 생성하여 반환함.


'''

# < 예제 1: 숫자 리스트를 오름차순으로 정렬 >
numbers = [5, 3, 9, 1]
print(sorted(numbers)) # 출력값: [1, 3, 5, 9]


# < 예제 2: 숫자 리스트를 내림차순으로 정렬 >
numbers = [5, 3, 9, 1]
print(sorted(numbers, reverse = True)) # 출력값: [9, 5, 3, 1]


# < 예제 3: 문자열을 알파벳 오름차순으로 정렬 >
word = 'banana'
print(sorted(word)) # 출력값: ['a', 'a', 'a', 'b', 'n', 'n']


# < 예제 4: 문자열을 알파벳 내림차순으로 정렬 >
word = 'banana'
print(sorted(word, reverse = True)) # 출력값: ['n', 'n', 'b', 'a', 'a', 'a']


# < 예제 5: '매개변수 key'를 사용하여 문자열 길이를 기준으로 짧은 길이의 문자열부터 정렬 >
words = ['apple', 'asaklfjlskdjfslfjsdlfjsdl', 'samsung', 'q', 'lotte giants', 'abc']
print(sorted(words, key=len)) # 출력값: ['q', 'abc', 'apple', 'samsung', 'lotte giants', 'asaklfjlskdjfslfjsdlfjsdl']


# < 예제 6: '매개변수 key'를 사용하여 튜플의 두 번째 요소를 기준으로 오름차순 정렬 >
tuples = [('one', 1), ('three', 3), ('five', 5),('two', 2)]
print(sorted(tuples, key=lambda x : x[1])) # 출력값: [('one', 1), ('two', 2), ('three', 3), ('five', 5)]


# < 예제 6: '매개변수 key'를 사용하여 튜플의 두 번째 요소를 기준으로 내림차순 정렬 >
print(sorted(tuples, key=lambda x : x[1], reverse = True))