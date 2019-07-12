#First project
#why?? Just to get a hang of project building
# I will be using tkinter for gui
# This app is for storing passwords offline in a encrypted manner


#Day1 :8,july,19

import tkinter as tk
import tkinter.messagebox as msgbox
import os


HEIGHT = 300
WIDTH = 600
root = tk.Tk()
root.title("STORE PASSWORD")
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
frame = tk.Frame(root,bg='white' )
frame.place(relwidth=1,relheight=1)

# windows that will open when 'create new account' button is pressed
# these function done on day2 8,july,19

# Functionality of Create My Account Button inside Create My Account Button

def check(New_User_Name, New_Password):  #check for empty fields and then for username uniqueness

    if New_Password != '' and New_User_Name != '':  # avoiding empty fields

        with open('UserNames.txt','r+') as UserName_check:
            if os.stat("UserNames.txt").st_size != 0:           # to check empty file
                if New_User_Name in UserName_check.readlines()[0].split(','):
                    msgbox.askretrycancel("Error","This UserName already exist")
                    return False
            return True

    else:
        msgbox.showinfo('Empty Fields', 'You left UserName/Password field empty')
        # if anyone field is left empty


def Verify_Login(UserName,Password):
    with open('UserInfo.txt','r') as Check_Usernames:
        user_info=str(UserName+','+Password)
        if Check_Usernames.readlines()[Check_Usernames.readlines().index(user_info)].split(',')[0] == UserName and Check_Usernames.readlines()[Check_Usernames.readlines().index(user_info)].split(',')[1]==Password:
            ShowPasswords()
        else:
            print("This account is not registered")














def ShowPasswords():
    msgbox.showinfo("Accounnt is here"," your account is with us")


def ADD_User_Info(New_User_Name,New_Password):         # after checkinh for uniqueness finally adding user
    with open('UserInfo.txt' , 'a') as add:
        add.write( New_User_Name + ',' + New_Password + '\n')
    with open('UserNames.txt','a') as Add_New_Username:
        Add_New_Username.write(New_User_Name+ ',')
    msgbox.showinfo("Account Created"  , "Your Account has been created")








def open_new_account_Window():

    # this function is for FINALLY creating account after user enters deatails.

    def Account_Creation():

        New_User_Name = entry_NEW_Username.get()
        New_Password = entry_New_Password.get()


        if check(New_User_Name , New_Password):

            ADD_User_Info(New_User_Name,New_Password)             # this fucnton finally adds this user and its password




    Create_New_Account_Window=tk.Toplevel()
    Create_New_Account_Window.title('Create New Account')

    tk.Canvas(Create_New_Account_Window,height=HEIGHT,width=WIDTH).pack()


    # UserName Label and Entry

    label_NEW_username=tk.Label(Create_New_Account_Window,text='New Username :',bg='white')
    label_NEW_username.place(relx=0,rely=0.25,relwidth=0.29,relheight=0.1)

    entry_NEW_Username = tk.Entry(Create_New_Account_Window,bg='lightgray')
    entry_NEW_Username.place(relx=0.3,rely=0.25,relwidth=0.5,relheight=0.1)

    # Password Label and Entry

    tk.Label(Create_New_Account_Window,text='Your Master Password',bg='white').place(relx=0,rely=0.4,relwidth=0.29,relheight=0.1)

    entry_New_Password=tk.Entry(Create_New_Account_Window,bg='lightgray',show='*')
    entry_New_Password.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.1)


    # Final Create My Account Button

    tk.Button(Create_New_Account_Window,text='Create My Account',cursor='hand2',command=Account_Creation).place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.1)


# Main Window

#create new account button

button_create_new_account=tk.Button(frame,text='Create New Account',cursor='hand2',command=open_new_account_Window)
button_create_new_account.place(relx=0.6,rely=0.9,relwidth=0.40,relheight=0.1)

# Username and its master password
label_username = tk.Label(frame,text='Username :',bg='white').place(relx=0,rely=0.25,relwidth=0.29,relheight=0.1)


entry_username=tk.Entry(frame,bg='lightgray')
entry_username.place(relx=0.3,rely=0.25,relwidth=0.5,relheight=0.1)

label_Login=tk.Label(frame,text='Enter your Master Password :',bg='white').place(relx=0,rely=0.4,relwidth=0.29,relheight=0.1)

entry_masterlogin_Password=tk.Entry(frame, bg='lightgray', show='@')
entry_masterlogin_Password.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.1)

# Day 2 9 july,2019  except command parameter
buttton_verify=tk.Button(frame,text='Let Me In',cursor='hand2',command=lambda: Verify_Login(entry_username.get(),entry_masterlogin_Password.get()))
buttton_verify.place(relx=0.5,rely=0.6,relheight=0.1,relwidth=0.1) #button to click Enter







root.mainloop()