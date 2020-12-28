# Functional List

### An implementation of a functional list structure in Python using Functional Programming

## Table of Conents
1. [Introduction](#introduction)
2. [List of Functions](#list-of-functions)

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

`sort(lst, to_strict)` O(nlog(n))
- takes a list, lst, and a strict total order, to_strict
- returns a list with the elements of lst sorted in non-decresing order according to to_strict
- O(nlog(n)) * O(to_strict) where O(to_strict) is the time complexity of to_struct