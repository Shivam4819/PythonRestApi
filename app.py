from logging import error, exception
import re
from flask import Flask, jsonify,json
from flask import request
from pymongo import MongoClient, collation, collection
import pymongo
import requests

try:
    conn= MongoClient("mongodb+srv://shivam:vostro@cluster0.kjgdz.mongodb.net/Project?retryWrites=true&w=majority")
    print("db connected")
except:
    print("db not connected")

app = Flask(__name__)
db= conn.get_database('Project')
collection= db.user


@app.route("/api/users",methods=['POST'])
def addUser():
    try:
        collection.insert_one(request.get_json())
        return jsonify({'code':200})
        
    except:
        return jsonify({'code':400,'msg':"something wrong"}) 


@app.route("/api/users",methods=['GET'])
def getUser():
    try:
        limit=int(request.args.get('limit'))
        data=collection.find({},{'_id':False}).sort('age',pymongo.DESCENDING).limit(limit)
        data=list(data)
        return jsonify({'code':200,'Records':data})

    except:
        return jsonify({'code':400,'msg':"some error from 1"}) 


@app.route("/api/users/<id>",methods=['GET'])
def specificUser(id):
    try:
        data=collection.find({'id':int(id)},{'_id':False})
        data=list(data)
        print(data)
        return jsonify({'code':200,'Records':data})

    except:
        return jsonify({'code':400,'msg':"id not matches"}) 


@app.route("/api/users",methods=['PUT'])
def updateUser():
    try:
        data=request.get_json()
        newvalues={
            'first_name':data['first_name'],
            'last_name':data['last_name'],
            'age':data['age']
        }
        filter = { "id": int(request.args.get('id')) }
        collection.find_one_and_update(filter,{"$set":newvalues})

        return jsonify({'code':200,'msg':'data updated'}) 

    except:
        return jsonify({'code':400,'msg':"id not matches"}) 



@app.route("/api/users",methods=['DELETE'])
def deleteUser():
    try:
        collection.find_one_and_delete({'id':int(request.args.get('id'))})
        return jsonify({'code':200,'msg':'data deleted success'}) 

    except:
        return jsonify({'code':400,'msg':"id not matches"}) 
 

