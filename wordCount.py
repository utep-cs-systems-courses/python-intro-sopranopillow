import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

# getting arguments
text_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# make sure text files exist
if not os.path.exists(text_file_name):
    print ("text file input %s doesn't exist! Exiting" % output_file_name)
    exit()

# getting words
file = open(text_file_name, "r")
words = re.split("[^a-zA-Z]+", file.read()) # regex: separate by anything that isn't letters
file.close()

words_dictionary = {}

# creating dictionary with all words
for word in words:
    lc_word = word.lower()
    if words_dictionary.get(lc_word) != None: # if get returns something then increase count otherwise create entry
        words_dictionary[lc_word] += 1
    else:
        words_dictionary[lc_word] = 1

# creating file
output_file = open(output_file_name, "w+")

# inserting values in a new file
for word in sorted(words_dictionary):
    if word != '': # needed for special case where dictionary does not have an empty space but it is somehow written
        output_file.write(word + ' ' + str(words_dictionary[word]) + '\n')

output_file.close()
