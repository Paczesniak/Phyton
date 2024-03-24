import math

def f(x):
    return 3 * x - math.cos(x) - 1

def falsi(a, b, epsilon):
    iteracje = 0
    while True:
        iteracje += 1
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < epsilon:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iteracje

a = 0.25
b = 0.75
epsilon = 0.00001

wynik, iteracje = falsi(a, b, epsilon)

print(f"Rzeczywisty pierwiastek równania 3x - cos(x) - 1 = 0 w przedziale [0.25, 0.75] to około {wynik:.5f}.")
print(f"Liczba iteracji: {iteracje}")
