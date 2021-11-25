import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
wlist = []
low_reg = []
leng_list = []
unic_list = []
with open('input.txt') as input:
    text = input.read()
pattern = re.compile(r'\b[A-z]+\b')
find = pattern.findall(text)
#print(*find, sep='\n')
for word in find:
    low_reg.append(word.lower())
for word in low_reg:
    if word not in wlist:
        wlist.append(word)
wlist = sorted(wlist)
for word in wlist:
    leng_list.append(len(word))
for i in range(1, max(leng_list)+1):
    unic_list.append(leng_list.count(i))
y=unic_list
x=range(1,16)
df = pd.DataFrame({'word length':x, 'count':y})
ax = df.plot.bar(x='word length', y='count', rot=30)
plt.ticklabel_format(style='plain', axis='y')
plt.show()
plt.savefig("regular_expressions.png")