# 상속

- 부모클래스: 상속하는 클래스
- 자식 클래스 : 상속받는 클래스를
- 자식클래스가 부모 클래스의 내용을 가져다 쓰기

```
class Animal():
    def walk(self):
        print("걷는다")
    def eat(self):
        print('먹는다')
    def greet(self):
        print('인사한다.')

```

# 상속 - Inherit

유전적인 특징을 물려준다.

class 괄호 안에 다른 class 넣는 것.

# Override

같은 이름을 가진 메소드를 덮어쓴다.

## Inherit, Override 예

```

class Cow(Animal):
	'''소'''
class Human(Animal):

    def wave(self):
        print('손을 흔든다')

    def greet(self):
	#부모와 같은 method만들면서 override가능
        self.wave()

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다')

    def greet(self):
        self.wag()


person = Human()
#override
person.greet()

dog=Dog()
#override
dog.greet()

cow= Cow()
#따로 greet method 정의 안해서, 부모클래스 greet그대로
cow.greet()

```

# Super

부모의 동작 불러오는 방법
자식클래스의 override한 method에서 부모 class의 method를 사용하고 싶을 때

```
super().<부모클래스메소드이름>
```

### Inherit, Override , Super 예

```
class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')
    def greet(self):
        print('{}이/가 인사한다.'.format(self.name))

class Human(Animal):

	def __init__(self, name, hand):
		super().__init__(name)
		#name은 부모의 init함수가 처리해주고
		self.hand = hand
		#hand는 Human class에서 받아줌
	def wave(self):
		print('{}손을 흔들면서'.format(self.hand))

	def greet(self):
		self.wave()
		super().greet()

person = Human("사람", '오른')
person.greet()
```

# 내 예외 만들기

- 직접 예외처리 코드의 직관성을 높일 수 있다.
- 파일을 하나 만들어 예외를 정의
- Exception 클래스를 상속받아 만든다

Exception Class

ValueError Class가 Exception Class상속

UnexpectedRSPValue는 ValueError Class,Exception
Class 상속

```
#UnexpectedRSPValue.py
class UnexpectedRSPValue(Exception):
	'''가위 바위 보 가운데 하나가 아닌 값인 경우에 발생하는 에러'''

```

```
#my_exception.py

from UnexpectedRSPValue import UnexpectedRSPValue
value = '가'

try:
	if value not in ['가위', '바위','보']:
		raise UnexpectedRSPValue
except UnexpectedRSPValue:
	print("Error가 발생했습니다.")

#value error 흔하게 나오는 에러.

```

```
#my_exception2.py
def sign_up():
    '''회원가입 함수'''
try:
    sign_up()
except BadUserName:
    print('이름으로 사용할 수 없는 입력')
except PasswordNotMatched:
    print('입력한 패스워드 불일치')

```
