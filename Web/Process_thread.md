# Process와 Thread

## 용어

### 프로그램(Program)

- 실행시킬 수 있는 파일
  - 어떤 작업을 위해 운영체제 위에서 실행할 수 있는 파일
  - 예를 들어 웹 브라우저, 워드 프로세서, 카카오톡 등

### 프로세스(Process)

- 현재 실행 중인 프로그램
  - 운영 체제 위에서 실행 중인 프로그램
  - 프로그램 명령어와 데이터들이 메모리에 올라오고 실행 중 또는 실행 대기 중인 상태
    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcFTRvI%2FbtroT6RuwQe%2FPYpM5UlvfM3lbkiTuYhKxk%2Fimg.jpg)
    운영체제가 스케줄링 하면서 프로세스를 Switching 위해서는
    위의 그림과 같은 프로세서의 상태 뿐만 아니라
    PCB(Process Control Block)도 알 수 있어야 한다.
- 프로세스의 구조
  - Stack, Heap, Data, Code
  - Stack을 제외한 세 가지 영역은 공유

### 프로세서(Processor)

- 그 작업을 실제로 실행하는 것
  - 프로세스가 동작될 수 있도록 하는 하드웨어(=CPU)
  * 동작 : 프로그램의 자원들이 메모리에 올라오고, 실행 되어야 할 코드의 메모리 주소를 CPU의 레지스터로 올리는 것

## multitasking?
- 작업관리자를 보면, 동시에 여러작업을 하는 것처럼 보이지만
- CPU는 한순간에 하나의 프로세스만 실행할 수 있다.
- 운영체제가 짧은 시간에 수십번에서 수천번 실행할 프로세스를 교체하고 있기 때문에, 우리는 동시에 여러 개의 작업이 실행되고 있다고 느낀다.

### 프로세스 마다 컴퓨터 자원을 분할해서 할당한다.

### Concurrency

프로그램 하나가 일부분씩 진행하는 것, context switching
동시에 진행되는 것처럼 느껴진다.

### Parallelism

- 프로세스 하나에 코어가 여러 개 달려서 각각 동시에 작업 수행

- multi core processor
  - 듀얼코어, 쿼드코어, 옥타코어 등
  - cpu의 속도가 발열 등 물리적 제약 때문에 빠르게 발전하지 못하자, 그 대안으로 코어를 여러 개 달아서 작업 분담할 수 있도록 만든 것

## Thread

- 한 프로세스 안에도 여러 개의 작업들이 동시에 진행
- 여러 개의 작업 중 하나의 작업이 Thread
- 컴퓨터의 같은 자원을 공유
  - 프로세스마다 주어진 전체 자원을 thread가 함께 사용

### Thread 프로그래밍

- 장점 : 속도와 효율
- 단점
  - 시간 문제로 발생하는 error 상황들 예상하고 방지해야 함
  - 코드를 짜기도, 디버깅을 해서 오류찾고 원인 밝히기도 어려움
  - 이해된다면 보다 나은 동시성 프로그래밍의 기초지식
  - 도구나 프로그래밍 방식 이용하기도 함 -> Closure, Functional Programming, Lambda, Actor




# multi process vs multi thread

아무 것도 실행하고 있지 않은 상태
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdyP3AH%2FbtroVjJU4GJ%2FVu3COcOQPoTJMClAsSSr9K%2Fimg.jpg)

## multi process

-> context switching
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXxi51%2Fbtro9HV29qJ%2FvOhXMLYrslWbUMSvWKMy81%2Fimg.png)

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbghcYX%2FbtroVkIMLpN%2FqWcKYRGgchbJVH8ljb94IK%2Fimg.jpg)

- (실제로 pcb가 아닌 register block이 들어가게 됨)

## multi thread

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbghcYX%2FbtroVkIMLpN%2FqWcKYRGgchbJVH8ljb94IK%2Fimg.jpg)
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcncyBG%2FbtroXMSnmCY%2FMDIa1ked0WkKKCbbzymDm0%2Fimg.png)
-> 그 다음 thread 할당 받음

- 다음 thread는 이전 thread와 code data, heap은 공유하고 있기 때문에
- pcb에 있던 register block : 이것만 바뀐다. thread별로 존재하므로

## multi Thread가 multi processing보다 context switching 비용이 적다.
