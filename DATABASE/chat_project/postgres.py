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
            
    def query_response(self,query):
        try:
            print("processing query: ",query)
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Exception as error:
            print(error)

    def update_query(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                return cursor.rowcount
        except Exception as error:
            print(error)
            raise error
           

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

    def insert_users(self, query):
        
        if query is None:
            insert_query = """
                INSERT INTO Account (ID, name, fullname, phone, username) VALUES
                (1, 'John', 'John Doe', '555-0101', 'john_doe'),
                (2, 'Jane', 'Jane Smith', '555-0102', 'jane_smith'),
                (3, 'abtin', 'abtin zandi', '0923131232', 'abnz'),
                (4, 'jcob', 'jcob marc', '0922222222', 'jaco'),
                (5, 'marc', 'marc Smith', '58222156', 'marc_smith'),
                (6, 'raty', 'raty raty', '555-011101', 'ratyyyyy'),
                (7, 'nader', 'nader Smith', '555-012202', 'nader'),
                (8, 'leo', 'leo messi', '111111111', 'goat'),
                (9, 'cristiano', 'cristiano ronaldo', '222222222222', 'cr7'),
                (10, 'Janee', 'Janee Smith', '58744156', 'janee_smith');
            """
            self.query_handler(query=insert_query)
        else:
            self.query_handler(query=query)
        
        self.query_handler(query="SELECT * FROM Account")

    def contacts_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO Contacts (ID, userID, chatID) VALUES
                    (1, 1, 1),
                    (2, 2, 1),
                    (3, 1, 2),
                    (4, 3, 2),
                    (5, 8, 3),
                    (6, 9, 3),
                    (7, 10, 4),
                    (8, 2, 4),
                    (9, 7, 5),
                    (10, 5, 5),
                    (11, 6, 6),
                    (12, 7, 6);
            """

            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        
        self.query_handler(query="SELECT * FROM Contacts")

    def chat_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO Chat (ID, firstUserID, secondUserID) VALUES
                    (1, 1, 2),
                    (2, 1, 3),
                    (3, 8, 9),
                    (4, 10, 2),
                    (5, 8, 3),
                    (6, 6, 7);
            """
            
            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        
        self.query_handler(query="SELECT * FROM Chat")

    def chat_message_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO ChatMessage (ID, senderID, chatID, text) VALUES
                    (1, 1, 1, 'Hello, how are you?'),
                    (2, 2, 1, 'I am fine, thanks!'),
                    (3, 8, 3, 'hi ciris, im the goat.'),
                    (4, 9, 3, 'Noooooooooooooooooooooooooo');
            """
            
            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        
        self.query_handler(query="SELECT * FROM ChatMessage")

    def group_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO Groups (ID, Name) VALUES
                    (1, 'Friends'),
                    (2, 'Barcelona'),
                    (3, 'Python'),
                    (4, 'Kotlin'),
                    (5, 'Database');
            """
            
            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        self.query_handler(query="SELECT * FROM Groups")

    def group_message_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO GroupMessage (ID, senderID, groupID, text) VALUES
                    (1, 1, 1, 'Welcome to Friends Group!'),
                    (2, 2, 1, 'Thank you, glad to be here.'),
                    (3, 8, 2, 'visca barca  and visca catolonia'),
                    (4, 3, 4, 'android.kotlin.life');
            """
            
            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        self.query_handler(query="SELECT * FROM GroupMessage")

    def group_user_insert(self, query):
       
        if query is None:
            insert_query = """
                    INSERT INTO GroupUsers (userID, groupID) VALUES
                    (1, 1),
                    (2, 1),
                    (3, 4),
                    (8, 2),
                    (9, 2);
            """
            
            self.query_handler(query=insert_query)
            
        else:
            self.query_handler(query=query)
        self.query_handler(query="SELECT * FROM GroupUsers")

    def init_table(self):
        self.insert_users(None)
        self.chat_insert(None)
        self.contacts_insert(None)
        self.chat_message_insert(None)
        self.group_insert(None)
        self.group_message_insert(None)
        self.group_user_insert(None)
