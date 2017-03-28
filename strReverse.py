wordLength = 0
def reverseWords():
    word = input("What is it you want reversed? ")
    if(len(word) > 0):
        wordLength = int(len(word))
        while(wordLength > 0):
            print(word[wordLength-1], sep = ' ', end=' ', flush=True)
            wordLength = wordLength - 1
    else:
        return 0

reverseWords()

