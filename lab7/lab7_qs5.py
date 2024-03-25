movies = []

while True:
    u_input = input("Please enter the movie name or end to print the list: ")
    if u_input == "end" :
        break
    elif u_input not in movies :
        movies.append(u_input)

movies.sort()
print()
print("Movies List:")
print("==============")

for indx, movie in enumerate(movies):
    print(f"{indx+1}) {movie}")
