# Hayden Bybee
# UWYO COSC 1010
# 10/24/24
# HW 02
# Lab Section: 16
# Sources, people worked with, help given to: 
# N/A
Translated = ""

mcalphabet = {" ":"","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....",
              "i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.",
              "q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-",
              "y":"-.--","z":"--.."}

Untranslated = input("Type out a sentence you would like to be translated into morse code! (plain alphabetical values and spacing only, no punctuation!!)")

for letter in Untranslated:
    if letter.isalpha() or letter == " ":
        for keys, values in mcalphabet.items():
            if letter.lower() == keys:
                Translated += values + " "


print(Translated)