import string

def processBook(filename):
    hashmap = {}
    file = open(filename, "r")
    for line in file:
        breakWords = line.split()
        for word in breakWords:
            cleanup = word.replace("'s", "")
            cleanup = cleanup.translate(cleanup.maketrans("", "",\
                                        string.punctuation))
            cleanup = cleanup.lower()
            hashmap[cleanup] = hashmap.get(cleanup, 0) + 1
    file.close()
    return hashmap

def numOccurences(hashmap, word):
    return hashmap.get(word, 0)
