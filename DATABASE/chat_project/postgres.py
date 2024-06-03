import psycopg2

class PostgresService():
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                dbname="dbname",
                user="Abnzandi",
                password="12345",
                host="localhost",  
                port="5433"
            )
            print("postgres connection is established.")
        except Exception as error:
            print("Failed to connect to the postgres! error message:", error)


    def query_handler(self,query):
        try:
            print("processing query: ",query)
            cursor = self.conn.cursor()
            cursor.execute(query)
            print(cursor.fetchone()) 
        except Exception as error:
            print(error)
        

    def create_table(self):

        queries = [
            "CREATE TABLE Account (ID INT PRIMARY KEY,name VARCHAR(255),fullname VARCHAR(255),phone VARCHAR(255) UNIQUE,username VARCHAR(255) UNIQUE);",
            "CREATE TABLE Chat (ID INT PRIMARY KEY,firstUserID INT,secondUserID INT,FOREIGN KEY (firstUserID) REFERENCES Account(ID),FOREIGN KEY (secondUserID) REFERENCES Account(ID));",
            "CREATE TABLE Contacts (ID INT PRIMARY KEY,userID INT,chatID INT,FOREIGN KEY (userID) REFERENCES Account(ID),FOREIGN KEY (chatID) REFERENCES Chat(ID));"
            "CREATE TABLE ChatMessage (ID INT PRIMARY KEY,senderID INT,chatID INT,text VARCHAR(255),Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (senderID) REFERENCES Account(ID),FOREIGN KEY (chatID) REFERENCES Chat(ID));",
            "CREATE TABLE Groups (ID INT PRIMARY KEY,Name VARCHAR(255));",
            "CREATE TABLE GroupUsers (userID INT,groupID INT,FOREIGN KEY (userID) REFERENCES Account(ID),FOREIGN KEY (groupID) REFERENCES Groups(ID));"
            "CREATE TABLE GroupMessage (ID INT PRIMARY KEY,senderID INT,groupID INT,text VARCHAR(255),Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (senderID) REFERENCES Account(ID),FOREIGN KEY (groupID) REFERENCES Groups(ID));"
        ]

        for query in queries:
            self.query_handler(query=query)

        print("Tables are created successfully")