import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
'''NLTK is a huge library and it is inadvisable to import all its packages and 
subpackages. If you examine the code, you will realize that only the required 
functionalities from the subpackages such as corpus and tokenize are imported 
within the code.'''

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))
'''Takes this text and produces the first part of the output in which the words are 
‘tokenized’ or simply separated by a whitespace. The same can be done with the 
split() function in the string, but the use of the package is far more efficient 
when it comes to larger blocks of code.'''

# Print statement 2
print(nltk.tokenize.sent_tokenize(text)) # takes this block of text and tokenizes by ‘sentences’.

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)
