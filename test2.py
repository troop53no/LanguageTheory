from Project2 import *

print("test test test test")

e = NotExpr(
	AndExpr(
		BoolExpr(True),
		NotExpr(BoolExpr(False))))

print(e)
e = step(e)
print(e)
e = step(e)
print(e)
e = step(e)
print(e)


print("done")
print(isinstance(BoolExpr(True),BoolExpr))