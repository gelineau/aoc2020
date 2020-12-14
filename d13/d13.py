# https://docs.sympy.org/latest/modules/solvers/diophantine.html

# https://fr.planetcalc.com/3303/
import math

from sympy.solvers.diophantine.diophantine import diop_solve
from sympy import symbols
x1, x2, t_0 = symbols('x1 x2 t_0')


input = "7,13,x,x,59,x,31,19"

data = list((-i, int(char)) for i, char in enumerate(input.split(",")) if char != 'x')

print(data)


# a x1 + b = c x2 + d
# 7 * x1 = 13 * x2 + 1
b, a = data[0]
d, c = data[1]

solved = diop_solve(a*x1 + b - d - c*x2)
print(solved)
# (13*t_0 + 2, 7*t_0 + 1)

reintegrated = a*solved[0] + b
print(reintegrated)
# 91*t_0 + 14


a = reintegrated.args[1].args[0]
b = reintegrated.args[0]
d, c = data[2]
solved = diop_solve(a*x1 + b - d - c*x2)
print(solved)
reintegrated = a*solved[0] + b
print(reintegrated)

a = reintegrated.args[1].args[0]
b = reintegrated.args[0]
d, c = data[3]
solved = diop_solve(a*x1 + b - d - c*x2)
print(solved)
reintegrated = a*solved[0] + b
print(reintegrated)

a = reintegrated.args[1].args[0]
b = reintegrated.args[0]
d, c = data[4]
solved = diop_solve(a*x1 + b - d - c*x2)
print(solved)
reintegrated = a*solved[0] + b
print(reintegrated)

a = reintegrated.args[1].args[0]
b = reintegrated.args[0]

print(a, b)

value = int(b/a)

x = -a*value + b

print(x)
print(x % 7)
print(x % 13)
print(x % 59)
print(x % 31)
print(x % 19)




input = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,653,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'

data = list((-i, int(char)) for i, char in enumerate(input.split(",")) if char != 'x')

print(data)


b, a = data[0]
d, c = data[1]

solved = diop_solve(a*x1 + b - d - c*x2)
print(solved)

reintegrated = a*solved[0] + b
print(reintegrated)



for d,c in data[2:]:
    a = reintegrated.args[1].args[0]
    b = reintegrated.args[0]
    solved = diop_solve(a * x1 + b - d - c * x2)
    print(solved)
    reintegrated = a * solved[0] + b
    print(reintegrated)

a = reintegrated.args[1].args[0]
b = reintegrated.args[0]

value = math.floor(b/a)

x = -a*value + b

print(x)




