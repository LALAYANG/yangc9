from z3 import *

p, q, r = Bools('p q r')

phi = And(
    Or(q, Not(r)), 
    Or(Not(p), r), 
    Or(Not(q), r, p), 
    Or(p, q, Not(q)), 
    Or(Not(r), q))


psi = q 

def save_encoding_to_file(expr, filename):
    with open(filename, 'w') as file:
        file.write(expr.sexpr())

save_encoding_to_file(phi, 'phi_encoding.smt2')
save_encoding_to_file(psi, 'psi_encoding.smt2')

print("Formulas have been encoded and saved.")
