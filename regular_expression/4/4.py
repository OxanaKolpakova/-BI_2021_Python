import re
with open('input.txt') as input:
    text = input.read()
pattern = re.compile(r'\b[A-Z][\w\s]*\!')
find = pattern.findall(text)
print(*find, sep='\n')
with open('output.txt', "w") as output:
    for str in find:
        output.write(str)
        output.write("\n")
