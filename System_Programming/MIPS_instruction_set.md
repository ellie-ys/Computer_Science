# MIPS Instruction Set Architecture

- Microprocessor without Interlocked Pipeline Stages
- IBM, 인텔 등 프로세서 마다 고유의 Instruction Set이 있지만 그 중에서도 MIPS Technologies에서 개발한 RISC 기반의 ISA를 말함
- 그 외에 또 많이 사용되는 RISC\*는 ARM이 있다.

# MIPS register

\_ register

- CPU안에 존재, 메모리 계층 가장 위에 존재하며 access 속도가 가장 빠른 저장장소
- instruction에 의해 직접 읽고 쓰기가 가능하며, 프로그램 수행 중 variable이나 temporary data를 저장하는데 사용

* MIPS32 ISA에서는 register 사이즈가 32bits이며, 32bits가 MIPS의 word가 됨

* 32bits는 이진법으로 000..00..000(32개)부터 11111..11..11(32개)까지 표현이 가능함
* word란, 컴퓨터가 한번에 인식하고 처리할 수 있는 단위이다. 레지스터가 몇 bits인지를 확인하면 알 수 있음

* 32개의 범용 register 그 외 special registers

  - Program counter(PC) 32bits , LO와 HI, 32개의 32bit Floating-point registers
    - PC : 다음번에 수행할 위치 담고 있음
    - LO,HI : 곱셈과 나눗셈 결과 저장하기 위함
      - lo는 낮은 자리수나 quotient, hi는 높은 자리수나 remainder을 저장

* MIPS에서 범용 레지스터는 왜 32개만 사용할까?
  - 접근 속도를 빠르게 하기위해서
  - 레지스터 수가 많으면 READ/WRITE속도가 느려져서 clock cycle time이 증가

## MIPS Memory

- MIPS를 Load-Store architecture라고 부른다.

  - mips에서 산술연산은 register를 operand로 사용
  - Data transfer instrucion으로만 메모리에 접근 가능

- memory
  - 8bits의 레지스터가 나열된 것, 즉 1bytes의 1차원적인 array
  - 각 메모리에 address가 할당되며 이것을 통해 memory operand에 접근 가능
  - MIPS와 ARM은 32bit- address 를 가지며 2^32개의 위치에 접근할 수 있다.
  - 접근 가능한 메모리 크기는 2^32 bytes (용량 4GB)

### 용어

- 단위

  - bit : binary digit
  - byte : 1개의 영문자를 저장하는 최소 단위
  - word : 컴퓨터가 한번에 인식하고 처리할 수 있는 단위. MIPS에서 1word는 4bytes(32bits)이다.

- RISC
  - 적은 수의 컴퓨터 명령어를 수행하도록 설계된 마이크로프로세서
  - 프로세서를 단순화했고, H/W 구조가 단순
  - cf. CISC 는 복잡한 명령어를 수행하도록 설계된 마이크로세서
    - 많은 특수 명령어 있고 H/W가 복잡하지만, 특정 명령에 최적화되어 설계되는 경우에는 RISC보다 속도가 더 빠르다

## Immediate addressing

- instruction 자체에 직접 포함되는 상수 필드
- 추가적 메모리 접근이 없어 빠른 연산 가능
- 단점: 재사용 불가(이유:기계어 자체에 피연산자가 들어 있기 때문에 다음 instruction에서 재사용불가), 32bit 내에 포함되므로
