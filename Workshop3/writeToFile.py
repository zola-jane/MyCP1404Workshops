""" ask the user for their name and opens a file called
"name.txt" and writes the name to it """

name = input("Enter your name: ")

out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


