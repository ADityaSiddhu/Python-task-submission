#Assignment 4
#Task 2: Write and Append Data to a File
from fileinput import close

try:
    file1 = open('output.txt','w')
    a = input("\nEnter text to write to the file: ")
    file1.write(a+"\n")
    print("Data successfully written to output.txt")
    file1.close()

    file2 = open('output.txt','a')
    b = input("\nEnter additional text to append: ")
    file2.write(b+"\n")
    print("Data successfully appended")
    file2.close()

    file3 = open('output.txt','r')
    readfile = file3.read()
    print("\nFinal Content of output.txt: \n",readfile)
    file3.close()

except FileNotFoundError:
    print("File not found")
