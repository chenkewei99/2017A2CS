factorial(1, 1).
factorial(X, Y) :-
    Z is X - 1 ,
    factorial(Z, B),
    Y is X * B.

bunnyears(0, 0).
bunnyears(X, Y) :-
    Z is X-1,
    bunnyears(Z, E),
    Y is E+2.

fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(X, Y) :-
    Z is X-1,
    fibonacci(Z, F),
    K is Z-1,
    fibonacci(K, O),
    Y is F+O.

bunnyears2(0,0).
bunnyears2(X, Y) :-
    Z is X-1,
    bunnyears2(Z,B),
    A is Z mod 2,
    Y is B+2+A.

triangle(0,0).
triangle(1,1).
triangle(X,Y):-
    Z is X-1,
    triangle(Z,T),
    Y is T+X.

sumdigits(0,0).
sumdigits(X,Y):-
    Z is X//10,
    sumdigits(Z, S),
    Y is S+X mod 10.

count7(0,0).
count7(X,Y):-
    Z is X//10,
    B is X mod 10,
    count7(Z, S),
    Y is S+ B//7-B//8.


























