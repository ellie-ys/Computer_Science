
# 빠르게 정리하는 PYTHON 기초

## 매개변수
```
def add(a,b):
    result = a+b
    print( "{} + {} = {}".format(a,b,result) )

add(10,5)
```


## str.format()
```
name = 'Ellie'
color = 'yellow'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색은 {}입니다.'.format(name,color))
```


## 리스트에 새로운 값을 추가하는 방법
```
list1 = [1, 2]
list1.append(3)
list2 = list1+[4]
list3 = list1 + list2
```


## 리스트에서 값을 지우는 방법
```
del list1[10]
list1.remove(2)
```

## enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
```
rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow) :
    print('{}번째 색은 {}'.format(i+1,color))

days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i, day in enumerate(days):
    print('{}월의 날짜수는 {}일 입니다.'.format(i+1,day))
```


## list
대괄호
```
list = [1,2,3,4,5]
list[2]= 33 #index2에 값 33 추가하기
print(list) #[1, 2, 33, 4, 5]
#index5는 out of range로 append()사용해야한다.
list.append(6) # list=[1,2,33,4,5,6]


#list지우기, del 이용, pop()이용

del (list[0]) # index0 삭제
list.pop(0) # indexo 0 지우면서 그 값 return 해줌
```


## dictonary
중괄호
```
dict = {'one':1, 'two':2}
print(dict) #{'one': 1, 'two': 2}
# dict 수정하기
dict['one'] = 11 
print(dict)#{'one': 11, 'two': 2}
# dict값 추가
dict['three']= 3

#dict remove
del(dict['one'])
print(dict.pop('two')) #2
print(dict) #{'one': 11}
```

## dictionary 반복문
순서상관없이 for문 실행
cf. 순서가 중요한 경우 list로 for문 실행하자.
```
ages = {'Tods':35, 'Ellie':32, 'Jay':37}

#key순회
for key in ages.keys():
    print(key)

#value순회
for value in ages.values():
    print(value)


# 대부분 가져오는 값이 key이므로 age.keys()에 .keys()생략가능
for key in ages:
    print('{}의 나이는 {}입니다'.format(key, ages[key]))


for key, value in ages.items():
    print('{}세는 {}의 나이입니다.'.format(value,key)
```


