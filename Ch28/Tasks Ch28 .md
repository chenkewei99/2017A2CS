# chapter 28
## task 01
A=2:
LDM #2
STO A

B=10:
LDM #10
STO B

C = A + B :
LDD A
ADD B
STO C

D=A-B:
LDD B
XOR #&FF
INC ACC 
ADD A 
STO D

## task 02
    LDD A
    CMP #0
    JPE ELSE
THEN: STO B
    JMP ENDIF
ELSE: LDD B
    DEC ACC
    STO B
ENDIF:………

## task 03
    LDM #1
    STO Number
    LDM #0
    STO Total
    LDM #5
    STO Max
LOOP: LDD Total
    ADD Number
    STO Total
    LDD Number
    INC ACC
    STO Number
UNTIL:CMP Max
    DEC ACC
    JPN LOOP
ENDLOOP:

## task 04
    LDM #0
    STO Count
    LDM #78
    STO Letter
LOOP: LDD Count
    INC ACC
    STO Count
    IN
    CMP Letter 
    JPN LOOP
ENDLOOP:

## task 05
    LDM #0
    STO Count
    LDM #78
    STO Letter
LOOP: LDD Count
    INC ACC
    STO Count
    IN
    CMP Letter 
    JPN LOOP
ENDLOOP:
    LDD Count
    OUT
    
## task 06
|label | opcode|operand|explanation|
|-|-|-|-|
||LDD| STACKBASE||
||STO| STACKPTR| initialise|
|LOOP1:| IN|| read|
||CMP #13| the end-of-line character?|
||JPE| LOOP2| yes – go to next loop|
||STI| STACKPTR| store|
||LDD| STACKPTR||
||INC| ACC| Increment stack pointer|
||STO| STACKPTR||
||JMP |LOOP1|
|LOOP2:| LDD| STACKPTR||
||CMP| STACKBASE |stack empty ?|
||JPE| ENDWORD||
||LDI |STACKPTR| Load contents at top of stack output character|
||OUT||
||LDD| STACKPTR|
||DEC |ACC| decrement stack pointer|
||STO| STACKPTR||
||JMP |LOOP2||
|ENDWORD:| END ||end of program|

## Exam-style questions
### 1 a 
AND compares two bits in the same position and if both are 1 it puts a 1 in this position of the result word, otherwise it puts a 0 in this position of the result word

### b 
AND MASK
MASK: B00001111 // mask

### c 
| Label | Opcode | Operand | Explanation |
| - | - | - | - |
|  | IN | | input first digit |
|  | AND | Mask | convert from ASCII to its digit value |
|  | LSL | #4 | move to upper nibble |
|  | STO | Result | store in location Result |
|  | IN | | input second digit |
|  | AND | Mask | convert from ASCII to its digit value |
|  | OR | Result | combine the two values |
|  | STO | Result | store result |
| Mask: | &0F |  | mask to convert from ASCII to digit equivalent |
| Result: | &00 | | memory location for result |

### 2
| Label | Opcode | Operand | Explanation |
| - | - | - | - |
|  | LDR | #0 | set index register to zero |
| LOOP: | IN |  | input character |
|  | STI | STRING | store it at STRING (modified by index register) |
|  | INC | IX | increment index register |
|  | CMP | #33 | is this character the ! key? |
|  | JPN | LOOP | no – jump to beginning of loop |
|  | END |  | end of program |
| STRING: |  |  | store input characters from here onwards |
