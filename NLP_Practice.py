import numpy as np
import tensorflow as tf
import keras
from keras import layers
import os


#This is meant as practice. Done with the intent of getting familiar with TensorFlow. 

print("Checking for installation:")
print("TensorFlow Version:", tf.__version__,"--> successfully intatlled.")
print("Keras Version:",keras.__version__,"--> successfully intatlled.")
print("Numpy Version:",np.__version__,"--> successfully intatlled.")

#This will specifically look into RNN/LSTM

#Sequence Data
#First Practice:
#Bag of words: 

#Every time we see a word, we will take it's respective number and add it to the 'bag'

#This only catches the frequency of the words that appear, doesn't keep the order of the words. 

#Therefore, cann't take into the context of the words. 

#I thought that the movie was going to be bad, but it was actually amazing. 
#I thought that the movie was going to be amazing, but it was actually bad. 

vocab={} #this will map the words to an integer
def bagOfWords(text):
    word_encoding=1
    words=text.lower().split(" ") #simply creates a list of all the words. 
    #for the time being, assumer there is no punctuation
    bag ={} #stores all of the encodings and their frequency
    for word in words:
        if word in vocab: 
            encoding = vocab[word]
        else: 
            vocab[word]= word_encoding
            encoding = word_encoding
            word_encoding+=1
        if encoding in bag: 
            bag[encoding]+= 1
        else:
            bag[encoding]=1
    return bag

text="this is a test to see if the program above works and runs smoothly"
bag = bagOfWords(text)
print("This shows the numerical encoding value for each word:   ",vocab)
print("This displays the numerical representation of a word and its frequency:   ",bag)



#Word Embedding, keeps the order of the words. 

#word embedding is a layer in our model, attempts to understand the context of where words are placed. 

#new version will make an array to keep track of the order of words

vocab={}
def oneHotEncoding(text):
    word_encoding=1
    words= text.lower().split(" ")
    encoding =[]
    for word in words: 
        if word in vocab:
            code= vocab[word]
            encoding.append(code)
        else:
            vocab[word]= word_encoding
            encoding.append(word_encoding)
            word_encoding +=1
    return encoding


text= "this is a test to see if it keeps track of the order of words correctly while also representing them numerically"
encoding = oneHotEncoding(text)
print("This shows each word and its encoded value:   ", vocab)
print("This is the order of words, using their encoded values:   ", encoding)




