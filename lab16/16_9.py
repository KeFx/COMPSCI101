def merge_frequency_dictionaries(dic1, dic2):
    merged_freq_dict = {}
    for letter, freq in dic1.items():
        merged_freq_dict[letter] = freq
    
    for letter, freq in dic2.items():
        if letter not in merged_freq_dict:
            merged_freq_dict[letter] = freq
        else:
            merged_freq_dict[letter] += freq

    return merged_freq_dict

letter_freq_dict1 = {"a": 1, "b": 2, "c": 3}
# letter_freq_dict1 = {}
letter_freq_dict2 = {"d": 5, "b": 6, "e": 19}
merged_freq_dict = merge_frequency_dictionaries(letter_freq_dict1, letter_freq_dict2)
for key in sorted(merged_freq_dict):
    print(f"{key}: {merged_freq_dict[key]}")
print(type(merged_freq_dict))