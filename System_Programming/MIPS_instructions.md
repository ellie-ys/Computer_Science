# MIPS Instruction

- Arithmetic/Logic instructions

  - 산술 논리 연산
  - Operand로 register만 오도록 설계되어 있음
  - input register 2와 output regitster 1
  - bit 단위로 and or 나타냄
  - 음수 연산할 때는 2의 보수로 표현
  - 메모리에 저장된 데이터와 연산을 해야 한다면 Data Transfer Instruction을 먼저 수행 후에 가능

- Data Transfer (Load/Store) instructions

  - 메모리에 있는 데이터를 register로 load, store 명령을 수행
  - 속도가 느림
  - data copy instruction
    - LOAD: 메모리로부터 레지스터로 , 메모리의 값을 cpu로 읽어들이는 것
      ex) lw $s1, 20($3) -> $s3라는 register로부터 +20된 주소에 접근하여 load
    - STORE : 레지스터로부터 메모리로
      ex) sw $s1, 32($s3) -> $s1에 있는 data를 $s3에서부터 +32된 주소에 store

- Conditional branch instructions

  - 조건 만족하면 브랜치를 하고 아니면 기존 다음 조건 수행 등 조건에 따라 분기하는 것
  - branch
    - 현재 위치로부터 상대적인 (떨어져있는 위치)로 jump하는 branch
    - 현재위치로부터 상대적인 점프할 때는 16비트, 2^18까지 addressing가능 (정확하게는 18비트)
  - set
    - compare
    - 레지스터 3개사용, branch라기보다는 논리연산이라고 보는게 타당

- Unconditional Jump instructions

  - Unconditional 무조건 수행할 위치로 PC 바꾸는 명령 - JUMP해라
  - 6bit 사용 & 나머지 26bit로 target address 설정

    - 기계어 4 배수 단위, 그 주소를 4로 나눈 값으로 적으면 되므로, 28 bit로 target address 접근 가능
      ex) j 2500 -> 10000째로 jump!

  - 위의 경우에는 모든 메모리로 점프는 불가능, 메모리 address는 32bit인데, 28bit만 표현 가능
    - 시간은 immediate constant보다 오래걸리지만 4G bytes 메모리 어느 주소든 표현 가능
    - jr $ra -> jump register의 뜻, ra는 $31

## 그 외에

- alignment restriction
  - Memory operand addresses must be multiple of their size.
  - 즉 4byte를 1word이므로 메모리 데이터에 접근하려면 주소가 4배수인 것에만 접근(1word = 4byte)
  - 1word가 MIPS64인 경우, 8byte이므로 주소는 8의 배수여야 함

* register 0번에는 항상 constant 0을 저장.
* ==0을 표현할 때 ==$0 이라고 표현

## 명령어 처리 단위

- word : 4byte 저장
- half word : 2byte 저장
- byte : 1byte 저장
