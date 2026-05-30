

def hangman():

    import random
    from word import word

    word=random.choice(word) 
    print(word)
    word1=word.upper()

    word_letters=list(word.upper())

    used_letters=[] 

    print("The first letter of the word is ",word_letters[0])
    print("Length of the word is ",len(word1))
    
    used_letters.append(word_letters[0])
    word_letters.remove(word_letters[0])

    lives =  6

    while len(word_letters)>0 and lives>0:
    
        guessed_letter=input("Guess the letter : ").upper()
        used_letters.append(guessed_letter)

        if guessed_letter in word_letters :
            word_letters.remove(guessed_letter)
        else:
            lives=lives-1
            pass

        new_list=[letter if letter in used_letters else '_ ' for letter in word1]

        print("used letters are : ",",".join(used_letters)) 
        print("".join(new_list))
        print("Remaining lives",lives)

    if(len(word_letters)==0):
        print("You won")
    else :
        print("You lose")
    

hangman()