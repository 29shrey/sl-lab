from functools import reduce
from collections import Counter

print("The words in the text file:")
f=open("file.txt")
content=f.read().split()
print(content)
print("\n")
print("Number of occurences of each word in descending order:")
countdic=Counter(content)
print(countdic)
print("\n")
print("Top 10 words with most number of occurences in descending order:")
s=sorted(countdic.items(),key=lambda x:x[1],reverse=True)
print(s[:10])
print("\n")
print("Average length of words is:")
wordlength=[len(i) for i,j in s[:10]]
avg= (reduce(lambda x,y:x+y,wordlength))/len(wordlength)
print(avg)
print("\n")
print("Squares of all odd numbers:")
coun=[i*i for i in wordlength if i%2!=0]
print(coun)