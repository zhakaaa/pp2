class MyClass() :
    def __init__(self,word) :
        self.word = word
        
    def printString(self) :
        print(self.word.upper())
    
word = input("Enter: ")

p1 = MyClass(word)
p1.printString()