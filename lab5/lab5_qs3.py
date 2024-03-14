number = int(input("Enter a number: "))

prime = number >= 2
divisor = 2
counter = 0

while divisor < number and prime:
    prime = number % divisor != 0
    divisor += 1
    counter += 1
        
if prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
    print(f"{number} is divisible by {divisor - 1}")

print(counter)