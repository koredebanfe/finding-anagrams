# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word, newWord):
    # [assignment] Add your code here
    word.lower()
    newWord.lower()
  
    for letter in word:
        if letter in newWord:
            return True
        return False
        
print(find_anagrams("elvis", "lives"))
print(find_anagrams("cars", "scar"))

