import tkinter as tk
from nltk.corpus import brown
import random

from tkinter import *

from tkinter import Button
import nltk



word_list = brown.words()
word_list = [x for x in word_list if x.isalpha()]
six_letters = [w.lower() for w in word_list if len(w) == 6]

    
def produce_letters():
    letters=[]
    random_word=six_letters[random.randint(0,len(six_letters))]
    for i in random_word:
        letters.append(i)
        print(i)
    

def solve(short,long):
    long = list(long)

    for s in short:
        if s in long and long:
            long.remove(s) 
          
        else:
            return False

    return True


def get_all(word):
    w=[]
    for l in word_list:
        if(solve(l,word) and len(l)>=3):
            w.append(l)
    return w

def gen():
    random_word = six_letters[random.randint(0, len(six_letters))]
    letters = random.sample(list(random_word), 6)
    print(letters)
    all_words = get_all(random_word)
    return set(all_words),letters

all,letters=gen()

final=[]

def submit():

    word=txt.get()
    txt.delete(0,"end")
    print(all)
    
    if word in all and word not in final:
        
        warning.configure(text=word + ' found!', fg="green")
        final.append(word)
        print(final)
    
    elif word in final and word in all:
        warning.configure(text=word + ' already found!', fg="red")
    elif word not in all:
        warning.configure(text=word + ' not found!', fg="red")
        
        
    if len(final) == len(all):
        warning.configure(text='Congratulations! You\'ve found all the words!', fg="green")


window=Tk()
window.geometry("430x450")

window.title("welcome")
window.configure(background='white') #important in making it look neat lol

blank1 = Label(window, text = "SPACE", bg='white', fg='white', font = ("Arial Bold",20))
blank1.grid(column = 0, row = 1)
    
letter_container=Label(window,text="Here are your letters: "+ str(letters[0])+" , "+str(letters[1])+" , "+ str(letters[2])+" , "+str(letters[3])+" , "+str(letters[4])+" , "+str(letters[5]),bg='white',fg='black',font=(("Arial",30)))
letter_container.grid(column = 0, row = 3)


txt = Entry(window, width = 20, font=("Arial, 20"), justify='center')
# use the grid function as usual to add it to the window
txt.grid(column=0, row=5)
txt.focus()

btn = Button(window, text = "Submit", bg = "white", fg = "black", command = submit, font = ("Arial",20))
btn.grid(column=0,row=6)

warning=Label(window,bg='white',fg='black',font = ("Arial",20))
warning.grid(column=0,row=7)




        
    
       
        
    







cdown = Label(window,text="count", bg='white', fg='black',font=("Arial", 30))
cdown.grid(column=0,row=9)

def countdown(count):
    if count>0 and len(final)!=len(all):
        cdown['text']=count
        print(cdown['text'])
        window.after(1000,countdown,count-1)
    elif len(final)==len(all):
        cdown['text']='0'
    else:
        txt.configure(state='disabled')
        score=len(final)
        warning.configure(text="TIME'S UP \n Final score: " + str(score), fg="red", font=("Arial", 30))
        not_found=[]
        for word in all:
            if word not in final:
                not_found.append(word)
        cdown.configure(text="Words not found: " + (', '.join(map(str, not_found))), font=("Arial", 20), wraplength=430, justify='center')
        
        
        

countdown(10)
        
             


    




window.mainloop()
