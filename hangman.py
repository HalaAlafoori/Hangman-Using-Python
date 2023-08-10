# created by: Hala Alafoori

from random import randint

def print_dashes(word):
    resulted_word=""
    for letter in word:
        if letter in guessed_letters:
            resulted_word+=letter
        else:
           resulted_word+='__ ' 
    return resulted_word
            
            
    
    

words=["Python","PHP","book"]
guessed_letters=[]
correct_word=words[randint(0,(len(words)-1))]
tries=5

found=False
shown_word=print_dashes(correct_word)
while not found:
   
    guess=input(f"guess the letters:\n {shown_word}")
    guessed_letters.append(guess)
    shown_word=print_dashes(correct_word)
    #print(guessed_letters)
    if tries==0 :
        print("Oops. You lose.")
        break
    if '_' not in  shown_word:
        print(f"Awesome! the word is {shown_word}")
        found=True
    else:
        tries-=1
        print(f"try again! you still have {tries} tries")
        
       
       