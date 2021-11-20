# 반복문

## while문

조건이 참인 경우 원하는 만큼 계속 실행하는 반복문
for 반복문으로 작성한 코드는 while 반복문으로 작성 가능
for를 먼저 고려하고, 너무 복잡하면 while ; 상황에 맞는 반복문 사용하기
cf. if문 : 조건이 맞으면 한번만 실행

```
seleted = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')

print('선택된 값은: ',selected)
```

만약 위의 코드를 while -> if로 수정한다면?
가위, 바위, 보 가 아닌 어떤 값을 넣더라도 한번만 실행

```
patterns = ['가위','바위','보']
length = len(patterns)
i = 0
#length가 3인데 3보다 작다면 계속 실행
while i < length:
    print(patterns[i])
    i = i+1
```

## break, continue

- break: 반복문 종료
- continue : 반복문 나머지 부분 보지않고 반복문의 맨 처음으로 돌아가기
- for, while문에서 똑같이 동작

### break

3의 배수를 찾는 조건문을 하다가 하나의 3의 배수만 찾고싶다면? break 위치?!
break가 포함된 블럭 (if문블럭)의 상위 블럭(for문블럭)을 종료시킨다.

```
list = [1,2,3,5,7,2,5,237,55]
for val in list:
    if val % 3 ==0:
        print(val)
        break
```

### continue

- 핵심이 되는 블럭이 깊이 들어가는 것을 막아주려고 예외 처리

```
list = [1,2,3,5,7,2,5,237,55]
# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)
```
