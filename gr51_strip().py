# [ strip() 함수 ]

'''
- '문자열의 맨 앞과 맨 뒤의 모든 공백을 제거'하는 함수. 
- 공백 문자: 스페이스, 탭, 라인 피드 등
- strip()을 인자값 없이 사용하면, 기본적으로 모든 공백 문자를 제거함.
- strip() 함수는 원본 문자열을 변경하지 않음. 대신, 공백이 제거된 새로운 문자열을 반환함.
- 사용자가 지정한 문자를 제거하고 싶다면, strip() 함수에 인자값으로 해당 문자를 전달하면 됨. 
  이 경우, 해당 문자도 문자열 앞뒤에서 제거됨.
- strip()을 사용하나, 사용하지 않나 sys.st 문제 풀 때 실제에서는 별 차이 없음.



# [ temp = sys.stdin.readline().strip().split() ]
- 요약: 위 이런 경우에는, strip()을 사용하나 사용하지 않나 결과는 동일함.

- readliine()함수로 입력 받아온 문자열 긑에 있는 '개행문자 \n'을 제거하기 위해 strip() 함수를 사용함.
  이를 통해, 입력된 문자열의 양쪽 끝에 있는 공백 및 특수문자를 삭제할 수 있음. 
- 그러나, strip()을 사용하나, 사용하지 않나 '리스트 temp'에 저장되는 것에는 차이가 없음.
  다음은 '뤼튼'의 답변
  : 예, 맞습니다. 결과적으로 두 방법 모두 temp에 저장되는 요소들에서 차이가 없습니다. 
  다만, 첫 번째 방법인 temp = sys.stdin.readline().strip().split() 는 입력 문자열의 양쪽 공백을 제거합니다. 
  그러나 실제로 값을 구별하는데 있어서는 큰 차이가 없습니다. 두 방법 모두 입력 문자열을 공백을 기준으로 분리하여 리스트 형태로 저장합니다.


'''

# < 예제 1: 기본적인 맨 앞 문자와 맨 뒤 문자 옆들의 모든 공백 제거 >
text = "      Hello, World!      "
print(text.strip()) # 출력값: 'Hello, World!'
                    # 맨 앞과 맨 뒤의 공백이 제거됨을 알 수 있음.
                     

# < 예제 2: 사용자가 지정한 문자 제거 >
text = "***Hello, World!***"
print(text.strip('*')) # 출력값: 'Hello, World!'
                       # 맨 앞 문자 'H'와 맨 뒤 문자 '!'의 옆에 있는 모든 '*'을 삭제함.
                       
                       
# < 예제 3: 복수의 사용자가 지정한 문자 제거 1 >
text = "--!!!!!     Hello, World     !!!!!!--"
print(text.strip('-!')) # 출력값: '     Hello, World     '


# < 예제 4: 복수의 사용자가 지정한 문자 제거 2 >
text = "--!!!!!     Hello, World     !!!!!--"
print(text.strip('-! ')) # 출력값: 'Hello, World'                   