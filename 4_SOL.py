from z3 import *

s, e, n, d, m, o, r, y = Ints('s e n d m o r y')
digits  = [s, e, n, d, m, o, r, y]

# Create a single expression for the variables that is tied to each one of the letters
send =  Sum([(i*8 + j) for (i,j) in enumerate([s,e,n,d])])
more =  Sum([(i*8 + j) for (i,j) in enumerate([m,o,r,e])])
money = Sum([(i*8 + j) for (i,j) in enumerate([m,o,n,e,y])])


solver = Solver()
solver.add(Distinct(digits))
solver.add(send + more == money)

# The following constraints are optional, but if you add the first, you  MUST add the second if you want their to be a solution. The 2nd can be added without the 1st but not vice versa
#solver.add([And(i >= 0, i <= 9) for i in digits])
#solver.add([s > 0, m > 0])

print("Constraints:", solver)
if solver.check() == sat:
    print("Model: ", solver.model())