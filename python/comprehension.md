# Comprehension

## List

```
areas = []
```

기존

```
for i in range(1, 11):
	if i% 2 == 0:
		areas = areas + [i*i]
	#areas = areas+ [i*i]
	print("areas", areas)
```

### list comprehension

계산식 for문

```
area1 = [i*i for i in range(1,11)]
```

계산식 for문 조건문

```
areas2 = [i*i for i in range(1,11) if i% 2 ==0]
print("areas2", areas2)
```

계산식 for문 for문

- 길이 15\*15 바둑판 각 좌표 튜플로

```
[ ( x, y ) for x in range(15) for y in range(15) ]
```

## Dictionary

```
students = ['태연','진우','정현','하늘', '성진']
```

기존

```
for number, name in enumerate(students):
	print("{}번의 이름은 {}입니다.".format(number, name))
```

list comprehension

- 형식 for문

```
students_dict = {"{}번".format(number+1) : name for number, name in enumerate(students)}

print(students_dict)
```

### zip

```
scores = [85, 92, 78, 90, 100]
```

기존

```
for x, y in zip(students, scores):
    print(x,y)

```

- for문 zip활용

```
score_dic = {student: score for student, score in zip(students,scores)}

print(score_dic)
```
