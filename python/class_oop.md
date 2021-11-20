# 자료형

## isinstance(값, 자료형)

```
isinstance(42, int) #True
```

# Class

함수나 변수들을 모아 놓은 집합체

# Instance

클래스에 의해 생성된 객체
인스턴스 각자 자신의 값을 가지고 있다.

## class와 instance를 사용하면

- 데이터와 코드를 사람이 이해하기 쉽게 표현 가능
- class에 function 넣을 수 있다.

### type확인

```
print(type(5))
# <class 'int'>

numbers1 = []
print(type(numbers1))
#<class 'list'>

numbers2 = list(range(10))
print(numbers2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = list("Hello")
print(characters)
# ['H', 'e', 'l', 'l', 'o']

print(type(numbers2))
# <class 'list'>
print(type(characters))
# <class 'list'>

```

### list라는 class의 각자 다른 instance라는 의미.

numbers1은 type이 list 인데 list와 완전히 같은 건 아니다.??

```
print(isinstance(numbers1, list))
# True

print(numbers1 == list)
#false
```

## class 만들기

```
# making_class.py

class Human():
	'''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

person1.name = 'seoul citizen'
person2.name = 'u s a citizen'

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))


speak(person1)
speak(person2)

```

Human class는 말할 수 있는 능력이 생김.

```
Human.speak = speak

person1.speak()
person2.speak()

```

리스트만드는 것과 비슷하다.

a = list()

print(a) #[]

# 모델링(modeling)

클래스로 현실의 개념을 표현

```
# class_modeling.py
class Human():
	'''인간'''

# <!-- person = Human()
# person.name = '철수'
# person.weight = 60.5 -->


def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight

    return person

Human.create = create_human

person = Human.create('철수', 60.5)


def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었슴".format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었슴".format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()
```

# Method

메소드는 함수와 비슷

클래스에 묶여서 클래스의 인스턴스와 관계되는 일 해줌

### class 내부에 함수 포함

```
#class_method.py
class Human( ):
	'''인간'''
    def __init__(self, name, weight):
        '''초기화 함수'''
        # instance만드는 순간에 자동호출
		self.name = name
		self.weight = weight

    def __str__(self):
        ''' 문자열화 함수'''
        # human을 string으로 표현할 때

        return "{} ( 몸무게 {}kg)".format(self.name, self.weight)

	def eat( self ):
		self.weight += 0.1
		print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

	def walk( self ):
		self.weight -= 0.1
		print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human.create("철수", 60.5)
person.eat()

person = Human( "사람", 60.5 ) # 초기화 함수 사용
print( person ) # 문자열화 함수 사용
```

### self

메소드의 첫번째 인자

인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달

### 특별한 method

- 초기화 함수
  ** \_ _ init _ \_ ** /
  인스턴스 만들때 실행
- 문자열화 함수
  ** \_ _ str _ \_ ** /
  인스턴스 자체를 출력할 때 형식 지정해줌
