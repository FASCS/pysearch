def search_word(a, keyword):
    searchresult = []
    for line in a:
        if (keyword in line):
            searchresult.append(line)
    return searchresult

def search_words(a, keywords):
    searchresult = []
    for line in a:
        if all(keyword in line for keyword in keywords):
            searchresult.append(line)
    return searchresult