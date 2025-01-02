-- mytable에 컬럼 값 입력
INSERT INTO mytable (userid, username, age, email) 
VALUES 
('lee','이순신',45,'lee@a.com'),

-- mytable에 컬럼 값 일괄입력
INSERT INTO mytable (userid, username, age, email) 
VALUES 
('kim','김유신',40,'kim@a.com'),
('kim1','김유신1',41,'kim1@a.com'),
('kim2','김유신2',42,'kim2@a.com'),
('kim3','김유신3',43,'kim3@a.com'),
('kim4','김유신4',44,'kim4@a.com'),
('kim5','김유신5',45,'kim5@a.com')

SELECT * FROM mytable WHERE username = '이순신'

SELECT * FROM mytable WHERE username LIKE '김유신%'

