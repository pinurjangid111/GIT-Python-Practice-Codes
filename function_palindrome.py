def is_palindrome(word):
    if word == word[::-1]:
        return "Palindrome"
    return "NoT Palindrome"
word=input("Enter a name to check : ")
print(is_palindrome(word))