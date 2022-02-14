#script by Matthew Henry
import os
import json

#this line will need to be altered on non-windows machines; curl should be available on Unix systems; curl only available on win 10 and up
os.chdir(os.path.dirname(__file__))
os.system('curl.exe -o file.txt --url https://raw.githubusercontent.com/python/peps/main/pep-0008.txt')

#Handling IO in try and with blocks to handle IO failures and make sure resources are cleaned up
try:
    with open('file.txt', 'r') as file:
        text = file.read()
except IOError:
    print("An error has occured")
    exit()
#PEP8 Python Style Guide
#https://github.com/python/peps/blob/main/pep-0008.txt


word_counts = {}

#lowercase pre-processing to avoid double counting of words with an without capitalization
text = text.lower()
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique word:', len(word_counts))

output = json.dumps(word_counts)

with open('dictionary.json', 'w') as file:
    file.write(output)
