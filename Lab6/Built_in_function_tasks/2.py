string = input()

countUpper = 0
countLower = 0

for i in string :
    if i.isupper() :
        countUpper=+1
    elif i.islower() :
        countLower+=1

print(f"Number of uppercase characters is : {countUpper}")
print(f"Number of lowercase characters is : {countLower}")