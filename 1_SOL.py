from z3 import *

x, y = Ints('x y')
solve(x + 2* y == 7, x > 2, y < 10)