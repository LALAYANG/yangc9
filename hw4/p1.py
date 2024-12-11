from z3 import *

solver = Solver()
f = Function('f', IntSort(), IntSort(), IntSort())

e = Const('e', IntSort())
c = Const('c', IntSort())

a, b = Ints('a b')
associativity = ForAll([a, b, c], f(a, f(b, c)) == f(f(a, b), c))

identity = ForAll([a], And(f(e, a) == a, f(a, e) == a))

other_identity = ForAll([a], And(f(a, c) == a, f(c, a) == a, c != e))

solver.add(associativity, identity, other_identity)

result = solver.check()

print(result)
if result == sat:
    print(solver.model())
else:
    print("unsat!")
