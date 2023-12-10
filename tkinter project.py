import tkinter
import json

#from PIL import ImageTk,Image
#def submit():
#----------create window-----------

win=tkinter.Tk()
win.title("login form")
win.geometry('340x440')
win.configure(bg="#05161A")
frame=tkinter.Frame()

def submit():
    txtuser=tkinter.Entry(win,font=("Arial bold",10))
    username = txtuser.get()
    password = txtpass.get()

    if not username or not password:
        lblmsg.config(text="Please enter both username and password.", fg="red")
        return

    users = load_users()
    if username in users:
        lblmsg.config(text="This username is already submited.", fg="red")
    else:
        users[username] = password
        save_users(users)
        lblmsg.config(text="submit successful.", fg="green")

def login():
     username=txtuser.get()  
     password=txtpass.get()
     with open("users.json","r")as f:
      data=json.load(f)
      if username in data:
          lblmsg.configure(text="welcome", fg="green",font=("Arial",15))
      else:
         lblmsg.configure(text="wrong user or pass!", fg="red",font=("Arial",15))
                
     username=txtuser.get()  
     print(username) 
     lbluser.configure(text=username)
    
def delete_account():
    username = txtuser.get()
    if not username:
        lblmsg.config(text="Please enter the username.", fg="red")
        return

    users = load_users()
    if username in users:
        del users[username]
        save_users(users)
        login.config(text="Account deleted successfully.", fg="green")
    else:
        login.config(text="Username not found.", fg="red")

def load_users():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    return users

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)


#---------create widget------------
lbl_login=tkinter.Label(win,text="welcome",bg="#05161A",fg="#294D61",font=("Arial bold",30),pady=30)
lbl_login.pack()

lbluser=tkinter.Label(win,text="username: ",bg="#05161A",fg="#FFFFFF",font=("Arial",15))
lbluser.pack()  
txtuser=tkinter.Entry(win,font=("Arial bold",10))
txtuser.pack()

lblpas=tkinter.Label(win,text="password: ",bg="#05161A",fg="#FFFFFF",font=("Arial",15))
lblpas.pack()
txtpass=tkinter.Entry(win,font=("Arial bold",10))
txtpass.pack()

lblmsg=tkinter.Label(win,text="")
lblmsg.pack()
login=tkinter.Button(win,text="login",command=login,bg="#0C7075",font=("Arial bold",12))
login.pack()

submit=tkinter.Button(win,text="submit",command=login,bg="#0F969C",font=("Arial bold",12))
submit.pack()

delete= tkinter.Button(win, text="Delete Account", command=delete_account,bg="#6DA5C0",font=("Arial bold",12))
delete.pack()

#img=ImageTk.PhotoImage(Image.open("login.png"))
#lblimage=tkinter.Label(image=img)
#lblimage.pack()
#pass_entry=tkinter.Entry(win,show="*")
win.mainloop()