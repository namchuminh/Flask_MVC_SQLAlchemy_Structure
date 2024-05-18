import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def index():
    return jsonify({
        "data": "index"
    })
def store():
    return jsonify({
        "data": "store"
    })
def show(user_id):
    return jsonify({
        "data": f"show {user_id}"
    })
def update(user_id):
    return jsonify({
        "data": f"update {user_id}"
    })
def delete(user_id):
    return jsonify({
        "data": f"delete {user_id}"
    })