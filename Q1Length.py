# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
while True:  
    a = str(input("type EXIT to break the escape the matrix "))
    print(len(a))
    if a == "EXIT":
        print("done")
        break