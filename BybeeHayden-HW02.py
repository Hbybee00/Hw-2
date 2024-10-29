# Hayden Bybee
# UWYO COSC 1010
# 10/24/24
# HW 02
# Lab Section: 16
# Sources, people worked with, help given to: 
# N/A
Translated = ""

mcalphabet = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....",
              "i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.",
              "q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-",
              "y":"-.--","z":"--.."}

Untranslated = input("Type out a sentence you would like to be translated into morse code! (plain alphabetical values, no punctuation!!)")

for letter in Untranslated:
    for keys, values in mcalphabet.items():
        if letter.lower() == keys:
            Translated += values + " "
        elif letter == " ":
            Translated += letter
#no matter which way I do the double spaces, it always comes out as way more than just double spacing in the output?? :(

print(Translated)