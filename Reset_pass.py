from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

 
# functionality
def change_password():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or ConfirmpasswordEntry.get() == '':
        messagebox.showerror('Error','All Fields Must Be Filled!')
    elif passwordEntry.get() != ConfirmpasswordEntry.get():
 
        messagebox.showerror('Error','Password and Confirm Psssword are not matching')
    else:
        # Connect to the database
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
        cursor = con.cursor()
 
        cursor.execute("SELECT * FROM Register WHERE Username = %s AND Password = %s", (usernameEntry.get(), passwordEntry.get()))
        row = cursor.fetchone() #Essentially, this part of the code verifies if the entered credentials correspond to a registered user. If row == None, it means the credentials are incorrect, and an error message is displayed. Otherwise, the password update proceeds.
        if row == None:
            messagebox.showerror('Error', 'Incorrect Username')
        else:
            query ='UPDATE REGISTER set Password=%s where Username=%s'
            cursor.execute(query,(ConfirmpasswordEntry.get(),usernameEntry.get()))
 
        # Close the database connection
        con.commit()
        con.close()

        
 
 
 
# GUI
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0, 0)
root.title('Reset Password')
 
bgImage = ImageTk.PhotoImage(file='Images/Forgot.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)
 
heading = Label(root, text='Reset Password!', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading.place(x=680, y=160)
 
 
 
Username = Label(root, text='Username:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Username.place(x=650, y=250)
 
usernameEntry = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
usernameEntry.place(x=720, y=250)

 
frame1 = Frame(root, width=220, height=2, bg='#A5256B')
frame1.place(x=720, y=270)
 
Password = Label(root, text='Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Password.place(x=650, y=300)
 
passwordEntry = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
passwordEntry.place(x=720, y=300)

 
frame2 = Frame(root, width=220, height=2, bg='#A5256B')
frame2.place(x=720, y=320)
 
Confirmpassword = Label(root, text='Confirm:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Confirmpassword.place(x=660, y=350)
 
ConfirmpasswordEntry = Entry(root, width=30, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
ConfirmpasswordEntry.place(x=720, y=350)
ConfirmpasswordEntry.config(show='*')

 
frame3 = Frame(root, width=220, height=2, bg='#A5256B')
frame3.place(x=720, y=370)
 
 
 
SubmitButton = Button(root, text='Submit', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=change_password)
SubmitButton.place(x=735, y=420)
 
 
root.mainloop()