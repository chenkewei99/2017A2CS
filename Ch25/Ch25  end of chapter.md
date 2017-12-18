#TASK 25.02 Dry run
###Kevin Chen option 1

Call number|Procedure call|n = 0|n = 1|Result|Return Value
---|---|---|---|---
1|X(19)|*False*|*False*|X(9)|
2|X(9)|*False*|*False*|X(4)|
3|X(4)|*False*|*False*|X(2)|
4|X(2)|*False*|*False*|X(1)|
5|X(1)|*False*|*True*||1
(4)|X(2)|*False*|*False*|0|0
(3)|X(4)|*False*|*False*|0|0
(2)|X(9)|*False*|*False*|1|1
(1)|X(19)|*False*|*False*|1|1

#Ch25 Exam-style Questions
###1. 
###a
####iteration will repeat one procedure. Recursion is calling itself in one function.
###b
####recursive subroutines' code is shorter, but it always take many addresses.
###2.
###a
####recursively defined is that in its own function, it call itself.
###b
Call number|Procedure call|Exponent = 0|Result
---|---|---|---
1|Power(2,4)|*False*|2*Power(2,3)
2|Power(2,3)|*False*|2*2*Power(2,2)
3|Power(2,2)|*False*|2*2*2*Power(2,1)
4|Power(2,1)|*False*|2*2*2*2*Power(2,0)
5|Power(2,0)|*True*|2*2*2*2*1
(4)|Power(2,1)|*False*|2
(3)|Power(2,2)|*False*|4
(2)|Power(2,3)|*False*|8
(1)|Power(2,4)|*False*|16

###c
####stack can store partial results. When exponent=0, the stack will output the results until the first procedure returned.

###e
```pseudocode
FUNCTION Power(Base : INTEGER, Exponent : INTEGER) RETURNS INTEGER
Result = 1
WHILE Exponent > 0
Result = Result * Base
Exponent = Exponent - 1 
ENDWHILE
RETURN Result
ENDFUNCTION
```
###f
**i**
####using less addresses
**ii**
####code is shorter 

####**3(a)**
####**i**  Line 04
####**ii**  Line 06

####**3(b)**
Call Varible | Procedure call | (n=1) or (n=0)| Result | Return Value |
--- | --- | --- | --- | ---
1 | Fibonacci(4) | False | Fibonacci(3) |  
2 | Fibonacci(3) | False | Fibonacci(2) |  
3 | Fibonacci(2) | False | Fibonacci(1) |  
4 | Fibonacci(1) | True | Fibonacci(0) | 1
5 | Fibonacci(0) | True | 1 | 1
6 | Fibonacci(2) | False | Fibonacci(1) |  
7 | Fibonacci(1) | True | Fibonacci(0) | 1
(3) |  | True |  | 1
8 | Fibonacci(0) | True | 1 | 1
(7)|||1
(1)|||3
