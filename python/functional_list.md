# List의 기능

- list.index( value ) : 값을 이용하여 위치를 찾는다.

  index는 list를 읽어서 값을 조사하는 역활.

```
list1 = [135, 462, 27, 2763, 234]
print(list1.index(27))
```

```
try :
	print(list1.index(50))
except ValueError:
	print('index가 존재하지 않습니다.')

#위와같이 하거나,

if 50 in lis1:
    print(list1.index(50))
#이렇게 조건을 달아주어도 괜찮다.
```

- list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가

```
# extend
list1 = [135, 462, 27, 2763, 234]
list1.extend([9, 10, 11])
print(list1) # [135, 462, 27, 2763, 234, 9, 10, 11]

# extend보다 성능은떨어진다. + 연산자
list2 = [1, 2, 3]+ [4, 5, 6]
```

- list.insert( index, value ) : 원하는 위치에 값을 추가

```
list = [1, 2, 3]
list.insert(3, 4)     #list = [1, 2, 3, 4]로 4가 추가


#insert 이용 2 index 에 999넣기
list1.insert(2, 999)
print(list1) #[135, 462, 999, 27, 2763, 234, 9, 10, 11]

list1.insert(-1,9999)
print(list1) #맨 뒤에 9999넣고 기존의 11이 한칸 밀림
#[135, 462, 999, 27, 2763, 234, 9, 10, 9999, 11]


#insert index벗어나는 값 넣으면 맨 마지막에 555넣는다.
print(list1.insert(10000,555))
print(list1) #[135, 462, 999, 27, 2763, 234, 9, 10, 9999, 11, 555]


```

- list.sort( ) : 값을 순서대로 정렬

```
list = [3, 5, 6, 4, 2, 1]
list.sort()           #list = [1, 2, 3, 4, 5, 6]으로 정렬
```

- list.reverse( ) : 값을 역순으로 정렬

```
list = [3, 5, 6, 4, 2, 1]
list.reverse()     #list = [1, 2, 4, 6, 5, 3]역순으로 정렬
```
