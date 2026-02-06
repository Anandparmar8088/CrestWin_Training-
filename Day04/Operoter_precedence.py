# operator precedence in python :-
'''  Order in which python evaluated operators in an expression 

     in py () perenthisis has the hoghest precedence and the := has the last precedance 

     The () override the order of ecexution 


(a+b) or A>2 and A<10

( ) has asociativity from left to right (LTR) 
 


The order of precedence is :-
 
 () : Parentheses (highest precedence) -> Associativity: Left to right
x[index], x[index:index] : Subscription, slicing -> Associativity: Left to right
await x : Await expression
** : Exponentiation -> Associativity: Right to left
+x, -x, ~x : Unary plus, unary minus, bitwise NOT -> Associativity: Right to left
*, @, /, //, % : Multiplication, matrix multiplication, division, floor division, remainder -> Associativity: Left to right
+, - : Addition and subtraction -> Associativity: Left to right
<<, >> : Bitwise shifts -> Associativity: Left to right
& : Bitwise AND -> Associativity: Left to right
^ : Bitwise XOR -> Associativity: Left to right
| : Bitwise OR -> Associativity: Left to right
in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, membership, identity tests -> Associativity: Left to right
not x : Boolean NOT -> Associativity: Right to left
and : Boolean AND -> Associativity: Left to right
or : Boolean OR -> Associativity: Left to right
if-else : Conditional expression -> Associativity: Right to left
lambda : Lambda expression
:= : Assignment expression (Walrus operator) -> Associativity: Right to left




#  Operator that do not have any associativity 

1) Lambda 
2) Await


# Non-associative operator  
if A == 10 and b+=10
= and += 

It will throught an error :- SyntaxError: invalid syntax '''

