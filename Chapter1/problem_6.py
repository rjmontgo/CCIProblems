def compress(str1):
    if len(str1) <= 2:
        return str1

    compress = []
    compress.append(str1[0])
    count = 1
    for i in range(len(str1)):
        if i == 0:
            continue
        if str1[i] == str1[i - 1]:
            count += 1
        else:
            compress.append(str(count) + str1[i])
            count = 1
    compress.append(str(count))
    compress = ''.join(compress)
    if len(str1) <= len(compress):
        return str1

    return compress
