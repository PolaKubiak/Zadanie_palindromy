#Define a function 

def isPalindrome(string): 

    if (string == string[::-1]): 

        return "True. The string is a palindrome." 

    else: 

        return "False. The string is not a palindrome." 

#Enter input string 

string=input("Enter string:")

print(isPalindrome(string))
