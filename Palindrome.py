def palindrome(word: str):
    syntaxword = word.lower()
    if syntaxword == syntaxword[::-1]:
        return True
    else:
        return False

word = input("Please enter what you want to check:\n")

print(palindrome(word))
