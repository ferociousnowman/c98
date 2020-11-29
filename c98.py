def countwordsfromfile():
    filename=input("enter the file name")
    numberofwords=0
    file=open(filename,"r")
    for line in file:
        words =line.split("'")
        numberofwords=numberofwords+len(words)
        print(numberofwords)
    print("number of words")
    print(numberofwords)

countwordsfromfile()

def greet(name):
    print(" hello "+name+" how are you " ) 

name=input("enter your name")
greet(name)