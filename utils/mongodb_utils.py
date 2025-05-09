import json
from utils.mongodb_encoder import MongoJSONEncoder


def parse_mongo_item_to_json(item):
    return json.loads(json.dumps(item, cls=MongoJSONEncoder))

def parse_mongo_list_to_json(documents):
    return [parse_mongo_item_to_json(doc) for doc in documents]
