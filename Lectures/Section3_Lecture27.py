try:
    print("Opening none existent file:")
    my_file = open('myfile2.txt')
except FileNotFoundError:
    print("FileNotFoundError: Uhm not here")
except:
    print("General Exception: Not sure")
finally:
    print("-------------------")

myfile = open('myfile.txt')

print("\nprint myfile FIRST time myfile.read() :\n", myfile.read())
print("\nprint myfile SECOND time:\n", myfile.read())
myfile.seek(0)
print("\nprint myfile THIRD time after myfile.seek(0) to reset cursor:\n", myfile.read())

myfile.seek(0)
myfile_list = myfile.readlines()
print("Using myfile.readlines()", myfile_list)
print("Get second element myfile_list[1]: ", myfile_list[1])

myfile.close();

print("\nFile Locations:\n----------------")

with open('test.txt', mode='w+') as f:
    print("Creating text file:")
    f.write("ONE ON FIRST\n");
    f.write("TWO ON SECOND\n");
    f.write("THREE ON THIRD\n");

with open('test.txt', mode='r') as f:
    contents = f.read()
    print("Contents:")
    print(contents)

with open('test.txt', mode='a') as f:
    print("Appending to text file:")
    f.write("FOUR ON FOURTH\n");

with open('test.txt', mode='r') as f:
    contents = f.read()
    print("Contents:")
    print(contents)