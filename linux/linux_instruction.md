# 프로세스 목록 보기 :ps

```
ps <option>
```

대표적인 옵션 5가지

\-e : 현재 실행중인 모든 프로세스 정보 출력

\-f : 실행중인 전체 사용자의 모든 프로세스 출력

\-a : 실행중인 전체 사용자의 모든 프로세스 출력

\-u : 프로세스를 실행한 사용자와 프로세스 시작 시간등을 출력

\-x : 터미널 제어 없이 프로세스 현황 보기

# 프로세스 목록보기 : ps

- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fp6Fce%2Fbtrkw5tVXvg%2FPOejCZnTM8GKtj7v1RTNoK%2Fimg.png)

PID 프로세스 고유아이디

TTY 텔레타입, 수행되고 있는 TERMINAL

TIME 프로세스가 생성되고 얼마나 지났는가? CPU사용된 시기

CMD 프로세서의 이름 BASH SHELL BASH PROCESS가 실행되고 있다는 뜻.

# 프로세스 목록 보기 : ps -ef

-![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FM2IBv%2FbtrkqHoipqD%2FoKEvK9ilIlQhksZPWqKkEK%2Fimg.png)

  \-e 현재 실행중인 모든 프로세스 확인하는 옵션

\-f 모든 정보 보여주는 옵션

두개의 옵션 합쳐서 -ef사용 : 모든 프로세스의 모든 속성을 볼 수 있다.

UID : 계정의 고유 아이디

PID : 1 int process, 2 kernel thread demon process(kthreadd)

PPID : 부모 프로세스가 없는 1,2 PID는 0

STIME : start time 약자. 프로세스 시작된 시간, 월 : 일/ 시:분/ 시:분:초 로 나타낸다

# 프로세스 목록 보기 :ps -aux

- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDtZO7%2Fbtrkun3Ge06%2FJLB0dd1a5aHROwdulzRQSk%2Fimg.png)

실행 중인 모든 프로세스 출력

process 실행한 사용자와, 시작시간, 터미널 제어없이 프로세스 상태 실시간 반영된다.

# 프로세스 종료 : kill

많은 프로세스가 실행된다면 당연히 그만큼 메모리가 사용되고 다른 프로그램의 속도에 영향을 미치니 필요없는 프로세스 종료시켜야 함. 강제종료위해서는 kill명령어와 함께, 시그널번호나 PID를 적어주어야 한다.

kill <option> <PID>

\* option

\-l : 사용가능한 시그널 목록을 출력

\* 자주 사용하는 시그널 번호

\-1 : 재실행(sighup)

\-9 : 강제종료(sigkill)

\-15 : 정상종료(sigterm)

makeprocess.out은 의미없는 프로세스니 강제종료 해보자.

- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FTTOxd%2Fbtrkw5AHXo1%2FxeuSv90kdBk1xTeubkuu01%2Fimg.png)

---

리눅스 쉘에서는 프로세스를 작업(job)이라는 단위로 관리하는데

작업은 포그라운드 (foreground)와 백그라운드 (background) 두 가지 방식으로 동작

포그라운드는 작업이 시작되고 종료되는 시점까지 다른 쉘 명령어를 수행할 수 없고 대기하는 방식

백그라운드는 작업을 수행하면 동시에 다른 명령어들을 실행

#### 생각 )

#### 리눅스 터미널 ctrl+c누르지않고 종료시켜보고 싶다.

#### shell 종료시키는 **shutdown **명령어\*\*\*\*

- shutdown -r now : 즉시 재부팅
- shutdown -h now : 즉시 **종료**
- shutdown -r +분 메세지 : 메세지를 보여주고 x분후에 재부팅
- shutdown -h +분 메세지 : 메세지를 보여주고 x분후에 **종료**

#### 포그라운드 작업수행중에 다른 명령어 실행하고 싶다. 

#### 리눅스에서 **새로운 shell을 만들기** 명령어

1.  **터미널** 실행 : Ctrl + Alt + T.
2.  **터미널**내에서 **새로운** 탭으로 **터미널** 실행 : Ctrl + Shift + T.
3.  **터미널**내에서 **새로운** 창으로 **터미널** 실행 : Ctrl + Shift + N.
4.  탭으로 실행된 **터미널** 종료 : Ctrl + Shift + W.
