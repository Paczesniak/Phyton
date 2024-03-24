def f(x):
    return x**3 + x**2 - 3*x - 3

def sieczne(x0, x1, epsilon):
    iteracje = 0
    while True:
        iteracje += 1
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(x2 - x1) < epsilon:
            break
        x0 = x1
        x1 = x2
    return x2, iteracje

x0 = 1
x1 = 2
epsilon = 0.0001

wynik, iteracje = sieczne(x0, x1, epsilon)

print(f"Pierwiastek równania x^3 + x^2 - 3x - 3 = 0 w przedziale [1, 2] to około {wynik:.5f}.")
print(f"Liczba iteracji: {iteracje}")
