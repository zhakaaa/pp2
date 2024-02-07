# Check word to palindrome

word = input("Enter word: ")
middle = len(word) / 2

def check_to_palindrome(word) :
    a = True
    for i in range(0,int(middle)) :
        if word[i] != word[len(word) - 1 - i] :
            a = False
            break
    if a :
        print("Palindrome")
    else :
        print("Not Palindrome")
        
check_to_palindrome(word)
