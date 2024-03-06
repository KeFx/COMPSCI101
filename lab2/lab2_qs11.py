import math
per_drink_volume_ml = 200
drinks_per_container = 65

while True:
    number_of_people = int(input("Enter the number of people: "))
    drinks_wasted = (drinks_per_container - number_of_people) % drinks_per_container
    volume_wasted_ml = drinks_wasted * per_drink_volume_ml

    print(drinks_wasted, "drinks ({}ml) are wasted.".format(volume_wasted_ml))