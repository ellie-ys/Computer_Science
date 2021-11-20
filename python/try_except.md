# 예외처리

- try:
- 에러가 발생할 가능성이 있는 코드
- except Exception: # 에러 종류
- 에러가 발생 했을 경우 처리할 코드

```
text = '100%'

try:
	number = int(text)
except ValueError:
	print('{}는 숫자가 아니네요.'.format(text))
```

## try_except -> if로 변경가능. 보통은 if 더 많이사용

### list 123에서 index 5인거 pop

```
# def safe_pop_print(list,index):
# 	try:
# 		print(list.pop(index))
# 	except IndexError:
# 		print('{} index의 값을 가져올 수 없습니다'.format(index))
# safe_pop_print([1,2,3],5)

def safe_pop_print(list, index):
	if index<len(list):
		print(list.pop(index))
	else:
		print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)
```

## try_except아니면 안되는애(if사용불가)

```
try:
	import my_module
except ImportError:
	print("my module이 없습니다.")
```

## 예외의 이름을 모를 때

```
try:
	# list=[]
	# print(list[0])

	text = 'abc'
	number = int(text)
except Exception as ex:
	print('에러가 발생했습니다.', ex)
#ex 발생한 에러의 이름을 받아오는 변수
```

# raise

에러 직접 발생시키는 방법
많이 사용하면 코드 가독성 떨어짐, 꼭 필요한 경우에만!

```
def rsp(mine, yours):
    #가위바위보 승패판단 함수
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed :
        raise ValueError

try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값을 넣은것 같아요')
```

### break 사용

190넘는 친구있으면 반을 출력하고 바로 정지
1반, 2반(dictonary 순서x) 모두 출력됨.
break로 첫for문은 종료되는데, 그 상위 for문은 종료되지 않고 한번더 2반을 탐색한다.

```
students_height = {'1반':[172,185,198,177,165,199], '2반':[165,177,167,180,199]}


for class_number, students in students_height.items():
	for student in students:
		if student >190:
			print(class_number,'에 190을 넘는 학생이 있습니다')
			break
```

### raise error

190넘는 친구있으면 반을 출력하고 바로 정지 #중첩된 for문 2개 다 바로 종료 #실행 흐름 깨트릴 때 유용

```
students_height = {'1반':[172,185,198,177,165,199], '2반':[165,177,167,180,199]}

try:
	for class_number, students in students_height.items():
		for student in students:
			if student >190:
				print(class_number,'에 190을 넘는 학생이 있습니다')
				raise StopIteration
except StopIteration:
	print('정상종료')

```

문구점 세곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력, 풀을 파는 가게 발견하면 for문 전체 즉시 종료.

```
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
	for shop, products in shops.items():
		for product, price in products.items():
			if product =='풀':
				print("{}: {}원".format(shop, price))
				raise StopIteration

except StopIteration:
    print('정상 종료')
```
