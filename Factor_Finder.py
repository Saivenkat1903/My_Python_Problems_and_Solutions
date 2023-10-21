''' Using Sympy to factor polynomials '''

from sympy import sympify, factor, pprint

expr=input("Enter an expression in terms of x\n")

try:
    expression=sympify(expr)
except:
    print("Invalid Input.")

answer=factor(expression)

print(answer)
