sum_temp = 0.0
spring_temp_count = 0

for idx, temp in enumerate(temperature_list):
    if temp >= 26:
        spring_temp_count = idx
        break
    sum_temp += temp

if spring_temp_count == 0:
    print(f"Average spring temperature: {sum_temp}")
else:
    print(f"Average spring temperature: {round(sum_temp/spring_temp_count, 2)}")