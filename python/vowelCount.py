vowels = [0, 0, 0, 0, 0]
def vowelCount():
	word = input("Insert any word, phrase, or sentence for a vowel count. ")
	#Check to see if they have letters
	if(len(word) > 0):
		wordLength = len(word)
		#Checking each vowel
		i = 0
		while(i < wordLength):
			if(word[i] == "a"):
				vowels[0] = vowels[0] + 1
				i = i + 1
			elif(word[i] == "e"):
				vowels[1] = vowels[0] + 1
				i = i + 1
			elif(word[i] == "i"):
				vowels[2] = vowels[0] + 1
				i = i + 1
			elif(word[i] == "o"):
				vowels[3] = vowels[0] + 1
				i = i + 1
			elif(word[i] == "u"):
				vowels[4] = vowels[0] + 1
				i = i + 1
			else:
				i = i + 1

	print("There are ", vowels[0], " a's, ", vowels[1], " e's, ", vowels[2], " i's, ", vowels[3], " o's, ", vowels[4], " u's.")
    
vowelCount()
