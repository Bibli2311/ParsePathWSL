import sys

try:
    path = sys.argv[1]
except IndexError:
    print("Error: Pass in an argument for specifying path")
    print("For example: python3 fixPath.py C:\\Users\\oscar\\Music\\")
    sys.exit(1)
   
print("you entered: " + path)

backslash = ord("\\")      #ascii value of backslash
parsedPath = ""

for element in path:
    if ord(element) == backslash:    #if character is a backslash
        element = "/"            
    parsedPath += element           #replaces backslash with forward slash

print(parsedPath)

resultPath = "/mnt/c" + parsedPath[2:] #add /mnt/c to string, and remove "C:/" from the parsed path
print(resultPath)
