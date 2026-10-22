def palindrome(string):
    string==string[::-1]
    return True
str1=input()
if palindrome(str1):
    print("Palindrome")
else:
    print("Not a Palindrome")