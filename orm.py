from mongoengine import connect

from MongoEngineE2E.Embedded_Orm import Author_profile, Author, Mains
from flask import Flask, request, json, Response, jsonify

app = Flask(__name__)


@app.route('/crud', methods=['POST'])
def data_insertion():

    connect(db="mongoe2e", host='127.0.0.1', port=27017)
    data=request.json
    auth_pro = Author_profile()
    auth_pro.experience = data["author_details"]["profile"]["experience"]
    auth_pro.courses = data["author_details"]["profile"]["courses"]
    auth_pro.books = data["author_details"]["profile"]["books"]

    author = Author()
    author.name = data["author_details"]["name"]
    author.call_name = data["author_details"]["call_name"]
    author.profile = auth_pro

    auth_main = Mains()
    auth_main.tittle = data["tittle"]
    auth_main.isbn = data["isbn"]
    auth_main.downloadable = data["downloadable"]
    auth_main.no_of_reviews = data["no_of_reviews"]
    auth_main.tags = data["tags"]
    auth_main.languages = data["languages"]
    auth_main.author_details = author

    auth_main.save()

    return "Insertion Done"
@app.route('/r', methods=['GET'])
def data_retrievel():
    connect(db="mongoe2e", host='127.0.0.1', port=27017)
    out=[]
    for data in Mains.objects():
        out.append(data.to_json())
    return out.__str__()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
