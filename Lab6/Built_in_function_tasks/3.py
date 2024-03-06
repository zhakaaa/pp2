string = input()

reverse_string = ''.join(reversed(string))  # separator.join(iterable) - joint iterable objects to string

if string == reverse_string :
    print("Palindrome")
else :
    print("Not Palindrome")
