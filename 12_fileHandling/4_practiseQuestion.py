k=0
with open("12_fileHandling/sample.txt","r") as f:
    data = f.readline()

    while (data):
        k=k+1
        if("alok" in data):
            print(f"alok found at {k} line")
            break
        data=f.readline()