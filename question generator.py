import pymysql
import msvcrt
import time
import re

def _question_gen(packet_row):
	question = packet_row[u'Questions']
	question_words = question.split(' ')
	return question_words

def _answer_gen(packet_row):
	answer = packet_row[u'Answers']
	return answer
	
def _question_reader(curr_question):
    for word in curr_question:
        print re.sub(u"(\u2018|\u2019|\u201c|\u201d)", "'", word),
        time.sleep(0.15)
        if msvcrt.kbhit():
            user_answer = raw_input("Type an answer")
            return user_answer
    user_answer = raw_input("Type an answer")
    return user_answer

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
results = cursor.fetchall()



while True:
        req_input = raw_input("Type 'n' for next question or 'q' to exit") #work on making this just a keypress especially for two player game later on
        if req_input == 'n':
                for row in results:
                        curr_question = _question_gen(row)
                        curr_answer = _answer_gen(row)
                        _question_reader(curr_question)

                        cont_input = raw_input("Type 'n' for next question or 'q' to exit")
                        if cont_input == 'n':
                                pass
                        else:
                                break
        elif req_input == 'q':
                break
        else:
                print("Please try again")
        


#closes database connection
connection.close()

#dealt with unicode errors using regex. 
#continue refactoring into functions;
#make a gui for this
#make a regex checker for anwers
#make it show up word by word #done!
#make it two player
