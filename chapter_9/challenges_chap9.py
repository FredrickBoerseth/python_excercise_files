file_location = r'C:\\Users\\fredr\\Desktop\\test.txt'

with open(file_location, "r") as f:
    content = f.read()
    print(content)
