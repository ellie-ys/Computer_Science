# Linux shell

리눅스 쉘에서는 프로세스를 작업(job)이라는 단위로 관리하는데 좀더 효율적으로 프로세스를 관리를 하기위해 포그라운드 (foreground)와 백그라운드 (background) 방식 으로 작업을 나누어 실행시킨다.

- 백그라운드: 작업을 수행하면 동시에 다른 명령어들을 실행, 실행시키는 명령어 뒤에 & 붙히게되면 background실행
- 포그라운드 : terminal 이용 해 돌아가는 거의 대부분 , 작업이 종료될 때까지 다른 쉘 명령어를 수행불가능

## job

- 백그라운드로 실행되는 작업을 보여주는 명령어
- Foreground <-> Background 더 효율적으로 관리
- terminal에 의존적이다.
  - process와 달리 터미널 명령을 통한 작업만을 의미한다
  - process를 실행할 수 있지만, terminal이 종료되면 job과 함께 process도 종료된다.
  - 각각 terminal마다 job 따로 존재

### job에서도 process와 마찬가지로 kill명령어 사용가능

\- kill %작업번호

ps명령어를 통해 PID 알아내 종료시키는 것도 가능  
process kill 명령어와 다른점) 옵션 붙히지않고 그냥 %를 사용해 작업번호를 넣어주면 된다.

### 예시 명령어

- sleep  
  해당 초만큼 기다리는 명령어
- sleep 500 &
- sleep 700 &
- jobs
- kill %1 #실행중인 백그라운드 프로세스 확인
- jobs

### 생각 )

백그라운드에서 실행되는 프로세스를 포그라운드로 가져오려면?  
\-> fg 와 bg를 이용  
정지되어 있는 프로세스를 백그라운드에서 실행시키기 위해 먼저 프로세스의 작업번호를 jobs명령어로 확인 하고

- fg \[jobs id\] ## 포그라운드로 프로세스 실행
- bg \[jobs id\] ## 백그라운드로 프로세스 실행

  ![](https://blog.kakaocdn.net/dn/QbmPA/btrkpsqTIay/NibRv9b5B94gRoaSlk7jtk/img.png)

  time.py를 백그라운드 실행

- ![](https://blog.kakaocdn.net/dn/rXaCf/btrkw4BSI3G/mPfIeXBrAA6oouhhkgBD8K/img.png)
- ps명령어로 현재 실행되고 있는 process 확인 -> 25번 PID사용중

- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZjcGs%2Fbtrku3jl52Q%2F6rDm79vdBkKzZX7RcThUYk%2Fimg.png)

jobs명령어로 1번으로 실행중인 python 확인  
kill명령어 이용해서 1번 종료시켜주고 다시 jobs 확인해보니 Terminated 된 것 확인
