# [ sort() 함수 ]

'''
- 리스트 안의 원소들을 정렬하는 데 사용되는 함수.
  숫자 문자열, 다른 자료형의 원소들을 오름차순이나 내림차순으로 정렬할 수 있음.
- **주의!!**원래의 리스트를 정렬하고, 그 결괏값으로 None을 반환함!! 즉, 새로운 리스트를 반환하지 않음.
  즉, 'print(리스트.sort())' 이렇게 하면, 출력값은 'None'이 나옴. 
  제대로 출력하려면, 'my_list = 리스트.sort()' 작성하고, print(my_list) 이렇게 해야, 원래의 리스트를 정렬한 것을 출력할 수 잇ㅇ므.
- cf) 'sorted() 함수'는 원본 시퀀스를 건드리지 않고, 새로운 리스트를 생성하여 반환함
- 정렬된 결과를 확인하려면, 리스트 자체를 출력하거나, 정렬된 리스트를 달느 변수에 저장해야 함.
- < 사용법 >
  리스트.sort() # 리스트의 원소들을 오름차순으로 정렬.
  리스트.sort(reverse = True) # 리스트의 원소들을 내림차순으로 정렬.
'''


# < 예제: 대소문자 무시하고 (알파벳 오름차순 순서에 따라) 문자열 정렬 >
words = ['CAT', 'BanAnA', 'aPPle', 'Diana']
words.sort(key = str.lower)
print(words) # 출력값: ['aPPle', 'Banana', 'CAT', 'Diana']



# < 예제: 내림차순 정렬 >
number_list = [3, 4, 2, 1, 5]
number_list.sort(reverse = True)
print(number_list) # 출력값: [5, 4, 3, 2, 1]



# < 예제: 각 원소의 길이를 기준으로 정렬 >
fruit = ['kiwi', 'orange', 'Yujong Cho', 'xy', 'mango', 'orangeeeeeeeeeeeee']
fruit.sort(key=len)
print(fruit) # 출력값: 



# < 예제: 리스트의 인덱스 순서대로 정렬 >. 이거 뭔가 잘못 작성한 듯. 에러 발생함.
# colors = ['red', 'blue', 'green', 'yellow', 'black']
# colors.sort(key = lambda x : colors.index(x))
# print(colors) # 출력값: ['red', 'blue', 'green', 'yellow', 'black']



# < 예제: 리스트의 원소들의 나이를 기준으로 정렬 >
people = [{'name':'Alice', 'age':30}, {'name':'Bob', 'age':25}, {'name':'Charlie', 'age':35}, {'name':'David', 'age':28} ]
people.sort(key = lambda x : x['age'])
print(people) # 출력값: [{'name': 'Bob', 'age': 25}, {'name': 'David', 'age': 28}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]



# < 예제: 리스트의 마지막 원소 기준 정렬 >
names = ['Alice', 'Bob', 'Charlie']
names.sort(key = lambda x : x[-1])
print(names)