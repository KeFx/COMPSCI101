def get_bands_per_genre(band_list):
    genre_dict = {}
    for band, genre in band_list:
        if genre not in genre_dict:
            genre_dict[genre] = [band]
        else:
            genre_dict[genre].append(band)
        
    for genre in genre_dict:
        genre_dict[genre].sort()
    return genre_dict