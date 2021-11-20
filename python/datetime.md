# Datetime
시간의 연산을 가능하게 해주는 클래스
```
import datetime

start_time = datetime.datetime.now()
print(start_time)
```
## replace

자기 자신 바꾸려면 별도 지정해주어야함
```
ellie_birthday = start_time.replace(year = 2022, month = 2, day = 9)
print(ellie_birthday)
```


## 시간이 얼마나 남았는지?
```
how_long = ellie_birthday - datetime.datetime.now()
print(type(how_long))

print(how_long.days)

print(how_long.seconds)


print("2월 9일까지는 {}일 {}시간이 남았습니다".format(how_long.days, how_long.seconds//3600))
```
# Timedelta
```
addtime = datetime.timedelta(days = 10)
datetime.datetime.now() + addtime    # 10일 후
datetime.datetime.now() - addtime    # 10일 전

thedate = datetime.datetime.now().replace(hour = 10, minute=0, second = 0)
          + datetime.timedelta(days = 3)       # 3일 후 10시 정각

```