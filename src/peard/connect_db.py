import pymysql
import logging

logger = logging.getLogger(__name__)


def doUserLogin(cursor: pymysql.connect.cursor, username: str, password: str) -> None:
    # Gets the table
    while True:
        try:
            query = "select * from usercredentials where username=%s and password=%s"
            cursor.execute(query, (username, password))
            break
        except pymysql.ProgrammingError:
            logger.info("The necessary login data tables does not exists")


def doUserRegistration(cursor: pymysql.connect.cursor, email: str, username: str, password: str) -> None:
    # Gets the table
    while True:
        try:
            registration_query = "insert into peard.usercredentials(email,username,password) values (%s,%s,%s)"
            cursor.execute(registration_query, (email, username, password))
            cursor.connection.commit()
            break
        except pymysql.IntegrityError:
            logger.info("An account for that email/username already exists")
            break


# try to create peard database, if get an error, then the database already exists and we can just use the existing one
def createDatabase(cursor: pymysql.cursors.DictCursor) -> None:
    while True:
        try:
            cursor.execute("create database peard")
            cursor.connection.commit()
            break
        except pymysql.Error as e:
            if e.args[0] == 1007:
                cursor.execute("use peard")
                logging.info("Database peard already found, using existing one.")
                break
            else:
                raise e
    # Loading user credentials table
    while True:
        try:
            cursor.execute("select * from peard.usercredentials")
            break
        except pymysql.ProgrammingError:
            logger.info("The peard.usercredentials table doesn't exists, creating it...")
            query = (
                """create table usercredentials(user id int auto_increment primary key not null,
                email varchar(50) not null unique, username varchar(100) not null unique,
                password varchar(20) not null)"""
                )
            cursor.execute(query)
            cursor.connection.commit()


# Connects to the database with the given info
def connectDB(hostname: str, usr: str, passwd: str):
    try:
        db = pymysql.connect(
            host="peard-database.cbiya7huefjt.us-east-1.rds.amazonaws.com",
            user="pearddev",
            passwd="Peepeep00p0031!"
            )
    except pymysql.err.OperationalError as e:
        if e.args[0] == 2003:
            # Invalid hostname error
            logger.error("Cannot connect to database. Invalid hostname provided!")
        if e.args[0] == 1045:
            # Access Denied
            logger.error("Access Denied. Invalid username or password provided!")
        db = None
    return db


def showTable(cursor: pymysql.cursors.DictCursor, table_name: str) -> None:
    # Used for development purposes only
    try:
        query = f"select * from {table_name}"
        cursor.execute(query)
        print(cursor.fetchall())
    except pymysql.ProgrammingError as e:
        print(f"couldn't find table with name: {table_name}")
        raise e


def main() -> None:
    db = connectDB(
        hostname="peard-database.cbiya7huefjt.us-east-1.rds.amazonaws.com",
        usr="pearddev",
        passwd="Peepeep00p0031!"
        )
    cursor = db.cursor()
    createDatabase(cursor)
    doUserRegistration(cursor=cursor, email="huyta55@gmail.com", username="huyta55", password="huytapassword")
    showTable(cursor=cursor, table_name="peard.usercredentials")


if __name__ == "__main__":
    main()
