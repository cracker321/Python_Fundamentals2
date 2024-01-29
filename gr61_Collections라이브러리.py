# [ Collections 라이브러리 ]

'''
- Collections 모듈은 파이썬의 기본 내장 컨테이너 데이터 구조인 list, tuple, set, dict를 확장한 고급 데이터 구조를 제공합니다. 
  이 모듈은 개발자들이 복잡한 데이터를 다루고를 더욱 효율적으로 작성할 수 있도록 도와줍니다.
- 
'''



#==================================================================================================


# [ Counter() 함수: 리스트 내부 원소들의 개수를 세고, 그것을 '딕셔너리 형태'로 만들어줌 ]

from collections import Counter


# < 예제: 리스트 내부의 원소들의 개수 세기 >
counter = Counter([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6])
print(counter) # 출력값: Counter{1 : 3, 2 : 3, 3 : 3, 4 : 1, 5 : 1, 6 : 1}
               # 원소 1이 3개, 원소 2가 3개, 원소 3이 3개, 원소 4가 1개, 원소 5가 1개, 원소 6이 1개


'''
counter = Counter([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7])
print(counter) # 출력값: Counter{1:1, 2:1, 3:1, 4:1, 5:2, 6:2:, 7:3}

'''
# < 예제: 리스트 내부의 원소들의 개수 세기 >
counter = Counter(["hello world"]) # 여기서는 'hello world'가 리스트의 '하나의 단일원소'로 기능하고 있음.
print(counter) # 출력값: Counter{'hello world':1}



# < 예제: 문자열에서 각 문자 원소들의 개수 세기 >
counter = Counter("hello")
print(counter) # 출력값: Counter{'l':2, 'h':1, 'e':1, 'o':1}


#==================================================================================================

# [ defaultdict() 함수: ]

'''
- 말 그대로 '기본(defalut)'값(value)'을 반환'하는 딕셔너리임.
- 일반 딕셔너리는, 키(key)가 존재하지 않을 때(=없는 키에 접근할 때) (당연히) 그 없는 값을 꺼내오고자 할 때, KeyError를 발생시키나,
  defalutdict() 함수를 사용하여 만들어진 딕셔너리 객체는, 키(key)가 존재하지 않을 때(=없는 키에 접근할 때)  (당연히) 그 없는 값을 꺼내오고자
                할 때, 말 그대로 '기본값'을 반환함.
- 'defaultdic 객체'를 생성할 때, 기본값을 설정할 수 있음.


- 말 그대로 기본(default)'값(value)'을 반환하는 딕셔너리(dictionary)입니다.

특징:

일반 딕셔너리와는 달리, 없는 키에 접근할 때 KeyError를 일으키지 않고 기본값을 반환합니다.
defaultdict 객체를 생성할 때 기본값을 설정할 수 있습니다.
기본값을 반환할 때 주어진 함수를 이용해 기본값을 생성합니다.
'''

from collections import defaultdict


# < 예제: 기본'값(value)'을 '정수 0'으로 하는 defaultdict 생성  >
int_dict = defaultdict(int) # 'int타입의 기본'값(value)''을 가지는 defaultdict 객체를 생성

print(int_dict['key1']) # 출력값: 0
                        # 특정 키에 해당하는 특정 값을 꺼내오고자 할 때,
                        # 여기서 'key1'이라는 '키'가 이 딕셔너리에 존재하지 않기에 당연히 값도 없는데, 이 때 KeyError를 반환하지 않고 
                        # int 타입의 기본값으로 설정한 0을 반환함.



# < 예제: 기본'값(value)'을 '공백 리스트'로 하는 defaultdict 생성 >
list_dict = defaultdict(list)
print(list_dict['key1']) # 출력값: [] (즉, 빈 리스트)



# < 예제: 기본'값(value)'을 '공백 집합'으로 하는 defaultdict 생성 >
set_dict = defaultdict(set)
print(set_dict['key1']) # 출력값: set() (즉, 빈 집합)



#==================================================================================================



# < 예제: '리스트'를 기본'값(value)'로 하는 '공백 리스트'의 기본'값(value)' 변경 >
# defaultdict의 기본값 변경(설정)할 때는 '기본'값(value)'을 생성하는 함수를 사용'한다. 


from collections import defaultdict


my_dict = defaultdict(list) # 1.일단, 기본'값(value)''을 '공백 리스트'로 하는 deafultdict 객체 생성함.


def default_value(): # 2.기본'값(value)'을 변경(설정)하기 위해 '임의의 사용자 정의 함수 default_value();를 생성함
  return ['기본값을 이 새로운 리스트로 한다!!']


