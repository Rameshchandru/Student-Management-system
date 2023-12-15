from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get()=='Ramesh' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')

window = Tk()
window.geometry('1530x790+0+0')
window.title('Login system of Stundent Management system')
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bgLable = Label(window, image=backgroundImage)
bgLable.place(x=0,y=0)

loginFrame = Frame(window,bg='white')
loginFrame.place(x=500, y=200)

logoImage = PhotoImage(file='logo.png')

logoLabel=Label(loginFrame, image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file= 'user.png')
usernameLabel = Label(loginFrame,image= usernameImage, text='username',compound=LEFT,
                      font=('times new roman','20','bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginFrame,font=('times new roman','20','bold'),bd=5,fg='royal blue')
usernameEntry.grid(row=1,column=1,pady=10,padx=10)


passwordImage = PhotoImage(file= 'password.png')
passwordLabel = Label(loginFrame,image= passwordImage, text='password',compound=LEFT,
                      font=('times new roman','20','bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry = Entry(loginFrame,font=('times new roman','20','bold'),bd=5,fg='royal blue')
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginButton = Button(loginFrame,text='Login',font=('times new roman','14','bold'),width=15,
                     fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                     activeforeground='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()
