# about tuple

dict {}, list []

tuple -> () 소괄호사용

list 처럼 순서가 정해져 있어 index로 값 가져올 수 있다.
tuple 값의 수정과 삭제가 불가능.

### 튜플 만들기

```
tuple1 = (1,2,3)
tuple2 = 1, 2, 3

list = [1, 2, 3]
tuple3 = tuple(list)
```

## packing vs unpacking

하나의 변수에 여러개의 변수 대입 가능

- packing
  하나의 변수에 여러개의 값을 넣는 것

```
#변수 d, e를 f에 packing
f = d,e
```

- unpacking
  패킹된 변수에서 여러개의 값을 꺼내오는 것

```
#c의 값을 unpacking, d,e에 넣어줌
c = (3, 4)
d, e = c
```

## 튜플의 활용

### 1. 두 변수의 값을 바꿀 때 임시변수가 필요 없다.

```
x, y = y, x
```

### 2. 함수의 리턴 값으로 여러 값을 전달할 수 있다.

- 튜플의 리스트 활용  
  list -> enumerate

```
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('{}번째 값: {}'.format(i,v))


#위와 같은 for문
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))
# a앞에 * 붙히면, tuple 나누라는 의미.
#'*a'대신에 'a[0], a[1]' 해주어도 된다.
```

- 튜플 딕셔너리 활용

  dictionary-> items()

```
ages = {'Ellie':32, 'Jay':37}
for a in ages.items():
    print('{}의 나이는 {}입니다'.format(*a))
#'*a'대신에 'a[0], a[1]' 해주어도 된다.

```
