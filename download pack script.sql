USE quizbowl;

LOAD XML INFILE 'TERP 2 Packet 1.xml'
	
REPLACE INTO TABLE `terp 2 packet 1` (@id, @Question, @ANSWER)

SET QuestionID=@id, Question=@Question, Answer=@ANSWER;
