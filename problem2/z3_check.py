from z3 import *

p, q, r = Bools('p q r')

phi = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p), Or(p, q, Not(q)), Or(Not(r), q))

psi = q

solver = Solver()

# Task 1: Check if phi is satisfiable
solver.add(phi)
if solver.check() == sat:
    print(f"{phi} is satisfiable")
    # print(f"Model for {phi}:", solver.model())
else:
    print(f"{phi} is not satisfiable")
    
solver.add(psi)
if solver.check() == sat:
    print(f"{psi} is satisfiable")
    # print(f"Model for {psi}:", solver.model())
else:
    print(f"{psi} is not satisfiable")

# Task 2: Check if phi and psi are equivalent
solver.reset()
solver.add(phi == psi)
if solver.check() == sat:
    print("phi and psi are equivalent")
else:
    print("phi and psi are not equivalent")
