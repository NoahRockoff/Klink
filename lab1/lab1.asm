.ORIG x3000
; write your code here

AND R1, R1, #0 ; bit counter
AND R2, R2, #0 ;digit counter

ADD R2, R2, #-4 ;sets digit counnter to under 4
CHECKCOUNT BRzp DONE

;init digit and bit counter below 
AND R0, R0, #0  ;digit
ADD R1, R1, #-4

TESTER BRzp OVER4BIT
ADD R0, R0, R0
ADD R3, R3, #0
BRzp JUMP
ADD R0, R0, #1
JUMP ADD R3, R3, R3
ADD R1, R1, #1
BR TESTER
; This will be the false branch of got <4 bits from R3

OVER4BIT ADD R0, R0, #-9

BRnz ADD0
ADD R0, R0, #7


ADD0 ADD R0, R0, #9
ADD R0, R0, XF 
ADD R0, R0, XF
ADD R0, R0, XF
ADD R0, R0, #3



OUT
ADD R2, R2, #1
BR CHECKCOUNT

DONE HALT
 

 
 .END
