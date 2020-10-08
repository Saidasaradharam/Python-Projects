import random

def hangman_draw(count):
    g=(" |------------\n |          |\n |          |\n |          o\n |         /|\ \n |         / \ \n---")
    f=(" |------------\n |          |\n |          |\n |          o\n |         /|\ \n |         /  \n---")
    e=(" |------------\n |          |\n |          |\n |          o\n |         /|\ \n |          \n---")
    d=(" |------------\n |          |\n |          |\n |          o\n |         /| \n |         \n---")
    c=(" |------------\n |          |\n |          |\n |          o\n |          | \n |         \n---")
    b=(" |------------\n |          |\n |          |\n |          o\n |          \n |          \n---")
    a=(" |------------\n |          |\n |          |\n |          \n |          \n |          \n---")
    a0=(" |------------\n |          |\n |          \n |          \n |          \n |          \n---")
    if(count==0):

        print(a0)
    elif(count==1):

        print(a)
    elif(count==2):

        print(b)
    elif(count==3):

        print(c)
    elif (count == 4):

        print(d)
    elif (count == 5):

        print(e)
    elif (count == 6):

        print(f)
    elif (count == 7):

        print(g)
        print("\t\t\tYOU KILLED HIM!!!!")
        print("\t\t\tYOU LOST THE GAME!!!!!")
        again()

def start():
    question={1:['Animal' , 'elephant'],2:['Movie' , 'premam'],3:['Insect' , 'spider'],4:['Food' , 'biriyani']
        ,5:['Fruit' , 'pineapple'], 6:['Social media', 'Instagram'],7:['Dress' , 'shirt'],8:['Country' , 'Australia'],
              9:['Colour' , 'black'],10:['Vegetable' , 'drumstick']}
    print("\t\t\t\t Welcome to play the game : HANGMAN.\n\n")
    no=random.randint(1,10)
    hint=question[no][0]
    answer=question[no][1].upper()

    check=str()
    gs_lt=[]
    l=len(answer)
    mdar=list()
    for i in range(l):
        mdar.append('_')

    print("\t\tGuess the word with the given hint.\n")
    print('\t\tHint : ',hint)
    print('\t\t','_ '*l)
    count=0
    while(count<8):
        letter=input("\nEnter guessed letter : ")
        letter=letter.upper()
        if(letter not in gs_lt ):
            gs_lt.append(letter)
            if(letter in answer):
                for i in range(l):
                    if(answer[i]==letter):
                        mdar.pop(i)
                        mdar.insert(i,letter)
                print("The letter guessed is correct !!\n")

                for i in mdar:

                    print(i,end=' ')
                print('\n\n')
                hangman_draw(count)
                flag=1
                for i in range(l):
                    if answer[i]!=mdar[i]:
                        flag=0
                        break
                if(flag==1):
                    print("\t\t\tCONGRATULATIONS!!!\n \t You have succefully completed the game!!!")
                    again()





            else:
                print("Letter guessed is worng....")
                count+=1
                hangman_draw(count)
                print("You have ",7-count,' more guesses left....')
                print('\t\tHint : ',hint)
                for i in mdar:

                    print(i,end=' ')
                print('\n\n')

            print("Letter which you have guessed  : ",end='')
            for i in gs_lt:
                print(i,end=' ')
            print()
        else:
            print("You have already guessed this letter, try a different one... ")
            print("Letter which you have guessed  : ",end='')
            for i in gs_lt:
                print(i,end=' ')
            print()

def again():

    choice=input('Do you want to play the game again?? Y(Yes) / N(No) ').upper()
    if(choice=='Y'):
        start()
    elif(choice=='N'):
        exit()
    else:
        print("Entered choice is wrong....Enter again!")

start()
