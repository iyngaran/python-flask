from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Computer",
                "price": 128.67
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}

@app.post("/stores")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/stores/<string:name>/item")
def create_item(name):
    for store in stores:
        if store["name"] == name:
            new_item = request.get_json()
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/stores/<string:name>/item")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store["items"]
    return {"message": "Store not found"}, 404