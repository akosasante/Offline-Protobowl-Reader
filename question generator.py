import pymysql

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
                        question = row[u'Questions']
                        answer = row[u'Answers']
                        print(question)
                        raw_input('>>>')
                        print(answer)
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

#refactor into functions
#make a gui for this
#make a regex checker for anwers
#make it show up word by word
#make it two player
