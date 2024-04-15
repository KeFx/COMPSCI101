alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_frequency = [0] * len(alphabet)

msg = input('Enter a message: ').lower()

for char in msg: 
    if char.isalpha() :
        alpha_frequency[alphabet.index(char)] += 1

print(f"The frequency list is:  {alpha_frequency}")