from z3 import *

solver = Solver()
f = Function('f', IntSort(), IntSort(), IntSort())

e = Const('e', IntSort())
a = Const('a', IntSort())
c1 = Const('c1', IntSort())
c2 = Const('c2', IntSort())

a, b, c = Ints('a b c')
associativity = ForAll([a, b, c], f(a, f(b, c)) == f(f(a, b), c))

identity = ForAll([a], And(f(e, a) == a, f(a, e) == a))

negated_uniqueness = And(f(a, c1) == e, f(c1, a) == e, f(a, c2) == e, f(c2, a) == e, c1 != c2)

solver.add(associativity, identity, negated_uniqueness)

result = solver.check()

if result == sat:
    print(solver.model())
else:
    print("unsat!")
