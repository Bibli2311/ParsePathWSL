# ParsePathWSL
A simple Python script which parses a path from windows into a format which is compatible with Windows Subsystem for Linux (WSL)

#Usage

python3 parsePathWSL.py 'C:\Users\ubuntu\Music\'
Then the script will return a WSL compatible path like this: /mnt/c/Users/ubuntu/Music/

One way to use this script is to do this: 
cd "$(python3 parsePathWSL.py '<Windows path>')"
This will use the result of the script directly with the cd command.

NOTE: The character "'" must be placed at the start and end of the argument in order for it to work.
This has something to do with how the terminal parses backslashes.
