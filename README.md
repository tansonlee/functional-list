# Functional List

### An implementation of a functional list structure in Python using Functional Programming

## Table of Conents
1. [Introduction](#introduction)
2. [List of Functions](#list-of-functions)
	- [Primitive Operations](#primitive-operations)
	- [More Operatioins](#more-operations)
	- [Abstract List Functions](#abstract-list-functions)
	- [Sort](#sort)
3. [Examples](#Examples)
	- [Primitive Operations](#primitive-operations)
	- [More Operatioins](#more-operations)
	- [Abstract List Functions](#abstract-list-functions)
	- [Sort](#sort) 

## Introduction

An implementation of a list as it is implemented in functional programming languages such as Haskell, Lisp, Scheme and Racket.
A list can be recursively defined as either
1. empty
2. cons(element, lst) where element can be anything and lst is a list

## List of Functions

*Note: in the time complexities, n = length(lst)*

#### Primitive Operations

|Function           |Input                           |Output                                |Time Complexity |
|-------------------|--------------------------------|--------------------------------------|----------------|
|`cons(elem, lst)`  |elem is anything; lst is a list |a list with elem at the head          |O(1)            |
|`car(lst)`         |lst is a list                   |the element at the head of lst        |O(1)            |
|`cdr(lst)`         |lst is a list                   |a list without the head of lst        |O(1)            |
|`empty`            |N/A                             |the empty list                        |O(1)            |
|`is_empty(lst)`    |lst is a list                   |true if lst is empty; false otherwise |O(1)            |


#### More Operations
|Function            |Input                                 |Output                                 |Time Complexity |
|--------------------|--------------------------------------|---------------------------------------|----------------|
|`is_list(lst)`      |lst is anything                       |true if lst is a list; false otherwise |O(1)            |
|`show(lst)`         |lst is a list                         |prints the list                        |O(n)            |
|`length(lst)`       |lst is a list                         |length of lst                          |O(n)            |
|`reverse(lst)`      |lst is a list                         |lst in reverse order                   |O(n)            |
|`list_ref(lst, i)`  |lst is a list; i is a number          |the i-th element of lst                |O(i)            |
|`append(lst1, lst2)`|lst1 and lst2 are lists               |lst1 and lst2 joined keeping order     |O(length(lst1)) |
|`take(lst, num)`    |lst is a list num is a number         |the first num elements of lst          |O(num)          |
|`drop(lst, num)`    |lst is a list num is a number         |lst without the first num elements     |O(num)          |

#### Abstract List Functions

`build_list(n, proc)`
- takes a non-negative integer, n, and a procedure, proc
- returns a list of n elements where each element is proc(i) and i = 0, 1, ..., n
- O(n) * O(proc) where O(proc) is the time complexity of proc

`map(proc, lst)`
- takes a procedure, proc, and a list, lst
- returns a list where proc is applied to each element of lst
- O(length(lst)) * O(proc) where O(proc) is the time complexity of proc

`filter(pred, lst)`
- takes a predicate, pred, and a list, lst
- returns a list of the elements of lst for which pred is true
- O(length(lst)) * O(pred) where O(pred) is the time complexity of pred

`foldl(proc, init, lst)`
- takes a procedure, proc; initial value, init; and a list, lst
- returns the elements of lst combined by proc starting with init from left to right in the list
- O(length(lst)) * O(proc) where O(proc) is the time complexity of proc

`foldr(proc, init, lst)`
- takes a procedure, proc; initial value, init; and a list, lst
- returns the elements of lst combined by proc starting with init from right to left in the list
- O(length(lst)) * O(proc) where O(proc) is the time complexity of proc

#### Sort

`sort(lst, to_strict)`
- takes a list, lst, and a strict total order, to_strict
- returns a list with the elements of lst sorted in non-decresing order according to to_strict
- O(nlog(n)) * O(to_strict) where O(to_strict) is the time complexity of to_strict

## Examples

#### Primitive Operations

```python
from list import *

a = cons(10, cons(100, cons(1000, empty)))

show(a) 
# prints '(10 100 1000)

print(is_empty(a))
# prints False

print(car(a))
# prints 10

show(cdr(a))
# prints '(100 1000)
```

#### More Operations

```python
from list import *

a = cons(10, cons(100, cons(1000, empty)))
b = cons(20, cons(200, cons(2000, empty)))
c = append(a, b)

show(c)
# prints '(10 100 1000 20 200 2000)

show(reverse(c))
# prints '(2000 200 20 1000 100 10)

print(list_ref(c, 2))
# prints 1000

show(take(c, 4))
# prints '(10 100 1000 20)

show(drop(c, 2))
# prints '(1000 20 200 2000)
```

#### Abstract List Functions

```python
from list import *

a = build_list(10, lambda x : x + 1)

show(a)
# prints '(1 2 3 4 5 6 7 8 9 10)

b = map(lambda x : x + 10, a)

show(b)
# prints '(11 12 13 14 15 16 17 18 19 20)

from math import sqrt
def is_prime(n):
	if n <= 1: return False
	if n == 2: return True
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

c = filter(is_prime, b)
show(c)
# prints '(11 13 17 19)

d = foldl(lambda x, y : x + y, 0, c)
print(d)
# prints 60  ## because 60 = 0 + 11 + 13 + 17 + 19
```

#### Sort

```python
from list import *
from random import randint

a = build_list(10, lambda x : randint(1, 10))

show(a)
# prints a list of 10 random numbers from [1, 10]
# for example, '(6 9 2 4 2 1 10 1 1 6)

b = sort(a, lambda x, y : x < y)

show(b)
# prints the list a in non-decreasing order
# for example, '(1 1 1 2 2 4 6 6 9 10)
```