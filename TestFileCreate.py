file = open("myfile.txt", "a")
file.write("Hello World!")
file.close()


try:
    file = open("myfile2.txt","r")
    contents = file.read()
    file.close()
    print(contents)
except:
    print("You have the wrong file. I will now create it for you.")
    file = open("myfile2.txt", "w")
    file.close()

