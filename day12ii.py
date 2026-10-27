sentence = input("Write a sentence: ")

sentence = sentence.lower()

if "football" in sentence:
    print("You mentioned football")
elif "game" in sentence:
    print("You mentioned game")
elif "python" in sentence:
    print("You mentioned python")
else:
    print("You didn't mention football, game, or python")