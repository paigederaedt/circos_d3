#!/usr/bin/python

import sys,csv,numpy as np
from textblob import TextBlob

#create alphabet matrix and count matrix
string = 'abcdefghijklmnopqrstuvwxyz'
list_string = list(string)
alpha_mat = [['0' for x in xrange(26)] for x in xrange(26)]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] = list_string[i]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] += list_string[j]
#for p in range(0,26):
#       print alpha_mat[p]
count_mat = [[0 for x in xrange(26)] for x in xrange(26)]

#take in arguments from command line
file_in = str(sys.argv[1])

#open read and write filestreams for I/O
filestream_in = open(file_in,'r+')

#read file and grab text, clean up for processing
text_for_processing = filestream_in.readlines()
text_for_blob = ''.join(text_for_processing)
for k in range(0,len(text_for_processing)):
        text_for_processing[k] = ''.join(e for e in text_for_processing[k] if not e.isdigit())
        text_for_processing[k] = ''.join(f for f in text_for_processing[k] if f.isalnum())
long_string = ''.join(text_for_processing)
long_string_char = list(long_string.lower())

#start processing to get counts in alpha table and create karyotype file
def CreateAlphaCountMatrix(data):
        for l in range(0,len(data) - 1):
                temp = data[l]
                compare = data[l+1]
                tuple_let = temp + compare
                for m in range(0,26):
                        for n in range(0,26):
                                if tuple_let == alpha_mat[m][n]:
                                        #print n,m,tuple_let
                                        count_mat[m][n] = count_mat[m][n] + 1
        return count_mat


blob = TextBlob(text_for_blob)
word_array = blob.words
print 'word array: ' + '\n'
print word_array
sentence_array = blob.sentences
word_alpha_mat_data = []
for word in word_array:
	word_alpha_mat_data.append(CreateAlphaCountMatrix(word));

print 'word alpha mat: ' + '\n'
print word_alpha_mat_data

count_mat = CreateAlphaCountMatrix(long_string_char)
#for r in range(0,26):
#        print count_mat[r]
print 'count_mat' + '\n'
print count_mat



