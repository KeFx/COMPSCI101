zodiacs = {
    8 : "Dragon",
    9 : "Snake",
    10 : "Horse",
    11 : "Sheep",
    0 : "Monkey",
    1 : "Rooster",
    2 : "Dog",
    3 : "Pig",
    4 : "Rat",
    5 : "Ox",
    6 : "Tiger",
    7 : "Hare"
}

year = int(input("Enter a year: "))

print(f"{year} is the year of the {zodiacs[year % 12]}.")