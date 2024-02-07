# Convert fagrenheit to centigrade

fahrenheit = int(input("Enter fahrenheit : "))

def convert_to_centigrade (fahrenheit) :
    centigrade = (5/9) * (fahrenheit - 32)
    print("Centigrade equals to" , centigrade)
    
convert_to_centigrade(fahrenheit)