# Count the frequency of words appearing in a string Using Python

def freq_words():
    str1 = input("Enter String\t")
    sepwords = str1.split()
    d = {}

    for i in sepwords:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
    print(d)


freq_words()
