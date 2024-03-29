-- COMANDOS TESTADOS NO SITE rextester.com

CREATE TABLE QUESTIONARIO (cd_Aluno INT)
GO

DECLARE @Q VARCHAR(1), @NUM INT, @QUESTAO VARCHAR(3), @QTCOL INT, @QTALUNO INT, @ALUCONT INT, @COLCONT INT

SET @Q = 'Q'
SET @NUM = 1
SET @QTCOL = 10 -- QT QUESTÕES/COLUNAS
SET @QTALUNO = 4 -- QT ALUNOS
SET @ALUCONT = 1
SET @COLCONT = 1

WHILE @ALUCONT <= @QTALUNO
BEGIN
    EXEC('INSERT INTO QUESTIONARIO VALUES (' + @ALUCONT + ')')
    SET @ALUCONT += 1
END

WHILE @COLCONT <= @QTCOL
BEGIN
    SET @ALUCONT = 1
    SET @QUESTAO = CONCAT(@Q,@COLCONT)
    EXEC('ALTER TABLE QUESTIONARIO ADD ' + @QUESTAO + ' INT')
    
    WHILE @ALUCONT <= @QTALUNO
    BEGIN        
        EXEC('UPDATE QUESTIONARIO SET ' + @QUESTAO + ' = ' + @NUM + ' WHERE cd_Aluno = ' + @ALUCONT)
        SET @ALUCONT += 1
        SET @NUM += 1 -- PARA TESTE
    END
    
    SET @COLCONT += 1
    
    SELECT * FROM QUESTIONARIO
END