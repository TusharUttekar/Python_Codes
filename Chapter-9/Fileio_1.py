#Basic of file operations read/write/append etc.

#Writing to file and also creating new file
F = open("File.txt", "w")
F.write("The new file is created")
F.close()

#Reading from the file
F = open("File.txt")
print(F.read())
F.close()

#Appending to the file which is read
F = open("File.txt", "a")
F.write("New appended line")
F.close()