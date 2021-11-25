import re
with open('input.txt') as input:
    text = input.read()
pattern = re.compile(r'\b\w+[aA]\w+\b')
find = pattern.findall(text)
print(*find, sep='\n')
with open('output.txt',"w") as output:
    for str in find:
        output.write(str)
        output.write("\n")