USE quizbowl;

LOAD XML INFILE 'TERP 2 Packet 1.xml'
	REPLACE
    INTO TABLE trashqs (@Question, @ANSWER)
    SET Questions=@Question, Answers=@ANSWER;
    