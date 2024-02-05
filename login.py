from tkinter import*
from PIL import ImageTk
import customtkinter as ctk





#functionality
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)





#GUI
root = Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Login Page')


bgImage=ImageTk.PhotoImage(file='Images/Screenshot 2024-02-02 at 18.18.35.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(root,text='WELCOME!',font=('Microsoft Yahei UI Light',30,'bold'),bg='#DFA7E4',fg='#A5256B')
heading.place(x=720,y=120)

heading1=Label(root,text='Sign in to your account',font=('Microsoft Yahei UI Light',22),bg='#DFA7E4',fg='#A5256B')
heading1.place(x=680,y=160)

usernameEntry=Entry(root,width=40,font=('Microsoft Yahei UI Light',11),bg='white',bd=0,fg='#A5256B',highlightbackground='white')
usernameEntry.place(x= 650,y=250)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(root,width=288,height=2,bg='#A5256B')
frame1.place(x=650,y=270)

passwordEntry=Entry(root,width=40,font=('Microsoft Yahei UI Light',11),bg='white',bd=0,fg='#A5256B',highlightbackground='white')
passwordEntry.place(x= 650,y=300)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)


frame2=Frame(root,width=288,height=2,bg='#A5256B')
frame2.place(x=650,y=320)

forgetButton = Button(root, text='Forgot Password?', bd=0, bg='#DFA7EA', activebackground='#DFA7E4', cursor='hand2', highlightbackground='#DFA7E4', font=('Microsoft Yahei UI Light', 9), fg='#A5256B')
forgetButton.place(x=825, y=350),

LoginButton = Button(root, text='Login', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0,width=13,height=1)
LoginButton.place(x=715, y=450)

RegisterLabel=Label(root,text="Don't have an account?",font=('Open Sans',9,),fg='#A5256B',bg='#DFA7EA')
RegisterLabel.place(x=650,y=550)

NewButton = Button(root, text='Create', font=('Open Sans', 9, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0)
NewButton.place(x=760, y=550)
























root.mainloop()