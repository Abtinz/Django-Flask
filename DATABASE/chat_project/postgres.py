import psycopg2

class PostgresService():
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(
            dbname = "chatproject",
            user = "postgres",
            password = "12345",
            host = "localhost",
            port = "5432"
            )

            print("database is created on 5432.port.postgres ")
        except Exception as error:
            print(error)
            

    def create_user_db(self):

        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE Account (ID INT PRIMARY KEY,name VARCHAR(255),fullname VARCHAR(255),phone VARCHAR(255) UNIQUE,username VARCHAR(255) UNIQUE);")
        print(cursor.fetchone())

    def create_chat_message_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE ChatMessage (ID INT PRIMARY KEY,senderID INT,chatID INT,text VARCHAR(255),Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (senderID) REFERENCES Account(ID),FOREIGN KEY (chatID) REFERENCES Chat(ID));")
        print(cursor.fetchone())

    def create_group_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE Group (ID INT PRIMARY KEY,Name VARCHAR(255));")
        print(cursor.fetchone())

    def create_chat_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE Chat (ID INT PRIMARY KEY,firstUserID INT,secondUserID INT,FOREIGN KEY (firstUserID) REFERENCES Account(ID),FOREIGN KEY (secondUserID) REFERENCES Account(ID));")
        print(cursor.fetchone())

    def create_contact_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE Contacts (ID INT PRIMARY KEY,userID INT,chatID INT,FOREIGN KEY (userID) REFERENCES Account(ID),FOREIGN KEY (chatID) REFERENCES Chat(ID));")
        print(cursor.fetchone())

    def create_group_message_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE GroupMessage (ID INT PRIMARY KEY,senderID INT,groupID INT,text VARCHAR(255),Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (senderID) REFERENCES Account(ID),FOREIGN KEY (groupID) REFERENCES Group(ID));")
        print(cursor.fetchone())

    def create_group_user_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE GroupUsers (userID INT,groupID INT,FOREIGN KEY (userID) REFERENCES Account(ID),FOREIGN KEY (groupID) REFERENCES Group(ID));")
        print(cursor.fetchone())

    def create_table(self):
        self.create_contact_db()
        self.create_chat_db()
        self.create_chat_message_db()
        self.create_group_db()
        self.create_group_message_db()
        self.create_group_user_db()
        self.create_user_db()