# PRIMITIVE OPERATIONS
# cons(a, b)    O(1)
# car(lst)      O(1)
# cdr(lst)      O(1)
# empty         O(1)
# is_empty(lst) O(1)

# MORE OPERATIONS
# is_list(lst)   O(1)
# show(lst)      O(n)
# length(lst)    O(n)
# reverse(lst)   O(n)
# list_ref(lst, pos) ;; zero indexed O(pos)
# append(lst1, lst2) O(n) where n = length(lst1)
# take(lst, n)   O(num)
# drop(lst, n)   O(n)

# ABSTRACT LIST FUNCTIONS
# build_list(n, proc) O(n)
# map(proc, lst)      O(n)
# filter(pred, lst)   O(n)
# foldl(proc, init, lst)  O(n)
# foldr(proc, init, lst)  O(n)
# sort(lst, to_strict) O(nlog(n))

class Pair:
	def __init__(self, a, b):
		self.a = a
		self.b = b

# PRIMITIVE OPERATIONS
def cons(a, b):
	return Pair(a, b)

def car(lst):
	return lst.a

def cdr(lst):
	return lst.b

empty = None

def is_empty(lst):
	return lst is empty

def is_list(lst):
	return isinstance(lst, Pair) or lst is empty

# MORE FUNCTIONS
def show(lst):
	if lst is None:
		print("empty")
		return
	def helper(lst, result):
		if is_empty(lst):
			print("'(" + result[1:] + ")")
			return
		else:
			helper(cdr(lst), result + " " + str(car(lst)))
	helper(lst, "")

def length(lst):
	def helper(lst, acc):
		if is_empty(lst):
			return acc
		else:
			return helper(cdr(lst), acc + 1)
	return helper(lst, 0)

def reverse(lst):
	def helper(old, new):
		if is_empty(old):
			return new
		else:
			return helper(cdr(old), cons(car(old), new))
	return helper(lst, empty)

def list_ref(lst, pos):
	if pos == 0:
		return car(lst)
	else:
		return list_ref(cdr(lst), pos - 1)

def append(lst1, lst2):
	def helper(l1, l2):
		if is_empty(l1):
			return l2
		else:
			return helper(cdr(l1), cons(car(l1), l2))
	return helper(reverse(lst1), lst2)

def take(lst, n):
	def helper(lst, n, acc):
		if n == 0:
			return acc
		else:
			return helper(cdr(lst), n - 1, cons(car(lst), acc))
	
	return reverse(helper(lst, n, empty))

def drop(lst, n):
	if n == 0:
		return lst
	else:
		return drop(cdr(lst), n - 1)

# ABSTRACT LIST FUNCTIONS
def build_list(n, proc):
	if n < 0:
		return None
	def helper(n, proc, acc):
		if n == 0:
			return cons(proc(n), acc)
		else:
			return helper(n - 1, proc, cons(proc(n), acc))
	return helper(n - 1, proc, empty)

def map(proc, lst):
	def helper(proc, lst, acc):
		if is_empty(lst):
			return acc
		else:
			return helper(proc, cdr(lst), cons(proc(car(lst)), acc))
	
	return reverse(helper(proc, lst, empty))

def filter(pred, lst):
	def helper(pred, lst, acc):
		if is_empty(lst):
			return acc
		else:
			if pred(car(lst)):
				return helper(pred, cdr(lst), cons(car(lst), acc))
			else:
				return helper(pred, cdr(lst), acc)
	return reverse(helper(pred, lst, empty))

def foldl(proc, init, lst):
	if is_empty(lst):
		return init
	else:
		return foldl(proc, proc(car(lst), init), cdr(lst))

def foldr(proc, init, lst):
	return foldl(proc, init, reverse(lst))


def sort(lst, to_strict):
	def split_list(lst):
		if is_empty(lst):
			return empty
		else:
			return cons(cons(car(lst), empty), split_list(cdr(lst)))
	
	def merge(lst1, lst2):
		def helper(l1, l2, acc):
			if is_empty(l1):
				return append(reverse(l2), acc)
			elif is_empty(l2):
				return append(reverse(l1), acc)
			elif to_strict(car(l1), car(l2)):
				return helper(cdr(l1), l2, cons(car(l1), acc))
			else:
				return helper(l1, cdr(l2), cons(car(l2), acc))
		return reverse(helper(lst1, lst2, empty))
	
	def merge_adjacent(lst):
		if is_empty(lst):
			return empty
		elif is_empty(cdr(lst)):
			return lst
		else:
			return cons(merge(car(lst), car(cdr(lst))), merge_adjacent(cdr(cdr(lst))))
	
	def helper(lst):
		if is_empty(cdr(lst)):
			return car(lst)
		else:
			return helper(merge_adjacent(lst))
	
	if is_empty(lst):
		return empty
	else:
		return helper(split_list(lst))

a = cons(10, cons(100, cons(1000, empty)))

b = build_list(10, lambda x : x * x)

c = map(lambda x : x ** 0.5, b)

d = filter(lambda x : x % 2 == 0, c)

e = foldl(lambda x, y: x + y, 0, build_list(10, lambda x : x + 1))

f = foldl(cons, empty, build_list(10, lambda x : x + 1))
g = foldr(cons, empty, build_list(10, lambda x : x + 1))

h = append(f, g)

from random import randint

i = build_list(5, lambda x : randint(0, 20))

j = sort(i, lambda x, y : x < y)
