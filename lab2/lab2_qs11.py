import math
per_drink_volume_ml = 200
per_container_drinks = 65
per_container_volume_ml = per_drink_volume_ml * per_container_drinks


number_of_people = int(input("Enter the number of people: "))
total_volume_required = number_of_people * per_drink_volume_ml
total_containers_required = math.ceil(total_volume_required / per_container_volume_ml)

volume_wasted_ml = (total_containers_required * per_container_volume_ml) - total_volume_required
drinks_wasted = round(volume_wasted_ml/per_drink_volume_ml)

print(drinks_wasted, "drinks ({}ml) are wasted.".format(volume_wasted_ml))