my_dict = defaultdict(default_value) # 3.defaultdict 객체 속에 '함수 default_value'를 넣고 이를 다시 변수 my_dict에 담음


my_dict['key1'].append('list_value1') # 4.defaultdict 객체에 일단 임의의 키-값 을 넣어줌.
my_dict['key1'].append('list_value2')
my_dict['key1'].append('list_value3')
my_dict['key2'].append('list_value1') 
# ****중요**** 현재까지의 my_dict 형태:
# my_dict = {
#            'key1':['list_value1', 'list_value2', 'list_value3'], 
#            'key2':['list_value1']
#           }
# 이 dictinoary 객체에서는 '값(value)'이 이미 '리스트 타입'이기 때문에, 이렇게 '한 개의 키(key)'에 대응되는 '값(value) 리스트'에
# 추가적으로 세부 원소 값(value)들을 넣어주는 것이다.
# cf) 만약, 그냥 보통의 평범한 1:1 대응하는 평범한 딕셔너리 객체였다면, 위에처럼 키-값을 넣는 것이 아니라, 일반적인 방법으로 넣음.
#     즉, normal_dict['key1'] = 'value1' 이런 형식으로 넣음.


# *****중요*****
# print(my_dict['key1'][1]) # 출력값: list_value1
#                           # '키 key1 의 값인 리스트'의 '인덱스 1번 원소'를 출력하는 것.


print(my_dict['key532']) # 출력값: ['기본값을 이 새로운 리스트로 한다!!']
                         # 위 defualtdict 객체인 my_dict에는 'key532'라는 키가 없기 때문에, 기본값을 반환해줌.


#==================================================================================================


# < 예제: '문자열'을 기본'값(value)'로 하는 기본'값(value)' 변경 >


your_dict = defaultdict(int) # 가장 '최초 기본'값(value)''을 그냥 '정수 0'으로 한다는 것이지, 
                             # 이 아래에서 '기본값입니다'라는 문자열과는 아무 상관 없음. 그냥 그 이상 이하도 아님. 
                             # 임의로 최초 기본값을 0으로 잠깐만 설정해둔 것일 뿐임.

def default_value():
  return '기본값을 이 새로운 문자열로 한다!!'

your_dict = defaultdict(default_value)

your_dict['key1'] = 'value1'
your_dict['key2'] = 'value2'
your_dict['key3'] = 'value3'

print(your_dict['key4']) # 출력값: '기본값을 이 새로운 문자열로 한다!!'
  







'''

[ 딕셔너리 객체에 '한 쌍의 키-값을 추가'하는 방법 ]

< 1. my_dict['key1'].append('value1') 방식 >
my_dict['key1'].append('value1') 이 방식은 key1에 해당하는 '값(value)'이 이미 '리스트 타입이라는 가정 하'에 작동합니다. 
따라서 'key1'의 '값(value)'이 없거나, '값(value)'이 리스트가 아니라면 오류 발생합니다. 예를 들어, my_dict이 다음과 같을 때 사용 가능합니다.


python
my_dict = {'key1': ['value1']}
위의 코드는 기존 'key1'에 해당하는 리스트에 'value1'을 추가하기 때문에, 이후 my_dict는 다음과 같이 됩니다.


python
my_dict = {'key1': ['value1', 'value1']}



< 2. my_dict['key1'] = 'value1' >
my_dict['key1'] = 'value1' 이 방식은 'key1'에 해당하는 '값(value)'을 'value1'로 설정합니다. 
만약 'key1'이 이미 존재한다면, 기존 '값(value)'을 value1'로 덮어씌웁니다. 'key1'이 없다면, 새 키-값 쌍('key1'-'value1')을 추가합니다. 
예를 들어, my_dict이 다음과 같을 때 사용 가능합니다.

python
my_dict = {'key1': 'old_value'}
위의 코드는 'key1'에 해당하는 '값(value)'을 'value1'로 덮어씌워서, 이후 my_dict는 다음과 같이 됩니다.


python
my_dict = {'key1': 'value1'}
결론적으로, my_dict['key1'].append('value1')은 리스트 '값(value)'을 추가하는 방식이고, 
my_dict['key1'] = 'value1'은 전체 키-값 쌍을 수정하거나 추가하는 방식입니다. 
이 두 방법은 서로 다른 상황에 적합하며, 사용하기 전에 딕셔너리와 키-값의 특성을 고려해야 합니다.
'''





#==================================================================================================


#==================================================================================================

