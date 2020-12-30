#A madlib game that asks the user to input words and inserts them
#into a story.

#Get user input for the blank spaces

noun1 = input("Noun:")
noun2 = input("Plural noun2:")
verb1 = input("Past tense verb:")
exclamation = input("Exclamation:")
adverb = input("Adverb:")
adjective = input("Adjective:")
verb2 = input("Present tense verb:")
color = input("Color:")

madlib = f"The dragon ran alongside the {noun1} and made his way \n \
toward the castle, breathing {noun2}. At the gate, a knight \n {verb1} \
swiftly and drew his sword. '{exclamation}!' he cried, \n slashing his sword \
{adverb} at the dragon. 'You chose the {adjective} day \n to challenge me. \
Take one step closer, and I'll {verb2}.' \n'Never mind,' said \
the dragon, turning a bright shade of {color}. 'I'll come back \n another time.'"

#Display the completed madlib
print(madlib)
