#reverse a string in place (Space complexity of O(1)
def swap(A,i,j):
     temp = A[i]
     A[i] = A[j]
     A[j] = temp

def rev(word):
    wordList = list(word)
    i = 0
    while (i <= len(wordList)/2):
        swap(wordList, i, len(word) - i -1)
        i += 1
    return ("".join(wordList))

print(rev(raw_input("word?: ")))

