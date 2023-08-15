from z3 import *


def max(list):
    out = list[0]
    for i in list:
        out = If(i>out, i, out)
    return out

def min(list):
    out = list[0]
    for i in list:
        out = If(i < out, i, out)
    return out


john, aries, joseph = Ints('john aries joseph')
bros = [joseph, aries, john]


s= Solver()
s.add(Distinct(bros))
s.add([And(i >= 0, i <= 2) for i in bros])
s.add(aries == max(bros))
s.add(john != min(bros))
if s.check() == sat:
    print(s.model())
    