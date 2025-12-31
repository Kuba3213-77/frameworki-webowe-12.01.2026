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
    return existing_ids[-1] +12