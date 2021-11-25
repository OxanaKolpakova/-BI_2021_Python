import re
with open('references.txt') as input:
    text = input.read()
pattern = re.compile(r'ftp[\w./]*\.[\w./]*[;\s]')
find = pattern.findall(text)
# print(*find, sep='\n')
with open('ftps.txt', "w") as output:
    for str in find:
        str = str.replace("\t", "\n")
        str = str.replace(";", "\n")
        output.write(str)
