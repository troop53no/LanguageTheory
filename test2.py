from Project2 import *

print("test test test test")

e = AndExpr(AndExpr(BoolExpr(True), BoolExpr(False)),BoolExpr(True))

print(e)
e = step(e)
print(e)
e = step(e)
print(e)
e = step(e)
print(e)
e = step(e)
print(e)
e = step(e)
print(e)