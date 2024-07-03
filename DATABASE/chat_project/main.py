import json
from flask import Flask, abort, request, jsonify

from postgres import PostgresService


app = Flask(__name__)

'''
    this api will create all tables, relations and entities
    Method: GET
    response:
        status and result of operation
'''
@app.route('/api/tables/create', methods=['GET'])
def create_tables():

    try:
        postgresService.create_table()
        return jsonify(200, {'message': 'database is created successfully'} )

    except Exception as error:
        return abort(500,{'message': f'connection failed in database system {error}'})

'''
    this api will initiate all tables with fake values
    Method: GET
    response:
        status and result of operation
'''    
@app.route('/api/tables/initialization', methods=['GET'])
def initiate_tables():

    try:
        postgresService.init_table()
        return jsonify(200, {'message': 'database values are created successfully'} )

    except Exception as error:
        return abort(500,{'message': f'connection failed in database system {error}'})

'''
 this api will will give us a list of all present users account information from our database
    Method: GET
    response:
       list of all present users account information
'''
@app.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        users = postgresService.query_response("SELECT * FROM Account;")
        return jsonify(users)
    except Exception as error:
        return abort(500, description=f'Failed to fetch users: {error}')

'''
 this api will give us an information of given user's id account from our database
    Method: GET
    parameter: user_id: int value of specific user
    response:
       user information
'''
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = postgresService.query_response(f"SELECT * FROM Account WHERE ID = {user_id};")
        return jsonify(user)
    except Exception as error:
        return abort(500, description=f'Failed to fetch user: {error}')
    
'''
 this api will give us an information of given user's id chats from our database
    Method: GET
    parameter: user_id: int value of specific user
    response:
       list of user's chats
'''
@app.route('/api/chats/<int:user_id>', methods=['GET'])
def get_user_chats(user_id):
    try:
        chats = postgresService.query_response(f"SELECT * FROM Chat WHERE firstUserID = {user_id} OR secondUserID = {user_id};")
        return jsonify(chats)
    except Exception as error:
        return abort(500, description=f'Failed to fetch chats: {error}')

'''
 this api will give us an information of given user's id contacts from our database
    Method: GET
    parameter: user_id: int value of specific user
    response:
       list of user's contacts
'''
@app.route('/api/contacts/<int:user_id>', methods=['GET'])
def get_user_contacts(user_id):
    try:
        contacts = postgresService.query_response(
            f"""SELECT c.ID, c.userID, c.chatID, a.name AS contact_name, a.fullname AS contact_fullname
            FROM Contacts c
            JOIN Account a ON c.userID = a.ID
            WHERE c.userID = {user_id};
            """
        )
        return jsonify(contacts)
    except Exception as error:
        return abort(500, description=f'Failed to fetch contacts: {error}')

'''
 this api will give us an information of given user's id contacts from our database
    Method: GET
    parameter: user_id: int value of specific user
    response:
       list of user's contacts
'''    
@app.route('/api/chat/messages/<int:chat_id>', methods=['GET'])
def get_chat_messages(chat_id):
    try:
        messages = postgresService.query_response(f"SELECT * FROM ChatMessage WHERE chatID = {chat_id};")
        return jsonify(messages)
    except Exception as error:
        return abort(500, description=f'Failed to fetch chat messages: {error}')

'''
 this api will give us a list of groups
    Method: GET
    response:
       list of groups
'''    
@app.route('/api/groups', methods=['GET'])
def get_all_groups():
    try:
        groups = postgresService.query_response("SELECT * FROM Groups;")
        return jsonify(groups)
    except Exception as error:
        return abort(500, description=f'Failed to fetch groups: {error}')

'''
 this api will give us an information of given group's id messages from our database
    Method: GET
    parameter: group_id: int value of specific group
    response:
       list of group_id's messages
'''   
@app.route('/api/group/<int:group_id>/messages', methods=['GET'])
def get_group_messages(group_id):
    try:
        messages = postgresService.query_response(f"SELECT * FROM GroupMessage WHERE groupID = {group_id};")
        return jsonify(messages)
    except Exception as error:
        return abort(500, description=f'Failed to fetch group messages: {error}')

'''
 this api will give us an information of given group's id users from our database
    Method: GET
    parameter: group_id: int value of specific group
    response:
       list of group_id's users
'''   
@app.route('/api/group/<int:group_id>/users', methods=['GET'])
def get_group_users(group_id):
    try:
        users = postgresService.query_response(f"SELECT userID FROM GroupUsers WHERE groupID = {group_id};")
        return jsonify(users)
    except Exception as error:
        return abort(500, description=f'Failed to fetch group users: {error}')        

'''
 this api will  insert any data and query dynamically to our database via postgresService.query_handler
    Method: POST
    parameter: group_id: int value of specific group
    response:
       list of group_id's users
'''  
@app.route('/api/insert/', methods=['POST'])
def insert_query():
    data = request.get_json()  # Get data from request body
    query = data.get('query')
    if not query:
        return jsonify({'message': 'there is no query provided!'}), 400

    try:
        postgresService.query_handler(query=query)
        return jsonify({'message': 'query executed correctly'}), 200
    except Exception as error:
        return abort(500, description=f'failed to execute insert query: {error}')

'''
 this api will  give us an information of given group's id users from our database
    Method: GET
    parameter: group_id: int value of specific group
    response:
       list of group_id's users
''' 
@app.route('/api/delete/', methods=['DELETE'])
def delete_query():
    data = request.get_json()  # Get data from request body
    query = data.get('query')
    if not query:
        return jsonify({'message': 'there is no query provided!'}), 400

    try:
        postgresService.query_handler(query=query)
        return jsonify({'message': 'query executed correctly'}), 200
    except Exception as error:
        return abort(500, description=f'failed to execute delete query: {error}')

@app.route('/api/update/', methods=['PULL'])
def update_query():
    data = request.get_json()  # Get data from request body
    query = data.get('query')
    if not query:
        return jsonify({'message': 'There is no query provided!'}), 400

    try:
        updated_value = postgresService.execute_dynamic_update(query)
        if updated_value > 0:
            return jsonify({'message': f'query is executed successfully and the table is updated in {updated_value} rows'}), 200
        else:
            return jsonify({'message': 'no rows updated (repeated data)'}), 200
    except Exception as error:
        return abort(500, description=f'failed to execute update query: {error}')

if __name__ == '__main__':
    #initializing the postgres database system
    postgresService = PostgresService()
    app.run(debug=False, host='0.0.0.0', port=5000)