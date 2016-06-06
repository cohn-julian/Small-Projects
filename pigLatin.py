#pig latin: https://en.wikipedia.org/wiki/Pig_Latin
VOWELS = ('a', 'e', 'i', 'o', 'u')
def pigLatin(word):
    first = word[0]
    while (not (first in VOWELS)): # while the first letter is not a vowel, move the first letter to the end
        word = word[1::] + word[0]
        first = word[0]
    word = word + "ay" #once the first letter is a vowel add ay
    return word
print( pigLatin(raw_input("word?: ")))

