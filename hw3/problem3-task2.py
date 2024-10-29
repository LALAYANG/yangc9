from z3 import *

s = Solver()
x, y = Reals('x y')
formula = ForAll([x], Exists([y], And(2*y > 3*x, 4*y < 8*x + 10)))

s.add(formula)
result = s.check()
print(result)
