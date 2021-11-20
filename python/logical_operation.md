# 논리연산

코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정

- test1과 test2 왜 차이가 날까?
  test2에서 첫번째값이 false여서 그것만 보고 전체가 false라 간주
  python에서는 and or연산에서 더이상 실행할 필요가 없으면 실행안한다.

```
def return_false():
	print("함수 return_false")
	return False
def return_true():
	print("함수 return_true")
	return True


print("test1")
#함수 return_false
#함수 return_true 모두 다 출력
a = return_false()
b = return_true()

if a and b :
	print(True)
else :
	print(False)


print("test2")
#함수 return_false만 출력
if return_false() and return_true():
	print("True")
else:
	print("False")
```

### key1이 dic에 없어서 else문으로 넘어가 print 된다.

```
dic = {'key2':'Value1'}
if 'key1' in dic and dic['key1'] =='Value1':
	print('Key1도 있고, 그 값은 Value1이네')
else:
	print('아니네')
```

### KeyError: 'key1'이런 에러나옴.

```
dic = {'key2':'Value1'}
if dic['key1'] =='Value1' and 'key1' in dic :
print('Key1도 있고, 그 값은 Value1이네')
else:
print('아니네')
```

### python 단락평가 지원,

```
if 'key1' in dic:
	if dic['key1']=='value1':
##위와 아래 같다
if 'key1' in dic and if dic['key1'] == 'value1':
```

# bool 값

true, false

- 숫자 0을 제외한 모든 수 - true
- 빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
- 아무 값도 없다는 의미인 None - false
- 빈문자열을 제외한 모든 문자열 - true

### A and B 연산,
A가 False 면 B는 볼것도없이 False 됨, A 가 True라면, 무조건 B의 값을 따른다.
### A or B 연산
A true면 단락평가에 의해 B값 검사안하고 A 값 따른다. A가 False라면 B의 값을 따른다.

```
value = input('입력해주세요>') or '아무것도 못받았어'
print('입력받은 값>', value)
```
