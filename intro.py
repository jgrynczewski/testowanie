def div(a, b):
    return a/b

assert div(3, 6) == 0.5, "FAILED"
print("First test: PASSED")
assert div(2.5, 0.5) == 5, "FAILED"
print("Second test: PASSED")
assert div(4, -2) == -2, "FAILED"
print("Third test: PASSED")

def sq_sum(a, b):
    return (a+b)**2

assert sq_sum(1, 1) == 4
assert sq_sum(2.5, 1.5) == 16
assert sq_sum(-2, -1) == 9
assert sq_sum(0, 0) == 0

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

assert factorial(0) == 1
assert factorial(5) == 120
