from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

def get_first_free_id():
    if not users:
        return 1
    existing_ids = sorted(users.keys())
    for i, uid in enumerate(existing_ids, 1):
        if uid != i:
            return i 
    return existing_ids[-1] + 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return "", 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(silent=True)
    if not data or 'name' not in data or 'lastname' not in data:
        return "", 400
    
    new_id = get_first_free_id()
    new_user = {
        "id": new_id,
        "name": data['name'],
        "lastname": data['lastname']
    }
    users[new_id] = new_user
    return "", 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    if user_id not in users:
        return "", 400

    data = request.get_json(silent=True)
    if not data:
        return "", 400
    
    if not any(key in data for key in ['name', 'lastname']):
        return "", 400

    user = users[user_id]
    if 'name' in data:
        user['name'] = data['name']
    if 'lastname' in data:
        user['lastname'] = data['lastname']

    return "", 204

@app.route('/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    data = request.get_json(silent=True)
    if not data or 'name' not in data or 'lastname' not in data:
        return "", 400

    users[user_id] = {
        "id": user_id,
        "name": data['name'],
        "lastname": data['lastname']
    }
    return "", 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return "", 204
    else:
        return "", 400
    
if __name__ == '__main__':
    app.run(debug=True)