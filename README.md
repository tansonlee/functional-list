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

#### Primitive Operations

*Note: in the time complexities, n = length(lst)*

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
|`list_ref(lst, i)`  |lst is a list; i is a natural number  |the i-th element of lst (zero indexed) |O(i)            |
|`append(lst1, lst2)`|lst1 and lst2 are lists               |lst1 and lst2 joined maintaining order |O(length(lst1)) |
|`take(lst, num)`    |lst is a list num is a natural number |the first num elements of lst          |O(num)          |
|`drop(lst, num)`    |lst is a list num is a natural number |lst without the first num elements     |O(num)          |

