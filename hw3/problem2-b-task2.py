from z3 import *

L1, U1 = Reals('L1 U1')
L2, U2 = Reals('L2 U2')
L3, U3 = Reals('L3 U3')
L4, U4 = Reals('L4 U4')

def nonempty(la, ua):
    return la < ua

def unequal(la, ua, lb, ub):
    return Not(And(la == lb, ua == ub))

def intersect(la, ua, lb, ub):
    x = Real('x')
    return Exists(x, And(la < x, x < ua, lb < x, x < ub))

s = Solver()

s.add(nonempty(L1, U1))
s.add(nonempty(L2, U2))
s.add(nonempty(L3, U3))
s.add(nonempty(L4, U4))

s.add(unequal(L1, U1, L2, U2))
s.add(unequal(L1, U1, L3, U3))
s.add(unequal(L1, U1, L4, U4))
s.add(unequal(L2, U2, L3, U3))
s.add(unequal(L2, U2, L4, U4))
s.add(unequal(L3, U3, L4, U4))

s.add(intersect(L1, U1, L2, U2))
s.add(intersect(L1, U1, L4, U4))
s.add(intersect(L2, U2, L3, U3))
s.add(intersect(L3, U3, L4, U4))

s.add(Not(intersect(L1, U1, L3, U3)))
s.add(Not(intersect(L2, U2, L4, U4)))

=result = s.check()
print(result)

if result == sat:
    print(s.model())
