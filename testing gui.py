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
sql_command = "SELECT Question, Answer FROM `terp 2 packet 1` ORDER BY rand()"
cursor.execute(sql_command)
rows = cursor.fetchall()


def _question_gen(packet_row):
	question = packet_row[u'Question']
	question_words = question.split(' ')
	return question_words

def _answer_gen(packet_row):
	answer = packet_row[u'Answer']
	return answer

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.button1 = Button(self.myContainer1, text="Display Next Question", background="green")
        self.button1.pack()
        self.button1.bind("<Button-1>", self.displayQ)
        
        self.button3 = Button(self.myContainer1, text="Display Answer", background="green")
        self.button3.pack()
        self.button3.bind("<Button-1>", self.answerClick)
        
        self.button2 = Button(self.myContainer1, text="Quit", background="red")
        self.button2.pack(side=RIGHT)
        self.button2.bind("<Button-1>", self.quitClick)
        
        self.answerwind = Entry(self.myContainer1, width=50)
        self.answerwind.pack()
        

        self.questionwind = Text(self.myContainer1)
        self.questionwind.pack()
        
        self.myParent.bind("<space>", self.endQ)
        
        self.askquestion = False
        self.answerQ = False
        
        
        self.curr_row_id = 0
        
        self.question_amt = len(rows)
        
        
        
    def displayQ(self, event):
        self.askquestion = True
        self.curr_row = rows[self.curr_row_id]
        if self.curr_row_id < self.question_amt:
            self.curr_quest = _question_gen(self.curr_row)
            while self.askquestion == True:
                for word in self.curr_quest:
                    self.word = word
                    self.questionwind.insert(END, word+" ")
                    time.sleep(0.15)
                    self.myParent.update()
                    
                    
                    while self.answerQ == True:
                        user_ans = self.answerwind.get()
                        curr_answer = _answer_gen(self.curr_row)

                        if user_ans == curr_answer:
                                print("correct!" + user_ans)
                                answerQ = False
                        elif user_ans == "":
                                answerQ = False
                        else:
                                print("wrong")
                                answerQ = False

                            
                    
                        
                self.askquestion = False
                self.curr_row_id += 1
                print self.curr_row_id
                break        
                    
            
    def endQ(self, event):
        self.answerwind.focus_set()
        self.answerQ = True
        
        

        
    def answerClick(self, event):
        curr_answer = _answer_gen(self.curr_row)
        self.questionwind.insert(END, '\n'*2 + curr_answer)
    
    def quitClick(self, event):
        self.myParent.destroy()
    
    
root = Tk()
myapp = MyApp(root)
root.mainloop()

#add keypress event to answer questions
#add answer checker and response
#make answer button disabled before question is pushed. 
