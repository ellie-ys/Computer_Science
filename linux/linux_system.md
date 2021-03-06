-   # 프로세스
    
    -   Process : 리눅스 시스템에서 메모리에 적재되어 실행되고 있는 모든 프로그램이 프로세스
        -   Program : 코드(명령어) 집합체
        -   process : 실행되고 있는 것
        -   multi process : 한 프로그램안에서 여러개 process 실행 - 운영체제에 의해 관리
    -   특징
        
        -   모든프로그램은 실행될 때 하나 이상의 process 를 갖는다
        -   병행적으로 실행 가능.
        -   부모 자식 관계를 가진다 (fork- 복사, 원본은 부모 복사본은 자식)
        -   커널에 의해 관리된다.
        -   모든 프로세스에는 소유자 (리눅스 계정)이 있다.
        -   PID
            -   모든 process 는 식별을 위한 고유 ID가 부여된다.
            -   PID1번은 init process, PID2번은 kthreadd 프로세스가 실행
            -   init process : 나머지 모든 시스템 프로세스의 부모 프로세스
            -   thread process : 모든 스레드의 부모 프로세스
        
        ex) 내가 thread 만들기위한해 프로세서 생성한다→ 2번 kthreadd 프로세서에서 fork
        -   프로세스 메모리는 크게 커널 주소 공간(kernel space)\[높은 메모리주소(0xFFF..F)\]과 사용자 주소 공간\[낮은 메모리주소(0x00..0)\]으로 분리
        -   이때 kernel 부분은 사용자 접근 불가능
        -   user address space : stack, heap, data, text 4영역으로 나뉨.
        -   사용자 주소 공간 내에 user space부분: 프로그램이 사용하는 라이브러리가 저장되는 공간이며 stack과 heap사이 공간
        -   data는 Bss 와 data로 구별할 수 있는데 간단하게 Bss는 초기화 되지 않은 정적변수들이 저장되며 data는 초기화 된 변수들이 저장
        -   코드영역
            -   코드 자체를 구성하는 메모리의 영역으로 하위 메모리부터 할당
            -   내가 프로그램짜고 코드 실행하면, 명령어화 되어서 저장하는 부분
        -   데이터 영역
            -   초기화된 변수 저장되는 곳
            -   전역 변수와 정적 변수, 구조체 등 저장
        -   BSS영역 : 초기화되지 않은 변수 저장, 프로그램 실행될 때 생성, 종료되면 시스템에 반환
        -   힙 영역
            -   동적인 메모리 할당영역
            -   동적으로 할당된 변수들이 낮은 주소로부터 높은 주소로 쌓임.
            -   위에서부터아래로 차근차근 쌓이면서(user space주소번호는 낮은번호-> 높은번호)
            -   동적 할당 변수 해제하면 힙영역에서 사라진다
        -   스택 영역 : **argv**, **argc** 그 외 **env**, **etc**
            -   프로그램이 자동으로 사용하는 임시 메모리영역, 매개변수, 메모리값등이 저장
            -   다른 영역들과 다르게 함수호출시 생성, 함수 끝나면 제거됨. 아래에서부터 위로 차근차근 쌓이면서 LIFO으로 작동.(user space주소는 높은번호→낮은번호)

# 프로세서의 메모리 구조
- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FuTfyR%2Fbtrktdtrwm4%2Fy0jLMv9LjXUVlKAo9ESO3K%2Fimg.png)

-   프로세스 메모리는 크게 커널 주소 공간(kernel space)\[높은 메모리주소(0xFFF..F)\]과 사용자 주소 공간\[낮은 메모리주소(0x00..0)\]으로 분리
-   이때 kernel 부분은 사용자 접근 불가능
-   user address space : stack, heap, data, text 4영역으로 나뉨.
-   사용자 주소 공간 내에 user space부분: 프로그램이 사용하는 라이브러리가 저장되는 공간이며 stack과 heap사이 공간
-   data는 Bss 와 data로 구별할 수 있는데 간단하게 Bss는 초기화 되지 않은 정적변수들이 저장되며 data는 초기화 된 변수들이 저장
-   코드영역
    -   코드 자체를 구성하는 메모리의 영역으로 하위 메모리부터 할당
    -   내가 프로그램짜고 코드 실행하면, 명령어화 되어서 저장하는 부분
-   데이터 영역
    -   초기화된 변수 저장되는 곳
    -   전역 변수와 정적 변수, 구조체 등 저장
-   BSS영역 : 초기화되지 않은 변수 저장, 프로그램 실행될 때 생성, 종료되면 시스템에 반환
-   힙 영역
    -   동적인 메모리 할당영역
    -   동적으로 할당된 변수들이 낮은 주소로부터 높은 주소로 쌓임.
    -   위에서부터아래로 차근차근 쌓이면서(user space주소번호는 낮은번호-> 높은번호)
    -   동적 할당 변수 해제하면 힙영역에서 사라진다
-   스택 영역 : **argv**, **argc** 그 외 **env**, **etc**
    -   프로그램이 자동으로 사용하는 임시 메모리영역, 매개변수, 메모리값등이 저장
    -   다른 영역들과 다르게 함수호출시 생성, 함수 끝나면 제거됨. 아래에서부터 위로 차근차근 쌓이면서 LIFO으로 작동.(user space주소는 높은번호→낮은번호)