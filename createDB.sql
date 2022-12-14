-- create an empty database. Name of the database: 
SET storage_engine=InnoDB;
SET FOREIGN_KEY_CHECKS=1;
CREATE DATABASE IF NOT EXISTS Cyclists;

-- use the db 
use Cyclists;

-- create tables

CREATE TABLE IF NOT EXISTS Team(
	TID CHAR(20) ,
	NameT CHAR(50) NOT NULL ,
	YearFoundation SMALLINT NOT NULL ,
	OfficeLocation CHAR(50),
	PRIMARY KEY (TID)
);

CREATE TABLE IF NOT EXISTS Cyclist(
	CID CHAR(20) ,
	Name CHAR(50) NOT NULL ,
	Surname CHAR(50) NOT NULL ,
	Nationality CHAR(50) NOT NULL ,
	TID CHAR(50) NOT NULL ,
	BirthYear SMALLINT NOT NULL,
	PRIMARY KEY (CID),
	FOREIGN KEY (TID)
		REFERENCES Team(TID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Stage(
	Edition CHAR(50) NOT NULL ,
	SID SMALLINT NOT NULL ,
	DepartureCity CHAR(50) NOT NULL ,
	ArrivalCity CHAR(50) NOT NULL ,
	Length INT NOT NULL,
	DeltaHeight SMALLINT NOT NULL,
	Difficulty SMALLINT NOT NULL,
	PRIMARY KEY (Edition,SID)
);

CREATE TABLE IF NOT EXISTS Individual_Ranking(
	CID char(50) NOT NULL,
	SID SMALLINT NOT NULL,
	Edition CHAR(50) NOT NULL,
	Location SMALLINT NOT NULL,
	FOREIGN KEY (Edition, SID)
		REFERENCES STAGE (Edition, SID)
		ON DELETE CASCADE
		ON UPDATE CASCADE ,
	FOREIGN KEY (CID)
		REFERENCES Cyclist(CID)
    	ON DELETE CASCADE
		ON UPDATE CASCADE
);

