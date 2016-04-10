import pymysql
import msvcrt
import time
import re

def _question_gen(packet_row):
	question = packet_row[u'Question']
	question_words = question.split(' ')
	return question_words

def _answer_gen(packet_row):
	answer = packet_row[u'Answer']
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

def answer_checker(u_answer):
    u_answer_arr = u_answer.split(' ')
    curr_answer_arr = curr_answer.split(' ')
    [x.lower for x in u_answer_arr]
    for word in u_answer_arr:
            if word.lower() in curr_answer_arr:
                print "Correct!"
                return
            else:
                print "Wrong!"
                print "You wrote: " + u_answer
                print "The correct answer is: " + curr_answer
                return

def continue_check():
    cont_input = raw_input("Type 'n' for next question or 'q' to exit")
    if cont_input == 'n':
        return True
    else:
        return False


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
results = cursor.fetchall()



while True:
        req_input = raw_input("Type 'n' for next question or 'q' to exit") #work on making this just a keypress especially for two player game later on
        if req_input == 'n':
                for row in results:
                        curr_question = _question_gen(row)
                        curr_answer = _answer_gen(row)
                        user_answer = _question_reader(curr_question)
                        answer_checker(user_answer)
                        if continue_check() == False:
                                continue
                        else:
                                continue

        elif req_input == 'q':
                break
        else:
                print("Please try again")
        


#closes database connection
connection.close()

#continue refactoring into functions;
#make a gui for this
#make a regex checker for anwers
#make it two player
