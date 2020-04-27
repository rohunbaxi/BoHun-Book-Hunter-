#Group 3, by Sahij, Rohun, Cole, Harshil, and BRIAN
#BOOK HUNTING SYSTEM. BoHun
#12/11/2017
#importing modules
import random
from tkinter import *
from tkinter import ttk
#globalizing variables used in multiple functions
global x
global blist
global n1
global n2
#setting the global variable values 
n1 = ''
n2 = ''
blist = []
x = 0
root = Tk()
root.title('BoHun')
#setting up the canvas
canvas = Canvas(root, width = 300, height = 200, bg = 'yellow')
canvas.pack()
canvas.create_text(150, 100, text = 'BoHun', font = 'Arial 28 bold', tags = 'title')
canvas.create_text(150, 130, text = 'Books are better, with BoHun', font = 'Arial 16 italic', tags = 'slogan')
#functions for student button
def student():
    canvas.delete('all')
    btStudent.pack_forget()
    btTeacher.pack_forget()
    canvas.create_text(100,20, text = 'Book Name', font = 'Arial 16 bold', tags = 'book')
    canvas.create_text(200,20, text = 'Author', font = 'Arial 16 bold', tags = 'author')
    for z in range(len(blist)):
        canvas.create_text(100,40+20*z, text = blist[z][0], font = 'Arial 14', tags = 'entry1')
        canvas.create_text(200,40+20*z, text = blist[z][1], font = 'Arial 14', tags = 'entry2')
    #function for adding names to the list of books
    def add():
        global e
        global f
        global x
        e = Entry(root)
        e.pack()
        e.delete(0, END)
        e.insert(0, 'Book Name')
        f = Entry(root)
        f.pack()
        f.delete(0, END)
        f.insert(0, 'Author')
        btAdd.pack_forget()
        btInsert.pack()
        x += 20
    #function for putting the book names onto the canvas and list
    def insert():
        global blist
        canvas.create_text(100,20+x, text = e.get(), font = 'Arial 14', tags = 'entry1')
        canvas.create_text(200,20+x, text = f.get(), font = 'Arial 14', tags = 'entry2')
        book = []
        book.append(e.get())
        book.append(f.get())
        blist.append(book)
        e.pack_forget()
        f.pack_forget()
        btAdd.pack()
        btInsert.pack_forget()
    #function for going back to homescreen
    def back():
        canvas.delete('all')
        btTeacher.pack()
        btStudent.pack()
        btAdd.pack_forget()
        canvas.create_text(150, 100, text = 'BoHun', font = 'Arial 28 bold', tags = 'title')
        btBack.pack_forget()
        btInsert.pack_forget()
        e.pack_forget()
        f.pack_forget()
    #buttons
    btAdd = Button(root, text = 'Add', command = add)
    btAdd.pack()
    btInsert = Button(root, text = 'Insert', command = insert)
    btBack = Button(root,text = 'Go Back', command = back)
    btBack.pack()

#if teacher is clicked on homescreen   
def teacher():
    canvas.delete('all')
    btTeacher.pack_forget()
    btStudent.pack_forget()

    canvas.create_text(100,20, text = 'Book Name', font = 'Arial 16 bold', tags = 'book')
    canvas.create_text(200,20, text = 'Author', font = 'Arial 16 bold', tags = 'author')
    
    for z in range(len(blist)):
        canvas.create_text(100,40+20*z, text = blist[z][0], font = 'Arial 14', tags = 'entry1')
        canvas.create_text(200,40+20*z, text = blist[z][1], font = 'Arial 14', tags = 'entry2')

    #removing books
    def remove():
        global e
        global f
        global x
        e = Entry(root)
        e.pack()
        e.delete(0, END)
        e.insert(0, 'Book Name')
        f = Entry(root)
        f.pack()
        f.delete(0, END)
        f.insert(0, 'Author')
        btRemove.pack_forget()
        btBought.pack()
        x -= 20
    #searching through the list to remove entered book and author from the list and screen
    def delete():
        global blist
        for y in range(len(blist)):
            n1 = e.get()
            n2 = f.get()
            if n1 == blist[y][0] and n2 == blist[y][1]:
                blist.pop(y)
                e.pack_forget()
                f.pack_forget()
                break

        btRemove.pack()
        btBought.pack_forget()
        canvas.delete('all')
        for z in range(len(blist)):
            canvas.create_text(100,40+20*z, text = blist[z][0], font = 'Arial 14', tags = 'entry1')
            canvas.create_text(200,40+20*z, text = blist[z][1], font = 'Arial 14', tags = 'entry2')
    #rolling a random number to choose which book is bought by the teacher
    def randompick():
        global blist
        global x
        booknumbers = len(blist) - 1
        booknumber = random.randint(0,booknumbers)
        canvas.delete('all')
        btRemove.pack_forget()
        btRafflePick.pack_forget()
        canvas.create_text(150, 100, text = 'The winner is...', font = 'Helvetica 15 bold', tags = 'winner')
        canvas.create_text(150, 120, text = blist[booknumber][0], font = 'Helvetica 16 bold')
        canvas.create_text(150, 140, text = blist[booknumber][1], font = 'Helvetica 16 bold')
        canvas.create_text(150, 160, text = 'It has been ordered and removed.', font = 'Helvetica 15 bold')
        blist.pop(booknumber)
        x -= 20
    #back to homescreen
    def back():
        canvas.delete('all')
        btTeacher.pack()
        btStudent.pack()
        btRemove.pack_forget()
        canvas.create_text(150, 100, text = 'BoHun', font = 'Arial 28 bold', tags = 'title')
        btBack.pack_forget()
        btRafflePick.pack_forget()
        btBought.pack_forget()
        e.pack_forget()
        f.pack_forget()
    #buttons in teacher screen
    btRemove = Button(root, text = 'Remove', command = remove)
    btRemove.pack()
    btBought = Button(root, text = 'Delete', command = delete)
    btBack = Button(root,text = 'Go Back', command = back)
    btBack.pack()
    btRafflePick = Button(root,text = 'Raffle Pick', command = randompick)
    btRafflePick.pack()

#homescreen buttons
btStudent = Button(root, text = 'Student', command = student)
btStudent.pack()
btTeacher = Button(root, text = 'Teacher', command = teacher)
btTeacher.pack()

root.mainloop()
