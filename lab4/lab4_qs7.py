months_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
end_dates = [19,18,20,19,20,20,22,22,22,22,21,21]

zodiac_signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

#
zodiac_signs_shifted = zodiac_signs.copy()
zodiac_signs_shifted.append(zodiac_signs_shifted.pop(0))

zodiac_signs_for_each_month = list(zip(zodiac_signs, zodiac_signs_shifted))

months_zodiac_chart = dict(zip(months_names, list(zip(end_dates, zodiac_signs_for_each_month))))

day = int(input("Enter the day: "))
month =  input("Enter the month: ")

print(months_zodiac_chart)