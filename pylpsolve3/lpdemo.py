# Script to demonstrate use of the lp_solve toolkit

from lpsolve55 import *

lp=lpsolve(b'make_lp',0,4)
lpsolve(b'add_constraint',lp,[3, 2, 2, 1],3,4)
lpsolve(b'add_constraint',lp,[0, 4, 3, 1],2,3)
lpsolve(b'set_obj_fn',lp,[2, 3, -2, 3])
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)

# Change a single element, and maximize

lpsolve(b'set_mat',lp,2,1,0.5)
lpsolve(b'set_maxim',lp)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)

# Change RHS

lpsolve(b'set_rh',lp,1,7.45)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)

# Set var 4 to an integer

lpsolve(b'set_int',lp,4,1)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)

# Put in lower and upper bounds

lpsolve(b'set_lowbo',lp,2,2)
lpsolve(b'set_upbo',lp,4,5.3)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)

# Delete a constraint

lpsolve(b'del_constraint',lp,1)
lpsolve(b'add_constraint',lp,[1, 2, 1, 4],3,8)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)
lpsolve(b'delete_lp',lp)

#%%%%%%%%%%%%

# More examples

# ex1.lp from the lp_solve distribution

lp=lpsolve(b'make_lp',2,2)
lpsolve(b'set_mat',lp,[[2, 1],[-4, 4]])
lpsolve(b'set_obj_fn',lp,[-1, 2])
lpsolve(b'set_int',lp,[1,1])
lpsolve(b'set_rh_vec',lp,[5, 5])
lpsolve(b'set_maxim',lp)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)
lpsolve(b'delete_lp',lp)

# Example 2

f = [50, 100]
A = [[10, 5],[4, 10], [1, 1.5]]
b = [2500, 2000, 450]
e = [-1, -1, -1]

m = len(A)
n = len(A[0])
lp=lpsolve(b'make_lp',m,n)
lpsolve(b'set_obj_fn',lp,f)
lpsolve(b'set_mat',lp,A)
lpsolve(b'set_rh_vec',lp,b)
lpsolve(b'set_maxim',lp)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)
lpsolve(b'delete_lp',lp)

# Example 3

f = [-40, -36]
vub = [8, 10]
A = [[5, 3]]
b = [45]
e = 1

m = len(A)
n = len(A[0])
lp=lpsolve(b'make_lp',m,n)
lpsolve(b'set_obj_fn',lp,f)
lpsolve(b'set_mat',lp,A)
lpsolve(b'set_rh_vec',lp,b)
lpsolve(b'set_constr_type',lp,1,2)
lpsolve(b'set_upbo',lp,1,8)
lpsolve(b'set_upbo',lp,2,10)
lpsolve(b'set_maxim',lp)
result=lpsolve(b'solve',lp)
obj=lpsolve(b'get_objective', lp)
print(obj)
x=lpsolve(b'get_variables', lp)[0]
print(x)
lpsolve(b'delete_lp',lp)
