#line1
class expr:
	pass


class BoolExpr(expr):
	def __init__(self,val):
		self.value = val
	def __str__(self):
		return str(self.value)


class NotExpr(expr):
	def __init__(self,e):
		self.expr = e
	def __str__(self):
		return " not " + str(self.expr);


class AndExpr(expr):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
	def __str__(self):
		return str(self.lhs) + " and " + str(self.rhs);


class OrExpr(expr):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs
	def __str__(self):
		return str(self.lhs) + " or " + str(self.rhs);


def same_str(e1,e2):
	return str(e1) == str(e2);


def same (e1, e2):
	if type(e1) is not type(e2):
		return false
	if type(e1) is BoolExpr:
		return e1.val == e2.val
	if type(e1) is NotExpr:
		return same(e1.expr, e2.expr)
	if type(e1) is AndExpr:
		return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs);
	if type(e1) is OrExpr:
		return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs);


def is_value(e):
	return type(e) is BoolExpr


def is_reducible(e):
	return not is_value(e)


def step(e):
	if is_value(e):
		return BoolExpr(e.value)
	

	if type(e) is NotExpr:
		return step_not(e)

	if type(e) is AndExpr:
		return step_and(e)

	if type(e) is OrExpr:
		return step_or(e)

	
def step_not(e):
	if is_value(e):
		return BoolExpr(not e.value);
	

def step_and(e):

	if is_value(e.lhs) and isvalue(e.rhs):
		return BoolExpr(e.lhs.value and e.rhs.value)
	if is_reducible(e.lhs):
		return AndExpr(step(e.lhs), e.rhs) ;
	if is_reducible(e.rhs):
		return AndExpr(e.lhs, step(e.rhs));


def step_or(e):
	if (is_value(e.lhs) and isvalue(e.rhs)):
		return BoolExpr(e.lhs.value or e.rhs.value)
	if is_reducible(e.lhs):
		return OrExpr(step(e.lhs), e.rhs);
	if is_reducible(e.rhs):
		return OrExpr(e.lhs, step(e.rhs));


def reduce(e):
	while is_reducible(e):
		e = step(e)
	return e