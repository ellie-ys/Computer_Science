# Procedure Call in Program Excecution
* 고급언어로 작성된 프로그램이 컴파일 되고 기계어로 바뀌고 실행되면 메모리에 각 실행파일의 주소공간이 할당된다.
* 이때 MIPS에서 주소공간은 논리적으로 낮은 0번지 부터 2^23-1까지 할당된다. 모든 프로그램마다 낮은 주소는 0번지 높은 주소는 2^32-1로 공간이 할당됨 이때는 실제 메모리의 물리적인 주소와 일치해서 생성되는 것이 아니기 때문에 논리적이라는 표현을 사용한것이다.

![image](https://user-images.githubusercontent.com/76929823/141066257-8052364b-ce14-48d1-aa53-78a8162cf3ec.png)

# What shold be done with procedure call?
- 함수 호출이후에도 값이 유지되어야 하는 register 저장
    - 이때는 register 마다 함수호출하는쪽과 호출 당하는쪽이 처리해야할 register가 나누어져 있다.
- return address의 저장(보통 stack에 저장하지만 return address만 처리하는 register가 비어있다면 이곳에 저장)
- argument 저장
- 지역 변수를 위한 공간 할당 필요(stack에 할당)
    - 같은 함수가 여러번 호출 되면 지역변수는 매번 호출 됨
    - stack pointer($sp)레지스터가 stack의 가장 최근 저장 위치를 가리킴
    - hign address부터 쌓여서 점점 low address로 쌓여감
## MIPS의 STACK
    - STACK에 정보 저장
        - sub $sp, $sp, 4
            - 스택읜 점점 낮은 주소 공간에 데이터를 쌓아가며 저장하기 때문에 현재 top위치에서 주소 4칸 이동하여(메모리는 byte당 하나의 주소를 갖고, 스택하나의 크기가 4byte이기 때문)
        - sw $t0, 0($sp)
    - Stack에서 정보 인출
        - lw $t0, 0(4sp)
        - add $sp, $sp, 4
            - 정보 다른 register로 옮기고 메모리주소 4칸 높은쪽으로 이동