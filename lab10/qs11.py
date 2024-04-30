def filter_positive_list(raw_data):
    for i in range(len(raw_data) - 1, -1, -1):
        if raw_data[i] <= 0:
            raw_data.remove(raw_data[i])