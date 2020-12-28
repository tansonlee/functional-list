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

|Function           |Input                           |Output                                |Time complexity |
|-------------------|--------------------------------|--------------------------------------|----------------|
|`cons(elem, lst)`  |elem is anything; lst is a list |a list with elem at the head          |O(1)            |
|`car(lst)`         |lst is a list                   |the element at the head of lst        |O(1)            |
|`cdr(lst)`         |lst is a list                   |a list without the head of lst        |O(1)            |
|`empty`            |N/A                             |the empty list                        |O(1)            |
|`is_empty(lst)`    |lst is a list                   |true if lst is empty; false otherwise |O(1)            |


#### More Operations
|Function
|
|
|
|
|
|