#Collect a string of text as user input
user_input = input("What would you like to check for readability? ")

words_list = []
characters_list = []
#Get all the words as a list
def word_in_list():
    for word in user_input.split():
        words_list.append(word)
word_in_list()

#Count the words
def word_count():
    return len(words_list)

#For each word count the number of alphabetic characters
def word_len():
    for word in words_list:
        characters_list.append(len(word))
    return sum(characters_list)

#Count the number of sentences
def sentance_count():
    sen_1 = user_input.count(".  ")
    sen_2 = user_input.count("?  ")
    sen_3 = user_input.count("!  ")
    sen_count = sen_1 + sen_2 + sen_3
    return sen_count

#assign counts to variables for the thing
characters = word_len()
words = word_count()
sentences = sentance_count()

print(characters)
print(words)
print(sentences)

#Calculate and print the score

readability = 4.71*(characters/words)+0.5*(words/sentences)-21.43
print(readability)
