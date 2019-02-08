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
	return isinstance(e,BoolExpr)

def is_reducible(e):
	return not is_value(e)


def step(e):
	"""compute the next state of the program"""
	assert is_reducible(e)

	if isinstance(e,NotExpr):
		"""	~~~~~~~~~~~~~~~~~~ Not-T
			not true -> false
			
			~~~~~~~~~~~~~~~~~~ Not-F
			not false > true
			
			Alternative for above:
			
			~~~~~~~~~~~~~~~~~~
			not v1 > `not [v1]`
			
				e1 > e1'
			~~~~~~~~~~~~~~~~~~ Not-E
			not e1 > not e1'
		"""
		if is_value(e.expr):
		#if type(e.expr) is BoolExpr:
			if e.expr.value == True:
				return BoolExpr(False) #not true
			else:
				return BoolExpr(True) #not false

		#else: if it's not a value, it is reducible, so we are allowed to take a step
		#ex = step(e.expr)
		#return Not(ex)

		return NotExpr(step(e.expr))

	if isinstance(e,NotExpr):
		return step_not(e)

	if isinstance(e,AndExpr):
		return step_and(e)

	if isinstance(e,OrExpr):
		return step_or(e)

	
def step_not(e):
	if is_value(e):
		return BoolExpr(not e.value);
	

def step_and(e):

	if (is_value(e.lhs) and is_value(e.rhs)):
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