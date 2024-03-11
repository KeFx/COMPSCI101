months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

look_up_table = {
    119 : "Capricorn",
    218 : "Aquarius",
    320 : "Pisces",
    419 : "Aries",
    520 : "Taurus",
    620 : "Gemini",
    722 : "Cancer",
    822 : "Leo",
    922 : "Virgo",
    1022 : "Libra",
    1121 : "Scorpio",
    1221 : "Sagittarius",
    1231 : "Capricorn"
}

day = int(input("Enter the day: "))
month =  months.index(input("Enter the month: ")) + 1

converted_day = month * 100 + day

for date in look_up_table:
    if (converted_day <= date):
        print(f"{day} {months[month-1]} is {look_up_table[date]}.")
        break