# Function to print words which can be created 
# using given set of characters 
# part 1  
  
def Check_Vow(string, vowels): 
    vowels = [each for each in string if each in vowels] 
    print(len(vowels)) 
    print(vowels) 
string = "jukeboxes"
vowels = "AaeEeIiOoUu"
Check_Vow(string, vowels);

text = 'jukeboxes'
print(text.split()) 
word = 'juke:boxes'
print(word.split(':')) 
word = 'boxoxesub'
print([word[i:i+3] for i in range(0, len(word), 3)])

"sub" in word
print(True)
"keb" in word
print(False)

