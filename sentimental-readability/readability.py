from cs50 import get_string

def main ():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    L = 100*letters/words
    S = 100*sentences/words
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index<1:
        print("Before Grade 1")
    if index>16:
        print("Grade 16+")
    elif(index > 1 and index < 16):
        print(f"Grade: {index}" )


def count_letters(text):
    counter = 0
    for char in text:
        if char.isalpha():
            counter += 1

    return counter



def count_words(text):
    counter = 1
    for i in range (0,len(text)):
        if text[i] == " ":
            counter+= 1

    return counter

def count_sentences(text):
    counter = 0
    for i in range(0,len(text)):
        if text[i] in ["?",".","!"]:
            counter += 1
    return counter


main()


