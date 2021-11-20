# list와 dictionary

## 공통점

생성, 호출, 삭제, 개수확인, 값 확인, 전부 삭제

## 차이점

- 삭제
  - list: 삭제시 순서가 바뀌기 때문에, index값도 바뀜
  - dictionary : key로 값을 가져오기 때문에, 삭제 여부와 상관없다.
- 결합
  - list: list1 + list2
  - dictonry : dict1.update(dict2)

# 공통점 예

## 1. 생성, 호출

```
list = [1,2,3,4,5]
dict = {'one':1, 'two':2}
```

## 2. 삭제하기

```
del(dict['one'])
print(dict) #{'two': 2}
```

## 3. 원소 값 확인

```
print(2 in list) #boolean

print('two'in dict.keys())
print('three'in dict.keys())

print(2 in dict.values())
```

## 4. 전체 지우기

```
dict.clear()
print(dict)

list.clear()
print(list)
```

# list와 dictionary 차이점 예

## 1. 삭제

list는 index가 변하고, dict는 key값이 그대로라

```
# list
list = [1,2,3,4,5]
dict = {'one':1, 'two':2}

print(list[2])#3
print(list.pop(0))
print(list[2]) #3이 아님.

#dict
print(dict['two'])#2
print(dict.pop('one'))
print(dict['two'])#key값으로 가져온 value이기에 그대로 2
```

## 2. 결합

```
### list
big_list = [1,2,3]+[4,5,6]
print(big_list)

### dict는 합집합개념
dict1={1:100, 2:200}
dict2 ={1:1000, 3:3000}
#dict1의 값에 dict2의 값 덮어버림
dict1.update(dict2)
print(dict1) #{1: 1000, 2: 200, 3: 3000}


dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}
dict2.update(dict1)
print(dict2) #{1: 100, 3: 300, 2: 200}
```
