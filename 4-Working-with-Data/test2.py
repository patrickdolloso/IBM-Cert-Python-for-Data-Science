# Writes 1 line to test2.txt
with open("./test2.txt","w") as File1:
    File1.write("This is line A")

# Writes list L in as a loop
Lines = ["This is line A\n","This is line B\n","This is line C\n"]
with open("./test2a.txt","w") as File2:
    for line in Lines:
        # test
        print(line)
        # loop
        File2.write(line)

# Append - Write this is line D in same file test2a.txt
with open("./test2a.txt","a") as File2:
    File2.write("This is line D")

# copy test2a.txt contents to a new file test2b.txt
with open("./test2a.txt","r") as readfile:
    with open("./test2b.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)