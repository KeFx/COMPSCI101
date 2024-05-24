def count_bands_per_genre(band_list):
    genre_dict = {}
    for band, genre in band_list:
        if genre not in genre_dict:
            genre_dict[genre] = 1
        else:
            genre_dict[genre] += 1

    return genre_dict