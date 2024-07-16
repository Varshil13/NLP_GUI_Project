from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
import json
class NLPApp:
    def __init__(self):

        #create db object
        self.dbo = Database()
        self.apio = API()
        #login gui

        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap("Resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg='#CC313D')
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text="LOGIN",bg="#CC313D",fg='#F2A7A7')
        heading.pack(pady=(60,50))
        heading.configure(font=("verdana",24,'bold'))

        label1 = Label(self.root,text="Enter Email",bg="#CC313D",fg='#F2A7A7')
        label1.pack(pady=(10,5))

        self.email_input = Entry(self.root,bg="#F2A7A7",width='30')
        self.email_input.pack(pady=(0,15))


        label2 = Label(self.root,text="Enter Password",bg="#CC313D",fg='#F2A7A7')
        label2.pack(pady=(10,5))

        self.password_input = Entry(self.root,bg="#F2A7A7",width='30',show="*")
        self.password_input.pack(pady=(0,15))

        login_button = Button(self.root,text="Login",width="15",height="2",command=self.perform_login)
        login_button.pack(pady=(25,10))

        label3 = Label(self.root,text="Not a member?",bg="#CC313D",fg='#F2A7A7')
        label3.pack(pady=(10,5))

        redirect_button = Button(self.root,text="Register now!",width="10",command=self.register_gui)
        redirect_button.pack(pady=(0,10))

    def register_gui(self):
        #clear the existing gui
        self.clear()
        heading = Label(self.root, text="Register", bg="#CC313D", fg='#F2A7A7')
        heading.pack(pady=(60, 50))
        heading.configure(font=("verdana", 24, 'bold'))

        label0 = Label(self.root, text="Enter Name", bg="#CC313D", fg='#F2A7A7')
        label0.pack(pady=(10, 5))

        self.name_input = Entry(self.root, bg="#F2A7A7", width='30')
        self.name_input.pack(pady=(0, 15))

        label1 = Label(self.root, text="Enter Email", bg="#CC313D", fg='#F2A7A7')
        label1.pack(pady=(10, 5))

        self.email_input = Entry(self.root, bg="#F2A7A7", width='30')
        self.email_input.pack(pady=(0, 15))

        label2 = Label(self.root, text="Enter Password", bg="#CC313D", fg='#F2A7A7')
        label2.pack(pady=(10, 5))

        self.password_input = Entry(self.root, bg="#F2A7A7", width='30', show="*")
        self.password_input.pack(pady=(0, 15))

        Reg_button = Button(self.root, text="Register", width="15", height="2",command=self.perform_reg)
        Reg_button.pack(pady=(25, 10))

        label3 = Label(self.root, text="Already a member?", bg="#CC313D", fg='#F2A7A7')
        label3.pack(pady=(10, 5))

        redirect_button = Button(self.root, text="Login now!", width="10",command=self.login_gui)
        redirect_button.pack(pady=(0, 10))
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def perform_reg(self):
        #fetch data from gui
        name = self.name_input.get()
        email= self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo("Success!","Registration successful!")

        else:
            messagebox.showerror("Error!","Email already registered!")
    def perform_login(self):
        email= self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo("Success!","Login successful!")
            self.home_gui()
        else:
            messagebox.showerror("Error!","Incorrect email or password!")

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text="HOME",bg="#CC313D", fg='#F2A7A7')
        heading.pack(pady=(30,50))
        heading.configure(font=("verdana",24,'bold'))

        sentiment_button = Button(self.root, text="Sentiment Analysis", width="20", height="2",command=self.sentiment_gui)
        sentiment_button.pack(pady=(25, 10))

        NER_button = Button(self.root, text="Language Recognition", width="20", height="2",command=self.ner_gui)
        NER_button.pack(pady=(25, 10))

        emotion_button = Button(self.root, text="Bad Words Analysis", width="20", height="2",command=self.badwords_gui)
        emotion_button.pack(pady=(25, 10))

        logout_button = Button(self.root, text="Logout", width="10", height="1",command=self.login_gui)
        logout_button.pack(pady=(100, 10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text="Sentiment Analysis",bg="#CC313D", fg='#F2A7A7')
        heading.pack(pady=(30,50))
        heading.configure(font=("verdana",24))

        label1= Label(self.root, text="Enter text", bg="#CC313D", fg='#F2A7A7')
        label1.pack(pady=(10,5))

        self.sentiment_input = Entry(self.root, bg="#F2A7A7", width='30')
        self.sentiment_input.pack(pady=(0, 15))

        sentiment_button = Button(self.root, text="Analyze Sentiment", width="15", height="1",command=self.do_sentiment_analysis)

        sentiment_button.pack(pady=(5, 10))

        self.sentiment_result = Label(self.root, text="", bg="#CC313D", fg='#F2A7A7')
        self.sentiment_result.pack(pady=(10, 5))
        self.sentiment_result.configure(font=("verdana", 8))

        goHome_button = Button(self.root, text="Go Back!", width="10", height="1",command=self.home_gui)
        goHome_button.pack(pady=(100, 10))

    def ner_gui(self):

        self.clear()

        heading = Label(self.root, text="Language Detector",bg="#CC313D", fg='#F2A7A7')
        heading.pack(pady=(30,50))
        heading.configure(font=("verdana",15))

        label1= Label(self.root, text="Enter text", bg="#CC313D", fg='#F2A7A7')
        label1.pack(pady=(10,5))

        self.ner_input = Entry(self.root, bg="#F2A7A7", width='30')
        self.ner_input.pack(pady=(0, 15))

        ner_button = Button(self.root, text="Analyze Sentiment", width="15", height="1",command=self.do_language_detection)
        ner_button.pack(pady=(5, 10))

        self.ner_result = Label(self.root, text="", bg="#CC313D", fg='#F2A7A7')
        self.ner_result.pack(pady=(10, 5))
        self.ner_result.configure(font=("verdana", 8))

        goHome_button = Button(self.root, text="Go Back!", width="10", height="1",command=self.home_gui)
        goHome_button.pack(pady=(100, 10))

    def badwords_gui(self):

        self.clear()

        heading = Label(self.root, text="Bad Words Analysis",bg="#CC313D", fg='#F2A7A7')
        heading.pack(pady=(30,50))
        heading.configure(font=("verdana",24))

        label1= Label(self.root, text="Enter text", bg="#CC313D", fg='#F2A7A7')
        label1.pack(pady=(10,5))

        self.badwords_input = Entry(self.root, bg="#F2A7A7", width='30')
        self.badwords_input.pack(pady=(0, 15))

        badwords_button = Button(self.root, text="Analyze Sentiment", width="15", height="1",command=self.do_badwords_analysis)
        badwords_button.pack(pady=(5, 10))

        self.badwords_result = Label(self.root, text="", bg="#CC313D", fg='#F2A7A7')
        self.badwords_result.pack(pady=(10, 5))
        self.badwords_result.configure(font=("verdana", 8))

        goHome_button = Button(self.root, text="Go Back!", width="10", height="1",command=self.home_gui)
        goHome_button.pack(pady=(100, 10))


    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis((text))
        converted_result = self.convert_result(result)
        self.sentiment_result['text'] = converted_result

    def do_badwords_analysis(self):

        text = self.badwords_input.get()
        result = self.apio.badwords_analysis(text)
        converted_result = self.convert_result(result)
        self.badwords_result['text'] = converted_result

    def do_language_detection(self):

        text = self.ner_input.get()
        result = self.apio.language_detector(text)
        converted_result = self.convert_result(result)
        self.ner_result['text'] = converted_result
    def convert_result(self,result):

        temp = result
        res = json.loads(temp)
        res = {key: res[key] for key in res.keys()}
        temp_res = ''
        for i in res:
            temp_res = temp_res + str(i).capitalize() + ' -> ' + str(res[i]).capitalize() + '\n'
        return temp_res



nlp = NLPApp()