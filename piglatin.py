pyg = 'ay'

original = raw_input('Enter a word:')
# this if statement checks if the word isn't an empty string and makes sure its all letters
if len(original) > 0 and original.isalpha():
    # this changes all the letters to lowercase
    word = original.lower()
    # this takes the first letter of the word using index
    first = word[0]
    # thid adds the word, with the first letter, then 'gy' after it
    new_word = word + first + pyg
    # this takes the first letter off the word so its not repeated
    new_word = new_word[1:len(new_word)]
else:
    print 'empty'
