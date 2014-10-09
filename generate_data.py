#!/usr/bin/python

import sys,csv,numpy as np
from textblob import TextBlob

## FUNCTION DEFINITIONS ##
#this function gets the alpha count matrix by looping through string of text and comparing tuple sequences
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


## CREATE ALPHA AND COUNT MATRICES ##
string = 'abcdefghijklmnopqrstuvwxyz'
list_string = list(string)
alpha_mat = [['0' for x in xrange(26)] for x in xrange(26)]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] = list_string[i]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] += list_string[j]
count_mat = [[0 for x in xrange(26)] for x in xrange(26)]


## TAKE IN ARGUMENTS FROM COMMAND LINE AND FILE I/O##
file_in = str(sys.argv[1])
#open read and write filestreams for I/O
filestream_in = open(file_in,'r+')


## DATA PREPARATION AND PROCESSING ##
#read file and grab text, clean up for processing
#readlines() gives lines returns output in an array
#TextBlob needs them in a string, so need separate data for text_for_blob and text_for_processing
text_for_processing = filestream_in.readlines()
text_for_blob = ''.join(text_for_processing)
#loops through all lines and and brings back only alphas characters with all special characters removed
for k in range(0,len(text_for_processing)):
        text_for_processing[k] = ''.join(e for e in text_for_processing[k] if not e.isdigit())
        text_for_processing[k] = ''.join(f for f in text_for_processing[k] if f.isalnum())
#need to put result into one long string
long_string = ''.join(text_for_processing)
long_string_char = list(long_string.lower())


## DATA ANALYSIS ##
#create alpha count matrix
count_mat = CreateAlphaCountMatrix(long_string_char)

#create textblob to work with and get necessary arrays
blob = TextBlob(text_for_blob)
word_array = blob.words
#initialize matrix that holds alpha count matrix for each word
word_alpha_count_mat = []
#calls CreateAlphaCountMatrix for each string/word in word array created from textblob
for word in word_array:
	word_alpha_count_mat.append(CreateAlphaCountMatrix(word))


#create matrix of word list arrays
#initialize matrix of word arrays
alpha_word_list_mat = [['meow' for x in xrange(26)] for x in xrange(26)]
#loop through alpha word list matrix
for row in range(0,26):
	for col in range(0,26):
		#initialize a temporary list to store words corresponding to each tuple
		temp_word_list = []
		for word in range(0,len(word_array)):
			temp = word_alpha_count_mat[word]
			if temp[row][col] > 0:
				temp_word_list.append(word_array[word])
		alpha_word_list_mat[row][col] = temp_word_list


## OUTPUT ##
#print alpha count matrix
print 'Count Matrix: ' + '\n'
print count_mat
print '\n'
#print word array matrix
print 'Word List Matrix: ' + '\n'
print alpha_word_list_mat
