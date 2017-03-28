wordStart = 0
vowelNum = 0

def vowelCount():
    word = input("Insert any word or sentence for a vowel count!")
    if(len(word) > 0 and word.isalpha()):
        wordLength = len(word)
        while(wordStart < wordLength):
            if(word[wordStart] == "aeiou"):
                vowelNum = vowelNum + 1
                wordStart = wordStart + 1
                print(str(vowelNum))
            else:
                wordStart = wordStart + 1
                print(str(vowelNum))



vowelCount()

