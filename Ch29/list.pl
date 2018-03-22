{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
member(I,[I|_]).\
member(I,[_|T]):-\
	member(I,T).\
\
myappend([],X,X).\
myappend([H|T],L,[H|R]):-\
	myappend(T,L,R).\
\
\
mylast(H,[H]).\
mylast(L,[_|X]):-\
	mylast(L,X).\
\
mylast2(X,[X,_]).\
mylast2(L,[_|X]):-\
	mylast2(L,X).\
\
element_at(H,[H|_],1).\
element_at(L,[_|T],X):-\
	M is X-1,\
	element_at(L,T,M).\
\
len([],0).\
len([_|T],L):-\
	len(T,X),\
	L is X+1.}