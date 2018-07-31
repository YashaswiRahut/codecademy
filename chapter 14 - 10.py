def censor(text, word):
    a = text.split()
    s = '*' * len(word)
    count = 0
    for j in a:
        if j == word:
            a[count] = s
        count += 1
    result =' '.join(a)

    return result
  
