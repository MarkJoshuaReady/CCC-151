from tkinter import *
import csv
from tkinter import messagebox as ms


# Setting this as global so it can be accessed and be manipulated all throughout the body
global data
global row
data = []
with open('Book2.csv', 'r') as rf:
    n = csv.reader(rf)
    for row in n:
        if row:
            data.append(row)


# Main Class which consist of all operations and codes for the GUI
class main:
    def __init__(self, master):
        self.master = master
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.id_number = StringVar()
        self.course = StringVar()
        self.yearLevel = StringVar()
        self.searched_id_number = StringVar()


        self.n_firstName = StringVar()
        self.n_lastName = StringVar()
        self.n_id_number = StringVar()
        self.n_course = StringVar()
        self.n_yearLevel = StringVar()


        # Create Widgets
        self.widgets()

    # This Function is used to search and verify if a contact exists
    def search_student(self):
        mirror = bool
        idNum = self.searched_id_number.get()
        for row in data:
            for field in row:
                if field == idNum:
                    mirror = True
                    print(row)
                    print(data)
                    self.find2  = Frame(self.master, padx = 10, pady = 10)
                    Button(self.find2, text='BACK', bd=3, font=('', 15), padx=5, command=self.search).grid(
                        row=0, column=0)

                    Label(self.find2, text='ID NUMBER: ', font=('', 15), pady=5, padx=5).grid(row=6, column=1)
                    id = Label(self.find2, text=row[2], font=('', 15))
                    id.grid(row=6, column=2)

                    Label(self.find2, text='FIRST NAME: ', font=('', 15), pady=5, padx=5).grid(row=7, column=1)
                    name = Label(self.find2, text=str(row[0]), font=('', 15))
                    name.grid(row=7, column=2)

                    Label(self.find2, text='LAST NAME: ', font=('', 15), pady=5, padx=5).grid(row=8, column=1)
                    name = Label(self.find2, text=str(row[1]), font=('', 15))
                    name.grid(row=8, column=2)

                    # COURSE
                    Label(self.find2, text='COURSE: ', font=('', 15), pady=5, padx=5).grid(row=9, column=1)
                    course = Label(self.find2, text=row[3], font=('', 15))
                    course.grid(row=9, column=2)

                    # YEAR LEVEL
                    Label(self.find2, text='YEAR LEVEL(Number): ', font=('', 15), pady=5, padx=5).grid(row=10, column=1)
                    yrLvl = Label(self.find2, text=row[4], font=('', 15))
                    yrLvl.grid(row=10, column=2)


                    Button(self.find2, text='EDIT', bd=3, font=('', 15), padx=5, command=self.update).grid(
                        row=13, column=1)
                    Button(self.find2, text='DELETE', bd=3, font=('', 15), padx=5, command=self.Delete).grid(row=13,
                                                                                                            column=2)

                    self.view()


        if mirror != True:
            ms.showerror('Error', 'Student not found!')
    def update(self):
        for row in data:
            for field in row:
                if field == self.searched_id_number.get():
                    ###---- EDITOR----###
                    self.edt = Frame(self.master, padx=10, pady=10)
                    Button(self.edt, text='BACK', bd=3, font=('', 15), padx=5, command=self.view).grid(
                        row=0, column=0)
                    Label(self.edt, text='Previous ID Number: ' + str(row[2]), font=('', 15), pady=5, padx=5).grid(
                        sticky=W, row=1, column=1)
                    Label(self.edt, text='First Name: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=2,
                                                                                            column=0)
                    self.n_firstName.set(str(row[0]))
                    Entry(self.edt, textvariable=self.n_firstName, bd=5, font=('', 15)).grid(row=2, column=1)

                    Label(self.edt, text='Last Name: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=3,
                                                                                            column=0)
                    self.n_lastName.set(str(row[1]))
                    Entry(self.edt, textvariable=self.n_lastName, bd=5, font=('', 15)).grid(row=3, column=1)

                    Label(self.edt, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
                    self.n_id_number.set('Enter New ID number')
                    Entry(self.edt, textvariable=self.n_id_number, bd=5, font=('', 15)).grid(row=4, column=1)

                    Label(self.edt, text='Course: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
                    self.n_course.set(str(row[3]))
                    Entry(self.edt, textvariable=self.n_course, bd=5, font=('', 15)).grid(row=5, column=1)

                    Label(self.edt, text='Year Level: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
                    self.n_yearLevel.set(str(row[4]))
                    Entry(self.edt, textvariable=self.n_yearLevel, bd=5, font=('', 15)).grid(row=6, column=1)

                    Label(self.edt, text='').grid(sticky=W)

                    Button(self.edt, text='Update', bd=3, font=('', 15), padx=5, pady=5,
                           command=self.editData).grid(
                        row=9, columnspan=4)
                    self.edit()


    def editData(self):
        print("heloo")
        x = int()
        idNum = self.searched_id_number.get()
        new_course = self.n_course.get()
        new_yrLvl = self.n_yearLevel.get()
        new_firstName = self.n_firstName.get()
        new_lastName = self.n_lastName.get()
        new_id = self.n_id_number.get()
        for row in data:
            for field in row:
                if idNum == field:
                    if self.n_id_number.get() == "":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    elif self.n_id_number.get() == "Enter New ID number":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    elif self.n_course.get() == "":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    elif self.n_yearLevel.get() == "":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    elif self.n_firstName.get() == "":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    elif self.n_lastName.get() == "":
                        ms.showerror('Oops!', 'Please fill up all desired information')
                    else:
                        print(data)
                        mirror = bool
                        for row in data:
                            for field in row:
                                if field == new_id:
                                    if new_id == idNum:
                                        mirror = False
                                    else:
                                        mirror = True
                        if mirror == True:
                            ms.showerror('Oops!', 'Student Already exists')
                        else:
                            while x != 1:
                                for row in data:
                                    for field in row:
                                        if field == idNum:
                                            row[0] = new_firstName
                                            row[1] = new_lastName
                                            row[2] = new_id
                                            row[3] = new_course
                                            row[4] = new_yrLvl
                                            x = 1
                            with open('Book2.csv', 'w') as wf:
                                write_data = csv.writer(wf)
                                for line in data:
                                    write_data.writerow(line)
                            ms.showinfo('Success!', 'Student data Updated')
                            self.search()

                            print(data)





    # This Function is used to Delete a student's data
    def Delete(self):
        id_num = self.searched_id_number.get()
        delt = ms.askquestion('Delete Info', 'Are you sure you want to delete this data?',
                              icon='warning')
        if delt == 'no':
            self.view()
        else:
            delt2 = ms.askquestion('Delete Info', 'Are you REALLY sure you want to delete this data?',
                                   icon='warning')
            if delt2 == 'no':
                self.view()
            else:
                for row in data:
                    for field in row:
                        if id_num == field:
                            data.remove(row)
                            with open('Book2.csv', 'w') as wf:
                                write_data = csv.writer(wf)
                                for line in data:
                                    write_data.writerow(line)
                            print(data)
                ms.showinfo('Success!', 'Student INFO Deleted')
                with open('Book2.csv', 'w') as wf:
                    write_data = csv.writer(wf)
                    for line in data:
                        write_data.writerow(line)
                self.search()

    # This Function is used to add data of a student and to append is data to the global list
    def add_student(self):
        if self.id_number.get() == "":
            ms.showerror('Oops!', 'Please fill up all desired information')
        elif self.course.get() == "":
            ms.showerror('Oops!', 'Please fill up all desired information')
        elif self.yearLevel.get() == "":
            ms.showerror('Oops!', 'Please fill up all desired information')
        elif self.firstName.get() == "":
            ms.showerror('Oops!', 'Please fill up all desired information')
        elif self.lastName.get() == "":
            ms.showerror('Oops!', 'Please fill up all desired information')
        else:
            print(data)
            mirror = bool
            idNum = self.id_number.get()
            for row in data:
                for field in row:
                    if field == self.id_number.get():
                        mirror = True
            if mirror == True:
                    ms.showerror('Oops!', 'Student Already exists')
            else:
                course = self.course.get()
                yrLvl = self.yearLevel.get()
                firstN = self.firstName.get()
                lastN = self.lastName.get()
                with open('Book2.csv', 'a') as rf:
                    fieldnames = ['FIRST_NAME','LAST_NAME', 'ID_NUMBER', 'COURSE', 'YEAR_LEVEL',]
                    n = csv.DictWriter(rf, fieldnames=fieldnames)
                    n.writerow(
                        {'FIRST_NAME': firstN, 'LAST_NAME': lastN, 'ID_NUMBER': idNum, 'COURSE': course, 'YEAR_LEVEL': yrLvl, })
                    print("MI WORK JUD SYA AY")

                ms.showinfo('Success!', 'Student Added')
                self.search()



    # This Functions are used to setup the Packing methods of the widgets for the GUI

    def add(self):
        self.n_id_number.set('')
        self.head['text'] = 'Sign Up'
        self.find.pack_forget()
        self.create.pack()

    def edit(self):
        self.find.pack_forget()
        self.create.pack_forget()
        self.find2.pack_forget()
        self.head['text'] = 'EDIT'
        self.edt.pack()

    def view(self):
        self.find.pack_forget()
        self.create.pack_forget()
        self.edt.pack_forget()
        self.head['text'] = 'HI STUDENT'
        self.find2.pack()

    def search(self):
        self.n_id_number.set('')
        self.create.pack_forget()
        self.find2.pack_forget()
        self.find.pack_forget()
        self.create.pack_forget()
        self.edt.pack_forget()
        self.head['text'] = 'Find Student'
        self.find.pack()

    # This is used to setup the interfaceu
    def widgets(self):
        # entry part
        self.head = Label(self.master, text="Hello Student!", font=('', 20))
        self.head.pack()
        Label(self.master, text="").pack()

        ##------- ADD STUDENT --------##
        self.create = Frame(self.master, padx=10, pady=10)
        Button(self.create, text='BACK', bd=3, font=('', 15), padx=5, command=self.search).grid(
            row=0, column=0)
        Label(self.create, text='First Name: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=2, column=0)
        Entry(self.create, textvariable=self.firstName, bd=5, font=('', 15)).grid(row=2, column=1)

        Label(self.create, text='Last Name: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=3, column=0)
        Entry(self.create, textvariable=self.lastName, bd=5, font=('', 15)).grid(row=3, column=1)

        Label(self.create, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.id_number, bd=5, font=('', 15)).grid(row=4, column=1)

        Label(self.create, text='Course: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.course, bd=5, font=('', 15)).grid(row=5, column=1)

        Label(self.create, text='Year Level: ', font=('', 15), pady=5, padx=5).grid(sticky=W)
        Entry(self.create, textvariable=self.yearLevel, bd=5, font=('', 15)).grid(row=6, column=1)

        Label(self.create, text='').grid(sticky=W)

        Button(self.create, text='Sign Up', bd=3, font=('', 15), padx=5, pady=5, command=self.add_student).grid(
            row=9, columnspan=4)
        ##------- SEARCH --------##
        self.find = Frame(self.master, padx=10, pady=10)
        Label(self.find, text='ID Number: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=5, column=0)
        Entry(self.find, textvariable=self.searched_id_number, bd=5, font=('', 15)).grid(row=5, column=1)
        Button(self.find, text='Search', bd=3, font=('', 15), padx=5, pady=5, command=self.search_student).grid(row = 6,
            column=1)

        scrollbar = Scrollbar(self.find)
        scrollbar.grid(row=7, column=2, ipady=60)
        mylist = Listbox(self.find, width=70, yscrollcommand=scrollbar.set, selectmode = SINGLE)
        for row in data:
            for field in row:
                if field == 'FIRST_NAME':
                    data.remove(row)
        d = sorted(data, key=lambda x: x[1]),
        for i in d:
            for field in i:
                mylist.insert(END, field)

        mylist.grid(row=7, column=1)
        mylist.bind('<<ListboxSelect>>', self.onselect)
        scrollbar.config(command=mylist.yview)

        self.find2 = Frame(self.master, padx = 10, pady = 10)
        self.edt = Frame(self.master, padx=10, pady=10)
        Button(self.find, text='Sign Up', bd=3, font=('', 15), padx=5, pady=5, command=self.add).grid(
            row=9, column=0)

        self.find.pack()
    def onselect(self, event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection)
        for i in picked:
            self.searched_id_number.set(picked[2])

        self.search_student()


# Runs the GUI
root = Tk()
main(root)
root.title("HELLO STUDENT!")
root.mainloop()
