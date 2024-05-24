def build_english_to_maori(translations_list):
    translation_dict = {}
    for e in translations_list:
        colon_idx = e.index(':')
        key = e[0:colon_idx]
        value = e[colon_idx+1::]

        translation_dict[key] = value
    
    return translation_dict