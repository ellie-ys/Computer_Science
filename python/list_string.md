# List와 String

- 리스트와 문자열은 유사하다.
- 서로 변환이 가능하다.
- list = str.split( ) : 문자열에서 리스트로
- " ".join( list ) : 리스트에서 문자열으로

```
my_list = [ 1, 2, 3, 4, 5, 6]

print(my_list[1])
#2

print(3 in my_list)
#True

print(my_list.index(5))
#4
```

```
characters = list('abcdef')
print(characters)
#['a', 'b', 'c', 'd', 'e', 'f']
```

```

words = 'HELLO는 프로그래밍 배우는 사이트'
words_list = words.split()
print(words_list)
#['HELLO는', '프로그래밍', '배우는', '사이트']

print(words_list)
#['HELLO는', '프로그래밍', '배우는', '사이트']

print(" ".join(words_list))
#HELLO는 프로그래밍 배우는 사이트

```

```
str = 'Hello World'
print(str[0])
#H

print('h' in str)
#False

print(str.index('r'))
#8
```

```
time_str = '10:35:27'
time_list = time_str.split(':')

print(time_list)
#['10', '35', '27']

print(":".join(time_list))
#10:35:27
```

# Slice

slicing : 리스트나 문자열에서 값을 여러개 가져오는 기능
slice[a:b] ->a값은 포함되고, b값은 포함되지 않는다.

```
text = "hello world"
text = text[ 1:5 ]

list = [ 0, 1, 2, 3, 4, 5 ]
list = list[ 1:3 ]
```

slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 줌

- 시작과 끝부분을 가져오는 방법

```
list[ 2: ] : 2번째부터 끝까지 반환
list[ : 2 ] : 처음부터 2번째 까지 반환
list[ : ] : 처음부터 끝까지 전부 반환
```

## Slice의 step

slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능

- list[ 시작값:끝값:step ]
- step은 음수 값을 가질수도 있다.

```
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list1[5:13])
#[5, 6, 7, 8, 9, 10, 11, 12]
```

### step 이 2일때

```
print(list1[5:13:2])
#[5, 7, 9, 11]
```

### step이 3일때

```
print(list1[5:13:3])
#[5, 8, 11]
```

### 음수의 step -> start, end 값 달라져야 함

```
print(list1[13:5:-1])
#[13, 12, 11, 10, 9, 8, 7, 6]
```

위의 list1[5:13]과 같은 값 나오게 하려면
slice[a:b] a값 함이고 b값 포함안되므로

```
print(list1[12:4:-1])

```

list1에서 3씩 띄운 값

```
list1[::3]
```

list1에서 -3씩 띄운 값

```
list1[::-3]
```
## slice 활용
삭제

del list[ :5 ] : 처음부터 5번째까지 삭제
```
numbers = [0,1,2,3,4,5,6,7,8,9]
numbers= list(range(10))
print(numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del numbers[0]
print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

del numbers[:5]
print(numbers)
#[6, 7, 8, 9]

```
- 수정

list[ 1:3 ] = [ 77, 88 ]

list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환

list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환
```

numbers[1:3] = [77, 88]
print(numbers)
#[6, 77, 88, 9]

numbers[1:3] = [77, 88, 99]
print(numbers)
#[6, 77, 88, 99, 9]
```
### typeError
숫자 하나 넣어줄때도 list만들어서 넣기
```
#numbers[1:4]=8 #error

numbers[1:4] = [8]
print(numbers)
#[6, 8, 9]
```
