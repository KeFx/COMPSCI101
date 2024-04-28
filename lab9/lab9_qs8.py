x = float(input('Enter x: '))
n = int(input('Enter the number of terms in the series: '))
s = 0

for i in range(n+1):
    s += x**i

f = 1/(1-x)

print(f"1 / (1 - {x}) = {round(f, 6)}")

print(f'The series with {n} terms differs by {round(f-s, 6)}')