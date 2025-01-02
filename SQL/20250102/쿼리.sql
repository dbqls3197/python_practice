---[ 프로젝트 진행을 위한 데이터베이스, 테이블, 사용자 생성 및 매핑 프로세스]
--- 데이터 베이스 생성
# 조합 인코딩 기본값: utf8mb4_general_ci
CREATE DATABASE mydb

--- 테이블 생성mytable
# 조합 인코딩 기본값: utf8mb4_general_ci
CREATE TABLE mytable(
	id INT AUTO_INCREMENT PRIMARY KEY,
	NAME VARCHAR(255) NOT NULL,
	age INTmydb2mytable
)

--- 사용자 생성
CREATE user 'sejong'@'localhost' IDENTIFIED BY '1234'; 


--- mydb에 있는 모든 테이블에 권한 부여
GRANT ALL PRIVILEGES ON mydb. * TO 'sejong'@'localhost';


--- sejong 사용자에 대해 모든 권한 취소
REVOKE ALL PRIVILEGES ON mydb.mytable * FROM 'sejong'@'localhost';


--- mydb에 있는 mytable 테이블에만 권한 부여
GRANT ALL PRIVILEGES ON mydb.mytable TO 'sejong'@'localhost';


--- 권한 적용
FLUSH PRIVILEGES;


-- 사용자 권한 확인
SHOW GRANTS FOR 'sejong'@'localhost';


FLUSH PRIVILEGES;