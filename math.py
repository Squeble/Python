from math import *
# Ceil - Take an input, return the smallest iteger greater than or equal to the input
x_ceil = ceil(5.0)
print("xceil: " + str(x_ceil))
# Floor - Take an input, return the largest integer less than or equal to the input
floor_y = floor(3.9)
print("floor_y: " + str(floor_y))

# Comb(n, k) - Return the number of ways to choose k items from n items without repitition
#              and without order.

num_people = 10 # n
num_seats = 6 # k
xcomb = comb(num_people, num_seats)

print("xcomb: " + str(xcomb))
# perm(n, k) - Returns the number of ways to choose k item from n items without repitition
#              and WITH order
num_people = 10
num_seats = 6
xperm = perm(num_people, num_seats)
print("xperm: " + str(xperm))

# Copysign(x, y) - Return a float with maginitude x, but the sign of y
speed = 10 #meters/second
distance_moved = -3 #meters
velocity = copysign(speed, distance_moved)

print("velocity: " + str(velocity))
" " + str()

# Fabs(x) - Returns the absoulte value of x
x_fabs = fabs(-8.3) #To jest to samo
x_abs = abs (-7.6) #To jest to samo tylko prosto z pythona

print("fabs: " + str(x_fabs))
print("abs: " + str(x_abs))

# Factorial(x) - Returns the factorial of x as an integer
x_facto = factorial(6) #1*2*3*4*5

print("xfactorial: " + str(x_facto))

# Fmod(x,y) - Returns the modulus (remainder of x / y) as a float
x_fmod = fmod(100, 9)

print("fmod: " + str(x_fmod))

# Frexp(x) - Returns the matissa (as a float) and exponent (as an integer) of x.
# scientific notation = matissa * 10^exponent
# x = matissa * 2^exponent

x_frexp = frexp(16)
y_frexp = x_frexp[0]*(2**x_frexp[1])
print("x_frexp: " + str(x_frexp))
print("y_frexp: " + str(y_frexp))
# Ldexp(x, i) - Essentially the reverse of frexp()
z_ldexp = ldexp(x_frexp[0], x_frexp[1])
print("Ldexp: " + str(z_ldexp))

# Fsum(iterable) - Returns an accurate floating point sum of values in the iterable
iterable = [.2, .2, .2, .2, .2, .2, .2, .2, .2, .2,]
x_sum = sum(iterable) # Funkcja wbudowana w pythona
y_fsum = fsum(iterable) # Jest bardziej dokładna niż pythonowa opcja

print("sum: " + str(x_sum))
print("fsum: " + str(y_fsum))

# gcd(*integers) - Returns the greatest common divisior of the specified integer arguments
x_gcd = gcd(36, 66)
print("gcd: " + str(x_gcd))

# New in python 3.9:
# gcd(36, 66, 24) = 666666
#lcm(*integers) - Returns the least common multiple of the specified integer arguments
# lcm(2, 3, 4, 6,) = 12
#_____________________________________



# isclose(a, b, rel_tol, abs_tol) - Returns True if a and b are close to each other and
#                                   return the False if otherwise

# rel_tol - (deafult: 1e-9). Is multiplied by the largest input value (a or b) and the 
#           smaller input value must be withing that range to be considered 'close'
a_isc = 3
b_isc = 4
#a must be between 2 and 4
x_isc = isclose(a_isc, b_isc, rel_tol = 0.5)
print("isclose x: " + str(x_isc))
# a must be between 3.2 and 4
y_isc = isclose(a_isc, b_isc, rel_tol = 0.20)
print("isclose y: " + str(y_isc))

# isinf(x) - Returns true if x is equal to infinity. False otherwise.
num = inf
x_isinf = isinf(num)
print("isinf: " + str(x_isinf))
# isnan(x) - Returns true if x is a NaN (Not a Number). False otherwise.
num = nan
x_isnan = isnan(num)
print("isnan: " + str(x_isnan))

# isfinite(x) - Returns true to neither infinity or NaN. False otherwise.
num = 9
x_isfinite = isfinite(num)
print("isfinite: " + str(x_isfinite))

# isqrt(x) - Takes the square root of x and rounds it down to the nearest integer.
x_isqrt = isqrt(8)
print("isqrt: " + str(x_isqrt))

x_isqrt2 = isqrt(9)
print("isqrt: " + str(x_isqrt2))

# modf(x) - Returns the fractional and integer parts of x

x_modf = modf(8.22)
print("modf: " + str(x_modf))

# prod(iterable, start=1) - Calculate the product of all the elements in the iterable.
iterable = [10, 2, 5]
# 1*10*2*5
x_prod = prod(iterable)
print("prod: " + str(x_prod))

# 2*10*2*5

x_prod2 = prod(iterable, start=2)
print("prod: " + str(x_prod2))