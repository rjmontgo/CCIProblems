def urlify(str):
    urlString = []
    for char in str:
        if char == ' ':
            urlString.append('%20')
        else:
            urlString.append(char)

    return ''.join(urlString)
