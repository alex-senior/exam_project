from re import findall
import pylab as pb
import numpy as np

filename = 'CLI/labs/lab7/files/text.txt'
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
x = np.arange(4)
items = list(map(len, [findall(r'(?ms)\w\.[^.]', text), findall(r'(?ms)\w!\s?', text),
                       findall(r'(?ms)\w\?\s?', text), findall(r'(?ms)\w\.\.\.\s?', text)]))
pb.bar(x, height=items)
pb.xticks(x, ['.', '!', '?', '...'])
pb.savefig("gist_sentences.png")
pb.show()