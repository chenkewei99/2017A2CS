## Exam-style questions
### 1 a AND compares two bits in the same position and if both are 1 it puts a 1 in this position of the result word, otherwise it puts a 0 in this position of the result word
### b AND MASK

### MASK: #B00001111 // mask

### c
| Label | Opcode | Operand | Explanation |

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
| - | - | - | - |

### 2
| Label | Opcode | Operand | Explanation |

|  | LDR | #0 | set index register to zero |
| LOOP: | IN |  | input character |
|  | STI | STRING | store it at STRING (modified by index register) |
|  | INC | IX | increment index register |
|  | CMP | #33 | is this character the ! key? |
|  | JPN | LOOP | no – jump to beginning of loop |
|  | END |  | end of program |
| STRING: |  |  | store input characters from here onwards |
| - | - | - | - |
