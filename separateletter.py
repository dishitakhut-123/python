#ask user to enter a number 
#separate letters in vowels and consonants list
text=(input("Enter a word"))
vowels=[]
consonants=[]
vowel="aeiouAEIOU"
for ch in text:
    if ch in vowel:
        vowels.append(ch)
    else:
        consonants.append(ch)
print("vowels",vowels)
print("consonants",consonants)