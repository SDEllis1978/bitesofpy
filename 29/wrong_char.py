def get_index_different_char(chars):
    alpha_numeric = []
    not_alpha_numeric = []

    for item in enumerate(chars):
        if str(item[1]).isalnum():
            alpha_numeric.append(item)
        else:
            not_alpha_numeric.append(item)

    char_index = [i[0][0] for i in [alpha_numeric, not_alpha_numeric] if len(i) == 1]
    return char_index[0]
