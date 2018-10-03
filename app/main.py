import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.eventsdb


@app.route('/r')
def pop_events():
    # _events = dzb.eventsdb.find()
    # events = json.dumps(_events)
    # events = [event for event in _events]
    return "events"


@app.route('/events', methods=['POST'])
def push_events():
    item_doc = request.get_json(force=True)
    item_doc_source = item_doc['source']
    result = db[item_doc_source].insert_one(item_doc)
    return jsonify(result=result.acknowledged, id=str(result.inserted_id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
