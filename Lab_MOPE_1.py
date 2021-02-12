import random

a0 = 2
a1 = 3
a2 = 1
a3 = 4

n = 8

def generation_of_x(start=0, end=20):
    return [random.randint(start, end) for _ in range(n)]

def y(x_1, x_2, x_3):
    return a0 + a1 * x_1 + a2 * x_2 + a3 * x_3

def count_x0i(x_results):
    return (max(x_results) + min(x_results)) / 2


def count_dxi(x0i, x_results):
    return x0i - min(x_results)


def count_xni(x0i, dxi, xi):
    return [(i - x0i) / dxi for i in xi]


def get_optimal_value_of_y(y):
    return min(y)


x1, x2, x3 = [generation_of_x() for i in range(3)]
Y = [y(x1[i], x2[i], x3[i]) for i in range(8)]

x01 = count_x0i(x1)
x02 = count_x0i(x2)
x03 = count_x0i(x3)

dX1 = count_dxi(x01, x1)
dX2 = count_dxi(x02, x2)
dX3 = count_dxi(x03, x3)

x1n = count_xni(x01, dX1, x1)
x2n = count_xni(x02, dX2, x2)
x3n = count_xni(x03, dX3, x3)

y_etalon = y(x01, x02, x03)

opt_y = get_optimal_value_of_y(Y)

print("Number of experiments", n)
print(f"Function: y = {a0} + {a1}x1 + {a2}x2 + {a3}x3")
print("X1:", x1)
print("X2:", x2)
print("X3:", x3)
print("Y =", Y)
print("x0: %s %s %s"%(x01, x02, x03))
print("dx: %s %s %s"%(dX1, dX2, dX3))
print("X1n: ", x1n)
print("X2n: ", x2n)
print("X3n: ", x3n)
print("Yет =", y_etalon)
print("Optimal value of y(min): ", opt_y)