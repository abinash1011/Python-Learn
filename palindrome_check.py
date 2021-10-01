word = input("give a word for palindromic check: ")
rvr_word = word[::-1]
if word == rvr_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
