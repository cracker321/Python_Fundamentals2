# [ sys.stdin.readline().split() ]
'''

- 'sys.stdin.readline()'는 정확히 'input()'과 동일한 위치에 들어가야 한다!

'''



# [ 아래의 '예제 1'과 '예제 2'는 동일한 결괏값을 보여준다 ]

# < 예제 1 >
import sys
 
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split()) # 반복문으로 여러 줄을 입력받는 상황에서 반드시 sys.stdin.readline()을 사용해야 시간초과 발생하지 않는다!


# < 예제 2 >
import sys

input = sys.stdin.readline

for _ in range(M):
    A, B = map(input.split())
    
    
    
    
# [ temp = sys.stdin.readline().strip().split() ]

'''
- readliine()함수로 입력 받아온 문자열 긑에 있는 '개행문자 \n'을 제거하기 위해 strip() 함수를 사용함.
  이를 통해, 입력된 문자열의 양쪽 끝에 있는 공백 및 특수문자를 삭제할 수 있음. 
- 그러나, strip()을 사용하나, 사용하지 않나 '리스트 temp'에 저장되는 것에는 차이가 없음.
  다음은 '뤼튼'의 답변
  : 예, 맞습니다. 결과적으로 두 방법 모두 temp에 저장되는 요소들에서 차이가 없습니다. 
  다만, 첫 번째 방법인 temp = sys.stdin.readline().strip().split() 는 입력 문자열의 양쪽 공백을 제거합니다. 
  그러나 실제로 값을 구별하는데 있어서는 큰 차이가 없습니다. 두 방법 모두 입력 문자열을 공백을 기준으로 분리하여 리스트 형태로 저장합니다.
'''