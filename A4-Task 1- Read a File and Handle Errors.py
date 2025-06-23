#Assignment 4
#Task 1: Read a File and Handle Errors
try:
    file1 = open('Sample.txt','r') #file has been opened in read mode
    readingfile = file1.read() #assigning a variable so that we can print the file content
    print("Reading file content: ")
    print(readingfile)
    file1.close() #once a file is open it needs to be closed
# If the file doesnt exist then it will hit this exception
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")