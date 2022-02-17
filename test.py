def first_word(str1,arr):
    ch=' '
    for x in str1.split(" "):
        if x not in arr:
            ch = x.capitalize()
        else:
            ch=' ';
    return ch;
print(first_word("this is crazy and fun",["fun" ,"is"]))