import json
from flask import Flask, abort, request, jsonify

from postgres import PostgresService


app = Flask(__name__)

@app.route('/api/tables/create', methods=['GET'])
def create_tables():

    try:
        postgresService.create_table()
        return jsonify(200, {'message': 'database is created successfully'} )

    except Exception as error:
        return abort(500,{'message': f'connection failed in database system {error}'})
    
@app.route('/api/tables/initialization', methods=['GET'])
def initiate_tables():

    try:
        postgresService.init_table()
        return jsonify(200, {'message': 'database values are created successfully'} )

    except Exception as error:
        return abort(500,{'message': f'connection failed in database system {error}'})


@app.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        users = postgresService.query_response("SELECT * FROM Account;")
        return jsonify(users)
    except Exception as error:
        return abort(500, description=f'Failed to fetch users: {error}')

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = postgresService.query_response(f"SELECT * FROM Account WHERE ID = {user_id};")
        return jsonify(user)
    except Exception as error:
        return abort(500, description=f'Failed to fetch user: {error}')

@app.route('/api/chats/<int:user_id>', methods=['GET'])
def get_user_chats(user_id):
    try:
        chats = postgresService.query_response(f"SELECT * FROM Chat WHERE firstUserID = {user_id} OR secondUserID = {user_id};")
        return jsonify(chats)
    except Exception as error:
        return abort(500, description=f'Failed to fetch chats: {error}')

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
    
@app.route('/api/chat/messages/<int:chat_id>', methods=['GET'])
def get_chat_messages(chat_id):
    try:
        messages = postgresService.query_response(f"SELECT * FROM ChatMessage WHERE chatID = {chat_id};")
        return jsonify(messages)
    except Exception as error:
        return abort(500, description=f'Failed to fetch chat messages: {error}')

@app.route('/api/groups', methods=['GET'])
def get_all_groups():
    try:
        groups = postgresService.query_response("SELECT * FROM Groups;")
        return jsonify(groups)
    except Exception as error:
        return abort(500, description=f'Failed to fetch groups: {error}')

@app.route('/api/group/<int:group_id>/messages', methods=['GET'])
def get_group_messages(group_id):
    try:
        messages = postgresService.query_response(f"SELECT * FROM GroupMessage WHERE groupID = {group_id};")
        return jsonify(messages)
    except Exception as error:
        return abort(500, description=f'Failed to fetch group messages: {error}')

@app.route('/api/group/<int:group_id>/users', methods=['GET'])
def get_group_users(group_id):
    try:
        users = postgresService.query_response(f"SELECT userID FROM GroupUsers WHERE groupID = {group_id};")
        return jsonify(users)
    except Exception as error:
        return abort(500, description=f'Failed to fetch group users: {error}')        

@app.route('/api/update/', methods=['GET'])
def update_query():
    query = request.args.get('query')
    if not query:
        return jsonify({'message': 'there is no query provided!'}), 400

    try:
        updated_value = postgresService.execute_dynamic_update(query)
        if updated_value > 0:
            return jsonify({'message': f'query is executed successfully and table is updated {updated_value} rows'}), 200
        else:
            return jsonify({'message': 'no rows updated(repeated data)'}), 200
    except Exception as error:
        return abort(500, f'message: failed to execute update query: {error}')

if __name__ == '__main__':
    #initializing the postgres database system
    postgresService = PostgresService()
    app.run(debug=False, host='0.0.0.0', port=5000)