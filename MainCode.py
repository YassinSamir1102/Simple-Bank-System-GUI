import os
import json
import random
from tkinter import *
from pathlib import Path

class App():

    def disable_resize(event):
        return False

    def __init__(self):
        self.root = Tk()
        self.root.title('Bank System')
        self.root.geometry('375x375')
        self.root.iconbitmap('AppLogo.ico')
        
        self.root.eval('tk::PlaceWindow . center')

        self.root.resizable(width=False, height=False)
        self.root.bind("<Control-=>", self.disable_resize)

        bg = PhotoImage(file='Background.png')
        Label(self.root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.MainLabel = Label(self.root, text='Bank System', font=('Georgia', 25), bg='#8EC2E9')
        self.MainLabel.pack(pady=15)

        self.Know = Button(self.root, text='Know your balance', width=30, command=self.Know_style)
        self.Know.pack(pady=15)

        self.Delete = Button(self.root, text='Delete your account', width=30, command=self.Delete_style)
        self.Delete.pack(pady=15)

        self.Create = Button(self.root, text='Create new account', width=30, command=self.Create_style)
        self.Create.pack(pady=15)

        self.Add = Button(self.root, text='Add money', width=30, command=self.Add_style)
        self.Add.pack(pady=15)

        self.Withdraw = Button(self.root, text='Withdraw money', width=30, command=self.Withdraw_style)
        self.Withdraw.pack(pady=15)

        self.root.mainloop()

    def Know_style(self):
        self.Delete.pack_forget()
        self.Know.pack_forget()
        self.Create.pack_forget()
        self.Add.pack_forget()
        self.Withdraw.pack_forget()

        self.MainLabel.config(text='Know your Balance')

        self.Field_1 = Entry(self.root, width=40)
        self.Field_1.pack(pady=15)
        self.Field_1.insert(0, 'Enter your id')

        self.Field_2 = Entry(self.root, width=40)
        self.Field_2.pack(pady=15)
        self.Field_2.insert(0, 'Enter your password')

        self.submit = Button(self.root, text='Know', width=20, command=self.Know_action)
        self.submit.pack(pady=15)

        self.Back = Button(self.root, text='Back to home', width=20, command=self.Back_action)
        self.Back.pack(pady=15)

        self.resultlabel = Label(self.root, text='', font=('Georgia', 10), fg='red', bg='#8EC2E9')
        self.resultlabel.pack(pady=15)

        self.condition = True

    def Delete_style(self):
        self.Delete.pack_forget()
        self.Know.pack_forget()
        self.Create.pack_forget()
        self.Add.pack_forget()
        self.Withdraw.pack_forget()

        self.MainLabel.config(text='Delete your account')

        self.Field_1 = Entry(self.root, width=40)
        self.Field_1.pack(pady=15)
        self.Field_1.insert(0, 'Enter your id')

        self.Field_2 = Entry(self.root, width=40)
        self.Field_2.pack(pady=15)
        self.Field_2.insert(0, 'Enter your password')

        self.submit = Button(self.root, text='Delete', width=20, command=self.Delete_action)
        self.submit.pack(pady=15)

        self.Back = Button(self.root, text='Back to home', width=20, command=self.Back_action)
        self.Back.pack(pady=15)

        self.resultlabel = Label(self.root, text='', font=('Georgia', 10), fg='red', bg='#8EC2E9')
        self.resultlabel.pack(pady=15)

        self.condition = True

    def Create_style(self):
        self.Delete.pack_forget()
        self.Know.pack_forget()
        self.Create.pack_forget()
        self.Add.pack_forget()
        self.Withdraw.pack_forget()

        self.MainLabel.config(text='Create new account')

        self.Field_1 = Entry(self.root, width=40)
        self.Field_1.pack(pady=15)
        self.Field_1.insert(0, 'Enter amount of money you wanna add')

        self.Field_2 = Entry(self.root, width=40)
        self.Field_2.pack(pady=15)
        self.Field_2.insert(0, 'Enter your password')

        self.submit = Button(self.root, text='Create', width=20, command=self.Create_action)
        self.submit.pack(pady=15)

        self.Back = Button(self.root, text='Back to home', width=20, command=self.Back_action)
        self.Back.pack(pady=15)

        self.resultlabel = Label(self.root, text='', font=('Georgia', 10), fg='red', bg='#8EC2E9')
        self.resultlabel.pack(pady=15)

        self.condition = True

    def Add_style(self):
        self.Delete.pack_forget()
        self.Know.pack_forget()
        self.Create.pack_forget()
        self.Add.pack_forget()
        self.Withdraw.pack_forget()

        self.MainLabel.config(text='Add money')

        self.Field_1 = Entry(self.root, width=40)
        self.Field_1.pack(pady=15)
        self.Field_1.insert(0, 'Enter your id')

        self.Field_2 = Entry(self.root, width=40)
        self.Field_2.pack(pady=15)
        self.Field_2.insert(0, 'Enter your password')

        self.Field_3 = Entry(self.root, width=40)
        self.Field_3.pack(pady=15)
        self.Field_3.insert(0, 'Enter amount of money you wanna add')

        self.submit = Button(self.root, text='Add', width=20, command=self.Add_action)
        self.submit.pack(pady=15)

        self.Back = Button(self.root, text='Back to home', width=20, command=self.Back_action)
        self.Back.pack(pady=15)

        self.resultlabel = Label(self.root, text='', font=('Georgia', 10), fg='red', bg='#8EC2E9')
        self.resultlabel.pack(pady=15)

        self.condition = False

    def Withdraw_style(self):
        self.Delete.pack_forget()
        self.Know.pack_forget()
        self.Create.pack_forget()
        self.Add.pack_forget()
        self.Withdraw.pack_forget()

        self.MainLabel.config(text='Withdraw money')

        self.Field_1 = Entry(self.root, width=40)
        self.Field_1.pack(pady=15)
        self.Field_1.insert(0, 'Enter your id')

        self.Field_2 = Entry(self.root, width=40)
        self.Field_2.pack(pady=15)
        self.Field_2.insert(0, 'Enter your password')

        self.Field_3 = Entry(self.root, width=40)
        self.Field_3.pack(pady=15)
        self.Field_3.insert(0, 'Enter amount of money you wanna withdraw')

        self.submit = Button(self.root, text='Withdraw', width=20, command=self.Withdraw_action)
        self.submit.pack(pady=15)

        self.Back = Button(self.root, text='Back to home', width=20, command=self.Back_action)
        self.Back.pack(pady=15)

        self.resultlabel = Label(self.root, text='', font=('Georgia', 10), fg='red', bg='#8EC2E9')
        self.resultlabel.pack(pady=15)

        self.condition = False

    def Know_action(self):
        try:
            stored_password_file = self.Field_1.get() + 'Pas.json'
            entry_password = self.Field_2.get()

            self.resultlabel.config(text='')

            path = Path(stored_password_file)
            contents = path.read_text()
            stored_password = json.loads(contents)

            if stored_password == [entry_password]:
                path = Path(self.Field_1.get() + '.json')
                contents = path.read_text()
                money = json.loads(contents)

                self.resultlabel.config(text=f'You have {money} in your bank account', fg='black')

            else:
                self.resultlabel.config(text='Invalid password', fg='red')

        except FileNotFoundError:
            self.resultlabel.config(text='Account not found', fg='red')

    def Delete_action(self):
        try:
            stored_password_file = self.Field_1.get() + 'Pas.json'
            entry_password = self.Field_2.get()

            self.resultlabel.config(text='')

            path = Path(stored_password_file)
            contents = path.read_text()
            stored_password = json.loads(contents)

            if stored_password == [entry_password]:
                os.remove(self.Field_1.get() + '.json')
                os.remove(stored_password_file)

                self.resultlabel.config(text='Your account is deleted successfully', fg='black')

            else:
                self.resultlabel.config(text='Invalid password', fg='red')

        except FileNotFoundError:
            self.resultlabel.config(text='Account not found', fg='red')

    def Create_action(self):
        check = False

        try:
            while not check:
                A = []
                for i in range(12):
                    A.append(str(random.randint(1, 12)))
                password = ''.join(A) + 'Pas.json'
                A = ''.join(A) + '.json'
                path = Path(A)
                check = not os.path.exists(path)

            path = Path(A)
            with path.open(mode='w') as file:
                contents = json.dumps(int(self.Field_1.get()))
                file.write(contents)

            path = Path(password)
            with path.open(mode='w') as file:
                contents = json.dumps(str(self.Field_2.get()))
                file.write(contents)

            self.resultlabel.config(text=f'Your id is {A}', fg='black')

        except ValueError:
            self.resultlabel.config(text='Account not found', fg='red')

    def Add_action(self):
        try:
            stored_password_file = self.Field_1.get() + 'Pas.json'
            entry_password = self.Field_2.get()
            self.resultlabel.config(text='')

            path = Path(stored_password_file)
            contents = path.read_text()
            stored_password = json.loads(contents)

            if stored_password == [entry_password]:
                path = Path(self.Field_1.get() + '.json')
                contents = path.read_text()
                money = json.loads(contents)

                money += int(self.Field_3.get())

                with path.open(mode='w') as file:
                    file.write(json.dumps(money))

                self.resultlabel.config(text=f'Now, you have {money} in your bank account', fg='black')

            else:
                self.resultlabel.config(text='Invalid password', fg='red')

        except FileNotFoundError:
            self.resultlabel.config(text='Account not found', fg='red')

    def Withdraw_action(self):
        try:
            stored_password_file = self.Field_1.get() + 'Pas.json'
            entry_password = self.Field_2.get()
            self.resultlabel.config(text='')

            path = Path(stored_password_file)
            contents = path.read_text()
            stored_password = json.loads(contents)

            if stored_password == [entry_password]:
                path = Path(self.Field_1.get() + '.json')
                contents = path.read_text()
                money = json.loads(contents)
                m = int(self.Field_3.get())

                if money >= m:
                    money -= m
                    self.resultlabel.config(text=f'Now, you have {money} in your bank account', fg='black')
                else:
                    self.resultlabel.config(text='There is not enough money to withdraw', fg='red')

                with path.open(mode='w') as file:
                    file.write(json.dumps(money))

            else:
                self.resultlabel.config(text='Invalid password', fg='red')

        except FileNotFoundError:
            self.resultlabel.config(text='Account not found', fg='red')

    def Back_action(self):
        if self.condition is False:
            self.Field_1.pack_forget()
            self.Field_2.pack_forget()
            self.Field_3.pack_forget()

        else:
            self.Field_1.pack_forget()
            self.Field_2.pack_forget()

        self.submit.pack_forget()
        self.resultlabel.pack_forget()
        self.Back.pack_forget()

        self.MainLabel.config(text='Bank System')

        self.Know.pack(pady=15)
        self.Delete.pack(pady=15)
        self.Create.pack(pady=15)
        self.Add.pack(pady=15)
        self.Withdraw.pack(pady=15)

if __name__ == '__main__':
    App()