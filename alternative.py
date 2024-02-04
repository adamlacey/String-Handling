sentence = input("What is a sentence that contains all the leters of the alphabet?: ") # Asks user to input answer.
result = ""

if sentence == "The quick brown fox jumps over the lazy dog":
    print(sentence)
else:
    print("You didn't enter the correct answer. Please try again. Here's a hint: the sentence involves a fox and a dog.")
    exit()                                                                             # Program exits if incorrect sentence is entered and the function below doesn't follow through.

for index in range(len(sentence)):                                                     # Iterator used.
    if index % 2 == 0:                                                                 # Equality opperator used for upper to get every 2nd character capitalised.
        result += sentence[index].upper()
    else:
        result += sentence[index]                                                      # Because upper function is used, every other character shouild be not capitalised.
  
print(result) 

sentence_capital = sentence.split()                                                    # New string variable which = the split of the original string.
sentence_capital[1::2] = [l.upper() for l in sentence_capital[1::2]]                   # Using 1::2 to jump to the next available word aka 'World'. Using upper function to capitalize.
new_phrase = " ".join(sentence_capital)                                                # Joining the split string in a new phrase which creates Hello WORLD.

print(new_phrase)