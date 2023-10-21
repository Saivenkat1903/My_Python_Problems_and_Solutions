''' Using sympy to solve inequalities '''

from sympy import *

def isolve(thing):
    ineq=sympify(thing)
    lhs=ineq.lhs
    var=list(lhs.free_symbols)[0]
    rel=ineq.rel_op

    if lhs.is_polynomial()==True:
        p=Poly(lhs,var)
        print(solve_poly_inequality(p, rel))
    elif lhs.is_rational_function()==True:
        num,den=lhs.as_numer_denom()
        p1=Poly(num)
        p2=Poly(den)
        print(solve_rational_inequalities([[((p1, p2),rel)]]))
    else:
        print(solve_univariate_inequality(ineq, var, relational=False))

x=input("enter\n")
isolve(x)
