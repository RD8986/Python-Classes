# How Do You Display the Contents of a Text File in Reverse Order?

path=r"E:\sample1.txt"
with open(path, 'r') as file:
    lines = file.readlines()

reversed_lines = lines[::-1]

for line in reversed_lines:
    print(line.strip())
