from Tkinter import *
import pymysql
import msvcrt
import time
import re
import random

# initiates variables for pymysql connection
connection = pymysql.connect(host="localhost",
user="root",
password="island",
db="quizbowl",
charset="utf8",
cursorclass=pymysql.cursors.DictCursor)

# initiates the cursor and then selects just questions from table and stores them in result.
cursor = connection.cursor()
sql_command = "SELECT Questions, Answers FROM trashqs ORDER BY rand()"
cursor.execute(sql_command)

def _fetchrow():
    result = cursor.fetchone()
    return result

def _question_gen(packet_row):
	question = packet_row[u'Questions']
	question_words = question.split(' ')
	return question_words

def _answer_gen(packet_row):
	answer = packet_row[u'Answers']
	return answer

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.button1 = Button(self.myContainer1, text="Display Next Question", background="green")
        self.button1.pack()
        self.button1.bind("<Button-1>", self.buttonClick)
        
        self.button3 = Button(self.myContainer1, text="Display Answer", background="green")
        self.button3.pack()
        self.button3.bind("<Button-1>", self.answerClick)
        
        self.button2 = Button(self.myContainer1, text="Quit", background="red")
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Button-1>", self.quitClick)
        
        self.questionwind = Text(self.myContainer1)
        self.questionwind.pack()
        
        self.myParent.bind("<space>", self.endQ)
        
        self.stopvar = False
        
    def buttonClick(self, event):
        self.stopvar = False
        curr_row = _fetchrow()
        curr_quest = _question_gen(curr_row)
        for word in curr_quest:
            self.word = word
            self.questionwind.insert(END, word+" ")
            time.sleep(0.15)
            self.myParent.update()
            if self.stopvar == True:
                break
            
    def endQ(self, event):
        self.stopvar = True
        return self.stopvar
        
    def answerClick(self, event):
        curr_row = _fetchrow()
        curr_answer = _answer_gen(curr_row)
        self.questionwind.insert(END, curr_answer)
    
    def quitClick(self, event):
        self.myParent.destroy()
    
    
root = Tk()
myapp = MyApp(root)
root.mainloop()

