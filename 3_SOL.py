from z3 import *
# don't work

c_dog, c_cat, c_mice = RealVal("15"), RealVal("1"), RealVal("0.25")
n_dog, n_cat, n_mice = Reals('n_dog n_cat n_mice')

s = Solver()
s.add(n_dog + n_cat + n_mice == 100)
s.add(n_dog > 0, n_cat > 0, n_mice > 0)
s.add((n_dog*15) + (n_cat *1) + (n_mice *.25) == 100)


if s.check == sat:
    print(s.model())
else:
    print(s)
