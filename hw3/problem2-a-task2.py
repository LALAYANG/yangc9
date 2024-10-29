from z3 import *

l1, u1, l2, u2 = Reals('l1 u1 l2 u2')
z, w = Reals('z w') 

s = Solver()
s.add(ForAll([z], Implies(And(l1 < z, z < u1, l2 < z, z < u2),
                           Exists([w], And(l1 < w, w < u1, l2 < w, w < u2, w != z)))))

print("Before QE:", s)

g = Goal()
g.add(s.assertions())
qe = Tactic('qe')
qe_result = qe(g)
print("After QE:", qe_result)
