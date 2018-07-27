import nltk
from nltk.util import ngrams
def possible_combination(text,n):
    token = nltk.word_tokenize(text)
    print("Please provide the output of tokenization")
    print(token)
    possible_combination_n=ngrams(token,n)
    return possible_combination_n
#Writtemn three text
Text1 = 'My name is Sanpreet Singh'
Text2 = "You are reading code on tokenization and combinations of words"
Text3 = "Hope you Like it"
#Combining these into one using concatenation
Text_Overall = Text1 + " " + Text2 + " " + Text3
#Let us choose how many words you need to combine in one line
n = 3
#Let us pass both the arguments to the function possible_combination
output = possible_combination(Text_Overall,n)
######################################################################
#Visualizing the output
for combibations in output:
    # print("Please see the combinations in one line. I have set three words per line:")
    # print("You may change the combination by settting the value of n:")
    print(combibations)

