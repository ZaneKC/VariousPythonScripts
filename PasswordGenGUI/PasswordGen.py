from tkinter import *
import random
import time

#loop variable
program = True

VariableC = 0
#list of characters that are being used to build the password
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "z", "t", "u", "v", "w", "x", "y", "z"]
CLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Symbols = ["&", "!", "?", "$",]
Password = 0

#Function that creates the passwords, as well as binds it with the right variable and file
def Pas():
    while program == True:
        Char = 0
        List = 0
        CurLet = ""
        Password = ""
        #grabbing the list and pulling random characters from them for a set amount
        while Char < 20:
            List = random.randint(1, 4)
            if List == 1:
                CurLet = random.choice(Letters)
            elif List == 2:
                CurLet = random.choice(Numbers)
            elif List == 3:
                CurLet = random.choice(CLetters)
            else:
                CurLet = random.choice(Symbols)
            #combines the current stores characters with the new character getting added to the scramble
            Password = (Password + CurLet)
            #parameter for the amount of characters it wants to pull
            Char = Char + 1

        print(Password)
        str(Password)
        #if statement sorting through which password button was clicked, then setting that file to the new scramble
        if VariableC == 1:
            f = open("save.txt", "w")
            f.write(Password)
            f.close()
        elif VariableC == 2:
            f = open("save2.txt", "w")
            f.write(Password)
            f.close()
        elif VariableC == 3:
            f = open("save3.txt", "w")
            f.write(Password)
            f.close()
        elif VariableC == 4:
            f = open("save4.txt", "w")
            f.write(Password)
            f.close()
        elif VariableC == 5:
            f = open("save5.txt", "w")
            f.write(Password)
            f.close()
        break

#functions for each button, giving them a set variable for the pas() to identify the right password to change

def Abutt():
    global VariableC
    VariableC = 1
    Pas()
    
def Bbutt():
    global VariableC
    VariableC = 2
    Pas()
    
def Cbutt():
    global VariableC
    VariableC = 3
    Pas()
    
def Dbutt():
    global VariableC
    VariableC = 4
    Pas()
    
def Ebutt():
    global VariableC
    VariableC = 5
    Pas()
    
root = Tk()
root.geometry('500x500')

#creates variables for the label text
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()

#sets the variables, giving a sense of a hidden password
var1.set("********")
var2.set("********")
var3.set("********")
var4.set("********")
var5.set("********")

#buttons designated for each password line
#They are opening the save and setting that password to the label text
def Abutt2():
    f = open("save.txt", "r")
    var1.set(f.read())
    f.close()

def Bbutt2():
    f = open("save2.txt", "r")
    var2.set(f.read())
    f.close()

            
def Cbutt2():
    f = open("save3.txt", "r")
    var3.set(f.read())
    f.close()

def Dbutt2():
    f = open("save4.txt", "r")
    var4.set(f.read())
    f.close()

def Ebutt2():
    f = open("save5.txt", "r")
    var5.set(f.read())
    f.close()

#commands to hide the password again
def Abutt3():
    var1.set("********")

def Bbutt3():
    var2.set("********")

def Cbutt3():
    var3.set("********")

def Dbutt3():
    var4.set("********")

def Ebutt3():
    var5.set("********")

#creating labels, buttons, title, etc
Title = Label(text = "Password Database", font=("Times", 30)).pack()

Aent = Label(root, width = 20, textvariable=var1).place(x=15, y=60)
Abut = Button(root, width = 5, bg="Dark Grey", text="₪", font=("Times", 10), command=Abutt).place(x=160, y=55)
Abut2 = Button(root, width = 5, bg="Red", text="See", font=("Times", 10), command=Abutt2).place(x=215, y=55)
Abut3 = Button(root, width = 3, bg="Light Pink", text="Hide", font=("Times", 10), command=Abutt3).place(x=270, y=55)

Bent = Label(root, width = 20, textvariable=var2).place(x=15, y=100)
Bbut = Button(root, width = 5, bg="Dark Grey", text="₪", font=("Times", 10), command=Bbutt).place(x=160, y=95)
Bbut2 = Button(root, width = 5, bg="Red", text="See", font=("Times", 10), command=Bbutt2).place(x=215, y=95)
Bbut3 = Button(root, width = 3, bg="Light Pink", text="Hide", font=("Times", 10), command=Bbutt3).place(x=270, y=95)

Cent = Label(root, width = 20, textvariable=var3).place(x=15, y=140)
Cbut = Button(root, width = 5, bg="Dark Grey", text="₪", font=("Times", 10), command=Cbutt).place(x=160, y=135)
Cbut2 = Button(root, width = 5, bg="Red", text="See", font=("Times", 10), command=Cbutt2).place(x=215, y=135)
Cbut3 = Button(root, width = 3, bg="Light Pink", text="Hide", font=("Times", 10), command=Cbutt3).place(x=270, y=135)

Dent = Label(root, width = 20, textvariable=var4).place(x=15, y=180)
Dbut = Button(root, width = 5, bg="Dark Grey", text="₪", font=("Times", 10), command=Dbutt).place(x=160, y=175)
Dbut2 = Button(root, width = 5, bg="Red", text="See", font=("Times", 10), command=Dbutt2).place(x=215, y=175)
Dbut3 = Button(root, width = 3, bg="Light Pink", text="Hide", font=("Times", 10), command=Dbutt3).place(x=270, y=175)

Eent = Label(root, width = 20, textvariable=var5).place(x=15, y=220)
Ebut = Button(root, width = 5, bg="Dark Grey", text="₪", font=("Times", 10), command=Ebutt).place(x=160, y=215)
Ebut2 = Button(root, width = 5, bg="Red", text="See", font=("Times", 10), command=Ebutt2).place(x=215, y=215)
Ebut3 = Button(root, width = 3, bg="Light Pink", text="Hide", font=("Times", 10), command=Ebutt3).place(x=270, y=215)

#tkinter mainloop command, allows the window to stay open
root.mainloop()


